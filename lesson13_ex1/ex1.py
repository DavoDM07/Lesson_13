#Write a Python script that reads a text file (input.txt) and counts the
#occurrences of each character (including spaces and punctuation). Output the
#character frequency to another text file (output.txt).
result = {}
with open('ex1_input.txt') as initial_file:
    text = initial_file.read()
    for i in text:
        if i not in result:
            result[i] = 1
        elif i in result:
            result[i] += 1
with open('ex1_output.txt', 'w') as final_result:
    for k,v in result.items():
        final_result.write(f'{k}: {v}\n')






