#sorting and splitting of string
Line = input("Enter the string :")
words = [word.lower() for word in Line.split()]
#sorting the word
words.sort()
print("Sorted words as follows :")
for word in words :
    print(word)
