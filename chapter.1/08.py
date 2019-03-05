def _cipher(ch):
    if ch.islower():
        scode = 219 - ord(ch)
        return chr(scode)
    else:
        return ch

def cipher(s):
    output = ""
    for ch in s:
        print(ch, _cipher(ch))
        output += _cipher(ch)

print(cipher("Kosuke"))
