def reverse_words(string):
    words=string.split(" ")
    rev_words=words[::-1]
    reverse_string=" ".join(rev_words)
    return reverse_string

string="blue is sky the"
print("Reverse of word is :",reverse_words(string))