from Modules.guessthenumber import  gameInterface
from Modules.madlibsgenerator import MadLibsGenerator


def main():
   gameInterface()
   def userInput():
    inp = input("Please enter only 6 words below! (in one sentence) \n")
    return inp.split()
   
   text = MadLibsGenerator('text.txt',user_text=userInput())
   print(text.func())
    

if __name__ == '__main__':
    main()