tSize = 80*1.25
pWidth = tSize
pHeight = tSize
mCols = 10
mRows = 10
wSize = (800*1.25, 800*1.25)
wWidth, wHeight = wSize
bColor = (0,0,0)
tColor = (255,255,255)
tFPS = 60
for v, r in globals().copy().items():
    try:
        globals()[v] = int(r)
    except:
        pass
