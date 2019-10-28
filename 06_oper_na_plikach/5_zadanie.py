filename = "pan_tadeusz.txt"

with open(filename) as f:
    content = f.read()

content = content.split()
print(content)

longest_word = ""

for word in content:
    if len(word) > len(longest_word):
        longest_word = word

print("Najdłuższe słowo to: ", longest_word)