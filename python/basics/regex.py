import re

print('\n01. Replacing special characters')
sentence = "I got to meet Elon Musk !!!! And also got to visit @SpaceX. It was F**king Awesome"
print('Original  : ' + sentence)
special_characters_replaces = re.sub('[^a-zA-Z0-9 \n\.]', '', sentence)
print('Formatted : ' + special_characters_replaces)

# Note : removes numbers though
print('\n02. Camel Case to normal string')
variable_name = 'MyNameIsEshanMEWANTHAHerath'
print('Original  : ' + variable_name)
extracted_words = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', variable_name)
joined = ' '.join(extracted_words)
print('Formatted : ' + joined)