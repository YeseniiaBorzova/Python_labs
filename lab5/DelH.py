s = input()
a = s.find('h')
b = s.rfind('h')+1
print(s[:a]+s[b:])