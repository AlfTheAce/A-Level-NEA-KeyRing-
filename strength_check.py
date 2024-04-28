# Strength checker

# defining the character types and settin the variables to 0
lower_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['!','£','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']',':',';','@','#','~','<',',','>','.','/','?','¬','`']
characters = ['lower_letter', 'upper_letter', 'number', 'symbol']
strength_list = []
score = 0
length = 0 

def assign_rating():
    # input the password 
    # run the function to find the score  
    score = find_score(password)
    # assign a rating to each score
    # if the score is 0, nothing has been entered, therefore it is invalid 
    if score == 0:
        print('invalid')
    if score == 1:
        print('very weak')
    if score == 2:
        print('weak')
    if score == 3:
        print('not bad')
    if score == 4:
        print('strong')
    if score == 5:
        print('very strong')

def find_score(password):
    score = 0
    length = 0 
    # change the password into a list 
    pswd_list = list(password)

    # make a new list called strength list and add the all the character types
    # for each character in the password list
    for x in pswd_list:
        if x in lower_letter:
            strength_list.append("lower_letter")
        elif x in upper_letter:
            strength_list.append("upper_letter")
        elif x in number:
            strength_list.append("number")
        elif x in symbol:
            strength_list.append("symbol")

    # check the list to see if the specific charcter type is in it
    # if it is add one to the score 
    if "lower_letter" in strength_list:
        score = score + 1
    if 'upper_letter' in strength_list:
        score = score + 1
    if 'number' in strength_list:
        score = score + 1
    if 'symbol' in strength_list:
        score = score + 1

    # add one to the score if the length is 12 characters or more 
    for x in strength_list:
        length = length+1
    if length > 11:
        score = score + 1
    strength_list.clear()
    return score

# run the main function 


   


