#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include <boost/regex.hpp>

#include <memory>
#include <vector>
#include <string>

class RecoEventInfoProducer : public edm::EDProducer
{
public:
  RecoEventInfoProducer(const edm::ParameterSet& pset);
  void produce(edm::Event& event, const edm::EventSetup& eventSetup) override;
  void beginRun(edm::Run& run, const edm::EventSetup& eventSetup) override;

private:
  typedef std::vector<double> doubles;
  typedef std::vector<std::string> strings;

  edm::InputTag vertexToken_;
  edm::InputTag hltToken_;

  std::string processName_;
  std::map<std::string, strings> hltGroup_;
  HLTConfigProvider hltConfig_;

};

RecoEventInfoProducer::RecoEventInfoProducer(const edm::ParameterSet& pset)
{
  vertexToken_ = pset.getParameter<edm::InputTag>("vertex");
  edm::InputTag hltLabel = pset.getParameter<edm::InputTag>("triggerResults");
  processName_ = hltLabel.process();
  hltToken_ = hltLabel;

  produces<int>("pvN");
  produces<double>("pvX");
  produces<double>("pvY");
  produces<double>("pvZ");
  produces<double>("weight");
  produces<double>("weight1");
  produces<double>("weight2");
  produces<double>("qScale");
  produces<double>("pthat");

  edm::ParameterSet hltSet = pset.getParameter<edm::ParameterSet>("HLT");
  const boost::regex matchVersion("_v[0-9\\*]+$"); // regexp from HLTrigger/HLTCore/HLTConfigProvider
  for ( auto& hltSetName : hltSet.getParameterNamesForType<strings>() )
    {
      const std::string hltGroupName = hltSetName;
      strings& hltPaths = hltGroup_[hltGroupName];
      hltPaths = hltSet.getParameter<strings>(hltGroupName);
      for ( auto& hltPath : hltPaths )
	{
	  hltPath = boost::regex_replace(hltPath, matchVersion, "");
	}
      produces<int>("HLT"+hltSetName);
    }
}

void RecoEventInfoProducer::beginRun(edm::Run& run, const edm::EventSetup& eventSetup)
{
  bool changed = true;
  if ( !hltConfig_.init(run, eventSetup, processName_, changed) ) 
    {
      edm::LogError("RecoEventInfoProducer") << "HLT config extraction failure with process name " << processName_;
    }

  //if ( changed ) 
  //{
  //  // The HLT config has actually changed wrt the previous Run, hence rebook your
  //  // histograms or do anything else dependent on the revised HLT config
  //}
}

void RecoEventInfoProducer::produce(edm::Event& event, const edm::EventSetup& eventSetup)
{
  double weight  = 1.;
  double weight1 = 0.;
  double weight2 = 0.;
  double qScale  = 0.;
  double pthat   = 0.;

  if (!event.isRealData()){
    edm::Handle<GenEventInfoProduct> eventInfos;
    event.getByLabel("generator", eventInfos);
    weight = eventInfos->weight();
    //std::cout << " as returned by the weight() method, integrated event weight = " << weight << std::endl;      
    if (eventInfos.isValid()){
      qScale = eventInfos->qScale();
      pthat = ( eventInfos->hasBinningValues() ? 
		(eventInfos->binningValues())[0] : 0.0);
      //std::cout << " qScale = " << qScale << " pthat = " << pthat << std::endl;
      weight1 = eventInfos->weights()[0]; // this is "stanrd Py6 evt weight;
      //std::cout << " weight1 = " << weight1 << std::endl;
      weight2 = eventInfos->weights()[1]; // in case you run in CSA mode or otherwise
      //std::cout << " weight2 = " << weight2 << std::endl;
    }
  }
  event.put(std::auto_ptr<double>(new double(weight)), "weight");
  event.put(std::auto_ptr<double>(new double(weight1)), "weight1");
  event.put(std::auto_ptr<double>(new double(weight2)), "weight2");
  event.put(std::auto_ptr<double>(new double(qScale)), "qScale");
  event.put(std::auto_ptr<double>(new double(pthat)), "pthat");

  edm::Handle<reco::VertexCollection> vertexHandle;
  event.getByLabel(vertexToken_, vertexHandle);

  const int nPV = vertexHandle->size();
  double pvX = 0, pvY = 0, pvZ = 0;
  if ( nPV > 0 )
    {
      pvX = vertexHandle->at(0).x();
      pvY = vertexHandle->at(0).y();
      pvZ = vertexHandle->at(0).z();
    }
  event.put(std::auto_ptr<int>(new int(nPV)), "pvN");
  event.put(std::auto_ptr<double>(new double(pvX)), "pvX");
  event.put(std::auto_ptr<double>(new double(pvY)), "pvY");
  event.put(std::auto_ptr<double>(new double(pvZ)), "pvZ");

  edm::Handle<edm::TriggerResults> hltHandle;
  event.getByLabel(hltToken_, hltHandle);

  for ( auto key = hltGroup_.begin(); key != hltGroup_.end(); ++key )
    {
      const std::string& hltGroupName = key->first;
      const strings& hltPaths = key->second;

      int psValue = 0;
      for ( auto& hltPath : hltPaths )
	{
	  const strings hltPathsWithV = HLTConfigProvider::restoreVersion(hltConfig_.triggerNames(), hltPath);
	  if ( hltPathsWithV.empty() ) continue;
	  const std::string& trigName = hltPathsWithV[0];

	  const unsigned int trigIndex = hltConfig_.triggerIndex(trigName);
	  if ( trigIndex < hltHandle->size() )
	    {
	      if ( hltHandle->accept(trigIndex) ) {
		const std::pair<int,int> prescales = hltConfig_.prescaleValues(event, eventSetup, trigName);
		psValue = prescales.first * prescales.second;
		break;
	      }
	    }
	}
      event.put(std::auto_ptr<int>(new int (psValue)), "HLT"+hltGroupName);
    }

}

DEFINE_FWK_MODULE(RecoEventInfoProducer);

