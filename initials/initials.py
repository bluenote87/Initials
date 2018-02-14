import string

def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    inits = fullname[0].upper()
    temp = ""
    counter = 0
    for char in fullname:
        if char.isspace():
            temp = fullname[counter + 1]
            inits = inits + temp.upper()
        counter = counter + 1

    return inits


def main():
    fullname = ""
    while fullname != "exit":
        fullname = input("What is your full name? (type 'exit' to quit)")
        if fullname != "exit":
            result = get_initials(fullname)
            print("The initials of '" + fullname + "' are " + result)
    print("Bye!")

if __name__ == "__main__":
    main()