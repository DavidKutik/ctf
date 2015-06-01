def encode(ptxt, key=3):
    ctxt = ''
    for letter in ptxt:
        ctxt += chr(((ord(letter)-ord('A')+key)%26)+ord('A'))
    return ctxt

def decode(ctxt, key=3):
    return encode(ctxt, 26-key)


def enc(ptxt, key):
    ctxt = ''
    for i in range(len(ptxt)):
        ctxt += chr((( ord(ptxt[i]) + ord(key[i%len(key)]) - 2*ord('A')) % 26) + ord('A'))
    return ctxt

def dec(ctxt, key):
    rkey =''
    for k in key:
        rkey += chr(26 - ord(k) + 2*ord('A'))
    return enc(ctxt, rkey)

bla = 'Hallo Welt'
#print decode(encode(bla.upper().replace(' ','')))

print bla.upper().replace(' ','')
print enc(bla.upper().replace(' ',''), 'DU')
