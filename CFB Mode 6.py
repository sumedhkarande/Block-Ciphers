from Crypto.Cipher import AES
def encryption(Message,Key,iv):
    mode=AES.MODE_CFB
    encryptor=AES.new(Key,mode,IV=iv)
    ciphertext=encryptor.encrypt(Message)
    return ciphertext

def decryption(Emessage,Key,iv):
    mode=AES.MODE_CFB
    decryptor=AES.new(Key,mode,IV=iv)
    plaintext=decryptor.decrypt(Emessage)
    return plaintext

def main():
    message=['ABCDEFGHIJKLMNOP','ABCDEFGHIJKLMNOP','BCDEFGHIJKLMNOPQ','BCDEFGHIJKLMNOPQ','CDEFGHIJKLMNOPQR','DEFGHIJKLMONPQRS','EFGHIJKLMNOPQRST']
    key= '0123456789abcdef'
    key1='0123456788abcdef'
    Init='iamsumedhkarande'
    Ciphertext=0
    for i in range(0,7):
        Ciphertext2=Ciphertext
        if i==0:
            print('The message is',message[i])
            Ciphertext= encryption(message[i],key,Init)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
            Plaintext= decryption(Ciphertext,key1,Init)
            print (Plaintext)
        else:
            print('The message is',message[i])
            Ciphertext= encryption(message[i],key,Ciphertext2)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
            Plaintext= decryption(Ciphertext,key1,Ciphertext2)
            print (Plaintext)

if __name__=="__main__" : main()
