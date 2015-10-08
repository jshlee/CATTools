import FWCore.ParameterSet.Config as cms
import os
process = cms.Process("ColorCoherenceAnalyzer")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#datadir = '/xrootd/store/user/jlee/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/v7-4-2_RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/150925_123825/0000/'
#datadir = '/pnfs/user/cattuple/cat53v4-merged/'
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('file:/xrootd/store/user/jlee/SingleMuon/v7-4-1_Run2015C-PromptReco-v1/150913_173449/0000/catTuple_125.root')
    fileNames = cms.untracked.vstring()
)

#for f in os.listdir(datadir):
    #process.source.fileNames.append("file:"+datadir+f)
#process.source.fileNames.append("file:/pnfs/user/cattuple/cat53v4-merged/cat53v4_JetHT_Run2012C-22Jan2013-v1.root")
process.source.fileNames.append("file:/pnfs/user/cattuple/cat53x-qcd-sumEt/crab_cat53x-qcd-sumEt-MC_QCD_HT-100To250_TuneZ2star_8TeV-madgraph-pythia/results/catTuple_118.root")

print process.source.fileNames
#runOnMC=True
### for run data
#lumiFile = 'Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON.txt'
#lumiFile = 'Cert_246908-255031_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt'
#for i in process.source.fileNames:
#    if 'Run2015' in i:
#        runOnMC=False
#if not runOnMC:
#    from FWCore.PythonUtilities.LumiList import LumiList
#    lumiList = LumiList(os.environ["CMSSW_BASE"]+'/src/CATTools/CatProducer/prod/LumiMask/'+lumiFile)
#    process.source.lumisToProcess = lumiList.getVLuminosityBlockRange()
#    print process.source.lumisToProcess
process.cc = cms.EDAnalyzer("ColorCoherenceAnalyzer",
    vtx = cms.InputTag("recoEventInfo", "pvN"),
    jets = cms.InputTag("catJets","","CAT"),
    mets = cms.InputTag("catMETs"),
    hlt80 = cms.InputTag("recoEventInfo", "HLTPFJet80"),
    hlt140 = cms.InputTag("recoEventInfo", "HLTPFJet140"),
    hlt320 = cms.InputTag("recoEventInfo", "HLTPFJet320"),

    #triggerBits = cms.InputTag("TriggerResults","","HLT"),
    #triggerObjects = cms.InputTag("selectedPatTrigger"),
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("test_cc.root")
)
process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring('ProductNotFound'))
process.p = cms.Path(process.cc)
process.MessageLogger.cerr.FwkReport.reportEvery = 50000

#process.source.fileNames = ['file:/pnfs/user/cattuple/cat53v4-merged/cat53v4_Jet_Run2012A-22Jan2013-v1.root']
