import numpy as np
from ECMC.uniformsampling import uniformsampling


def test_uniformsampling():
    Q = np.array([[1, -0.5, -0.5], [-0.3, 0.8, -0.5], [-0.4, -0.2, 0.6]])
    result = uniformsampling(Q, 10, 0, 2)
    assert isinstance(result, list)
    assert len(result) > 0
