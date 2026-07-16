from PIL import Image, ImageDraw
import math

BG = (28,25,21,255)      # --bg
BRASS = (201,164,92,255) # --brass
CLOTH = (53,121,75,255)  # --cloth
WHITE = (243,238,224,255)
WHITE_STROKE = (184,176,154,255)
RED = (200,52,43,255)
RED_STROKE = (122,23,18,255)

def draw_icon(size, maskable=False, transparent_bg=False):
    img = Image.new('RGBA', (size, size), (0,0,0,0))
    d = ImageDraw.Draw(img)

    if maskable:
        d.rectangle([0,0,size,size], fill=BG)
        pad = size*0.16
    elif transparent_bg:
        pad = size*0.04
    else:
        radius = size*0.22
        d.rounded_rectangle([0,0,size-1,size-1], radius=radius, fill=BG)
        pad = size*0.10

    inset = pad
    ring_w = max(2, round(size*0.022))
    d.ellipse([inset, inset, size-inset, size-inset], fill=CLOTH, outline=BRASS, width=ring_w)

    # aim line (cue ball -> object ball), drawn dashed
    cx1, cy1 = size*0.35, size*0.42
    cx2, cy2 = size*0.63, size*0.63
    steps = 7
    for i in range(steps):
        if i % 2 == 0:
            t0 = i/steps; t1 = (i+0.6)/steps
            x0 = cx1 + (cx2-cx1)*t0; y0 = cy1 + (cy2-cy1)*t0
            x1 = cx1 + (cx2-cx1)*t1; y1 = cy1 + (cy2-cy1)*t1
            d.line([x0,y0,x1,y1], fill=BRASS, width=max(2, round(size*0.018)))

    r = size*0.115
    d.ellipse([cx2-r, cy2-r, cx2+r, cy2+r], fill=RED, outline=RED_STROKE, width=max(1, round(size*0.008)))
    d.ellipse([cx1-r, cy1-r, cx1+r, cy1+r], fill=WHITE, outline=WHITE_STROKE, width=max(1, round(size*0.006)))

    return img

sizes = [192, 512]
for s in sizes:
    draw_icon(s).save(f'icons/icon-{s}.png')
draw_icon(512, maskable=True).save('icons/icon-maskable-512.png')
draw_icon(180).save('icons/apple-touch-icon.png')
# favicon-style small transparent icon
draw_icon(32, transparent_bg=True).save('icons/favicon-32.png')
print('done')
