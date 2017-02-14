import pprint
message = "Rain drops drop tops smokin on cookie in the hotbox "
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
