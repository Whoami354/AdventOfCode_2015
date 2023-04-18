import hashlib

input = "bgvyzdsv"
index = 0
result = input + str(index)
md5_output = hashlib.md5(result.encode()).hexdigest()

while not md5_output.startswith("000000"):
    index += 1
    result = input + str(index)
    md5_output = hashlib.md5(result.encode()).hexdigest()

print(index)

