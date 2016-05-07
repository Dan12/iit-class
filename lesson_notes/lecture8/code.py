import timeit
print(timeit.timeit("dct[random.randrange(10**6)]",
              'import random; '
              'dct = {x: x*2 for x in range(10**6)}',  
              number = 100000))
              
def time_list(size):
    return timeit.timeit("dct[random.randrange({})]".format(size),
              'import random; '
              'dct = {{x: x*2 for x in range({})}}'.format(size),  
              number = 100000)
              
print(time_list(10**4))