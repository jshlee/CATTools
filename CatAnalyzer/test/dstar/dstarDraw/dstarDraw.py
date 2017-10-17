#!/usr/bin/env python
import ROOT, CATTools.CatAnalyzer.CMS_lumi, json, os, getopt, sys, math
from CATTools.CatAnalyzer.histoHelper import *
import DYestimation
ROOT.gROOT.SetBatch(True)
'''
topDraw.py -a 1 -s 1 -c 'tri==1&&filtered==1' -b [40,0,40] -p nvertex -x 'no. vertex' &
topDraw.py -a 1 -s 1 -b [100,-3,3] -p lep1_eta,lep2_eta -x '#eta' &
'''
#datalumi = 5.98 #3.21 #5.98 #4.14 #4.41 #2.66#5.98 # Run2016 BtoHv3(v806)
datalumi = 35.92 # Run2016 BtoHv3(v806)
#datalumi = 19.7  # Run2016 BtoF(v806)
#datalumi = 16.07  # Run2016 GtoHv3(v806)
CMS_lumi.lumi_sqrtS = "%.1f fb^{-1}, #sqrt{s} = 13 TeV"%(datalumi)
datalumi = datalumi*1000 # due to fb
CMS_lumi.extraOverCmsTextSize  = 0.65
CMS_lumi.extraText  = "Private work"

#mcfilelist = ['TT_powheg', 'WJets', 'ZZ', 'WW', 'WZ', 'DYJets', 'DYJets_10to50']
mcfilelist = ['TT_powheg', 'WJets', 'SingleTbar_tW', 'SingleTop_tW', 'ZZ', 'WW', 'WZ', 'DYJets', 'DYJets_10to50']
#mcfilelist = ['TT_powheg', 'WJets', 'ZZ', 'WW', 'WZ', 'DYJets', 'DYJets_10to50']
#rdfilelist = ['MuonEG_Run2016B','DoubleEG_Run2016B','DoubleMuon_Run2016B']
rdfilelist = ['MuonEG_Run2016','DoubleEG_Run2016','DoubleMuon_Run2016']
#rdfilelist = ['MuonEG_Run2016_BtoF','DoubleEG_Run2016_BtoF','DoubleMuon_Run2016_BtoF']
#rdfilelist = ['MuonEG_Run2016_GtoHv3','DoubleEG_Run2016_GtoHv3','DoubleMuon_Run2016_GtoHv3']
#rdfilelist = ['MuonEG_Run2016B','MuonEG_Run2016C','MuonEG_Run2016D','MuonEG_Run2016E','MuonEG_Run2016F','MuonEG_Run2016G','MuonEG_Run2016H_v2','MuonEG_Run2016H_v3','DoubleEG_Run2016B','DoubleEG_Run2016C','DoubleEG_Run2016D','DoubleEG_Run2016E','DoubleEG_Run2016F','DoubleEG_Run2016G','DoubleEG_Run2016H_v2','DoubleEG_Run2016H_v3','DoubleMuon_Run2016B','DoubleMuon_Run2016C','DoubleMuon_Run2016D','DoubleMuon_Run2016E','DoubleMuon_Run2016F','DoubleMuon_Run2016G','DoubleMuon_Run2016H_v2','DoubleMuon_Run2016H_v3']
rootfileDir = "/xrootd/store/user/seulgi/topmass_806_171010/results_merged/cattree_"
#rootfileDir = "/xrootd/store/user/dayoung/topmass_806_170921/results_merged/cattree_"
#rootfileDir = "/xrootd/store/user/quark2930/dilepton_mass_v806_17032301/cattree_"
#rootfileDir = "/xrootd/store/user/king11kr/ntuples_TtbarDstar_v806/CMSSW_8_0_26_patch1/"
#rootfileDir = "/xrootd/store/user/jhkim/ntuples_topDstar_v806_170718/results_merged/TtbarDiLeptonAnalyzer_"
channel_name = ['MuEl', 'ElEl', 'MuMu']

datasets = json.load(open("%s/src/CATTools/CatAnalyzer/data/dataset/dataset.json" % os.environ['CMSSW_BASE']))

#defalts
step = 1
channel = 0 #combined: channel = 0
cut = 'tri!=0&&filtered==1'
#cut = 'tri==1&&filtered==1&&is3lep==2'
#weight = 'genweight*puweight*mueffweight*eleffweight*tri'
#cut = '1==1'
#weight = 'genweight*puweight*mueffweight*eleffweight*topPtWeight'
weight = 'genweight*puweight*mueffweight*eleffweight*btagweight'#topPtWeight*tri'
binning = [60, 20, 320]
plotvar = 'dilep.M()'
x_name = 'mass [GeV]'
y_name = 'Events'
dolog = False
overflow = False
binNormalize = False
suffix = ''

