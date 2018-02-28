birthday = {"lucy": "Dec 12", "lili": "Nov 12", "lilei": "Feb 06"}
while True:
    print("Please enter your name:(or enter nothing to stop)")
    name = input()
    if name == " ":
        break
    if name in birthday:
        print(birthday[name] +" is the birthday of " + name)
    else:
        print("I donnot have the birthday information for " + name)
        print("What is you birthday?")
        bday = input()
        birthday[name] = bday
        print("birthday database is updated.")
    # print(birthday)
