from random import randint


class Guesser:

    def __init__(self,user_number, n = 10):
        self.user_number = user_number
        self.computer_number = randint((-1)*int(n),n)
        
    def show(self):
        return f"Your number is: {self.user_number} and computer number is: {self.computer_number}"

    def guesser(self):
        if self.computer_number == self.user_number:
            return "USER WIN!"
        else:
            return self.show() + "\nBetter luck next time, buddy..."
        
def gameInterface():
    
    i = 'game'
    while i=='game':
        number = int(input("Please enter your number: "))
        game = Guesser(number)
        print(game.guesser())
        i = input("\nStart again? YES - 'y', NO - 'n': ")
        if i == 'n':
            print("BYE!!!")
            break
        else:
            i = 'game'
        
