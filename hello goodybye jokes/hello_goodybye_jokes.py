def hello():
    print("Welcome to the code")
    print("Hope your doing well")
def goodbye():
    print("Hope you had a good time")
    print("See you in the future")
def joke():
    print("You don't need to have a joke")
    print("Your already the joke :|")
def mat(x,y):
    return x+y, "This is a super secret return"

hello()
do = ""
while do != "leave":
    do = input("\nType joke to see a joke, or leave to leave: ")
    if do == "joke":
        joke()
    elif do == "leave":
        goodbye()

i=0
j=""
math1 = int(input("\nEnter a number"))
math2 = int(input("Enter a number"))
i, j = mat(math1,math2)
print(f"Your answer is {i}")