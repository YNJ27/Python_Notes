#Else block is only executed if the try block works without throwing an error.

#This can be useful when you want to separate the code that should run if everything
#goes well from the code that handles exceptions

#Without the else block, you might have to include the success case handling in the 
#try block itself, which can make the code harder to read and maintain.

#For now , you can consider that it is used only to make the program easy to read , nothing else

#Ex with else
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An IOError occurred while reading the file.")
    else:
        print("File content successfully read:")
        print(content)
        file.close()
    finally:
        print("Finished file operation.")

# Example usage
read_file("example.txt")



#Ex without else
def read_file_no_else(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print("File content successfully read:")
        print(content)
        file.close()
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An IOError occurred while reading the file.")
    finally:
        print("Finished file operation.")

# Example usage
read_file_no_else("example.txt")

