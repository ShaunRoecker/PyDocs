

#  Write a method that compresses a string "aabcccccaaa" to "a2b1c5a3" if the compressed
#  string is shorter than the input string, or else return the input string.


def compress_string(string: str)-> str:
    compressed = []
    counter = 0
    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i] + str(counter))
            counter = 0
        counter += 1

    if counter:
        compressed.append(string[-1] + str(counter))

    return min(string, "".join(compressed), key=len)


print(compress_string("aabcccccaaa"))
