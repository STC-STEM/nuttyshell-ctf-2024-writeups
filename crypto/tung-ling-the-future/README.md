`chall.py`:
```Python
from Crypto.Util.number import getRandomInteger
from flag import flag, m, a, c

class Rand:
    def __init__(self, seed):
        self.m = m
        self.a = a
        self.c = c
        self.seed = seed
        if seed % 2 == 0:
            self.seed += 1

    def rand(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

def main():
    rng = Rand(getRandomInteger(32))

    print("I give you the past, can you predict the future?")
    for _ in range(10):
        print(rng.rand())

    for _ in range(10):
        x = int(input('input next number> '))
        if x != rng.rand():
            print("You should study Tong Ling More")
            return

    print("You are Tong Ling master")
    print(flag)


if __name__ == "__main__":
    main()
```

The PRNG generates a random number base on the current seed, and set the generated number to be its next seed.
Given 10 consecutive seeds, we are asked to predict the next 10 seeds.



Denote the initial seed as $s_0$, and the subsequent seeds generated as $s_1$, $s_2$, ...

After a few trials, we will notice that the largest $s_n$ is very close to $10^{19}$

We only have to consider 4 consecutive seeds. Let pick $s_1$, $s_2$, $s_3$ and $s_4$

For convenience, we'll be using these variables

$p = s_2 - s_1$

$q = s_3 - s_2$

$r = s_4 - s_3$

Since $s_{n+1} \equiv as_n + c \pmod m$

Therefore $s_{n+2} - s_{n+1} \equiv (s_{n+1} - s_n)a \pmod m$

$q \equiv pa \pmod m$

$r \equiv qa \pmod m$

Cross multiplying, we have $(q^2 - pr) \mid m$

With a few trials

$(q^2 - pr) = 60681367337024189986701450616061524848 = 2^4 × 3 × 7^2 × 191 × 959207 × 3412547641 × 41266117556007997$

$(q^2 - pr) = 39640735732326914687871304305465235424 = 2^5 × 191 × 277 × 959207 × 3412547641 × 7152988539803923$

$(q^2 - pr) = 28275749127143381290655390330303517184 = 2^9 × 11^2 × 191 × 599 × 163643 × 959207 × 7447493 × 3412547641$

all of which are divisible by m

Recalling that the largest $s_n$ (i.e., the value of $m$) is very close to $10^19$

Consider the common factor of the above numbers, we have $m = 2^4 * 191 * 959207 * 3412547641$

Then $a \equiv p^{-1}q \pmod m$

Solving the equation, we have

$a = 2217558108606715201$

$c = 8407371931683985347$


After knowing the value of `a` and `c`, we can solve the challenge easily.

`solve.py`:
```Python
from pwnlib.tubes.remote import remote

r = remote('chal.polyuctf.com', 21338)
r.recvline()  # I give you the past ...
seed = [0]
for i in range(10):
    seed.append(int(r.recvline()))

print(seed)

m = 2 * 2 * 2 * 2 * 191 * 959207 * 3412547641
a = 2217558108606715201
c = 8407371931683985347

last_seed = seed[10]
for i in range(10):
    last_seed = (a * last_seed + c) % m
    r.sendlineafter(b'input next number>', str(last_seed).encode('utf-8'))

print(r.recvline())
print(r.recvline())
```

And we got the flag: `PUCTF24{n0w_1_can_tung11ng_the_future_d41d8cd98f00b204e9800998ecf8427e}`
