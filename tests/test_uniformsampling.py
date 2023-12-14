import random

import numpy as np
from ECMC.uniformsampling import uniformsampling


def test_uniformsampling():
    random.seed(2023)
    Q = np.array([[1, -0.5, -0.5], [-0.3, 0.8, -0.5], [-0.4, -0.2, 0.6]])
    result = uniformsampling(Q, 50, 0, 2)
    assert isinstance(result, list)
    assert len(result) == 4
    assert result[0][0] == 0
    assert result[2][0] == 2
    assert result[3][0] == 2
