# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 04:37:22 2022

@author: Mowibox
"""

import random as rd
import matplotlib.pyplot as plt

#Retraction ratio (1/retraction)
retraction = 2 

#Enable/Disable eavesdropping
E = [False,True]

N = list(range(10,2020,10))
PF = []
PT = []
DE = []

for i in range(len(N)):
    for j in range(len(E)):
        base = ['+','x']
        qubit = [0,1]
        Eve = E[j]
        n = N[i]

        #Alice chooses a random base and qubit for each photon
        def baseQubitAlice(n):
            bqA = []
            for i in range(n):
                qB = []
                r = rd.randint(0,1)
                qB.append(base[r])
                r = rd.randint(0,1)
                qB.append(qubit[r])
                bqA.append(qB)
            return bqA
        
        #Photons are polarized based on the chosen base and qubit
        def polarisationAlice(bqA):
            polarisation = []
            for i in range(len(bqA)):
                if bqA[i] == ['+',0]:
                    polarisation.append("→")
                elif bqA[i] == ['+',1]:
                    polarisation.append("↑")
                elif bqA[i] == ['x',0]:
                    polarisation.append("↗")
                else: 
                    polarisation.append("↖")
            return polarisation
        
        #Eve also chooses bases randomly
        def baseEve(n):
            bE = []
            for i in range(n):
                Te = []
                r = rd.randint(0,1)
                Te.append(base[r])
                bE.append(Te)
            return bE
        
        #If Eve chooses the same base as Alice, the qubit remains unchanged
        #Otherwise, it takes a random value between 0 and 1
        def checkEve(pA,bE):
            cE = []
            for i in range(len(bE)):
                if (pA[i] == "→" and bE[i] == ['+']):
                    cE.append('+')
                    cE.append(0)
                elif (pA[i] == "↑" and bE[i] == ['+']):
                    cE.append('+')
                    cE.append(1)
                elif (pA[i] == "↗" and bE[i] == ['x']):
                    cE.append('x')
                    cE.append(0)
                elif (pA[i] == "↖" and bE[i] == ['x']):
                    cE.append('x')
                    cE.append(1)
                
                elif (pA[i] == "→" and bE[i] == ['x']):
                    r = rd.randint(0,1)
                    cE.append('x')
                    cE.append(r)
                elif (pA[i] == "↑" and bE[i] == ['x']):
                    r = rd.randint(0,1)
                    cE.append('x')
                    cE.append(r)
                elif (pA[i] == "↗" and bE[i] == ['+']):
                    r = rd.randint(0,1)
                    cE.append('+')
                    cE.append(r)
                elif (pA[i] == "↖" and bE[i] == ['+']):
                    r = rd.randint(0,1)
                    cE.append('+')
                    cE.append(r)
            return cE
        
        #Photons are polarized on the bases and qubits are determined by Eve
        def polarisationEve(cE):
            polarisation = []
            for i in range(0,len(cE),2):
                if cE[i] == '+' and cE[i+1] == 0:
                    polarisation.append("→")
                elif cE[i] == '+' and cE[i+1] == 1:
                    polarisation.append("↑")
                elif cE[i] == 'x' and cE[i+1] == 0:
                    polarisation.append("↗")
                else: 
                    polarisation.append("↖")
            return polarisation
        
        #Bob chooses his bases randomly
        def baseBob(n):
            bB = []
            for i in range(n):
                Tb = []
                r = rd.randint(0,1)
                Tb.append(base[r])
                bB.append(Tb)
            return bB
        
        #Bob receives polarized photons from Eve or Alice (depends of E value)
        #If he chooses the correct base, the qubit remains unchanged
        #Otherwise, it takes a random value between 0 and 1
        def checkBob(pA,pE,bB):
            cB = []
            if Eve:
                for i in range(len(bB)):
                    if (pE[i] == "→" and bB[i] == ['+']):
                        cB.append(0)
                    elif (pE[i] == "↑" and bB[i] == ['+']):
                        cB.append(1)
                    elif (pE[i] == "↗" and bB[i] == ['x']):
                        cB.append(0)
                    elif (pE[i] == "↖" and bB[i] == ['x']):
                        cB.append(1)
                    else:
                        r = rd.randint(0,1)
                        cB.append(r)
                return cB
            else:
                for i in range(len(bB)):
                    if (pA[i] == "→" and bB[i] == ['+']):
                        cB.append(0)
                    elif (pA[i] == "↑" and bB[i] == ['+']):
                        cB.append(1)
                    elif (pA[i] == "↗" and bB[i] == ['x']):
                        cB.append(0)
                    elif (pA[i] == "↖" and bB[i] == ['x']):
                        cB.append(1)
                    else:
                        r = rd.randint(0,1)
                        cB.append(r)
                return cB
        
        #Alice and Bob publicy share the bases they used
        #They discard measurements where the wrong bases were chosen by Bob
        def suppression(bqA,bB,cB):
            cleA = []
            cleB = []
            for i in range(len(bqA)):
                if bqA[i][0] == bB[i][0]:
                    cleA.append(bqA[i][1])
                    cleB.append(cB[i])
            return cleA,cleB
        
        #Bob sends half of the remaining qubits t ALice for verification
        #If they are all equal, there has been no eavesdropping
        #If at least 25% of the qubits are different, eavesdropping has occured
        def verification(cleA,cleB,n2):
            s = 0
            assert n2 < len(cleA)
            for i in range(len(cleA)-n2):
                if cleA[i] == cleB[i]:
                    s += 1
            return s/(len(cleA)-n2)
        
        
        bqA = baseQubitAlice(n)
        pA = polarisationAlice(bqA)
        bE = baseEve(n)
        cE = checkEve(pA, bE)
        pE = polarisationEve(cE)
        bB = baseBob(n)
        cB = checkBob(pA,pE,bB)
        cleA = suppression(bqA,bB,cB)[0]
        cleB = suppression(bqA,bB,cB)[1]
        n2 = len(cleA)//retraction            
        p = verification(cleA,cleB,n2)
        if E[j]:
            PT.append(p*100)
        else:
            PF.append(p*100)
            DE.append(75)
            
#Plotting   
for i in range(len(N)):
    if i == len(N)-1 :
        plt.plot(N,PF,'g',label="Eve Absence")
        plt.plot(N,PT,'r',label="Eve Presence")
        plt.plot(N,DE,'y',label="Eavesdropping Detection")
        plt.title("Similar Qubits with a 1/{} retraction of Qubits".format(retraction))
        plt.ylabel("Similar Qubits (in %)")
        plt.xlabel("Size of the Photon Set")
        plt.legend()
        plt.grid()
    else:
        plt.plot(N,PF,'g')
        plt.plot(N,PT,'r')
        plt.plot(N,DE,'y')
        plt.grid()
           
plt.show()