s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
first_nums = (1, 5, 6, 7, 8, 9, 15, 16, 19)

output = []
for i, word in enumerate(s.split(" "), 1):
    if i in first_nums:
        output.append( word[:1] )
    else:
        output.append( word[:2] )

print(output)
