"""This code file opens files and prints their content"""
def read_file(filename:str):
    # TODO Open file and read contents then
    file_content = []
    file = open(filename, "r+")
    for line in file.readlines():
        file_content.append(line)
    return file_content

def print_file_contnet(content):
    """Prints the file content"""
    # TODO print content
    print(content)

def main():
    read_file 
    print_file_contnet

challenge = read_file("challenge.txt")

print(challenge)