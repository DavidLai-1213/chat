
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    new = []
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    msg = s[1:]
    new.append(time + name + msg)
    
with open('3out.txt', 'w', encoding = 'utf-8-sig') as f:
    for line in f:
        f.write(new + '\n')

