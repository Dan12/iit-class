puzzle = """4.....8.5
            .3.......
            ...7.....
            .2.....6.
            ....8.4..
            ....1....
            ...6.3.7.
            5..2.....
            1.4......"""
            
rows = 'ABCDEFGHI'
cols = '123456789'

squares = [r+c for r in rows for c in cols]
row_units = [[r+c for c in cols] for r in rows]
col_units = [[r+c for r in rows] for c in cols]
box_units = [[r+c for r in rs for c in cs]
            for rs in (rows[i:i+3] for i in range(0,len(rows),3))
            for cs in (cols[i:i+3] for i in range(0,len(cols),3))]
all_units = row_units + col_units + box_units
units = {s: [u for u in all_units if s in u] 
         for s in squares}
print(units['C2'])

# dictionary
peers = {s: set(sq for u in units[s] for sq in u) - {s}
        for s in squares}
        
def parse_puzzle(puz):
    # list
    puzzle = [c if c.isdigit() else None
              for c in puz if c not in ' \n']
    assert(len(puzzle) == 81)
    #dict
    return {squares[i]: puzzle[i]
            for i in range(0, len(squares))}

import pprint as pp
pp.pprint(parse_puzzle(puzzle))

def assign(sol, sq, val):
    # sol-dict mapping string of 123..9 to square names "C2"
    # eliminate all values from square sq except val
    sol[sq] = str(val)
    for peer in peers[sq]:
        eliminate(sol, peer, val)
        
def eliminate(sol, sq, val):
    # remove value val from square sq, then
    # (1) if there's only one value left, eliminate 
    #     it from all my peers
    # (2) if we just eliminated the second-to-last
    #     entry for a given value in some unit, 
    #     assign the value to the final square
    
    wasOne = False
    if len(sol[sq]) == 1:
        wasOne = True
    
    sol[sq] = sol[sq].replace(str(val),'')
    if not wasOne and len(sol[sq]) == 1:
        assign(sol,sq,sol[sq])
        
sol = {s: '123456789' for s in squares}

for sq, val in parse_puzzle(puzzle).items():
    if val:
        assign(sol, sq, val)
        
def print_puzzle(sol):
    "Display these values as a 2-D grid."
    width = 1+max(len(sol[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(sol[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print()
    
def search(sol):
    # find a square with the least number of values > 1
    #
    # (1) "guess" one of the values (assign it) and
    #     try to solve the rest of the puzzle 
    #
    # (2) if we guessed wrong and the solution is broken,
    #     backtrack --- i.e., restore the original values
    #     and guess another value
    
    # check if sol is solved
    # i.e, every square has one number
    for i in sol:
        if len(sol[i]) != 1:
            break
    #solved puzzle
    else:
        return True
    
    # initialize minimun key
    minKey = ""
    # find square with lowest number
    # of possibilities
    for i in sol:
        if len(sol[i]) > 1:
            if minKey == "" or len(sol[i]) < len(sol[minKey]):
                minKey = i
    
    # for every possibility for
    # the square
    for c in sol[minKey]:
        # make a copy of current solution
        savedSol = sol.copy()
        # assign value guess to square
        assign(sol, minKey, c)
        # make sure guess didn't break board
        for i in sol:
            if sol[i] == "":
                sol.update(savedSol)
                break
        # if board is still intact
        else:
            
            # do a new search on current board
            # and if we found the solution
            if search(sol):
                return True
            # else, revert
            else:
                sol.update(savedSol)
        
    
    return False
    
search(sol)
print_puzzle(sol)