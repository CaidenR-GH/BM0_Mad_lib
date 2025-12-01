import random
import time

print("Enter a verb (action): ")
verb = input()

print("Enter a noun (person, place, thing): ")
noun = input()

print("Enter an adjective (descriptor): ")
adjective = input()

random_integer = random.randint(1, 3)

if random_integer == 1:
	print(f"Today I wanted to {verb}, so I did.")
	time.sleep(1)
	print(f"I wanted to see {noun}, so I went to see them.")
	time.sleep(1)
	print(f"On my way to see {noun}, I saw a {adjective} man walking down the street.")
	time.sleep(1)
	print("The man waved to me, so I waved back.")
elif random_integer == 2:
	print(f"{noun} died today.")
	time.sleep(1)
	print(f"I thought I would feel sad, but instead, I felt {adjective}.")
	time.sleep(1)
	print("It was an odd feeling.")
	time.sleep(1)
	print(f"It made me want to {verb}, so I did.")
else:
	print(f"Yesterday I went to {verb} on the beach.")
	time.sleep(1)
	print(f"The sun was very hot, so I felt {adjective}.")
	time.sleep(1)
	print("I grew tired, so I decided to lie down.")
	time.sleep(1)
	print(f"While lying down, I hallucinated {noun}.")