angle = float(input())
if angle % 30 == 0:
    print(0)
else:
    minAngle = angle % 30
    part = 30/minAngle
    print(round((360/part),5))