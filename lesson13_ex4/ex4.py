#Develop a Python Function that reads a large text le (input.txt) and splits it
#into smaller les, each containing a specied number of lines. Function paramis
#ter the number of lines per le. Generate multiple output les (output1.txt,
#output2.txt, etc.).

def split_file(input_file, lines_count):
    with open(input_file) as initial:
        lines = initial.readlines()

    num_files = (len(lines) + lines_count - 1) // lines_count
    for i in range(num_files):
        output_file = f'output{i + 1}.txt'
        start_line = i * lines_count
        last_line = start_line + lines_count
        with open(output_file, 'w') as outfile:
            for line in lines[start_line:last_line]:
                outfile.write(line)
        print(f"File '{output_file})' created.")


input_file = 'ex4_initial_text.txt'
lines_count = 1
split_file(input_file, lines_count)