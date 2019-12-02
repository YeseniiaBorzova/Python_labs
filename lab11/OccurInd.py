line = [i for i in input().split(' ')]
occurs = {}
for word in line:
    if word in occurs:
        occurs[word]+=1
    else:
        occurs[word]=0
    print(occurs[word], end=" ")