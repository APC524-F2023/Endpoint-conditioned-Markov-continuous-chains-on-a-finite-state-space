import numpy as np
import directsampling

def test_directsampling():
    Q = np.array([[-0.5, 0.5], [0.5, -0.5]])
    T = 10
    result = directsampling.directsampling(Q, T)
    
    # Check if the first element of the result is a tuple
    print(result[0])
    assert isinstance(result[0], tuple), "Each element in the result should be a tuple"
    
    # Check if the first element of the result is (0, 0)
    assert result[0] == (0, 0), "The first element of the result should be (0, 0)"
    
    # Check if the second element of each tuple is increasing
    for i in range(1, len(result)):
        print(result[i][1], result[i-1][1])
        assert result[i][1] > result[i-1][1], "The second element of each tuple should be increasing"