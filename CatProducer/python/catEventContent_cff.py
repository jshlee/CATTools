import FWCore.ParameterSet.Config as cms

catEventContent = cms.untracked.vstring()
catEventContentExtended = cms.untracked.vstring()

catEventContent.extend([
    'keep *_catMuons_*_*',
    'keep *_catElectrons_*_*',
    'keep *_catPhotons_*_*',
    'keep *_catJets_*_*',
    'keep *_catMETs_*_*',
    'keep *_catMCParticles_*_*',
    'keep *_catGenTops_*_*',
    ])

catEventContentExtended.extend([
    'drop *',
    'keep *_catJets_*_*',
    'keep *_catMuons_*_*',
    'keep *_catMETs_*_*',
    'keep *_me0SegmentMatching_*_*',
    'keep *_goodOfflinePrimaryVertices_*_*',
    'keep recoGenParticles_genParticles_*_*',
    'keep recoGenJets_selectedPatJetsPFlow_*_*',
    ])
