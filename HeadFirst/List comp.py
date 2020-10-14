#Find all of the numbers from 1-100 that are divisible by 7

results = [num for num in range(1,101) if num%7 ==0]
#print(results)

#Find all of the numbers from 1-100 that have a 3 in them

results = [num for num in range(1,101) if '3' in str(num)]
#print(results)

#Count the number of spaces in a string

teststring = 'Find all of the words in a string that are less than 4 letters'
#print(teststring.count(' '))

#For sake of this

results = [char for char in teststring if char == ' ']
#print(len(results))

#Remove all of the vowels in a string [make a list of the non-vowels]

teststring = 'Find all of the words in a string that are less than 4 letters'
vowels = ['a','e','i','o','u',' ']
results = [i for i in teststring if i.lower() not in vowels]
#print(results)

#Find all of the words in a string that are less than 4 letters
teststring = 'Find all of the words in a string that are less than 4 letters'
results = [word for word in teststring.split(' ') if len(word)<4 and word.isalpha() == 1]
#print(results)


# CHALLENGE!
#Use a dictionary comprehension to count the length of each word in a sentence.
sentence = 'Use a dictionary comprehension to count the length of each word in a sentence'
results = {word:len(word) for word in sentence.split()}
#print(results)

#Use a nested list comprehension to find all of the numbers from 1-100 that
#are divisible by any single digit besides 1 (2-9)
# comprehension testing truth for divisibilty: [True for divisor in range(2,10) if num % divisor == 0]
results = [num for num in range(1,101) if True in [True for divisor in range(2,10) if num % divisor == 0]]
print(results)