from helpers import *

def encrypt(text, rot):
    result = ""
    for letter in text:
        new_character = rotate_character(letter, rot) 
        result += new_character
    return result

def main():
    mess = input("Enter the message to encrypt:")
    rotation = int(input("Enter the rotation:"))
    print(encrypt(mess, rotation))

if __name__=="__main__":
    main() 
   
             