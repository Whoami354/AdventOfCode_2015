lines = input = open("input", "r", encoding='utf-8').read().strip().split("\n")
#lines = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
code_length = 0
encoded_length = 0
for line in lines:
    encoded = line
    print(encoded)
    code_length += len(encoded)
    encoded = encoded.replace("\\", "\\\\")
    encoded = encoded.replace('"', '\\"')
    encoded = '"' + encoded + '"'
    print(encoded)
    encoded_length += len(encoded)


print(encoded_length - code_length)