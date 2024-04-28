# interface (main menu)
import tkinter as tk
from tkinter import messagebox
import csv
import password_generation
import strength_check
import encryption_and_decryption
import save_to_file
import master_password_storage
# set all variables to null 
pswd_length = ""
generated_password = ""
password = ""
encrypted_password = ""
decrypted_password = ""
website_name = ""
account_name = ""
new_password = ""
# define the main window and window size 
win = tk.Tk()
frame = tk.Frame(win)
win.geometry("1000x400")

# Main menu title
main_title = tk.Label(win, text="KeyRing", font=('Arial bold', 80))
main_title.pack()

# Password generation title 
password_generation_title = tk.Label(win, text="Password Generation", font=('Arial bold', 20))
password_generation_title.place(x=30, y=140)

# Password length subtitle 
password_length_title = tk.Label(win, text="Password Length", font=('Arial', 20))
password_length_title.place(x=30, y=180)

# Password length entry 
password_length = tk.Entry(win, textvariable= pswd_length, font=('Arial',10))
password_length.place(x=30, y=220)

# Function to generate the password 
def generate_click():
    # get the password length from the password_length input box 
    pswd_length = int(password_length.get())
    # run the generate function from the password_generation file
    generated_password = password_generation.generate(pswd_length)
    # insert the output text into the output box 
    password_output.insert(0, generated_password)

# Button that generates password 
generate_button = tk.Button(win, text=('Generate'), font=('Arial', 10), command= generate_click)
generate_button.place(x=30, y=245)

# Output box where the password is displayed 
password_output = tk.Entry(win, textvariable= generated_password, font=('Arial',10))
password_output.place(x=30, y=280)



# Strength check subtitle
strength_check_title = tk.Label(win, text=('Strength Test'), font=('Arial',20))
strength_check_title.place(x=30, y=310)

# Strength check input box
strength_check_input = tk.Entry(win, textvariable= password, font=('Arial',10))
strength_check_input.place(x=30, y=345)

# create a function for the strength check button to run the find score function in the strength_check file 
def test_strength():
    password = strength_check_input.get()
    score_result = strength_check.find_score(password)
    # get the score and assign a rating to the value 
    if score_result == 0:
        final_score = 'invalid'
    if score_result == 1:
        final_score = 'very weak'
    if score_result == 2:
        final_score = 'weak'
    if score_result == 3:
        final_score = 'not bad'
    if score_result == 4:
        final_score = 'strong'
    if score_result == 5:
        final_score = 'very strong'
    # output the rating in an info message box
    tk.messagebox.showinfo('password score', final_score)

# Strength check button
strength_check_button = tk.Button(win, text=('Test Strength'), command= test_strength)
strength_check_button.place(x=30, y=370)

# Decryption subtitle
decryption_title = tk.Label(win, text=('Decrypt Password'), font=('Arial bold', 20))
decryption_title.place(x=380, y=140)

# Enter encrypted password
enter_encrypted_title= tk.Label(win, text=('Enter encrypted password:'), font=('Arial', 10))
enter_encrypted_title.place(x=380, y=180)


# Decryption entry box
decryption_input = tk.Entry(win, textvariable= encrypted_password, font=('Arial', 10))
decryption_input.place(x=385, y=210)

# Decrypted output box
decryption_output = tk.Entry(win, textvariable= decrypted_password, font=('Arial', 10))
decryption_output.place(x=385, y=280)

# make a decrypt function that can be run as a command on the button 
def decrypt():
    # get the input from the decryption input box 
    encrypted_password = decryption_input.get()
    # run the decrypt function using the text from the box 
    decrypted_password = encryption_and_decryption.decrypt(encrypted_password)
    # insert the decrypted text into the output box 
    decryption_output.insert(0, decrypted_password)

# Decryption Button
decryption_button = tk.Button(win, text=('Decrypt'), font=('Arial', 10), command= decrypt)
decryption_button.place(x=385, y=240)

# encrypt and save
save_title = tk.Label(win, text=('Encrypt and Save'), font=('Arial bold', 20))
save_title.place(x=700, y=140)

# website name
website_title = tk.Label(win, text=('Website Name:'), font=('Arial', 10))
website_title.place(x=700, y=170)

# website entry
website_entry = tk.Entry(win, textvariable= website_name, font=('Arial', 10))
website_entry.place(x=700, y=190)

# account name title 
account_name_title = tk.Label(win, text=('Account Name:'), font=('Arial', 10))
account_name_title.place(x=700, y=210)

# account name entry box
account_name_entry = tk.Entry(win, textvariable= account_name, font=('Arial', 10))
account_name_entry.place(x=700, y=230)

# Password title
password_title = tk.Label(win, text=('Password:'), font=('Arial', 10))
password_title.place(x=700, y=250)

# Password entry box
password_entry = tk.Entry(win, textvariable= new_password, font=('Arial', 10), show='*')
# the "show='*'" part of the line above displays the text in the box as *s 
password_entry.place(x=700, y=270)

def save():
    
    website_name = website_entry.get()
    account_name = account_name_entry.get()
    new_password = password_entry.get()
    encrypted_new_password = encryption_and_decryption.encrypt(new_password)
    print(encrypted_new_password)
    save_to_file.save_details(website_name, account_name, encrypted_new_password)

# Save Button that runs the save function
save_button = tk.Button(win, text=('Save'), font=('Arial', 10), command= save)
save_button.place(x=700, y=300)

def view_saved():
    master_password_storage.view_passwords()

# view saved passwords button
view_saved = tk.Button(win, text=('View Saved'), font=('Arial', 10), command= view_saved)
view_saved.place(x=700, y=330)


    

win.mainloop()    
    

