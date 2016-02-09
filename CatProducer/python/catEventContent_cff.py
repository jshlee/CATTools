import FWCore.ParameterSet.Config as cms

catEventContent = cms.untracked.vstring()
catEventContentExtended = cms.untracked.vstring()
catEventContentRD = cms.untracked.vstring()

catEventContent.extend([
    'keep *_catMuons_*_*',
    'keep *_catElectrons_*_*',
    'keep *_catPhotons_*_*',
    'keep *_catJets_*_*',
    'keep *_catMETs_*_*',
    'keep *_catMCParticles_*_*',
    'keep *_catGenTops_*_*',
    'keep edmTriggerResults_TriggerResults__*',
    'keep *_catTrigger_*_*',
    ])

catEventContentExtended.extend([
    'drop *',
    'keep *_cat*_*_*',
    #'keep *_goodOfflinePrimaryVertices_*_*',
    'keep recoGenParticles_genParticles_*_*',
    'keep recoGenJets_selectedPatJetsPFlow_*_*',
    "keep GenEventInfoProduct_generator_*_*",
    "keep *_recoEventInfo_*_*",
    "keep *_pdfWeight_*_*",
    "keep *_pileupWeight_*_*",
    'keep edmTriggerResults_TriggerResults__*',
    'keep *_catTrigger_*_*',
    ])

catEventContentRD.extend([
    'keep *_lumiMask*_*_*'
])
