from typing import List, Union, Tuple

def f(x:float):
    # сложные дейсвия
    return 5*x**2 + 1


def maximum(x: Tuple) -> Union[int, float]:
    m = x[0]
    for i in x[1:]:
        if m < i:
            m = i
    return m


arr = (1, 2, 3, 1.2, 5.2)
b = maximum(arr)
print(b)