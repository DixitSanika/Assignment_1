from collections import OrderedDict

def word():    
    w = int(input("Enter the number of words: "))
    word_count = OrderedDict()

    for i in range(w):
        word = input(f"Enter the word {i + 1}: ")

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print("\nNumber of distinct words:", len(word_count))

    for word, count in word_count.items():
        print(f"{word} {count}")

word()