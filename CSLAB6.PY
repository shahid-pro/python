import sys

def check_python_location():
    print("Python is located at:", sys.executable)

def check_shell_location():
    print("Shell is located at:", sys.exec_prefix)

def check_network_proxy():
    print("Network proxy settings... (placeholder)")

def display_menu():
    print("Menu:")
    print("1. Check the location of Python")
    print("2. Check the location of Shell")
    print("3. Check network proxy")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_python_location()
        elif choice == '2':
            check_shell_location()
        elif choice == '3':
            check_network_proxy()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()