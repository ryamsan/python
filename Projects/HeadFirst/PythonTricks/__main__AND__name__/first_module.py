#print(__name__)

def main():
    print('First Module\'s Name: {}'.format(__name__))

#if __name__ == '__main__':
#    main()

if __name__ == '__main__':
    print('Run Directly')
else:
    print('Run from Import')