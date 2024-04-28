
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letters_dict = get_chars_dict(text)
    print(letters_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    letters_dict = {}
    lowered_text = text.lower()
    for ch in lowered_text:
        if ch in letters_dict:
            letters_dict[ch] += 1
        else:
            letters_dict[ch] = 1
    return letters_dict

main()