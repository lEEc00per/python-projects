with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_word = i

    if char == target_end and start_word != -1:
        word = story[start_word + 1 : i]
        words.add(word)
        start_word = -1

answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story) 
# prints the out pyt according to the words you have entered