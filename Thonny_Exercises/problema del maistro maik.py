i = 0
e = "*"
s = " " * 20
while i < 10:
    print(s + e)
    s = s[1:] 
    e += "**"
    i += 1
