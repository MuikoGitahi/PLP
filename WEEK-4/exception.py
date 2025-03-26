#Task Requirements:
'''
Create a file called input.txt and write at least five lines of text into it.
Write a Python script to:
Read the contents of input.txt.
Count the number of words in the file.
Convert all text to uppercase.
Write the processed text and the word count to a new file called output.txt.
Print a success message once the new file is created.
'''

with open("input.txt", "w") as file:
    file.write("Hi, my name is Michael.\n")
    file.write("Welcome to the exception handling tutorial\n")
    file.write("I'll be showing you how to create a file,\n")
    file.write("How to handle errors gracefully.\n")
    file.write("Stay tuned!\n")



#Read the content of the input.txt file 
with open("input.txt", "r") as inFile:
    content =inFile.read()



#count the number of words in the file
count = len(content.split())

#convert all text to uppercase
convert = content.upper()

#Write the processed text and the word count to a new file called output.txt.
with open("output.txt", "w") as outFile:
    outFile.write(convert + "\n")
    outFile.write(f"Wordcount: {count} \n")


#Print a success message once the new file is created.
print("New file successfully created!")


