from Crypto.Cipher import AES
def encrypt(Message,Key,iv):
    mode=AES.MODE_CBC
    encryptor=AES.new(Key,mode,IV=iv)
    ciphertext=encryptor.encrypt(Message)
    return ciphertext

def decrypt(Emessage,Key,iv):
    mode=AES.MODE_CBC
    decryptor=AES.new(Key,mode,IV=iv)
    plaintext=decryptor.decrypt(Emessage)
    return plaintext

def main():
    message=['ABCDEFGHIJKLMNOP','ABCDEFGHIJKLMNOP','ABCDEFGHIJKLMNOP','BCDEFGHIJKLMNOPQ','BCDEFGHIJKLMNOPQ','CDEFGHIJKLMNOPQR','DEFGHIJKLMONPQRS','EFGHIJKLMNOPQRST']
    key= '0123456789abcdef'
    Init='iamsumedhkarande'
    Ciphertext=0
    for i in range(0,7):
        Ciphertext2=Ciphertext
        if i==0:
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key,Init)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
            Plaintext= decrypt(Ciphertext,key,Init)
            print (Plaintext)
        else:
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key,Ciphertext2)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
            Plaintext= decrypt(Ciphertext,key,Ciphertext2)
            print (Plaintext)

if __name__=="__main__" : main()
