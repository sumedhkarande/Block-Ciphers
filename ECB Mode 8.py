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
    message1='Give  Eve   $100'
    key= '0123456789abcdef'
    print message1
    Ciphertext2=encrypt(message1,key)
    ListCT=[]

    for i in range(0,6):
        print('The message is',message[i])
        Ciphertext= encrypt(message[i],key)
        Ciphertext1=Ciphertext.encode("hex")
        print (Ciphertext1)
        ListCT.append(Ciphertext)
    ListCT[2]=Ciphertext2
    ListCT[3]=Ciphertext2
    ListCT[4]=Ciphertext2
    for j in range(0,6):
        Plaintext= decrypt(ListCT[j],key)
        print (Plaintext)

if __name__=="__main__" : main()
