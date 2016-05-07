rows = "ABCDEFGHI"
cols = "123456789"

squares = [r+c for r in rows for c in cols]

row_units = [[r+c for c in cols] for r in rows]
print(row_units)

col_units = [[r+c for r in rows] for c in cols]
print(col_units)

box1 = [r+c for r in rows[0:3] for c in cols[0:3]]
print(box1)

box_units = [[r+c for r in rows[rs:rs+3] for c in cols[cs:cs+3]] 
              for rs in range(0,9,3) 
              for cs in range(0,9,3)]
print(box_units)

all_units = ([[r+c for c in cols] for r in rows]+
            [[r+c for r in rows] for c in cols]+
            [[r+c for r in rows[rs:rs+3] for c in cols[cs:cs+3]] 
              for rs in range(0,9,3) 
              for cs in range(0,9,3)])
              
print(all_units)

c2_units = [u for u in all_units if 'C2' in u]
print(c2_units)

# list of tuples
square_units = [(s, [u for u in all_units if s in u]) for s in squares]

print(square_units[0])

to_find = 'C2'
for entry in square_units:
    if entry[0] == to_find:
        units = entry[1]
        break
else: # enter when loop goes through all values and doesn't break
    units = None
    
print(units)

# dictionary
alter_egos = {'Superman':'Clark Kent',
              'Batman':'Bruce Wayne',
              'Spiderman':'Peter Parker'}
print(alter_egos['Superman'])
alter_egos['Iron man'] = 'Tony stark'
print(alter_egos)

try:
    print(alter_egos['Dr. Doom'])
except:
    print('No key')
else:
    print('Yes key')
finally:
    print('Finally')
    
print(alter_egos.get('Super'))
print(alter_egos.get('Super', 'No Key'))

  # tuple of key/value pairs
for kv in alter_egos.items():
    print(kv[0], '=>', kv[0])
  # spliting assignments
for k, v in alter_egos.items():
    print(k, '=>', v)

# sorted    
for sup in sorted(alter_egos.keys()):
    print(sup, '=>', alter_egos[sup])
    
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             #keys     values
alpha_num = {alpha[i]: i+1 for i in range(0,len(alpha))}
print(alpha_num)

units = {s: [u for u in all_units if s in u] for s in squares}
print(units['C2'])
c2_units = units['C2']

c2_peers = set([sq for u in c2_units for sq in u]) - {'C2'}

print(len(c2_peers))
print(sorted(c2_peers))

peers = {s: (set([sq for u in units[s] for sq in u]) - {s}) for s in squares}
print(peers['C2'])

assert(len(squares) == 81)
assert(len(squares) == 8)