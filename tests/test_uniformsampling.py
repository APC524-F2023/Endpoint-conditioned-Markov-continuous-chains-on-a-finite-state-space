import unittest
import numpy as np
from ECMC.directsample-generalcase import sample_path, path_prob, P_matrix, Muv  # Adjust the imports as needed

class TestECMCDirectSampleGeneralCase(unittest.TestCase):

    def setUp(self):
        # Initialize a transition matrix and other constants used in multiple tests
        self.T = np.array([[0, 1/2, 1/2, 0, 0, 0, 0],
                           [1/3, 0, 1/3, 1/3, 0, 0, 0],
                           [1/2, 1/2, 0, 0, 0, 0, 0],
                           [0, 1/4, 0, 0, 1/4, 1/4, 1/4],
                           [0, 0, 0, 1/2, 0, 1/2, 0],
                           [0, 0, 0, 1/3, 1/3, 0, 1/3],
                           [0, 0, 0, 1/2, 0, 1/2, 0]])
        self.a = 1
        self.b = 7
        self.N = 4

    def test_sample_path_length(self):
        path = sample_path(self.a, self.b, self.N, self.T)
        self.assertEqual(len(path), self.N + 1)  # Path length should be N + 1

    def test_sample_path_validity(self):
        # Test if the start and end states of the path are correct
        path = sample_path(self.a, self.b, self.N, self.T)
        self.assertEqual(path[0], self.a)
        self.assertEqual(path[-1], self.b)

    def test_path_prob(self):
        path = np.array([1, 2, 4, 6, 7], dtype=int)
        prob = path_prob(path, self.a, self.b, self.N, self.T)
        self.assertGreaterEqual(prob, 0)
        self.assertLessEqual(prob, 1)  # Probability should be between 0 and 1

    def test_P_matrix(self):
        u, v = 2, 3
        P = P_matrix(self.a, self.b, u, v, 1, self.N, self.T)
        self.assertGreaterEqual(P, 0)
        self.assertLessEqual(P, 1)  # Matrix element should be a valid probability

    def test_Muv(self):
        u, v = 2, 3
        M = Muv(self.a, self.b, u, v, self.N, self.T)
        self.assertIsInstance(M, float)  # Ensure Muv returns a float value

# Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
