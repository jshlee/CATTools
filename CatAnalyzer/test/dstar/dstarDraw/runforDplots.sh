#!/bin/bash

treename='nom'

if [ $# != "0" ]; then
	treename=$1
fi

#cut='d0_L3D>0.2 && d0_LXY>0.1&& dstar_L3D>0.2 && dstar_LXY>0.1 && abs(dstar_diffMass-0.145)<0.01'
#cut='abs(dstar_diffMass-0.145)<0.02 && dstar_LXY>0.09'
cut='tri!=0&&filtered==1'
cut_d0='tri!=0&&filtered==1&&d0_L3D>0.2&&d0_LXY>0.1' #&&abs(d0.M()-1.8648)<0.040'
cut_dstar='tri!=0&&filtered==1&&d0_L3D>0.2&&d0_LXY>0.1&&dstar_L3D>0.2&&dstar_LXY>0.1' #&&abs(dstar_diffMass-0.145)<0.01'
cut_dstar_nomassConstain='d0_L3D>0.2&&d0_LXY>0.1&&dstar_L3D>0.2&&dstar_LXY>0.1'
cut_dstar_noCut='abs(dstar_diffMass-0.145)<0.01'

eval `scramv1 runtime -sh`

#for step in 5 
#for step in 1 2 3 4 5 
#do
#./dstarDraw.py -t $treename -s $step -b [40,0,40] -p 'nvertex' -x 'no. vertex' > /dev/null &
#./dstarDraw.py -t $treename -s $step -b [60,20,320] -p dilep.M\(\) -x 'M(ll) [GeV]' > /dev/null &
#./dstarDraw.py -t $treename -s $step -b [10,0,10] -p 'njet' -x 'Jet Multiplicity' > /dev/null &
#./dstarDraw.py -t $treename -s $step -b [20,0,200] -p 'met' -x 'Missing Et [GeV]' > /dev/null &
#./dstarDraw.py -t $treename -s $step -b [6,0,6] -p 'nbjet' -x 'b Jet Multiplicity' > /dev/null &
#./dstarDraw.py -t $treename -s $step -b [9,20,290] -p lep1.Pt\(\),lep2.Pt\(\) -x 'p_{T}^{lep} [GeV]' > /dev/null &
#./dstarDraw.py -t $treename -s $step -b [10,-2.5,2.5] -p lep1.Eta\(\),lep2.Eta\(\) -x 'lepton #eta' > /dev/null &
#done

./dstarDraw.py -c "${cut_d0}" -t $treename -s 5 -b [20,1.6,2.2] -p d0.M\(\) -x 'Mass of D0 [GeV/c^{2}]'
#./dstarDraw.py -c "${cut_d0}" -t $treename -s 5 -b [20,0.0,80.0] -p d0.Pt\(\) -x 'p_{T}^{D0} [GeV]' > /dev/null &
#./dstarDraw.py -c "${cut_d0}" -t $treename -s 5 -b [25,-2.5,2.5] -p d0.Eta\(\) -x 'D0 #eta' > /dev/null &
#./dstarDraw.py -c "${cut_dstar}" -t $treename -s 5 -b [20,1.9,2.1] -p dstar.M\(\) -x 'Mass of D* [GeV/c^{2}]' > /dev/null &
#./dstarDraw.py -c "${cut_dstar}" -t $treename -s 5 -b [20,0.0,80.0] -p dstar.Pt\(\) -x 'p_{T}^{D*} [GeV]' > /dev/null &
#./dstarDraw.py -c "${cut_dstar}" -t $treename -s 5 -b [25,-2.5,2.5] -p dstar.Eta\(\) -x 'D* #eta' > /dev/null &
#./dstarDraw.py -c "${cut_dstar}" -t $treename -s 5 -b [20,0.135,0.17] -p 'dstar_diffMass' -x 'M_{K #pi #pi}-M_{K #pi} [GeV/c^{2}]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [40,2.0,4.0] -p Jpsi.M\(\) -x 'Mass of J/#psi [GeV/c^{2}]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [20,0.0,100.0] -p Jpsi.Pt\(\) -x 'p_{T}^{J/#psi} [GeV]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [25,-2.5,2.5] -p Jpsi.Eta\(\) -x 'J/#psi #eta' > /dev/null &

#./dstarDraw.py -t $treename -s $step -b [60,0,0.1] -p 'd0_dca' -x 'DCA of D0 Cands [cm]' > /dev/null &
#./dstarDraw.py -t $treename -s $step -b [60,0,0.1] -p 'dstar_dca' -x 'DCA of D* Cands [cm]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [60,0,0.3] -p 'd0_vProb' -x 'Vertex Probability of D0 Cands' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [60,0,0.3] -p 'dstar_vProb' -x 'Vertex Probability of D* Cands' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [60,0,0.3] -p 'Jpsi_vProb' -x 'Vertex Probability of J/#psi Cands' > /dev/null &

#./dstarDraw.py -t $treename -s 5 -b [60,0,0.5] -p 'd0_LXY' -x 'Lxy of D0 Cands [cm]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [60,0,0.5] -p 'dstar_LXY' -x 'Lxy of D* Cands [cm]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [60,0,0.5] -p 'Jpsi_LXY' -x 'Lxy of J/#psi Cands [cm]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [60,0,1] -p 'd0_L3D' -x 'L_{3D} of D0 Cands [cm]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [60,0,1] -p 'dstar_L3D' -x 'L_{3D} of D* Cands [cm]' > /dev/null &
#./dstarDraw.py -t $treename -s 5 -b [60,0,1] -p 'Jpsi_L3D' -x 'L_{3D} of J/#psi Cands [cm]' > /dev/null &
