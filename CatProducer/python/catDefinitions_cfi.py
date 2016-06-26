import FWCore.ParameterSet.Config as cms

bunchCrossing  = 25
globalTag_mc   = '80X_mcRun2_asymptotic_2016_miniAODv2'
globalTag_rd   = '80X_dataRun2_Prompt_v8'
#lumiJSON       = 'Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON'
lumiJSON       = 'Cert_271036-275125_13TeV_PromptReco_Collisions16_Plus_DCSOnly_275282-275782_JSON'
pileupMCmap    = '2016_25ns_SpringMC'

JetEnergyCorrection = 'Spring16_25nsV3'
#JECUncertaintyFile  = 'CATTools/CatProducer/data/JEC/%s_DATA_UncertaintySources_AK4PFchs.txt'%JetEnergyCorrection
JECUncertaintyFile  = 'CATTools/CatProducer/data/JEC/%s_DATA_Uncertainty_AK4PFchs.txt'%JetEnergyCorrection

