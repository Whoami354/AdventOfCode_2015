lines = open("input", "r", encoding='utf-8').read().strip()

print(lines.count('(') - lines.count(')'))