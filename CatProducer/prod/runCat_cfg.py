from CATTools.CatProducer.catTemplate_cfg import *
process.load('Configuration.Geometry.GeometryExtended2023SHCalNoTaper4EtaReco_cff')
process.load('Configuration.Geometry.GeometryExtended2023SHCalNoTaper4Eta_cff')
#process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2019_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')

## some options
doSecVertex=False # for jpsi candidates
doTriggerSkim=False # for qcd trigger skim on data

## setting up arguements
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('python')
options.register('runOnMC', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "runOnMC: True default")
options.register('globalTag', '', VarParsing.multiplicity.singleton, VarParsing.varType.string, "globalTag: 1  default")

options.parseArguments()
runOnMC = options.runOnMC
globalTag = options.globalTag

if globalTag:
    process.GlobalTag.globaltag = cms.string(globalTag)
if not globalTag:
    from Configuration.AlCa.autoCond import autoCond
    if runOnMC:
        process.GlobalTag.globaltag = autoCond['startup']
    else:
        process.GlobalTag.globaltag = autoCond['com10']
print "using globaltag", process.GlobalTag.globaltag

####################################################################################################
## running PAT
postfix = "PFlow"
jetAlgo="AK5"
from CATTools.CatProducer.catPatSetup_cff import *
catPatConfig(process, runOnMC, postfix, jetAlgo, doTriggerSkim)

####################################################################################################

from CATTools.CatProducer.catSetup_cff import *
catSetup(process, runOnMC, doSecVertex)

from CATTools.CatProducer.catEventContent_cff import catEventContentExtended
process.out.outputCommands = catEventContentExtended

process.maxEvents.input = options.maxEvents

process.source.fileNames = options.inputFiles
#process.source.skipEvents=cms.untracked.uint32(7000)
## to suppress the long output at the end of the job
process.MessageLogger.cerr.threshold = ''
if options.maxEvents < 0:
    process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options.wantSummary = False
process.options.allowUnscheduled = cms.untracked.bool(True)

process.pfIsolatedMuonsPFlow.cut = cms.string('pt > 5')
process.pfMuonsFromVertexPFlow.d0Cut = cms.double(1000)
process.pfMuonsFromVertexPFlow.dzSigCut = cms.double(999999.0)
process.pfMuonsFromVertexPFlow.dzCut = cms.double(1000)
process.pfMuonsFromVertexPFlow.d0SigCut = cms.double(999999.0)

#process.pfPileUpPFlow.Enable = cms.bool(True)
