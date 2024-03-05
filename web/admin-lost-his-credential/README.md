`app.py`:
```Python
# ...

@app.route('/profile')
def profile():
    if request.cookies.get('identity'):
        try:
            cookie = decrypt(request.cookies.get('identity'))
            username = cookie.split('&')[0].split('=')[1]
            admin = cookie.split('&')[1].split('=')[1]
            if admin == 'True':
                flag = open('flag.txt', 'r').read()
                return 'Welcome, ' + username + '! Here is your flag: ' + flag + ' <br/>(This is a secret for admin only)'
            else:
                return 'Welcome, ' + username + '! <br/> <a href="/logout">Logout</a>'
        except:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

# ...

def decrypt(cipher):
    buf = bytes.fromhex(base64.b64decode(cipher).hex())
    i = 0
    output = []
    for b in buf:
        output.append( b ^ key[i % len(key)] )
        i = i + 1
    output = bytes(output).decode()
    return output
```

Where
`identity` is a base64-encoded strings that looks like this:
`WmOm6E638GaMkeG6RzBBbUB/86sGt/lu2JaxnUs9XG8=`.

Our goal is to create an `identity`,
which, when xor-decrypted, produce a string `username=[user]&admin=True`. Since `clear_text ⊕ key = identity`, we can retrieve the key by knowing `clear_text` and `identity`

- By creating an account with username `imamangoo01`, we know that the `clear_text` will be `username=imamangoo01&admin=True`.

- We can find `identity` by inspecting the http headers.
`solve.py`:

```Python
username = b"username=imamangoo01"
identity = base64.b64decode("WmOm6E638GaMkeG6RzBBbUB/86sGt/lu2JaxnUs9XG8=")

key = xor(identity, username)[:16]
adminIdentity = base64.b64encode(xor(b"username=imamangoo01&admin=True", key))
```

Logging in with this `identity`, we've got our flag: `PUCTF24{y0u_kn0w_h0w_t0_b5c0m5_adm1n15tr4t0r_3af9b6a0718c4e239d5c6fe802b9e517}`
