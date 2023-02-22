def myFun(*argv):
    for arg in argv:
        print("argument is: ", arg)



myFun("Hello", "Welcome", "to", "GeeksforGeeks")


def my_function(**kids):
    print("His last name is " + kids["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

