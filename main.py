def main():
    file_contents = get_file_contents("books/frankenstein.txt")
    #print(file_contents)
    #print(num_words(file_contents))
    print(num_chars(file_contents))

def get_file_contents(filename):
    with open(filename) as f:
        return f.read()

def num_words(file_contents):
    words = file_contents.split()
    return len(words)

def num_chars(file_contents):
    char_count = {}
    for i in range(len(file_contents)):
        char = file_contents[i].lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()