tname = "cattree/nom"

#get input
try:
    opts, args = getopt.getopt(sys.argv[1:],"hdnot:c:w:b:p:x:y:a:s:f:",["tree","binNormalize","overflow","cut","weight","binning","plotvar","x_name","y_name","dolog","channel","step","suffix"])
except getopt.GetoptError:          
    print 'Usage : ./dstarDraw.py -c <cut> -w <weight> -b <binning> -p <plotvar> -x <x_name> -y <y_name> -d <dolog> -f <suffix>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'Usage : ./dstarDraw.py -c <cut> -w <weight> -b <binning> -p <plotvar> -x <x_name> -y <y_name> -d <dolog> -f <suffix>'
        sys.exit()
    elif opt in ("-t", "--tree"):
        tname = "cattree/" + arg 
    elif opt in ("-c", "--cut"):
        cut = arg
        #cut = "%s&&%s"%(cut,arg)
    elif opt in ("-a", "--channel"):
        channel = int(arg)
    elif opt in ("-s", "--step"):
        step = int(arg)
    elif opt in ("-w", "--weight"):
        weight = arg
    elif opt in ("-b", "--binning"):
        binning = eval(arg)
    elif opt in ("-p", "--plotvar"):
        plotvar = arg
    elif opt in ("-x", "--x_name"):
        x_name = arg
    elif opt in ("-y", "--y_name"):
        y_name = arg
    elif opt in ("-d", "--dolog"):
        dolog = True
    elif opt in ("-o", "--overflow"):
        overflow = True
    elif opt in ("-n", "--binNormalize"):
        binNormalize = True
    elif opt in ("-f", "--suffix"):
        suffix = "_"+arg

#cut define
stepch_tcut =  'step>=%i&&channel==%i'%(step,channel)
ttother_tcut = '!(gen_partonChannel==2 && gen_partonMode==gen_pseudoChannel && gen_partonMode==%d)'%(channel)
if channel == 0:
    ttother_tcut = '!(gen_partonChannel==2 && gen_partonMode==gen_pseudoChannel && gen_partonMode==channel && gen_partonMode!=0)'
    stepch_tcut =  'step>=%i'%(step)
    #stepch_tcut =  '1==1'
if step == 6: stepch_tcut = stepch_tcut+'&&step6'#desy smeared

tcut = '(%s&&%s)*(%s)'%(stepch_tcut,cut,weight)
ttother_tcut = '(%s&&%s&&%s)*(%s)'%(stepch_tcut,cut,ttother_tcut,weight)
rd_tcut = '%s&&%s'%(stepch_tcut,cut)
#print "TCut =",tcut

'''
#namming
unit = ""
if len(binning) == 3:
    num = (binning[2]-binning[1])/float(binning[0])
    if num != 1:
       if x_name.endswith(']'):
            unit = x_name.split('[')[1]
            print "unit =", unit
            unit = unit.split(']')[0]
            print "unit =", unit
        y_name = y_name + " / %.2g %s"%(num,unit)
        print "y_name =", yname
if len(binning) == 3 : nbins = binning[0]
else : nbins = len(binning)-1
'''

#DYestimation
if not os.path.exists('./DYFactor.json'):
    DYestimation.printDYFactor(rootfileDir, tname, datasets, datalumi, cut, weight, rdfilelist)#This will create 'DYFactor.json' on same dir.
dyratio=json.load(open('./DYFactor.json'))

#title_l = ["t#bar{t}", "W+jets", "Single top", "Single top", "Dibosons", "Dibosons", "Dibosons", "Z/#gamma^{*}#rightarrow#font[12]{l#lower[-0.4]{+}l#lower[-0.4]{#font[122]{\55}}}", "Z/#gamma^{*}#rightarrow#font[12]{l#lower[-0.4]{+}l#lower[-0.4]{#font[122]{\55}}}"]
sysNameList = ['jer','jes','mu','el','puweight','mueffweight','eleffweight','btagweight']

#saving mc histos
errList = []
mchistList = []
sysErr_up = []
sysErr_dn = []
for sysname in sysNameList:
    sysErr_up.append(defTH1(sysname+'_up', sysname+'_up', binning))
    sysErr_dn.append(defTH1(sysname+'_dn', sysname+'_dn', binning))

