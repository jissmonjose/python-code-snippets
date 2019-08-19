# Cat and Mouse Problem


def cat_mouse(x, y, z):
    dist1 = x - z
    if dist1 < 0:
        dist1 = -dist1
    dist2 = y - z
    if dist2 < 0:
        dist2 = -dist2
    if dist1 < dist2:
        print("Cat A")
    elif dist2 < dist1:
        print("Cat B")
    else:
        print('Mouse C')


position_A = int(input('Enter Position of Cat A: '))
position_B = int(input('Enter Position of Cat B: '))
position_C = int(input('Enter Position of Mouse C: '))
cat_mouse(position_A, position_B, position_C)

