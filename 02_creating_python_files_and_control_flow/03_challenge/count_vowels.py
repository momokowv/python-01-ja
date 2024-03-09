# ここにコードを書いてください

number_vowels = 0
word = input ("Enter a string:")
for x in word:
    if( x == "a" or x == "i" or x == "u" or x == "e" or x == "o"):
        number_vowels = number_vowels + 1

print("Number of vowels:" + str(number_vowels))