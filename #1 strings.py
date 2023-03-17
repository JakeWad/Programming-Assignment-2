input_string = "abcdefghijklmnopqrstuvwxyz"
result_string = ""

for i in range(len(input_string)):
    if i % 6 < 3:
        result_string += input_string[i]

print(result_string)
