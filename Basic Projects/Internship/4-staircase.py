def staircase():
    n = input("Enter the number of steps: ")
    while n.isnumeric == False:
        n = input("Invalid input. Enter the number of steps: ")

    for i in range(1, int(n)):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
staircase()
