import numpy as np

from uniformsampling import uniform_sampling


def test_uniform():
    Q = np.array([[-1, 0.5, 0.5],
              [0.3, -0.8, 0.5],
              [0.4, 0.2, -0.6]])
    uniform_sampling(Q, 10, 0, 2)
