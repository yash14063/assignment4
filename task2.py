
def write_to_file(filename):
    
    initial_content = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(initial_content + "\n")
    print("Data successfully written to output.txt.")
    
    
    append_content = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(append_content + "\n")
    print("Data successfully appended.")
    
    
    print("\nFinal content of output.txt:")
    with open(filename, 'r') as file:
        print(file.read())


if __name__ == "__main__":
    write_to_file("output.txt")
