from Crypto.Cipher import AES
def encrypt(Message,Key,iv):
    mode=AES.MODE_OFB
    encryptor=AES.new(Key,mode,IV=iv)
    ciphertext=encryptor.encrypt(Message)
    return ciphertext

def decrypt(Emessage,Key,iv):
    mode=AES.MODE_OFB
    decryptor=AES.new(Key,mode,IV=iv)
    plaintext=decryptor.decrypt(Emessage)
    return plaintext

def main():
    message=['ABCDEFGHIJKLMNOP','ABCDEFGHIJKLMNOP','ABCDEFGHIJKLMNOP','BCDEFGHIJKLMNOPQ','BCDEFGHIJKLMNOPQ','CDEFGHIJKLMNOPQR','DEFGHIJKLMONPQRS','EFGHIJKLMNOPQRST']
    message1='Give  Eve   $100'
    key= '0123456789abcdef'
    Init='iamsumedhkarande'
    print message1
    Ciphertext3=encrypt(message1,key,Init)
    ListCT=[]
    ListCT2=[]
    Ciphertext=0
    for i in range(0,7):
        Ciphertext2=Ciphertext
        ListCT2.append(Ciphertext2)
        if i==0:
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key,Init)
            ListCT.append(Ciphertext)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
        else:
            print('The message is',message[i])
            Ciphertext= encrypt(message[i],key,Ciphertext2)
            ListCT.append(Ciphertext)
            Ciphertext1=Ciphertext.encode("hex")
            print (Ciphertext1)
    ListCT[0]=Ciphertext3
    for j in range(0,7):
        if j==0:
            Plaintext= decrypt(ListCT[j],key,Init)
            print (Plaintext)
        elif j==1:
            Plaintext= decrypt(ListCT[j],key,ListCT[j-1])
            print (Plaintext)
        else:
            Plaintext= decrypt(ListCT[j],key,ListCT2[j])
            print (Plaintext)

if __name__=="__main__" : main()
