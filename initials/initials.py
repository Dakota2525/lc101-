def get_initials(fullname):
   
    initials_list = fullname.split()
    initials = ""
    for name in initials_list:
        initials = initials + name[0].upper() 
    return initials

def main():
    fullname = input("What is your full name?")
    print(get_initials(fullname))

if __name__ == '__main__':
    main()

