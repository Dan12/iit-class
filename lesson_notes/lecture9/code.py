lst = [(x, x*2) for x in range(10**6)]

def search(lst, key):
    for x in lst:
        if key == x[0]:
            return x[1]
    else:
        return None
    
dct = {x: x*2 for x in range(10**6)}

from timeit import timeit
def time_list_search(size):
    return timeit('search(lst, random.randrange({}))'.format(size),
                  'import random ; ' # one big string
                  'from __main__ import search ; '
                  'lst = [(x, x*2) for x in range({})]'.format(size),
                  number=100)/100

def time_dict_search(size):
    return timeit('dct[random.randrange({})]'.format(size), 
                  'import random ; '
                  'dct = {{x: x*2 for x in range({})}}'.format(size),
                  number=100)/100
                  
sizes = range(10, 1000, 100)

print(list(time_list_search(n) for n in sizes))
print(list(time_dict_search(n) for n in sizes))

def binary_search(lst, key):
    bot = 0
    top = len(lst) - 1
    iters = 0
    while bot < top:
        iters += 1
        mid = (bot + top) // 2        
        if lst[mid][0] == key:
            return lst[mid], iters
        elif lst[mid][0] < key:
            bot = mid + 1
        else:
            top = mid - 1
    return None, iters
    
print(binary_search(lst, 123456))
print(binary_search(lst, -1))
for n in range(10**3, 10**4, 10**3):
    #       formatting stuff
    print('{:>6} elements, max of {:>2} iterations'.format(
          n,
          binary_search([(x,x) for x in range(n)], -1)[1]))
          
for n in (2**e for e in range(8, 20)):
    print('{:>6} elements, max of {:>2} iterations'.format(
          n,
          binary_search([(x,x) for x in range(n)], -1)[1]))