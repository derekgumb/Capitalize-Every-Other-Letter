string = input("Enter a sentence here: ")
final_string = ""

for idx, char in enumerate(string):
    if (idx+1) % 2 ==0:
        final_string+= char.upper()
    else:
        final_string += char

print(final_string)