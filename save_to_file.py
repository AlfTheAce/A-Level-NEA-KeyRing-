import csv
#take all the variables from the input boxes in the main file and add them to the function
def save_details(website_name, account_name, encrypted_new_password):
    save_list = []
    save_list.append(website_name)
    save_list.append(account_name)
    save_list.append(encrypted_new_password)
    # open the accounts_file and use utf-8 encoding 
    with open('accounts_file.csv', mode='a', encoding='utf-8') as accounts_file:
        # set the rules for writing each row and seperate each item with a comma
        accounts_writer = csv.writer(accounts_file, delimiter=',')
        # add the list to the current row then go down to the next row 
        accounts_writer.writerow(save_list)
    save_list.clear()


    
    
