from Crypto.Cipher import AES
def encrypt(Message,Key,iv):
    mode=AES.MODE_CFB
    encryptor=AES.new(Key,mode,IV=iv)
    ciphertext=encryptor.encrypt(Message)
    return ciphertext

def decrypt(Emessage,Key,iv):
    mode=AES.MODE_CFB
    decryptor=AES.new(Key,mode,IV=iv)
    plaintext=decryptor.decrypt(Emessage)
    return plaintext

def main():
    message=['ABCDEFGHIJKLMNOP','ABCDEFGHIJKLMNOP','ABCDEFGHIJKLMNOP','BCDEFGHIJKLMNOPQ','BCDEFGHIJKLMNOPQ','CDEFGHIJKLMNOPQR','DEFGHIJKLMONPQRS']
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
        elif i==1:
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key,Ciphertext2)
            Ciphertext3= Ciphertext
            Ciphertext=bytearray(Ciphertext)
            Ciphertext[0]=Ciphertext[0]^2
            Ciphertext=str(Ciphertext)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
            Plaintext= decrypt(Ciphertext,key,Ciphertext2)
            print (Plaintext)
        elif i==2:
            Ciphertext2=Ciphertext
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key,Ciphertext3)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
            Plaintext= decrypt(Ciphertext,key,Ciphertext2)
            print (Plaintext)
        else:
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key,Ciphertext2)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
            Plaintext= decrypt(Ciphertext,key,Ciphertext2)
            print (Plaintext)

if __name__=="__main__" : main()
