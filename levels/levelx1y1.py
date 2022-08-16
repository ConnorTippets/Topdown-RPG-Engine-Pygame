from properties import *
def generate_empty():
    _ = []
    def generate_column_full():
        for x in range(mCols):
           _.append(1)
    
    def generate_column_box():
        _.append(1)
        for x in range(mCols-2):
            _.append(0)
        _.append(1)
    
    generate_column_full()
    for y in range(mRows-2):
        generate_column_box()
    generate_column_full()
    return _
map = generate_empty()
for x in range(mCols-1):
    map[9*mCols+x] = 0
for y in range(1, mRows-1):
    map[y*mCols] = 0
map[9*mCols] = 1