for i, mcname in enumerate(mcfilelist):
    data = findDataSet(mcname, datasets)
    scale = datalumi*data["xsec"]
    #print "datalumi:%.2f, data[xec]:%.2d, scale:%.2d"%(datalumi,data["xsec"],scale)
    colour = data["colour"]
    title = data["title"]
    #title = title_l[i]
    if ('DYJets' in mcname) and channel!=0:
        scale = scale*dyratio[channel][step]

    rfname = rootfileDir + mcname +".root"
    tfile = ROOT.TFile(rfname)
    wentries = tfile.Get("cattree/nevents").Integral()
    scale = scale/wentries
    #print scale
    print "wentries:%.2d, scale:%.2d"%(wentries,scale)
    #if 'TT' in mcname:
    #    scale = scale * 0.8
		
    N = getWeightedEntries(rfname, tname, 'tri', tcut)
    err = math.sqrt(abs(N))*scale
    print "N:", N, "err:", err

    mchist = makeTH1(rfname, tname, title, binning, plotvar, tcut, scale)
    #for i, sysname in enumerate(sysNameList):
    #    if 'weight' in sysname:
    #        sysErr_up[i].Add(makeTH1(rfname, tname, title, binning, plotvar, tcut.replace(sysname,sysname+'_up'), scale))
    #        sysErr_dn[i].Add(makeTH1(rfname, tname, title, binning, plotvar, tcut.replace(sysname,sysname+'_dn'), scale))
    #    else:
    #        sysErr_up[i].Add(makeTH1(rfname, "cattree/%s_u"%sysname, title, binning, plotvar, tcut, scale))
    #        sysErr_dn[i].Add(makeTH1(rfname, "cattree/%s_d"%sysname, title, binning, plotvar, tcut, scale))

    mchist.SetLineColor(colour)
    mchist.SetFillColor(colour)
    if overflow: overFlow(mchist)
    mchistList.append(mchist)
    
    if 'TT' in mcname:
        if len(binning) == 3:
            ttothershist = ROOT.TH1D("name_others", title+' others', binning[0], binning[1], binning[2])
        else:
            ttothershist = ROOT.TH1D("name_others", title+' others', len(binning)-1, array.array('f', binning))

        dstar_tcut = "((%s&&%s)&&abs(dstar_relPtTrue)<0.1&&abs(dstar_dRTrue)<0.1&&abs(d0_dRTrue)<0.1&&abs(d0_relPtTrue)<0.1)*(%s)"%(stepch_tcut,cut,weight)
        d0_tcut = "((%s&&%s)&&(abs(d0_relPtTrue)<0.1&&abs(d0_dRTrue)<0.1)&&!(abs(dstar_relPtTrue)<0.1&&abs(dstar_dRTrue)<0.1))*(%s)"%(stepch_tcut,cut,weight)

        d0_true_hist = makeTH1(rfname, tname, title+'(w D0)', binning, plotvar, d0_tcut, scale)
        dstar_true_hist = makeTH1(rfname, tname, title+'(w D*)', binning, plotvar, dstar_tcut, scale)
        #ttddothershist.Add(ttothers)
        d0_true_hist.SetLineColor(906)
        d0_true_hist.SetFillColor(906)
        dstar_true_hist.SetLineColor(806)
        dstar_true_hist.SetFillColor(806)
        
        mchistList.append(d0_true_hist)
        mchistList.append(dstar_true_hist)
        mchist.Add(d0_true_hist, -1)
        mchist.Add(dstar_true_hist, -1)

    errList.append(err)

#data histo
if channel != 0:
    rfname = rootfileDir + rdfilelist[channel-1] +".root"
    rdhist = makeTH1(rfname, tname, 'data', binning, plotvar, rd_tcut)
else:
    rdhist = mchistList[0].Clone()
    rdhist.Reset()
    for i, rdfile in enumerate(rdfilelist):
        rfname = rootfileDir + rdfile +".root"
        rdtcut = 'channel==%d&&%s&&%s'%((i+1),stepch_tcut,cut)
        rdhist.Add(makeTH1(rfname, tname, 'data', binning, plotvar, rdtcut))
if overflow: overFlow(rdhist)
rdhist.SetLineColor(1)
nbins = rdhist.GetNbinsX()

#namming
unit = ""
if len(binning) == 3 and rdhist.GetBinWidth(1) != 1:
    if x_name.endswith(']'):
        unit = x_name.split('[')[1]
        unit = unit.split(']')[0]
    y_name = y_name + " / %.2g %s"%(rdhist.GetBinWidth(1),unit)

#error band(sys)
errorBand = copy.deepcopy(rdhist)
errorBand.SetFillColor(14)
errorBand.SetFillStyle(3001)
errorBand.SetMarkerStyle(0)

h_nom = defTH1("nom", "nom", binning)
for h in mchistList:
    h_nom.Add(h)

