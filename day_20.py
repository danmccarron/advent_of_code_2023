input = R'''&sr -> hp
%sh -> lr
%jm -> pj, tf
&xr -> sn, sb, hd
%xt -> cc, tf
%br -> fm
%hd -> tp, xr
%rg -> xr, dl
%sb -> jh
%xg -> rd
%nf -> gx, gd
%pj -> tf, dk
%gq -> jm
%vv -> br
%gd -> gx
&hp -> rx
%cz -> gk, vv
&gk -> vq, vv, br, zt, dj, xg
%gr -> zn, xr
&tf -> cc, rf, kk, xt, gq
%dk -> tb, tf
%nt -> ph, gk
%fh -> xr, xs
%jh -> xr, bz
%pd -> gk, kb
%kb -> nt, gk
%fm -> dj, gk
%kr -> tf
%tp -> xr, rq
%lr -> mz, gx
&sn -> hp
%mz -> rv
%kj -> gx, hs
%rv -> gx, ck
%cr -> kk, tf
%rq -> gr, xr
%kk -> fc
%ck -> gx, nf
broadcaster -> hd, xt, kj, zt
%tt -> gf
%tb -> kr, tf
%gf -> gx, sh
%cc -> cr
%fc -> qx, tf
%dl -> xr
&gx -> mz, sh, tt, sr, kj, tk
%dj -> pd
%zt -> gk, xg
&rf -> hp
&vq -> hp
%xs -> sb, xr
%qx -> tf, gq
%bz -> xr, rg
%ph -> gk
%hs -> gx, tk
%tk -> tt
%rd -> gk, cz
%zn -> fh, xr'''

lines = '{"' + input.replace(' -> ','":"').replace('\n','",\n"') + '"}'

config = eval(lines)
for a in config.keys():
    config[a] = {'destinations':config[a].split(', ')}
    
#print([a for a in config if a['destinations'] == ['sn', 'sb', 'hd']])

config2 = eval(lines)
for a in config.keys():
    config2[a] = {'destinations':config2[a].split(', ')}

for a in config.keys():
    if a[0] == '&':
        #print([list(config.values()).index(z) for z in [{'destinations':y} for y in [x['destinations'] for x in config.values()] if a[1:] in y]])
        config2[a] = config[a] | {'memories':dict(pair for d in [{list(config.keys())[q].replace('%','').replace('&',''):'L'} for q in [list(config.values()).index(z) for z in [{'destinations':y} for y in [x['destinations'] for x in config.values()] if a[1:] in y]]] for pair in d.items())}
for a in config.keys():
    if a[0] == '%':
        config2[a] = config[a] | {'status':0}

print(config2)

# print(dict(pair for d in config['&inv']['memories'] for pair in d.items()))


print()
def pressButton(conf):
    confToUse = conf.copy()
    pulses = [[x,'L','broadcaster'] for x in confToUse['broadcaster']['destinations']]
    HPulsesSent = 0
    LPulsesSent = 1 
    pulsesToRX = 0
    feeders = []
    while len(pulses) > 0: 
        #print(pulses)
        HPulsesSent += len([x for x in pulses if x[1] == 'H'])
        LPulsesSent += len([x for x in pulses if x[1] == 'L']) 
        pulsesToRX += len([x for x in pulses if x[0] == 'rx']) 
        nextPulses = []
        for a in pulses:
            if a[0] != 'output':
                if len([x for x in list(config2.keys()) if x[1:] == a[0]]) != 0:
                    dest = [x for x in list(config2.keys()) if x[1:] == a[0]][0]
                    if dest[0] == '%':
                        if a[1] == 'L':
                            confToUse[dest]['status'] = 1 if confToUse[dest]['status'] == 0 else 0
                            if confToUse[dest]['status'] == 1:
                                nextPulses += [[x,'H',dest[1:]] for x in confToUse[dest]['destinations']]
                            elif confToUse[dest]['status'] == 0:
                                nextPulses += [[x,'L',dest[1:]] for x in confToUse[dest]['destinations']]
                    if dest[0] == '&':

                        confToUse[dest]['memories'][a[2]] = a[1]
                        if len([x for x in confToUse[dest]['memories'].values() if x == 'H']) == len([x for x in confToUse[dest]['memories'].values()]):
                            nextPulses += [[x,'L',dest[1:]] for x in confToUse[dest]['destinations']]
                        else:
                            nextPulses += [[x,'H',dest[1:]] for x in confToUse[dest]['destinations']]      
                    if dest == 'broadcaster':
                        nextPulses += [[x,a[1]] for x in confToUse[dest]['destinations']]
        pulses = nextPulses
        feeders += [x for x in nextPulses if x[2] in ['gx', 'xr', 'tf', 'gk'] and x[1] == 'L']
#        feeders += [x for x in nextPulses if x[2] in ['nf', 'gd', 'sn','lr', 'kj', 'rv', ' ck', 'gf', 'hs']] # and x[1] == 'H']
    # if pulsesToRX != 0:
    #     print('----------')
    #     print(pulsesToRX)
    #     print('----------')


    return confToUse, HPulsesSent, LPulsesSent, feeders
        

newConfig = config2.copy()
TotalHPulses = 0
TotalLPulses = 0
for i in range(20000):
    newConfig, HPulsesToAdd, LPulsesToAdd, feeders = pressButton(config2)
    TotalHPulses += HPulsesToAdd
    TotalLPulses += LPulsesToAdd
    if len(feeders) > 0:
        print(i, feeders)
    #print(newConfig)
    #print(TotalHPulses, TotalLPulses)
    # if i%100 == 0:
    #     print(i)
    # if LPulsesToRX != 0:
    #     print(LPulsesToRX, i)
    #     break

print(TotalHPulses*TotalLPulses)



# rx
# hp
# sr sn rf vq
# gx xr tf gk
# 
# nf gd lr kj rv ck gf hs
# hd rg gr fh jh tp rq dl xs bz zn
# 

# gk every 3917
# gx every 3923
# xr every 3967
# tf every 4021


import math

print(math.lcm(3917,3923,3967,4021))