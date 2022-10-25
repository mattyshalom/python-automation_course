# To return a given word in double with the lenght

def double_word(word):
    return(word * 2) + str(len(word * 2))

print(double_word("hello")) # will return hellohello10
print(double_word("abc"))   # will return abcabc6
print(double_word(""))  # will return zero
