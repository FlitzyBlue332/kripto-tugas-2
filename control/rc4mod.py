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

# utility array
def swap(a, i:int, j:int):
    '''tukar element array'''
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def geserkanan(a):
    '''geser isi array ke kanan, paling ujung di keluarin'''
    x = a[-1]
    for i in range(1, len(a)):
        a[-i] = a[-i-1]
    return x

# normal RC4
def ksakeygen(key:str):
    '''
    generate stream key dalam bentuk KSA
    '''
    arraykey = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + arraykey[i] + ord(key[i % len(key)])) % 256
        swap(arraykey, i, j)
    return arraykey

def prga(plaintext, key):
    '''modded prga'''
    i = 0
    j = 0
    arraykey = myOwnKSAGen(key)
    ciphertext = []
    for k in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + arraykey[i]) % 256
        swap(arraykey, i, j)
        indexkey = (arraykey[i] + arraykey[j] + ord(key[k%len(key)])) % 256

        # digabung dengan extvigenerecipher
        cipherchar = (arraykey[indexkey] ^ plaintext[k])
        ciphertext.append(cipherchar)

        # after cipher, digunakan prinsip lfsr tapi pada byte yang ada dalam array key
        x = geserkanan(arraykey)
        arraykey[0] = arraykey[1] ^ x
    return ciphertext    

# masalah convert
def arrinttobyte(arrint):
    output = b''
    for n in arrint:
        output += n.to_bytes(1, 'little')
    return output

def arrinttotext(arrint):
    output = ''
    for n in arrint:
        output += chr(n)
    return output

def texttoarrint(text):
    output = []
    for char in text:
        output.append(ord(char))
    return output

def utf8tob64(text):
    '''convert text ke b64'''
    text_bytes = text.encode('utf-8')
    b64_textbytes = base64.b64encode(text_bytes)
    b64_text = b64_textbytes.decode('utf-8')
    return b64_text

def b64toutf8(b64text):
    b64_textbytes = b64text.encode('utf-8')
    text_bytes = base64.b64decode(b64_textbytes)
    text = text_bytes.decode('utf-8')
    return text


# def my own key
def myOwnKSAGen(key):
    return vignereExtCipher(ksakeygen(key), key)
    # return ksakeygen(key)

# def enc and dec prep
def cipherTextEnc(plaintext, key):
    plaintext_arrint = texttoarrint(plaintext)
    ciphertext_arrint = prga(plaintext_arrint, key)
    ciphertext = utf8tob64(arrinttotext(ciphertext_arrint))
    return ciphertext

def cipherTextDec(ciphertext, key):
    '''only accepts b64 text'''
    ciphertext_arrint = texttoarrint(b64toutf8(ciphertext))
    plaintext_arrint = prga(ciphertext_arrint, key)
    plaintext = arrinttotext(plaintext_arrint)
    return plaintext

def cipherFile(plaintext_byte, key):
    '''only accepts file object, method readnya "rb"'''
    ciphertext_arrint = prga(plaintext_byte, key)
    ciphertext_byte = arrinttobyte(ciphertext_arrint)
    return ciphertext_byte

# # testing (uncomment the following code to test)

# testing file (done)
# f = open('sussy_gavial.gif', 'rb')
# cipher = cipherFile(f, 'schwarz')
# f.close()
# f1 = open('sussy_gavial_enc.gif', 'wb')
# f1.write(cipher)
# f1.close
# f2 = open('sussy_gavial_enc.gif', 'rb')
# plain = cipherFile(f2, 'schwarz')
# f2.close
# f3 = open('sussy_gavial_dec.gif', 'wb')
# f3.write(plain)
# f3.close


# testing text (done)
# plain = 'schwarzuwu>_<'
# k = 'uwu'
# a = cipherTextEnc(plain, k)
# b = cipherTextDec(a, k)
# print(a)
# print(b, len(b))

