import re
sentence = "I got to meet Elon Musk !!!! And also got to visit @SpaceX. It was F**king Awesome"
special_characters_replaces = re.sub('[^a-zA-Z0-9 \n\.]', '', sentence)
print(special_characters_replaces)