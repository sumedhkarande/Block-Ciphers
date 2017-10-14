from Crypto.Cipher import AES
key= '0123456789abcdef'
IV='iamsumedhkarande'
mode=AES.MODE_CBC
encryptor=AES.new(key,mode,IV=IV)

text='Hi,How you doing'
ciphertext=encryptor.encrypt(text)
print ciphertext

decryptor=AES.new(key,mode,IV=IV)
plaintext=decryptor.decrypt(ciphertext)
print plaintext
