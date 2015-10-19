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

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

#include <boost/regex.hpp>

#include <memory>
#include <vector>
#include <string>

class CATTriggerProducer : public edm::EDProducer
{
public:
  CATTriggerProducer(const edm::ParameterSet& pset);
  void produce(edm::Event& event, const edm::EventSetup& eventSetup);
  void beginRun(const edm::Run& run, const edm::EventSetup& eventSetup);

private:
  typedef std::vector<double> doubles;
  typedef std::vector< std::string > strings;
  typedef std::vector< std::pair < std::string, std::string> > pairstrings;

  edm::InputTag triggerBits_;
  edm::InputTag triggerObjects_;
  edm::InputTag metFilterBitsPAT_;
  edm::InputTag metFilterBitsRECO_;

  strings selectTrigObjects_;
  pairstrings hltNames_;
  pairstrings metFilterNames_;
  //HLTConfigProvider hltConfig_;
};

CATTriggerProducer::CATTriggerProducer(const edm::ParameterSet& pset)
{
  triggerBits_ = pset.getParameter<edm::InputTag>("triggerBits");
  triggerObjects_ = pset.getParameter<edm::InputTag>("triggerObjects");
  metFilterBitsPAT_ = pset.getParameter<edm::InputTag>("metFilterBitsPAT");
  metFilterBitsRECO_ = pset.getParameter<edm::InputTag>("metFilterBitsRECO");

  const boost::regex matchVersion("_v[0-9\\*]+$"); // regexp from HLTrigger/HLTCore/HLTConfigProvider

  for ( auto& selectTrigObject : pset.getParameter<strings>("selectTrigObjects") ){
    selectTrigObjects_.push_back(selectTrigObject);
  }
  if (selectTrigObjects_.size()){
    produces<pat::TriggerObjectStandAloneCollection >();
  }

  for ( auto& hltPath : pset.getParameter<strings>("hltPathNames") ){
    hltPath = boost::regex_replace(hltPath, matchVersion, "");
    std::string hltSavedAs = hltPath;
    hltSavedAs.erase(std::remove(hltSavedAs.begin(), hltSavedAs.end(), '_'), hltSavedAs.end());
    std::cout << " " << hltPath << std::endl;
    produces<int >( hltSavedAs );
    hltNames_.push_back(std::make_pair(hltPath, hltSavedAs));
  }
  for ( auto& hltPath : pset.getParameter<strings>("metFilterNames") ){
    std::cout << " " << hltPath << std::endl;
    produces<bool >( hltPath );
    metFilterNames_.push_back(std::make_pair("Flag_"+hltPath, hltPath));
  }
}

void CATTriggerProducer::beginRun(const edm::Run& run, const edm::EventSetup& eventSetup)
{
  // bool changed = true;
  // if ( !hltConfig_.init(run, eventSetup, processName_, changed) )
  // {
  //   edm::LogError("CATTriggerProducer") << "HLT config extraction failure with process name " << processName_;
  // }

  // if ( changed )
  // {
  //   edm::LogError("CATTriggerProducer") << "HLT config has changed " << processName_;
  //  // The HLT config has actually changed wrt the previous Run, hence rebook your
  //  // histograms or do anything else dependent on the revised HLT config
  // }
}

void CATTriggerProducer::produce(edm::Event& event, const edm::EventSetup& eventSetup)
{
  edm::Handle<edm::TriggerResults> triggerBits;
  event.getByLabel(triggerBits_, triggerBits);

  const edm::TriggerNames &trigNames = event.triggerNames(*triggerBits);

  if (selectTrigObjects_.size()){
    // filtering TriggerObjectStandAlone
    edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
    event.getByLabel(triggerObjects_, triggerObjects);
    pat::TriggerObjectStandAloneCollection *catTriggerObjects = new pat::TriggerObjectStandAloneCollection();
    for (pat::TriggerObjectStandAlone trigObj : *triggerObjects) { // note: not "const &" since we want to call unpackPathNames
      bool keepTriggerObject = false;
      //trigObj.unpackPathNames(trigNames);
      std::vector<std::string> pathNamesAll  = trigObj.pathNames(false);
      for (unsigned h = 0, n = pathNamesAll.size(); h < n; ++h) {
	for ( auto& selectTrigObject : selectTrigObjects_ ){
	  if (pathNamesAll[h].find(selectTrigObject) == 0){
	    if (trigObj.hasPathName( pathNamesAll[h], true, true )){
	      keepTriggerObject = true;
	    }
	  }
	}
      }
      if (keepTriggerObject){
	//trigObj.packPathNames(trigNames);
	catTriggerObjects->push_back(trigObj);
      }
    }

    event.put(std::auto_ptr<pat::TriggerObjectStandAloneCollection>(catTriggerObjects));
  }

  if (hltNames_.size()){
    // saving trigger info as preScale value (int)
    for ( auto& hltPath : hltNames_ ){
      const strings hltPathsWithV = HLTConfigProvider::restoreVersion(trigNames.triggerNames(), hltPath.first);
      int psValue = 0;
      if ( hltPathsWithV.empty() ){
	//std::cout << "Warning:: trigger does not exist "<< hltPath.first << std::endl;
	continue;
      }
      const std::string& trigName = hltPathsWithV[0];
      unsigned int trigIndex = trigNames.triggerIndex(trigName);
      if ( trigIndex < triggerBits->size() ){
	if ( triggerBits->accept(trigIndex) ) {
	  psValue = 1;
	}
      }
      event.put(std::auto_ptr<int>(new int (psValue)), hltPath.second);
    }
  }
  if (metFilterNames_.size()){
    // save filter info
    edm::Handle<edm::TriggerResults> metFilterBits;
    if (!event.getByLabel(metFilterBitsPAT_, metFilterBits)){
      event.getByLabel(metFilterBitsRECO_, metFilterBits);
    }
    const edm::TriggerNames &metFilterNames = event.triggerNames(*metFilterBits);

    for ( auto& hltPath : metFilterNames_ ){
      bool passMet = false;
      unsigned int trigIndex = metFilterNames.triggerIndex(hltPath.first);
      if ( trigIndex < metFilterBits->size() ){
	if ( metFilterBits->accept(trigIndex) )
	  passMet = true;
      }
      event.put(std::auto_ptr<bool>(new bool (passMet)), hltPath.second);
    }
  }
  // // for full list of metFilterger names that pass
  // for (unsigned int i = 0, n = metFilterBits->size(); i < n-3; ++i) {
  //   std::cout << i << " metFiltername "<<metFilterNames.triggerName(i)<< std::endl;
  // }

}

DEFINE_FWK_MODULE(CATTriggerProducer);

