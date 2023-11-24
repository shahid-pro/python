import os

def display_files_in_path(folder_path):
    files = os.listdir(folder_path)
    print("Files in the path:")
    for file in files:
        print(file)

def create_shell_script():
    shell_location = "/bin/bash"  # Default location for bash shell

    # Find the location of the bash shell
    try:
        shell_location = os.popen("which bash").read().strip()
    except Exception as e:
        print("Error finding the location of the bash shell:", str(e))

    # Create the shell script file
    script_content = f"#!/bin/bash\n\n# Add your commands here\n"
    script_file = "script.sh"

    try:
        with open(script_file, "w") as file:
            file.write(script_content)
        os.chmod(script_file, 0o755)
        print("Shell script created successfully:", script_file)
    except Exception as e:
        print("Error creating the shell script:", str(e))

def main():
    folder_path = input("Enter the folder path: ")
    display_files_in_path(folder_path)

    python_file = input("Enter the Python file to run: ")
    os.system(f"python {python_file}")

    create_shell_script()

if __name__ == '__main__':
    main()