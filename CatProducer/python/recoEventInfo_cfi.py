import FWCore.ParameterSet.Config as cms

recoEventInfo = cms.EDProducer("RecoEventInfoProducer",
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    triggerResults = cms.InputTag("TriggerResults", "", "HLT"),
    HLT = cms.PSet(
        #DoubleMu = cms.vstring("HLT_Mu17_Mu8_v*", "HLT_Mu17_TkMu8_v*"),
        #for qcd jet analysis
        ## Jet40 = cms.vstring("HLT_Jet40_v*"),
        ## Jet60 = cms.vstring("HLT_Jet60_v*"),
        ## Jet80 = cms.vstring("HLT_Jet80_v*"),

        ## PFJet40 = cms.vstring("HLT_PFJet40_v*"),
        ## PFJet60 = cms.vstring("HLT_PFJet60_v*"),
        
        ## PFJet80  = cms.vstring("HLT_PFJet80_v*"),
        ## PFJet140 = cms.vstring("HLT_PFJet140_v*"),
        ## PFJet320 = cms.vstring("HLT_PFJet320_v*"),
    ),
)

