def file_read_write():
    import os
    
    # Prompt the user for the filename to read
    filename = input("hello world")
    
    try:
        # Attempt to open the file for reading
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (to uppercase)
        modified_content = content.upper()
        
        # Define the new filename for the modified content
        new_filename = "modified_{}".format(filename)
        
        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print("File '{}' has been modified and saved as '{}'.".format(filename, new_filename))
    
    except FileNotFoundError:
        print("Error: The file '{}' does not exist. Please check the name and try again.".format(filename))
    except PermissionError:
        print("Error: Permission denied for file '{}'.".format(filename))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))

# Run the function
file_read_write()
