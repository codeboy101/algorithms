from string import ascii_lowercase
import random
import time

letters = [i for i in ascii_lowercase]

def score_string(word, real_word):
	return sum(x == y for x, y in zip(word, real_word))	

def mutate_string(word, real_word):
	if len(word) != len(real_word):
		print('unequal string lengths not allowed')
		return -1

	print('current = {}, target = {}'.format(word, real_word))
	word = list(word)
	real_word = list(real_word)
	counter = 1
	max_generated = word
	max_score = score_string(max_generated, real_word)
	done = False
	fixed_letters = []
	while not done:
		for x, y in zip(word, real_word):
			if x == y and fixed_letters.count(x) < real_word.count(x):
				fixed_letters.append(x)
			if x != y:
				index = word.index(x)
				a = random.choice(letters)
				temp_word = word
				temp_word[index] = a
				if score_string(temp_word, real_word) > max_score:
					word[index] = a

		score = score_string(word, real_word)
		if score == len(real_word):
			done = True
		elif score > max_score:
			max_score = score
			max_generated = word

		print('at iteration {}, best match = {}'.format(counter, ''.join(i for i in max_generated)))
		counter += 1	

	return word, counter


target = input('target string: ')
print('target string length = {}'.format(len(target)))
start = input("start string: ")
if start == '':
	print('starting with a random string')
	start = ''.join([random.choice(letters) for i in range(len(target))])
result, counter = mutate_string(start, target)
print('string found ! -> {} , counter = {}'.format(''.join(i for i in result), counter))

