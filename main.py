def main():
    ABC = 'abcdefghijklmnopqrstuvwxyz'
    BOOK_PATH = "books/frankenstein.txt"

    abecedary_dict = create_abecedary_dict(ABC)
    words =  get_words_list(BOOK_PATH)
    abecedary_dict = populate_with_count(words, abecedary_dict)
    sorted_list = create_sorted_list_of_dict(abecedary_dict)

    # Print Report
    print(f"--- Begin report of {BOOK_PATH} --- \n{len(words)} words found in the document\n")
    for item in sorted_list:
        print(f"The letter '{item['letter']}' was found {item['times']} times.")
    print("--- End report ---")

# Return words list
def get_words_list(path):
    with open(path) as f:
        content = f.read()
        words = content.split()
    return words

# Populate Dictionary with letters count as values
def populate_with_count(words, abecedary_dict):
    for word in words:
        lowercase = word.lower()
        lowercase_list = list(lowercase) # List of word's letters
        for letter in abecedary_dict:
            times = lowercase_list.count(letter)
            abecedary_dict[letter] += times
    return abecedary_dict

# Creates a dictionary of the ABC letters as Keys and '0' as default value
def create_abecedary_dict(abecedary):
    dict = {}
    abc_list = list(abecedary) # abc_list -> ['a', 'b' , 'c' ....]
    for letter in abc_list:
        dict[letter] = 0  # dict -> {'a': 0 , 'b': 0, 'c': 0 ....}
    return dict


# Create a List of dictionaries with 'letter' and 'times' as keys
def create_sorted_list_of_dict(abecedary):
    # Sort by key 'times'
    def sort_on(e):
        return e['times']

    dict_to_sort_list = []
    for letter in abecedary:
        dict_to_sort_list.append(
            {
                'letter': letter,
                'times': abecedary[letter]
            }
        )
    dict_to_sort_list.sort(reverse=True, key=sort_on)
    return dict_to_sort_list
main()
