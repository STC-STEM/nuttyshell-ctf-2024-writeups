In this challenge, we are given 3 files:
- `screencap.png`:
- `chall.cpython-312.pyc`
- `output.txt`

`screencap.png` shows a timestamp

![screencap.png](screencap.png?raw=true "screencap.png")

Since the file size of `chall.cpython-312.pyc` is quite tiny, we have decided to manually reverse it. The below shows the main procedure of the program:

```
...

 43          74 PUSH_NULL
             76 LOAD_NAME                5 (init)
             78 CALL                     0
             86 POP_TOP

 44          88 PUSH_NULL
             90 LOAD_NAME                9 (open)
             92 LOAD_CONST               9 ('output.txt')
             94 LOAD_CONST              10 ('w')
             96 CALL                     2
            104 BEFORE_WITH
            106 STORE_NAME              10 (f)

 45         108 LOAD_NAME                1 (flag)
            110 GET_ITER
        >>  112 FOR_ITER                25 (to 166)
            116 STORE_NAME              11 (i)

 46         118 LOAD_NAME               10 (f)
            120 LOAD_ATTR               25 (NULL|self + write)
            140 PUSH_NULL
            142 LOAD_NAME                7 (encrypt)
            144 LOAD_NAME               11 (i)
            146 CALL                     1
            154 CALL                     1
            162 POP_TOP
            164 JUMP_BACKWARD           27 (to 112)

 45     >>  166 END_FOR
```

Reversed:

```Python
init()
f = open('output.txt', 'w')
for i in flag:
    f.write(encrypt(i))
```

Reversing the other functions:
```Python
def init():
    if isPrime(3):
        seed = datetime.now()
        print(seed.strftime('%Y/%m/%d %H:%M:%S'))
        seed = int(seed.timestamp())
        random.seed(seed)
        
def encrypt(char):
    if isPrime(3):
        char = ord(char)
        rand = 0
        while not isPrime(rand):
            rand = random.randint(0, 256)
        char = (char + rand) % 256
        return chr(char)
```

Since Pseudo Random Number Generators (PRNG) always generate the same sequence of random number for a given seed, we can decrypt `output.txt` by setting the seed to the unix timestamp (in seconds) shown in `screencap.png`.

`solve.py`:

```Python
seed = datetime.strptime('2024/02/20 18:09:38', '%Y/%m/%d %H:%M:%S')
random.seed(int(seed.timestamp()))

with open('output.txt', 'r') as f:
    output = f.read(1000)

def decrypt(char_data):
    if isPrime(3):
        char = ord(char_data)
        rand = 0
        while not isPrime(rand):
            rand = random.randint(0, 256)
        char = (char - rand) % 256
        return chr(char)

flag = ''.join([str(decrypt(char_data)) for char_data in output])
print(flag)
```

which outputs the flag: `PUCTF24{n0w_1_can_tung11ng_the_history_677e48204d85705361a1d6b35e3a72b8}`