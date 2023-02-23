# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    my_list = sentence.split(' ')
    new_sentence = ''
    for i in my_list:
        if my_list.index(i) != 0 and len(my_list) != 1 :
            new_sentence += ' '
            
        if len(i) >= 5:
            new_sentence += i[::-1]
        else:
            new_sentence += i
    return new_sentence

print(spin_words("Welcome"))
print(spin_words("to"))
print(spin_words("CodeWars"))

print(spin_words("Hey fellow warriors"))
print(spin_words("This sentence is a sentence"))
