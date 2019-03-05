s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

output = []
for word in s.split(" "):
    output.append( len(word.rstrip("," ".")) )

print(output)
