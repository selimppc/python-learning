
# QUESTION 1 : find our most used character and list


from pprint import pprint
sentence = "This is a common interview question."

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

most_used = char_frequency_sorted[0]
print(most_used)
