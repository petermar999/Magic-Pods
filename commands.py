#!/usr/bin/env python
# coding: utf-8


import math
import random
def podzal(pods, names):
    peepsperpod = math.floor(len(names)/pods)
    all_pods = [[] for i in range(0, pods)]
    while len(names) > 0:
        selection = names[0]
        randompod = random.randint(0, (pods-1))
        if len(names) == 1:
            podn = []
            for pod in all_pods:
                podn.append(len(pod))
            if len(names) == 0:
                None
            elif sum(podn)%peepsperpod == 0:
                all_pods[randompod].append(selection)
                names = []
            else:
                minindex = podn.index(min(podn))
                all_pods[minindex].append(selection)
                names = []
        elif len(all_pods[randompod]) != peepsperpod:
            all_pods[randompod].append(selection)
            del names[0]
        elif len(all_pods[randompod]) == peepsperpod:
            None
    stringer = []
    n = 1
    for pod in all_pods:
        stringer.append('Pod '+str(n)+': '+" ".join(str(name) for name in pod))
        n = n+1
    return all_pods, stringer
        
        







