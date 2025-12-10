word = input("enter a word: ")
char = input("entera character to find theoccurrence of: ")

count=0
i=0
while i < len(word):
    if word[i] == char:
        count +=1
    i +=1

print("the total occurrences: ", count)