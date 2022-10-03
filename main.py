from Modules.guessthenumber import Guesser, gameInterface
from Modules.madlibsgenerator import Reader


def main():
   #gameInterface()
    text = Reader('text.txt')
    print(text.file_reader_txt())
    

if __name__ == '__main__':
    main()