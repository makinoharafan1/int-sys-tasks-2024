"""
compare function for choosing direction between current and destination floors

cmp(3, 5)  ->  1  (move up)
cmp(7, 2)  -> -1  (move down)
cmp(4, 4)  ->  0  (stop)
"""

def cmp(a, b):
    return (b > a) - (b < a)
