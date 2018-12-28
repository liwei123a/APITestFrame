#coding:utf-8

def is_digit(x):
    if isinstance(x, int) or isinstance(x, float):
        return True
    else:
        return False

def cmp(a,b):
    if is_digit(a) and is_digit(b):
        c = a - b
        if c > 0:
            return 1
        elif c == 0:
            return 0
        elif c < 0:
            return -1
    else:
        raise ValueError("invalid params!")