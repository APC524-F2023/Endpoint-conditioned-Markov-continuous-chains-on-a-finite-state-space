# source: Hobolth, A., & Stone, E. A. (2009). Efficient simulation from finite-state, continuous-time Markov chains with incomplete observations. Annals of Applied Statistics, 3, 1204-1231.
# adapted from Hobolth and Stone's R code
from pickle import TRUE
import numpy as np
import random 
from scipy.stats import poisson
import math

def uniform(BgnSt, EndSt, RateM, Tm):
    lam, U = np.linalg.eig(rate)
    invU = np.linalg.inv(U)
    temp = (U @ np.diag(math.exp(Tm*lam)))@invU
    PrbBgnEnd = temp[BgnSt, EndSt]
    nSt = np.shape(RateM)[0]
    Mx = max(-np.diag(RateM))
    TransM = np.diag(np.ones(nSt)) + RateM/Mx
    TransMn = TransM

    rU = random.uniform()
    if BgnSt == EndSt:
        cum = poisson.pmf(0, Mx*Tm)/PrbBgnEnd
    else:
        cum = 0
    
    nJmp = 0
    notExceed = True
    if (cum > rU):
        notExceed = False
    
    while(notExceed):
        nJmp = nJmp + 1
        prb = poisson.pmf(nJmp, Mx*Tm)*TransMn[BgnSt-1, EndSt-1]/PrbBgnEnd
        cum = cum + prb
        if (cum > rU):
            notExceed = False
        if (nJmp == 1):
            TransArr = TransM.reshape(nSt, nSt, 1)
        else:
            temp1 = np.concatenate([TransArr, TransMn])
            TransArr = temp1.reshape(nSt, nSt, nJmp)
        TransMn <- TransMn @ TransM
    
    Path = []
    if (nJmp == 0):
        Path = [[BgnSt, EndSt], [0, Tm]]
        return Path
    elif (nJmp == 1):
        if(BgnSt == EndSt):
            Path = [[BgnSt, EndSt], [0, Tm]]
            return Path
        Path = [[BgnSt, EndSt], [0, Tm*random.uniform, Tm]]
        return Path
    
    JmpTmV = Tm*(random.uniform(nJmp)).sort()
    JmpStV = np.zeros(nJmp - 1)
    Prb1 = TransM[BgnSt-1, ]
    for i in range(nJmp - 1):
        Prb2Mat = TransArr[,,(nJmp-i)]
        Prb2 = Prb2Mat[, EndSt]
        #
        JmpStV[i] = random.sample(1:nSt, 1)
        Prb1 <- TransM[JmpStV[i]-1, ]
    
    JmpStV = np.concatenate(JmpStV, EndSt)
    TrueSub = (np.concatenate(JmpStV, EndSt) != np.concatenate(JmpStV[0:nJmp-1], EndSt))
    Path = [np.concatenate(BgnSt, JmpStV[TrueSub], EndSt), 
            np.concatenate(0, JmpTmV[TrueSub], Tm)]
    return Path