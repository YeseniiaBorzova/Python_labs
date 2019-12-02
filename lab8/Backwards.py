def backwards():
    a = int(input())
    if a != 0:
        backwards()
    print(a)


backwards()