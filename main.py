import program

def main():
    MenuList='''
Welcome to QuizFusion

What do you want to play?
1. Addition Game
2. Subtraction Game
3. Multiplication Game
4. Chinese Game
5. Exit
'''
    while True:
        print(MenuList)
        choice = input("Enter your choice: ")

        if choice == "1":
            program.addition_game()
        elif choice == "2":
            program.substraction()
        elif choice == "3":  
            program.multiplication1()
        elif choice == "4":
            program.chinese_game()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

main()