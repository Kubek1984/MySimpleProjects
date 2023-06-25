
def dekor(func):
    def inner_func(*args):

        print('Decorator start')
        result = func(*args)
        print('DEcorator end')
        return result
    return inner_func

@dekor
def get_pi(multiplier, abc, defg):
    return 3.14 * multiplier * abc / defg

@dekor
def get_e():
    return 2.73

# print(get_pi())
# print(dekor(get_pi))

print(get_pi(2, 8, 3))
print(get_e())