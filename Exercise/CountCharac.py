from pprint import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message :
    if character == " ":
        continue
    else:
        count.setdefault(character, 0)
        count[character] += 1

pprint (count)
