
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)

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

def get_sorted_list_of_dicts(dict):
    list_of_dicts = []
    for key in dict:
        if key.isalpha():
            list_of_dicts.append({"key": key, "num": dict[key]})

    def sort_on(dict):
        return dict["num"]
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")

    letters_dict = get_chars_dict(text)
    list_of_dicts = get_sorted_list_of_dicts(letters_dict)
    for dict in list_of_dicts:
        key = dict["key"]
        num = dict["num"]
        print(f"The '{key}' character was found {num} times")

    print("--- End report ---")

main()