#for i in range(len(sysNameList)):
#    overFlow(sysErr_up[i])
#    overFlow(sysErr_dn[i])
#    sysErr_up[i].Add(h_nom, -1)
#    sysErr_dn[i].Add(h_nom, -1)
#    for j in range(1,nbins+1):
#        maxErr = max(abs(sysErr_up[i].GetBinContent(j)), abs(sysErr_dn[i].GetBinContent(j)))
#        sumErr = math.sqrt(errorBand.GetBinError(j)**2+maxErr**2) 
#        errorBand.SetBinError(j, sumErr)

#get event yeild table
#num, err = table(mchistList, errList, mchistList[0], errList[0])
#for k in num.keys():
#    print '%s  ~&~ $%8d \\pm %6.2f$'%(k, max(0,num[k]), err[k])
#print 'data  ~&~ $%8d           $ \n'%rdhist.Integral(0,nbins+1)

#overflow
if overflow:
    for hist in mchistList:
        hist.SetBinContent(nbins, hist.GetBinContent(nbins)+hist.GetBinContent(nbins+1))
        hist.SetBinContent(1, hist.GetBinContent(1)+hist.GetBinContent(0))
    rdhist.SetBinContent(nbins, rdhist.GetBinContent(nbins)+rdhist.GetBinContent(nbins+1))
    rdhist.SetBinContent(1, rdhist.GetBinContent(1)+rdhist.GetBinContent(0))

'''
#bin normalize
if binNormalize and len(binning)!=3:
    for hist in mchistList:
        for i in range(len(binning)):
            hist.SetBinContent(i, hist.GetBinContent(i)/hist.GetBinWidth(i))
            hist.SetBinError(i, hist.GetBinError(i)/hist.GetBinWidth(i))
    for i in range(len(binning)):
        rdhist.SetBinContent(i, rdhist.GetBinContent(i)/rdhist.GetBinWidth(i))
        rdhist.SetBinError(i, rdhist.GetBinError(i)/rdhist.GetBinWidth(i))
    y_name = y_name + "/%s"%(unit)
'''

# Getting # of events
fIntMC = 0.0

for mchist in mchistList:
  fIntMC = fIntMC + mchist.Integral()

print "Integral (MC) : ", step, channel, fIntMC
print "Integral (data) : ", step, channel, rdhist.Integral()

'''
#Drawing plots on canvas
var = plotvar.split(',')[0]
#var = ''.join(i for i in var if not i.isdigit())
var = var.replace('.','_').lower()
var = var.replace('()','')
#outfile = "%s_s%d_%s%s"%(channel_name[channel-1],step,var,suffix)
outfile = "%s_s%d_%s.png"%(channel_name[channel-1],step,var)
#if channel == 0: outfile = "Dilepton_s%d_%s%s"%(step,var,suffix)
if channel == 0: outfile = "Dilepton_s%d_%s.png"%(step,var)
canv = drawTH1(outfile, CMS_lumi, mchistList, rdhist, x_name, y_name, dolog, True, 0.5)

canv.SaveAs(outfile)
print outfile
'''

#bin normalize
if binNormalize:
    for hist in mchistList:
        hist.Scale(1,"width")
    rdhist.Scale(1,"width")
    errorBand.Scale(1,"width")

#Drawing plots on canvas
var = plotvar.split(',')[0]
var = ''.join(i for i in var if not i.isdigit())
var = var.replace('.','_').lower()
var = var.replace('()','')
outfile = "%s_s%d_%s.png"%(channel_name[channel-1],step,var)
if channel == 0: outfile = "Dilepton_s%d_%s.png"%(step,var)
canv = drawTH1(outfile, CMS_lumi, mchistList, rdhist, x_name, y_name, dolog, True, 0.5)

## Additional draw
## you can get list of objects on canvavs via 'canv.GetListOfPrimitives()'
## in case you know the name, 'obj = canv.GetPrivmitive(name)'
mainPad = canv.GetPrimitive("mainPad")
mainPad.cd()
errorBand.Draw("e2same")
mainPad.GetPrimitive("data").Draw("esamex0")
extraText(canv, [0.3,0.85], outfile.split("_")[0])
canv.Update()

ratioPad = canv.GetPrimitive("ratioPad")
ratioPad.cd()
#sysErrRatio = errorBand.Clone()
#sysErrRatio.Divide(rdhist)
#sysErrRatio.Draw("e2same")
ratioPad.GetPrimitive("hratio").Draw("esame")
canv.Update()

canv.SaveAs(outfile)
#canv.SaveAs(outfile.replace(".png",".pdf"))
print outfile

