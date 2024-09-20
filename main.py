def main():
    file_contents = get_file_contents("books/frankenstein.txt")
    #print(file_contents)
    word_count = num_words(file_contents)
    #print(num_chars(file_contents))
    char_list = convert_dict_to_list(num_chars(file_contents))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for d in char_list:
        ch = d["ch"]
        cnt = d["num"]
        print(f"The '{ch}' character was found {cnt} times")
    print("--- End report ---")

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

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    list_of_dicts = []
    for key in dict:
        if key.isalpha():
            list_of_dicts.append({"ch": key, "num": dict[key]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

main()