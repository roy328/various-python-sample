input_string = """dasfasdf

fasdfas
() asdfasdfdsf dasf asd fds.s dfads fasd"""

# Find the index of the substring "()" and slice the string from there
substring = "() "
start_index = input_string.find(substring)

if start_index != -1:
    # Get the substring starting from the end of "() "
    result = input_string[start_index + len(substring):].strip()
    print(result)
else:
    print("Substring not found")