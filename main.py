print(" THE PYRAMID PATTERN ")
n= int(input( "please enter the number of rows in the pyramid"))
for i in range(n):
    for j in range (i+1):
        print("* ",end="")
    print("")
