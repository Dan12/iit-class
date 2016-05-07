print("Hello")

rows = "ABCDEFGHI"
cols = "123456789"

squares = [r+c for r in rows for c in cols]

print(squares)
print(len(squares))

#c2_rows = squares[9*2:9*3]
c2_rows = ["C"+c for c in cols]
print(c2_rows)
c2_col = [r+"2" for r in rows]
print(c2_col)
c2_box = [r+c for r in rows[0:3] for c in cols[0:3]]
print(c2_box)

all_rows = [[r+c for c in cols] for r in rows ]
print(all_rows)

all_cols = [[r+c for r in rows] for c in cols]
print(all_cols)

all_boxes = [[r+c for r in rs for c in cs] for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
print(all_boxes)