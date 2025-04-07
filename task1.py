
def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for i, line in enumerate(file, 1):
                print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    read_file_content("sample.txt")
