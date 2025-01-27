#Implement a Python program that reads a text file (input.txt), prompts the user
#for a word to find, and another word to replace it with. Replace all occurrences of
#the first word with the second word and save the modified text to a new file
#(output.txt).
word_of_interest = input('write the word you are looking for ')
replacement = input("write the word you want to replace ")
with open('ex2_input.txt') as initial_file:
    text = initial_file.read()
    result = text.replace(word_of_interest, replacement)
with open('ex2_output.txt', 'w') as final_result:
    final_result.write(result)


