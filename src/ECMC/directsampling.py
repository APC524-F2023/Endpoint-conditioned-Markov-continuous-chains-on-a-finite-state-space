"""
Created on Sun Nov 12 19:02:27 2023

@author: ct347
"""

import numpy as np
from numpy.random import choice, exponential


def directsampling(Q, T):
    # Initial state and time
    a = 0  # assuming the first state for demonstration
    current_time = 0
    sample_path_with_times = [(a, current_time)]

    while current_time < T:
        # Calculate waiting time in state a
        waiting_time = exponential(1 / abs(Q[a, a]))

        # Update the current time with the waiting time
        current_time += waiting_time
        if current_time > T:
            break

        # Calculating probabilities for state transitions (excluding self-transitions)
        p_i = []
        for i in range(Q.shape[0]):
            if i != a:
                numerator = Q[a, i]
                denominator = -Q[a, a]  # diagonal element for state a
                pi = numerator / denominator
                p_i.append(np.real(pi))

        # Normalizing pi
        p_i_normalized = np.array(p_i) / np.sum(p_i)

        # Sampling the next state
        next_state = choice(
            [state for state in range(Q.shape[0]) if state != a], p=p_i_normalized
        )
        sample_path_with_times.append((next_state, current_time))

        # Update the current state
        a = next_state

    return sample_path_with_times
