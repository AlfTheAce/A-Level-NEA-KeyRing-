# encrypt and decrypt with ROT13 using ord() and chr() with object oriented

# defining and naming the seperate lists 
num_list = []
encrypt_list = []
decrypt_list = []
num_list2 = [] 

# the main function of this algorithm where the user inputs the message to encrypt and decrypt 
def main():
    decrypted_password = input("input a message to encrypt: ")
    result = encrypt(message1)
    print(result)
    
    encrypted_password = input("input a message to decrypt: ")
    result = decrypt(message2)
    print(result)

# encryption function 
def encrypt(new_password):
    # clear both lists  
    for c in new_password:
        # convert to ascii and add 13 to every character in message1 
        y = ord(c) + 13
        num_list.append(y)
    for i in num_list:
        # convert every number in num_list back into characters 
        z = chr(i)
        encrypt_list.append(z)
    # convert to a string by joining each letter in the list with no space 
    a = "".join(encrypt_list)
    num_list.clear()
    encrypt_list.clear()
    return a

# decryption function
def decrypt(encrypted_password):
    # clear both of the lists 
    for c in encrypted_password:
        # convert each character in message2 into ASCII then - 13 from the value
        t = ord(c) - 13
        num_list2.append(t)
    for i in num_list2:
        # convert the value back into characters 
        u = chr(i)
        decrypt_list.append(u)
    # turn the decrypt_list into a string by joining them with no spaces
    b = "".join(decrypt_list)
    num_list2.clear()
    decrypt_list.clear()
    return b



        
        
        

        
        

