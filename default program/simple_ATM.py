import random

r1 = random.randint(0, 1000)


def getdate():
    import datetime
    return datetime.datetime.now()


user = int(r1)

while True:
    print("What can you do with our ATM??")
    l1 = ["savings", "withdraw", "deposit", "check history"]
    for i in l1:
        print(i)
    userin = input("Your Choice ==> ")
    if userin.lower() == 's' or userin.title() == "Savings" or userin == "1":
        print("You have Rs.", user, "in your account")
        f = open("user.txt", "a")
        f.write(str(getdate()) + " : " + "You checked your Saving" + "\n")
        f.close()

    elif userin.lower() == 'w' or userin.title() == "Withdraw" or userin == "2":
        withdraw = int(input("How much money you want to withdraw : "))
        user = user - withdraw
        if withdraw > user:
            print("You don't have sufficient balance")
        print("Now ,you have Rs.", user, "in your account")
        f = open("user.txt", "a")
        f.write(str(getdate()) + " : " + "You withdrawed Rs." + str(withdraw) + " from your account" + "\n")
        f.close()


    elif userin.lower() == 'd' or userin.title() == "Deposit" or userin == "3":
        deposit = int(input("How much money you want to deposit : "))
        user = user + deposit
        print("Now ,you have Rs.", user, "in your account")
        f = open("user.txt", "a")
        f.write(str(getdate()) + " : " + "You deposited Rs." + str(deposit) + " to your account" + "\n")
        f.close()

    elif userin.lower() == 'c' or userin.title() == "Check History" or userin == "4":
        f = open("user.txt")
        a2 = f.read()
        print(a2)
        f.close()

    elif userin.lower() == "quit" or userin.lower() == "exit" or userin.lower() == "no":
        break
    print("Anything Else?? (type 'quit' for exit)")

print("Thanks for choosing our bank")
