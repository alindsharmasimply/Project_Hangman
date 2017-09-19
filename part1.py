import random

fp = open("words.txt","r")

i= random.randrange(0,10)

hang = 7

for x in range(i):
	word = fp.readline()

fp.close()

word = list(word)
w = word[:-1]

print w

for i in range(0,len(w)):
	print "_ ",
while hang > 0:
	I = raw_input("Enter an alphabet ")
	if I in w:
		for t in w:
			if t == I:
				print I," ",
			else:
				print "_ ",
	else:
		hang = hang - 1