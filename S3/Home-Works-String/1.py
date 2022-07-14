# آریا توانا، تکلیف مبحث رشته، سوال 1

text = input("Please, Enter your text: ")

sentences = text.count(".") + text.count("?") + \
    text.count("!") + text.count(";")
words = text.count(" ") + 1
characters = len(text)
letters = characters - (text.count(".") + text.count("?") + text.count(
    "!") + text.count(";") + text.count(",") + text.count(":") + text.count(" "))

print("Number of sentences", sentences, sep=" : ")
print("Number of words", words, sep=" : ")
print("Number of characters", characters, sep=" : ")
print("Number of letters", letters, sep=" : ")
