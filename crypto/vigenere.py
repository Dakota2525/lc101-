
from helpers import * 


def get_rot(key, index_of_key):
   letter = key[index_of_key]
   shift = alphabet_position(letter)
   return shift


def encrypt(text, key):
    result = ""
    index_of_key = 0
    for character in text: 
        if character.isalpha():
            rot = get_rot(key, index_of_key) 
            new_character = rotate_character(character, rot) 
            result += new_character 
            index_of_key += 1
            if (index_of_key > len(key) - 1):
                index_of_key = 0 
                
        else: 
            result += character
    return result 
        
def main():
    mess = input("Enter message to encrypt:")
    key = (input("Enter the key word:"))
    print(encrypt(mess, key))

if __name__=="__main__":
    main() 
  

            




    