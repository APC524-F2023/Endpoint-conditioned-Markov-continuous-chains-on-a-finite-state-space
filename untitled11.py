# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:41:45 2023

@author: ct347
"""

# Problem 1 : Functional Programming

#In the Week 4 materials, we have covered the topics of working with immutable data through the means of functional programming. This problem will explore other common passing functions beyond `map`, `filter`, and `reduce`.

#Before we start, let us import the three passing functions that we have defined in the lecture notes.

import functools


class FunctionalIterable:
    def __init__(self, this, /):
        self._this = this

    def __repr__(self):
        return repr(self._this)

    def map(self, func):
        return self.__class__(map(func, self._this))

    def filter(self, func):
        return self.__class__(filter(func, self._this))

    def reduce(self, func):
        return functools.reduce(func, self._this)
    
#Consider this sample code written in the typical programming pattern to numerically calculate the average energy of an object moving under some force `f(t, x, v)` between time `t = 0` to `t = 1` discretized into `n_grid`. In this code we evolve the state of the particle `s = (x, v)` as a function of time.
import math
import numpy as np

# Function
def f(t, s, kp, aw, om):
    """Force of a driven SHO system"""
    return -kp * s[0] + aw * math.cos(om * t)


# Problem inputs
## Set the basic parameter
kp_in = 1.0
aw_in = 1.0
om_in = 1.0

## Set the initial condition
state = (0.0, 0.0)
ng_in = 1000

import math
import numpy as np

# Function
def f(t, s, kp, aw, om):
    """Force of a driven SHO system"""
    return -kp * s[0] + aw * math.cos(om * t)


# Problem inputs
## Set the basic parameter
kp_in = 1.0
aw_in = 1.0
om_in = 1.0

## Set the initial condition
state = (0.0, 0.0)
ng_in = 1000

from typing import Tuple
def calc_rms_energy(
    n_grid: int, state_init: Tuple[float, float], force, f_args: Tuple[float, ...]
) -> float:
    """
    Calculate the average energy of a particle subject to a force function
    between t = 0 and t = 1 discretized to n_grid steps.

    The force function should have a form of force(t, state, *f_args)
    """

    # Build the time and energy arrays
    t_arr, dt = np.linspace(0.0, 1.0, num=n_grid, retstep=True)
    e_arr = np.zeros(n_grid)

    # Copy the initial state
    s = state_init

    for i in range(n_grid):
        f = force(t_arr[i], s, *f_args)
        s = (s[0] + dt * s[1], s[1] + dt * f)

        e_arr[i] = 0.5 * (s[0] ** 2 + s[1] ** 2)

    # Calculate the average energy
    K_tot = 0.0

    for i in range(n_grid):
        K_tot = K_tot + e_arr[i]

    # Return the RMS energy
    return K_tot / n_grid

ek_avg = calc_rms_energy(ng_in, state, f, (kp_in, aw_in, om_in))
print(f"<K> = {ek_avg}")
## Question 1.1
# Your task is now to rewrite the code into its functional form through several steps by extending `FunctionalIterable` class using several methods. Denoting `FunctionalIterableExtended(x)` as `{x}`, the methods that we want to implement are:

# 0. `__eq__`\
#   This should implement `{x} == {y}` such that it is equivalent to `x == y`.
# 1. `apply`\
#   This should implement `{x}.apply(f) = {f(x)}`
# 2. `join`\
#   This should implement `{x}.join({y}) = {x, y} ` using `itertools.chain`. They should preserve the original class of `x` if `y` is in the same class, otherwise return `itertools.chain` object.
# 3. `nest`\
#   This should implement `{x}.nest(f, n) = {f(f(...))}` where function `f` is applied `n` times to `{x}`.
# 4. `nestlist`\
#   This should implement `{x}.nestlist(f, n) = {x, f(x), f(f(f(x))), ...}` with the last term is `f` is applied `n` times to `{x}`.

# **Note**: For the last two methods assume that `n >= 0`. You should be able to implement these functions without explicit `for` loops using recursion.
import itertools
import functools

class FunctionalIterableExtended(FunctionalIterable):
    def __eq__(self, other):
        if not isinstance(other, FunctionalIterableExtended):
            return False
        if type(self._this) != type(other._this):
            return False
        return list(self._this) == list(other._this)

    def join(self, y):
        if isinstance(y, self.__class__):
            if type(self._this) != type(y._this):
                # 使用 itertools.chain 但包装在 FunctionalIterableExtended 实例中
                return self.__class__(itertools.chain(self._this, y._this))
            elif isinstance(self._this, tuple):
                return self.__class__(self._this + y._this)
            elif isinstance(self._this, set):
                return self.__class__(self._this.union(y._this))
            else:
                return self.__class__(list(itertools.chain(self._this, y._this)))
        else:
            # y 不是 FunctionalIterableExtended 实例，使用 itertools.chain
            return self.__class__(itertools.chain(self._this, y))


    def apply(self, f):
        return self.__class__(f(self._this))

    def nest(self, f, n):
        if n == 0:
            return self
        return self.__class__(f(self.nest(f, n-1)._this))

    def nestlist(self, f, n):
     
        result = self._this.copy()  # 初始化结果列表
        current = self._this
        for _ in range(n):
           current = f(current)
           result.extend(current)  # 扩展结果列表而不是追加       
        return self.__class__(result)
    def __iter__(self):
      # 实现迭代方法，返回迭代器
      return iter(self._this)
    #Test your implementation such that the cell below evaluates without any exception.
fi_list = FunctionalIterableExtended([1, 2, 3])
fi_tuple = FunctionalIterableExtended((0.1, 0.2))
fi_set = FunctionalIterableExtended(set([10, 20, 20, 30]))
fi_str = FunctionalIterableExtended("abc")
fi_strlist = FunctionalIterableExtended(["def"])


def fi_f(x):
    return [i * 2 for i in x]


# __eq__
assert fi_list == FunctionalIterableExtended([1.0, 2.0, 3.0])
assert fi_list != FunctionalIterableExtended((1, 2, 3))

# apply
assert fi_list.apply(fi_f) == FunctionalIterableExtended([2, 4, 6])
assert fi_tuple.apply(fi_f) == FunctionalIterableExtended([0.2, 0.4])
assert fi_set.apply(fi_f) == FunctionalIterableExtended([20, 40, 60])
assert fi_str.apply(fi_f) == FunctionalIterableExtended(["aa", "bb", "cc"])

# join
assert fi_list.join(fi_tuple.apply(fi_f)) == FunctionalIterableExtended(
    [1, 2, 3, 0.2, 0.4]
)
assert fi_set.join(fi_set) == fi_set
assert type(fi_tuple.join(fi_tuple)._this) == tuple
assert type(fi_list.join(fi_str)._this) == itertools.chain

# nest
assert fi_list.nest(fi_f, 4) == FunctionalIterableExtended([16, 32, 48])
assert fi_str.nest(fi_f, 3) == FunctionalIterableExtended(
    ["aaaaaaaa", "bbbbbbbb", "cccccccc"]
)
assert fi_strlist.nest(fi_f, 2) == FunctionalIterableExtended(["defdefdefdef"])

# nestlist
assert fi_list.nestlist(fi_f, 4) == FunctionalIterableExtended(
    [1, 2, 3, 2, 4, 6, 4, 8, 12, 8, 16, 24, 16, 32, 48]
)
assert fi_strlist.nestlist(fi_f, 2) == FunctionalIterableExtended(
    ["def", "defdef", "defdefdefdef"]
)
## Question 1.2
# Now implement the new `FunctionalIterableExtended` class that you have to solve the original problem with functional programming. For this let us start by defining the state in this class as `state_f = FunctionalIterableExtended(...)` which will be initialized from the original value of `state`.

# It is also useful to define your curried evolution function as
# ```python
# def f_f(s):
#   # Depends on ng_in, f, and parameters of f
#```
state_f = FunctionalIterableExtended([(0.0, *state)])
dt = 1.0 / ng_in  # 时间步长


def f_f(s):
    t, (x, v) = s[0]
    new_force = f(t, (x, v), kp_in, aw_in, om_in)
    new_x = x + dt * v
    new_v = v + dt * new_force
    return [(t + dt, (new_x, new_v))]
    
# 初始化 state_f
state_f = FunctionalIterableExtended([(0.0, state)])

# 使用 nestlist 方法重复应用 f_f 来演化状态
evolved_states = state_f.nestlist(f_f, ng_in+1)

#print(evolved_states)
# # 计算每个状态的能量
energies = evolved_states.map(lambda s: 0.5 * (s[1][0] ** 2 + s[1][1] ** 2))

#A=list(energies)

# # 计算平均能量
# #print(energies)
# #print(evolved_states)

ek_avg_f:float = sum(list(energies))/ (ng_in+1)

print(f"<K>   = {ek_avg}")
print(f"<K>_f = {ek_avg_f}")


# Problem 2: Static typing
## Question 1.1

#Add static types to the following code from week 3 on integrators. A handy type alias has been given for you to
#use if you want. You do not need variable annotations with
#one exception - and that has already been done for you.
