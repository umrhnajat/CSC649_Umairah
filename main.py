# CSC649: My first python experiment

sentence = input("Enter a sentences: ")

if sentence.strip() == "":
    print("You did not enter a sentence.")
else:
    word_count = len(sentence.split())
    character_count = len(sentence)

    print("Word count:", word_count)
    print("Character count (including spaces):", character_count)
    print("Thank you very much.")