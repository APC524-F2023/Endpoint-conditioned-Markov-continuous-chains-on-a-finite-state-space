import random

import numpy as np


def forward_sampling(Q, T, a, b, t=0):
    tau = np.exp(Q) * random.random()
    if tau > T:
        return a
    else:
        return forward_sampling(Q, T, a, b, tau)


def rejection_sampling(Q, T, a, b):
    if a == b:
        result = forward_sampling(Q, T, a, b)
        if result == b:  # accept sampling if Q matches b when t=T
            return result
    tau = np.exp(Q) * random.random()
    f = Q * np.exp(-tau * Q) / (1 - Q * np.exp(-T * Q))
    c = np.exp(Q) * random.random() * f
    result = forward_sampling(Q, T, c, b, tau)
    if result == b:  # accept sampling if Q matches b when t=T
        return result
    else:
        return rejection_sampling(Q, T, c, b)
