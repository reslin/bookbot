def main():
    file_contents = get_file_contents("books/frankenstein.txt")
    print(file_contents)
    print(num_words(file_contents))

def get_file_contents(filename):
    with open(filename) as f:
        return f.read()

def num_words(file_contents):
    words = file_contents.split()
    return len(words)

main()