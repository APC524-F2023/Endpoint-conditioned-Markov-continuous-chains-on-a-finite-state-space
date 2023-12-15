import random
import numpy as np

from ECMC.rejectionsampling import rejectionsampling


def test_uniformsampling():
    random.seed(2023)
    Q = np.array([[1, -0.5, -0.5], [-0.5, 1, -0.5], [-0.5, -0.5, 1]])
    bgnst = 1
    endst = 2
    result = modifiedforward(bgnst, endst, Q, 10)
    assert isinstance(result, Path)
    assert len(result.array_a) == len(result.array_b)
    assert result.array_a[0] == bgnst
    assert result.array_a[-1] == endst