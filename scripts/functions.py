

class Bot:
    def __init__(self):
        self.greetings = ["Good Morning", "Good Day", "Hi!", "Hello",
                          "Good Evening", "Good Night!"]

    def Greet(self):
        print("Choose a proper greeting by selecting a number from 1 to 6:")
        i = 0
        for greet in self.greetings:
            print(i + 1)
            i += 1

        s = int(input())
        if (s == 1):
            print(self.greetings[0])
        elif (s == 2):
            print(self.greetings[1])
        elif (s == 3):
            print(self.greetings[2])
        elif (s == 4):
            print(self.greetings[3])
        elif (s == 5):
            print(self.greetings[4])
        else:
            print(self.greetings[5])
