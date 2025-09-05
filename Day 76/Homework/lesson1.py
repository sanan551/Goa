def count_vowels(word):
    word = word.lower()
    count = 0
    for char in word:
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("Hello"))