#!/bin/bash

check_python_location() {
    echo "Python is located at:" $(which python)
}

check_shell_location() {
    echo "Shell is located at:" $SHELL
}

check_network_proxy() {
    echo "Network proxy settings... (placeholder)"
}

display_menu() {
    echo "Menu:"
    echo "1. Check the location of Python"
    echo "2. Check the location of Shell"
    echo "3. Check network proxy"
    echo "4. Exit"
}

while true; do
    display_menu
    read -p "Enter your choice (1-4): " choice

    if [ "$choice" == "1" ]; then
        check_python_location
    elif [ "$choice" == "2" ]; then
        check_shell_location
    elif [ "$choice" == "3" ]; then
        check_network_proxy
    elif [ "$choice" == "4" ]; then
        echo "Exiting the program..."
        break
    else
        echo "Invalid choice. Please try again."
    fi
done