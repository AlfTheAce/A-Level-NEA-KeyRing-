# master password
import _pickle as cPickle
import hashlib
import tkinter as tk
from tkinter import messagebox
import subprocess
account_check =  ""
password_check = ""
def view_passwords():
    win2 = tk.Tk()
    frame = tk.Frame(win2)
    win2.geometry("300x150")
    # account entry title
    account_entry_title = tk.Label(win2, text=('Account Name:'), font=('Arial', 10))
    account_entry_title.pack()

    # account entry box
    account_entry_box =tk.Entry(win2, textvariable= account_check, font=('Arial', 10))
    account_entry_box.pack()

    # password entry title
    password_entry_title = tk.Label(win2, text=('Password:'), font=('Arial', 10))
    password_entry_title.pack()

    # password entry box
    password_entry_box = tk.Entry(win2, textvariable= password_check, font=('Arial', 10), show='*')
    password_entry_box.pack()
    
    def check_password():
        # open the 2 pickle files and read the contents of them 
        with open('account_file.pkl', 'rb') as f:
            account_name_loaded = cPickle.load(f)
            print(account_name_loaded)
        with open('master_password_file.pkl', 'rb') as f:
            master_password_loaded = cPickle.load(f)
            print(master_password_loaded)
        account_check = account_entry_box.get()
        # Check if the Account name entered in the box is the same as the one in the pickle file 
        if account_check == account_name_loaded:
            account_check = True
        else:
            account_check = False
        # Hash the user input in the entry box using sha256 
        password_check = password_entry_box.get()
        hash_check = hashlib.sha256(password_check.encode())
        hex_check = hash_check.hexdigest()
        # Check if the hashed passwords match 
        if hex_check == master_password_loaded:
            password_check = True
        else:
            password_check = False
        # Final Checks and print the results in the shell
        if account_check == True:
            print("account correct")
        else:
            print("account incorrect")
        if password_check == True:
            print("password correct")
        else:
            print("password incorrect")
        if account_check and password_check == True:
            final_check = True
        else:
            final_check = False
        if final_check == False:
            tk.messagebox.showinfo('password score', 'incorrect')
        if final_check == True:
            print("Correct")
            file = open("accounts_file.csv", mode = 'r', encoding='utf-8')
            print(file.read())
            file.close()
    # check password button
    check_password_button = tk.Button(win2, text=('Enter'), font=('Arial', 10), command= check_password)
    check_password_button.pack()
        
            
            
def decryption():
    win2 = tk.Tk()
    frame = tk.Frame(win2)
    win2.geometry("300x150")
    # account entry title
    account_entry_title = tk.Label(win2, text=('Account Name:'), font=('Arial', 10))
    account_entry_title.pack()

    # account entry box
    account_entry_box =tk.Entry(win2, textvariable= account_check, font=('Arial', 10))
    account_entry_box.pack()

    # password entry title
    password_entry_title = tk.Label(win2, text=('Password:'), font=('Arial', 10))
    password_entry_title.pack()

    # password entry box
    password_entry_box = tk.Entry(win2, textvariable= password_check, font=('Arial', 10), show='*')
    password_entry_box.pack()
    def decryption_check():
        with open('account_file.pkl', 'rb') as f:
            account_name_loaded = cPickle.load(f)
            print(account_name_loaded)
        with open('master_password_file.pkl', 'rb') as f:
            master_password_loaded = cPickle.load(f)
            print(master_password_loaded)
        account_check = account_entry_box.get()
        if account_check == account_name_loaded:
            account_check = True
        else:
            account_check = False
        password_check = password_entry_box.get()
        hash_check = hashlib.sha256(password_check.encode())
        hex_check = hash_check.hexdigest()
        if hex_check == master_password_loaded:
            password_check = True
        else:
            password_check = False
        if account_check == True:
            print("account correct")
        else:
            print("account incorrect")
        if password_check == True:
            print("password correct")
        else:
            print("password incorrect")
        if account_check and password_check == True:
            final_check = True
        else:
            final_check = False
        return final_check
    # check password button
    check_password_button = tk.Button(win2, text=('Enter'), font=('Arial', 10), command= check_password)
    check_password_button.pack()


# function to encrypt and store a master password and aan account name in seperate files 
def new_user():
    # get the desired user name and password from the user
    master_password = input("new password: ")
    account_name = input("account name: ")

    # hash the master password using the SHA256 algorithm 
    hash_object = hashlib.sha256(master_password.encode())
    hex_dig = hash_object.hexdigest()

    # open the pickle files and store the hashed password and account name 
    with open('account_file.pkl', 'wb') as f:
        cPickle.dump(account_name, f)
    with open('master_password_file.pkl', 'wb') as f:
        cPickle.dump(hex_dig, f)

    # return the hashed password for later 
    return(hex_dig)



