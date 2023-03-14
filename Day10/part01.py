lines = "1321131112"
#lines = "211"
result = ""

def look_and_say(sequence):
    result = ""
    i = 0
    while i < len(sequence):
        print("i:",i)
        count = 1
        while i < len(sequence) - 1 and sequence[i] == sequence[i+1]:
            count += 1
            print("count1:",count)
            i += 1
        result += str(count) + sequence[i]
        print("count2:", count)
        i += 1
    return result

for i in range(40):
    lines = look_and_say(lines)

print(len(lines))
