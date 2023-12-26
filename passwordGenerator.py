#Will generate a password that contains
#2 uppercase letters
#2 lowercase letters
#2 digits from 0 to 9
#2 punctuation signs

import random

validInput = False

#COntinually ask the length of the password until a valid value is given
while(validInput == False): 
    #Ask how long the passowrd should be
    totalLength = int(input("Enter the length of the password: "))

    #Check if user inputted 0
    if totalLength  <= 0:
        print("Invalid Input, try again.")
        
    else:
        validInput = True

#Figure out how many characters are going to be lowercase, uppercase, special symbols etc
#Priority Order: lowercase, uppercase, numbers, symbols

#Set a max amount for each character type to ensure the password is randomized
maxLowerCase = totalLength // 2

maxUpperCase = totalLength // 2

numOfLowerCaseLetters = random.randint(0, maxLowerCase)
print("Number of lowercase: " + str(numOfLowerCaseLetters))

totalLength = totalLength - numOfLowerCaseLetters
print(totalLength)

numOfUpperCase = random.randint(0, maxUpperCase)
print("Number of uppercase: " + str(numOfUpperCase))

totalLength = totalLength - numOfUpperCase
print(totalLength)

numOfNumbers = totalLength - random.randint(0, totalLength)
print("Number of numerical values: " + str(numOfNumbers))

totalLength = totalLength - numOfNumbers
print(totalLength)

numOfSymbols = totalLength 
print("Number of special symbols: " + str(numOfSymbols))

totalLength = totalLength - numOfSymbols
print(totalLength)

#All the possible characters that can make up the password
allUpperCase = ("A", "B", "C", "D", "E", "F", "G", "H" , "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
allLowerCase = ("a", "b", "c", "d", "e", "f", "g", "h" , "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
allDigits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
allPunctuation = ('!', '?', '#', "@")

#Initalize the password
password = "";

#Generate the lowercase letters
for x in range(numOfLowerCaseLetters):
    lowerCase = random.choice(allLowerCase)
    password = password + lowerCase #Adding the new letter to the password

#Generate the uppercase letters
for x in range(numOfUpperCase):
    upperCase = random.choice(allUpperCase)
    password = password + upperCase #Adding the new letter to the password

#Generate the numerical values
for x in range(numOfNumbers):
    numbers = random.choice(allDigits)
    password = password + str(numbers); #Adding the new numbers to the password

#Generate the special symbol values
for x in range(numOfSymbols):
    specialSymbols = random.choice(allPunctuation)
    password = password + specialSymbols

#Outputing the password    
passwordList = list(password) #convert string to a list
random.shuffle(passwordList) #randomize the order of the characters
password = ''.join(passwordList)

print("Here is your unique password: " + password)
