#!/usr/bin/python

## Challenge: Wie lautet das Passwort?
passw = "****************"


## clean() entfernt alle Buchstaben aus dem Text die nicht im Alphabet enthalten sind.
def clean(txt):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cltxt = ''
    for char in txt.upper():
        if char in alphabet:
            cltxt += char
    return cltxt


def enc(ptxt, key):
    ctxt = ''
    for i in range(len(ptxt)):
        ctxt += chr( (ord(ptxt[i]) ^ ord(key[i%len(key)])) + ord('A') )
    return ctxt

def dec(ctxt, key):
    ptxt = ''
    for i in range(len(ctxt)):
        ptxt += chr( ((ord(ctxt[i]) - ord('A')) ^ ord(key[i%len(key)])) )
    return ptxt


## ENCRYPT and WRITE TO FILE:
#plain = open("./plain.txt","r").read()
#ofile = open("./cipher.txt", "w")
#ofile.write(enc(clean(plain), passw))

## DECRYPT
cipher = open("./cipher.txt","r").read()
print dec(cipher, passw),
