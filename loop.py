while True:

    print("1. Add numbers")
    print("2. Display numbers")
    print("3. Exit")

    choice = int(input("Choose: "))

    if choice == 1:

        a = int(input("First number: "))
        b = int(input("Second number: "))

        print("Sum:", a + b)

    elif choice == 2:

        n = int(input("Enter a number: "))

        for i in range(1, n + 1):
            print(i)

    elif choice == 3:

        print("Program finished")
        break

    else:
        print("Invalid choice")