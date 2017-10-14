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
        if i==1:
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key)
            b= bytearray(Ciphertext)
            b[0]=b[0]^2 #CHANGING ONE BIT OF THE CIPHERTEXT
            b=str(b)
            Ciphertext1=b.encode("hex")
            print (Ciphertext1)
            Plaintext= decrypt(b,key)
            print (Plaintext)
        else:
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
            Plaintext= decrypt(Ciphertext,key)
            print (Plaintext)

if __name__=="__main__" : main()
