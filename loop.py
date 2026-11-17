
while True:
    print("\n===== Rectangle Project =====")

    # گرفتن ابعاد مستطیل
    width = int(input("Enter rectangle width: "))
    height = int(input("Enter rectangle height: "))

    # بررسی ابعاد با شرط
    if width <= 0 or height <= 0:
        print("Error: Width and height must be positive!")
    else:
        print("\nYour Rectangle:\n")

        # رسم مستطیل با حلقه for
        for i in range(height):
            for j in range(width):
                print("*", end=" ")
            print()

        # گزارش پروژه
        print("\n===== Project Report =====")
        print("Width:", width)
        print("Height:", height)
        print("Area:", width * height)
        print("Perimeter:", 2 * (width + height))

    # تصمیم برای ادامه یا پایان
    choice = input("\nDo you want to continue? (y/n): ")

    if choice.lower() == "n":
        print("Program finished!")
        break
    elif choice.lower() == "y":
        continue
    else:
        print("Invalid choice! Program will continue.")
