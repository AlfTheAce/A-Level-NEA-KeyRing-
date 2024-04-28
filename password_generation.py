import random
# store all of the lists for the character types 
lower_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['!','£','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']',':',';','@','#','~','<',',','>','.','/','?','¬','`']
characters = ['lower_letter', 'upper_letter', 'number', 'symbol']
character_list = []
pswd_list = []

def main():
    pswd_length = 0 
    pswd_length = int(input("enter the desired length of your password: "))
    password = generate(pswd_length)
    print(password)

# define the generate function 
def generate(pswd_length):
    # generate a list with a random combination of character types
    for x in range(pswd_length):
        x = random.choice(characters)
        character_list.append(x)
    # checks to make sure that at least one of each character type is included in the final password
    for x in range(4):
        # if lower case letter is not in the list delete the first item and add a lower case letter on the end 
        if 'lower_letter' not in character_list:
            del character_list[0]
            character_list.append('lower_letter')
            
        # if upper case letter is not in the list delete the first item and add an upper case letter on the end
        elif 'upper_letter' not in character_list:
            del character_list[0]
            character_list.append('upper_letter')
            
        # if a number is not in the list delete the first item and add a number on the end 
        elif 'number' not in character_list:
            del character_list[0]
            character_list.append('number')
            
        # if a symbol is not in the list delete the first item and add a symbol on the end 
        elif 'symbol' not in character_list:
            del character_list[0]
            character_list.append('symbol')
            
    # for loop that checks each item in the character_list if the item in the lists matches one of the stored
    # character types, take a random item from the specific list and add it to the pswd_list. 
    for x in character_list:
        if x == 'lower_letter':
            a = random.choice(lower_letter)
            pswd_list.append(a)
            
        elif x == 'upper_letter':
            a = random.choice(upper_letter)
            pswd_list.append(a)
            
        elif x == 'number':
            a = random.choice(number)
            pswd_list.append(a)
            
        elif x == 'symbol':
            a = random.choice(symbol)
            pswd_list.append(a)
            
    # join the password list with no spaces to make it into a string 
    complete_pswd = "".join(pswd_list)
    print(complete_pswd)
    character_list.clear()
    pswd_list.clear()
    return complete_pswd





