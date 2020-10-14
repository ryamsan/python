def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file, {filename}, does not exist.")
        pass
        '''pass Statements can be used to fail silently'''
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file, {filename}, has about {num_words} words.")


# filename = 'alice.txt'
# count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)