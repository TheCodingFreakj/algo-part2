def find_longest_words(words):
    max_count = len(words[0])
    longest_words = []
    for i in range(len(words)):
        if (len(words[i]) >= max_count and i != 0):
            max_count = len(words[i])
            if (len(longest_words) != 0 and len(words[i]) > len(longest_words[len(longest_words)-1])):
                longest_words.pop()
            longest_words.append(words[i])     
    print((",".join(longest_words)).replace(',', '\n'))


words = ["dog", "cat", "elephant","mouse", "hippopotamus"]
find_longest_words(words)
