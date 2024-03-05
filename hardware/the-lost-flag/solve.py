import csv

# char_map[upper][lower]
char_map = [
    [' ']*16,
    [' ']*16,
    [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ],
    list('0123456789:;<=>?'),
    list('?ABCDEFGHIJKLMNO'),
    list('PQRSTUVWXYZ[￥]^_'),
    list('`abcdefghijklmno'),
    list('pqrstuvwxyz{|}<>'),
    list('                '),
    list('                '),
    list('                '),
    list('                '),
    list('                '),
    list('                '),
    list('                '),
    list('                '),
    list('                '),
]

rows = None
with open('./Sniffed_Conversations.csv', newline='') as csvfile:
    rows = list(csv.reader(csvfile))

# D7, D6, D5, D4, EN
rows = [[x[8], x[1], x[2], x[3]] for x in rows if x[5] == ' 1' and x[4] == ' 1']
rows = [[int(x[0]), int(x[1]), int(x[2]), int(x[3])] for x in rows]
rows = [[str(x[0]), str(x[1]), str(x[2]), str(x[3])] for x in rows]

data = ''
upper = 0

j = 0
for i in rows:
    print(i)
    j = (j + 1) % 2
    if j == 1:
        upper = int(''.join(i), 2)
    if j == 0:
        lower = int(''.join(i), 2)
        data += char_map[upper][lower]
        print()
    print(data)

print(data)
