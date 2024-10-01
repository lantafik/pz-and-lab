import math


def get_math_text(a, b, c):
    d = (b**2) - 4*a*c
    c = []
    if d < 0:
        c.append(None)
    else:
        x1 = (math.sqrt(d)-b) / (2*a)
        x2 = (-math.sqrt(d)-b) / (2*a)
        if x1 != x2:
            c.append(x1)
            c.append(x2)
        else:
            c.append(x1)
    return c
