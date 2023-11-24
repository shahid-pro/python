#!/bin/bash

# Function to display files in a given path
display_files_in_path() {
  local folder_path=$1
  files=($(ls "$folder_path"))
  echo "Files in the path:"
  for file in "${files[@]}"; do
    echo "$file"
  done
}

# Function to create a shell script
create_shell_script() {
  # Default location for bash shell
  shell_location="/bin/bash"

  # Find the actual location of the bash shell
  if ! command -v bash >/dev/null; then
    shell_location=$(which bash) || {
      echo "Error finding the location of the bash shell"
      exit 1
    }
  fi

  # Create the shell script file
  script_content="#!/bin/bash\n\n# Add your commands here\n"
  script_file="script.sh"

  if [ ! -f "$script_file" ]; then
    echo "$script_content" > "$script_file"
    chmod +x "$script_file"
    echo "Shell script created successfully: $script_file"
  else
    echo "Shell script already exists: $script_file"
  fi
}

# Main function
main() {
  # Get the folder path from the user
  echo "Enter the folder path: "
  read folder_path

  # Display files in the specified path
  display_files_in_path "$folder_path"

  # Get the Python file to run from the user
  echo "Enter the Python file to run: "
  read python_file

  # Run the specified Python file
  if [ -f "$python_file" ]; then
    python "$python_file"
  else
    echo "Error: Python file not found: $python_file"
  fi

  # Create the shell script
  create_shell_script
}

# Call the main function
main
