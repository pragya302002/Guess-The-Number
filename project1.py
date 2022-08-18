import random
class numberguessinggame:
    def __init__(self):                                # # define the range
        self.LOWER = 1
        self.HIGHER = 10

    def get_random_number(self):                       # # generate the random number
        return random.randint(self.LOWER, self.HIGHER)

    def start(self):

        random_number = self.get_random_number()
        print(f"Guess the number from the range {self.LOWER}  to {self.HIGHER}")

        chances = 0 
        while True:
            user_number = int((input("ENTER THE GUESSED NUMBER: ")))
            if user_number == random_number:
                print(f"wuhuh you got it in {chances +1} step { 's' if chances >1 else ''}!")
                break
            elif user_number < random_number:
                print(" Your number is less than random number")
            else:
                print("your number is greater than the random number")
            chances +=1

numberguessinggame =  numberguessinggame()
numberguessinggame.start()
