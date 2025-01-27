#Write a Python script that takes multiple text les as input and concatenates their
#contents into a single text le.

text_file_1 = open('ex3_text_N1.txt')
text1 = text_file_1.read()
text_file_2 = open('ex3_text_N2.txt')
text2 = text_file_2.read()
text_file_3 = open('ex3_text_N3.txt')
text3 = text_file_3.read()

with open('ex3_final_result.txt','w') as final_result:
    final_result.write(f"{text1} {text2} {text3}")

text_file_1.close()
text_file_2.close()
text_file_3.close()
