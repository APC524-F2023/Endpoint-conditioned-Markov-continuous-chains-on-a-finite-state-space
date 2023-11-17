import pytest
from your_script_name import direct_sampling_with_times  # Replace with your actual script name
import numpy as np

def test_direct_sampling_with_times():
    Q = np.array([[-1, 0.5, 0.5],
                  [0.3, -0.8, 0.5],
                  [0.4, 0.2, -0.6]])
    T = 13
    result = direct_sampling_with_times(Q, T)
    
    # Test for output type
    assert isinstance(result, list), "Output should be a list"
    
    # Test for non-empty output
    assert len(result) > 0, "Output list should not be empty"

    # More tests can be added here, like checking the length, structure, etc.
