import re

email = 'abc@example.com'

# Match
match_string = re.match(r'[a-z]+@[a-z]+\.[a-z]+', email)
print(match_string)
print(match_string.start())
print(match_string.end())
print(match_string.span())
print(match_string.group())

# Search
emails = 'aaa@example.com bbb@example.com ccc@example.com'
match_list = re.findall(r'[a-z]+@[a-z]+\.[a-z]+', emails)
print(match_list)

# Replace
replace_string = re.sub(r'[a-z]+@', 'ABC@', email)
print(replace_string)

# Split
split_string = re.split(r'@', email)
print(split_string)

# Text Cleaning 
# Get only alphabets and spaces and convert to lower case 
text = "HELLO, WORLD! This is a sample text with numbers [123] and special characters [#@&]."
cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text) # ^: not, a-zA-Z: alphabets, \s: spaces
cleaned_text = cleaned_text.lower()
print(cleaned_text)
