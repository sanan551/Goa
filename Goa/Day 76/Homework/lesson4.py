def longest_word(sentence):
    words = sentence.split() 
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("This is an awesome test")) 

 # split() ყოფს წინადადებას სიტყვების სიაში