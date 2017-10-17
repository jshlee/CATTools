#./DYdraw.py -c <cut> -w <weight> -b <binning> -p <plotvar> -x <x-name> -y <y_name> -f <f_name> -d <dolog> 

std_cut     = 'dilep.M()>60&&step==5'

weight      = 'weight*(mueffweight)'

json_used   = 'Golden'

x_name_l    = ["Invariant Mass [GeV]", "Transverse Momentum [GeV]"]

plotvar_l   = ["dilep.M\(\)", "dilep.Pt\(\)"]

binset_l    = ["[300,0,300]", "[250,0,300]", "[200,0,300]", "[150,0,300]"]

MCat_l      = ["VBFT_M", "GGFT_M", "VBFL_M", "JetT_M", "JetL_M"]

PTCat_l     = ["VBFT_Pt", "GGFT_Pt", "VBFL_Pt", "JetT_Pt", "JetL_Pt"] 

lst         = []

User_input = raw_input(" How would you like it listed? b = Bin, c = Cut, p = Plot Name or BDT: ") 
if User_input =="BDT":
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [150,50,200] -p 'dilep.M()' -x 'm(\mu^+\mu^-)(GeV)' -y 'Event' -f 'Dilept_M' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [60,0,300] -p 'dilep.Pt()' -x 'p_t(\mu^+\mu^-)(GeV)' -y 'Event' -f 'Dilept_Pt' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [45,0,200] -p 'lep1.Pt()' -x 'p_t(\mu_1)(GeV)' -y 'Event' -f 'lept1_Pt' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [30,-2.5,2.5] -p 'lep1.Eta()' -x '\eta(\mu_1)(GeV)' -y 'Event' -f 'lept1_eta' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [45,0,200] -p 'lep2.Pt()' -x 'p_t(\mu_2)(GeV)' -y 'Event' -f 'lept2_Pt' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [30,-2.5,2.5] -p 'lep2.Eta()' -x '\eta(\mu_2)(GeV)' -y 'Event' -f 'lept2_eta' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [150,50,200] -p 'dilep.M()' -x 'm(\mu^+\mu^-)(GeV)' -y 'Event' -f 'Dilept_M' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [150,50,200] -p 'dilep.M()' -x 'm(\mu^+\mu^-)(GeV)' -y 'Event' -f 'Dilept_M' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [150,50,200] -p 'dilep.M()' -x 'm(\mu^+\mu^-)(GeV)' -y 'Event' -f 'Dilept_M' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [150,50,200] -p 'dilep.M()' -x 'm(\mu^+\mu^-)(GeV)' -y 'Event' -f 'Dilept_M' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [150,50,200] -p 'dilep.M()' -x 'm(\mu^+\mu^-)(GeV)' -y 'Event' -f 'Dilept_M' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    cmd ="./h2muDraw.py -c '%s' -w '%s' -b [150,50,200] -p 'dilep.M()' -x 'm(\mu^+\mu^-)(GeV)' -y 'Event' -f 'Dilept_M' -j 'Golden' -d 'True' > /dev/null &"%(std_cut, weight)
    lst.append(cmd)   
    
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


