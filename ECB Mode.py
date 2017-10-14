from Crypto.Cipher import AES
key= '0123456789abcdef'
#IV=16* '\x00'


def encrypt(Message,Key):
    mode=AES.MODE_ECB
    encryptor=AES.new(Key,mode)
    ciphertext=encryptor.encrypt(Message)
    return ciphertext

def decrypt(Emessage,Key):
    mode=AES.MODE_ECB
    decryptor=AES.new(Key,mode)
    plaintext=decryptor.decrypt(Emessage)
    return plaintext

def main():
    message=['ABCDEFGHIJKLMNOP','ABCDEFGHIJKLMNOP','BCDEFGHIJKLMNOPQ','CDEFGHIJKLMNOPQR','DEFGHIJKLMONPQRS','EFGHIJKLMNOPQRST']
    key= '0123456789abcdef'
    for i in range(0,6):
        print('The message is',message[i])
        Ciphertext= encrypt(message[i],key)
        print Ciphertext
        Ciphertext1=Ciphertext.encode("hex")
        print (Ciphertext1)
        Plaintext= decrypt(Ciphertext,key)
        print (Plaintext)

if __name__=="__main__" : main()
