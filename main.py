def main():
    book_index = "./books/frankenstein.txt" 
    with open(book_index) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        #print(file_contents)
        print(f"--- Begin report of {book_index} ---")
        print(f"This document has {word_count} words")
        for char in char_count:
            print(f"The '{char}' character was found {char_count[char]} times")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_characters(file_contents):
    character_count={}
    lowered_characters = file_contents.lower()
    alphabet =["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for char in lowered_characters:
        if char in alphabet:
            if char not in character_count:
                character_count[char] = 1
            else:
                character_count[char] += 1
    return character_count

if __name__ == "__main__":
    main()

