s = input()
p = s.find(' ')
print(s[s.rfind(' ')+1:]+s[s.find(' '):s.rfind(' ')+1]+s[:s.find(' ')])