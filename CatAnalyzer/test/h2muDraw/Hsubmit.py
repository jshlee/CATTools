#./DYdraw.py -c <cut> -w <weight> -b <binning> -p <plotvar> -x <x-name> -y <y_name> -f <f_name> -d <dolog> 
"""
presel_cut  = 'dilep.M()>20&&jet1.Pt()>40&&jet2.Pt()>30&&step==5'
VBFT_cut    = '%s&&dijet.M()>650&&abs(dijet.Eta())>3.5'%(presel_cut)
GGFT_cut    = '%s&&!(%s)&&dijet.M()>250&&dilep.Pt()>50'%(presel_cut, VBFT_cut)
BFL_cut     = '%s&&!(%s)&&!(%s)'%(presel_cut, VBFT_cut, GGFT_cut)
JetT_cut    = '!(%s)&&dilep.M()>20&&step==5&&dilep.Pt()>=25'%(presel_cut)
JetL_cut    = '!(%s)&&dilep.Pt()<25&&dilep.M()>20&&step==5'%(presel_cut)
"""

std_cut     = 'dilep.M()>2&&step==5'

weight      = 'weight*(mueffweight)'

json_used   = 'Golden'

x_name_l    = ["Invariant Mass [GeV]", "Transverse Momentum [GeV]"]

plotvar_l   = ["dilep.M\(\)", "dilep.Pt\(\)"]

binset_l    = ["[300,0,300]", "[250,0,300]", "[200,0,300]", "[150,0,300]"]

MCat_l      = ["VBFT_M", "GGFT_M", "VBFL_M", "JetT_M", "JetL_M"]

PTCat_l     = ["VBFT_Pt", "GGFT_Pt", "VBFL_Pt", "JetT_Pt", "JetL_Pt"] 

lst         = []

User_input = raw_input(" How would you like it listed? b = Bin, c = Cut, p = Plot Name: ") 

if User_input == "c":
    for i in [0,1,2,3,4]:
        for b in (plotvar_l):
            for a in (binset_l):
                for c in (x_name_l):
                    if a == "[150,0,300]":    
                        if (b,c) == ("dilep.M\(\)", "Invariant Mass [GeV]"): 
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -y 'Events/2' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd + " -f '%s'"%(MCat_l[i])
                           
                        elif (b,c) == ('dilep.Pt\(\)', 'Transverse Momentum [GeV]'):
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -y 'Events/2' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd +" -f '%s'"%(PTCat_l[i])

                        else:
                            continue

                    else: 
                        if (b,c) == ("dilep.M\(\)", "Invariant Mass [GeV]"): 
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd + "-f '%s'"%(MCat_l[i])

                        elif (b,c) == ('dilep.Pt\(\)', 'Transverse Momentum [GeV]'):
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd +" -f '%s'"%(PTCat_l[i])
                        
                        else:
                            continue
                    cmd = cmd +' > /dev/null &'
                    lst.append(cmd)   

if User_input == "b":
    for a in (binset_l):
        for b in (plotvar_l):
            for i in [0,1,2,3,4]:
                for c in (x_name_l):
                    if a == "[150,0,300]":    
                        if (b,c) == ("dilep.M\(\)", "Invariant Mass [GeV]"): 
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -y 'Events/2' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd + " -f '%s'"%(MCat_l[i])
                           
                        elif (b,c) == ('dilep.Pt\(\)', 'Transverse Momentum [GeV]'):
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -y 'Events/2' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd +" -f '%s'"%(PTCat_l[i])

                        else:
                            continue

                    else: 
                        if (b,c) == ("dilep.M\(\)", "Invariant Mass [GeV]"): 
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd + " -f '%s'"%(MCat_l[i])

                        elif (b,c) == ('dilep.Pt\(\)', 'Transverse Momentum [GeV]'):
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd +" -f '%s'"%(PTCat_l[i])
                        
                        else:
                            continue
                    cmd = cmd +' > /dev/null &'
                    lst.append(cmd)   

if User_input == "p":
    for b in (plotvar_l):
        for a in (binset_l):
            for i in [0,1,2,3,4]:
                for c in (x_name_l):
                    if a == "[150,0,300]":    
                        if (b,c) == ("dilep.M\(\)", "Invariant Mass [GeV]"): 
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -y 'Events/2' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd + " -f '%s'"%(MCat_l[i])
                           
                        elif (b,c) == ('dilep.Pt\(\)', 'Transverse Momentum [GeV]'):
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -y 'Events/2' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd +" -f '%s'"%(PTCat_l[i])

                        else:
                            continue

                    else: 
                        if (b,c) == ("dilep.M\(\)", "Invariant Mass [GeV]"): 
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd + "-f '%s'"%(MCat_l[i])

                        elif (b,c) == ('dilep.Pt\(\)', 'Transverse Momentum [GeV]'):
                            cmd ="./h2muDraw.py -c \'%s&&cat==%s\' -b %s -p %s -x '%s' -w '%s' -j '%s'"%(std_cut, i+1, a, b, c, weight, json_used)
                            cmd = cmd +"-f '%s'"%(PTCat_l[i])
                        
                        else:
                            continue
                    cmd = cmd +' > /dev/null &'
                    lst.append(cmd)   
for l in lst:
    print l


