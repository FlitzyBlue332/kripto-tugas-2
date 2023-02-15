# import-import module uwu
import base64

# vigenere cipher
def trueVignereChipherKey(ptext, key):
    true_key = []
    for i in range(len(ptext)):
        true_key.append(key[i % len(key)])
    return true_key

def vignereExtCipher(ptext, key):
    true_key = trueVignereChipherKey(ptext, key)
    cptext = []

    for i in range(len(ptext)):
        enc_char = (ptext[i] + ord(true_key[i]))%256
        cptext.append(enc_char)
    return cptext

# normal RC4
def ksakeygen(key):
    arraykey = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + arraykey[i] + ord(key[i % len(key)])) % 256
        temp = arraykey[i]
        arraykey[i] = arraykey[j]
        arraykey[j] = temp
    return arraykey

# masalah int to b64
def normtexttob64(text):
    text_bytes = text.encode('ascii')
    b64_textbytes = base64.b64encode(text_bytes)
    b64_text = b64_textbytes.decode('ascii')
    return b64_text

def b64tonormtext(b64text):
    b64_textbytes = b64text.encode('ascii')
    text_bytes = base64.b64decode(b64_textbytes)
    text = text_bytes.decode('ascii')
    return text


# def my own key
def myOwnKeyGen(key):
    return vignereExtCipher(ksakeygen(key), key)

def myOwnStreamCipher(plaintext, key):
    cp = []
    arraykey = ksakeygen(key)

    for i in range(len(plaintext)):
        cp.append(ord(plaintext[i]) ^ arraykey[i % 256])
    
    return cp

testtext = 'schwarzuwu>_<'
b64text = normtexttob64(testtext)
normtext = b64tonormtext(b64text)
print(b64text)
print(normtext)
