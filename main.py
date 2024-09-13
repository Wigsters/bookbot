def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    char_dict = get_character_count(text)
    #print(char_dict)
    bookreport(num_words, char_dict)

def get_book_text(path):
        with open(path) as f:
            return f.read()

def get_num_words(text):
        words = text.split()
        return len(words)

def get_character_count(text):
    chardict = {}
    lowercase_text = text.lower()
    for character in lowercase_text:
        if character in chardict.keys():
            chardict[character] += 1
        else:
            chardict[character] = 1
    return chardict

def bookreport(num_words, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    char_dict_list = []
    for key in char_dict:
        if key.isalpha():
            char_dict_list.append({"char": key, "num": char_dict[key]})
    char_dict_list.sort(reverse=True, key=sort_on)
    print()
    for dict in char_dict_list:
        char = dict["char"]
        num = dict["num"]
        print(f"The {char} character was found {num} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]
main()