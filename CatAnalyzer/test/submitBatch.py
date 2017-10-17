#!/usr/bin/env python 
# catGetDatasetInfo v7-4-4 # to make dataset lists
# sed -i 's/^\/store/root:\/\/cms-xrdr.sdfarm.kr:1094\/\/xrd\/store/g' *

import os
username = os.environ['USER']

analysis = 'h2muAnalyzer'
#analysis = 'TtbarDiLeptonAnalyzer'

pythonCfg = 'run_'+analysis+'_cfg.py'
#analysis=analysis+'Silver'
RunFiles = [
              'WMinusH_HToMuMu',
              'WPlusH_HToMuMu',
              'ZH_HToMuMu',
              'VBF_HToMuMu',
              'GG_HToMuMu',
              "WWTo2L2Nu",
              "WZTo3LNu_amcatnlo",
              "WZTo2L2Q",
              "ZZTo2L2Nu",
              "ZZTo2L2Q",
              "ZZTo4L",
              "WWW",
              "WWZ",
              "WZZ",
              "ZZZ",
              "ttZToLLNuNu",
              "ttWToLNu",
              "SingleTop_tW_noHadron",
              "SingleTbar_tW_noHadron",
              "SingleTop_tW",
              "SingleTbar_tW",
              "TTJets_DiLept",
              "TTJets_DiLept_Tune4",
              'TTJets_aMC', 
              'DYJets',
              'DYJets_MG_10to50',
              'DYJets_MG2',
              'DYJets_2J',
              'DYJets_1J',
              'DYJets_0J',
              'DYJets_10to50', 
              'SingleMuon2_Run2016B',
              'SingleMuon2_Run2016C',
              'SingleMuon2_Run2016D',
              'SingleMuon2_Run2016E',
              'SingleMuon2_Run2016F',
              'SingleMuon2_Run2016G',
              'SingleMuon2_Run2016H',
              'SingleMuon_Run2016B',
              'SingleMuon_Run2016C',
              'SingleMuon_Run2016D',
              'SingleMuon_Run2016E',
              'SingleMuon_Run2016F',
              'SingleMuon_Run2016G',
              'SingleMuon_Run2016H',
              ]
import os,json
datadir = os.environ["CMSSW_BASE"]+'/src/CATTools/CatAnalyzer/data/dataset/'
dataset_json = datadir + 'dataset.json'
version = os.environ["CMSSW_VERSION"]
for i in RunFiles:
    datasetName = i
#with open(dataset_json) as data_file:    
#    data = json.load(data_file)
#    for i in data:
#        print data[0]
#        datasetName = i['name']
#        if "QCD" in datasetName:
#            continue
#        if "Electron" in datasetName:
#            continue       
#        if "Photon" in datasetName:
#            continue 
#        if "Double" in datasetName:
#            continue 
#        if "JetHT_Run" in datasetName:
#            continue 
#        if "star" in datasetName:
#            continue
#        if "TT_powheg" in datasetName:
#            continue 
#        if "MuonEG" in datasetName:
#            continue 
#        if "TTTT" in datasetName:
#            continue 

    fileList = datadir + 'dataset_' + datasetName + '.txt'
    jobName = analysis+'_'+datasetName
    #createbatch = "create-batch --cfg %s --jobName %s --fileList %s --maxFiles 10"%(pythonCfg, jobName, fileList) 
    #createbatch = "create-batch --cfg %s --jobName %s --fileList %s --maxFiles 50 --transferDest \"root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/pseudotop/ntuples/%s/%s\""%(pythonCfg, jobName, fileList, version, datasetName)
    createbatch = "create-batch --cfg %s --jobName %s --fileList %s --maxFiles 50 --transferDest \"root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/%s/cattreeMuEl/%s/%s\""%(pythonCfg, jobName, fileList, username, version, datasetName)
    print createbatch
    os.system(createbatch)
