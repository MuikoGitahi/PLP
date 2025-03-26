# Ask the user for the filename
filename = input("Enter the filename to read: ")

try:
    # Attempt to open and read the file
    with open(filename, "r") as infile:
        content = infile.read()
    
    # Modify the content (convert to uppercase)
    modified_content = content.upper()
    
    # Define the output file name
    output_filename = "modified_" + filename
    
    # Write the modified content to a new file
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)
    
    print(f"File processed successfully! Modified version saved as {output_filename}")

except FileNotFoundError:
    print(" Error: The file was not found. Please check the filename and try again.")
except PermissionError:
    print("Error: Permission denied. You don’t have access to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
