class Analyzer : 
    def __init__(self, pwd):
        self.pwd = pwd 
        self.score = 0 
        self.Uppercase = False
        self.Lowercase = False
        self.Number = False


    def letter_counter (self):
        print("lenght =", len(self.pwd))

        if len(self.pwd) >= 8 and len(self.pwd) < 12 :
            self.score += 1
            
        elif len(self.pwd) >= 12 :
            self.score += 2

    def character_analyzer (self) :
        for character in self.pwd : 
            if character.isupper()  :
                self.score += 1
                self.Uppercase = True

            elif character.islower()  :
                self.score += 1
                self.Lowercase = True

            elif character.isdigit()  :
                self.Number = True
                self.score += 1
        


    def grading_tool (self) :
        if self.Uppercase  :
            print("Uppercase = YES")
        else : 
            print("Uppercase = No")

        if self.Lowercase :
            print("Lowercase = YES")
        else:
             print("Lowercase = No")

        if self.Number  :
            print("Number = Yes")
        else :
            print("Number = No")

        if self.score <= 2 :
            print("Stength = Weak")
        elif self.score <= 4 and self.score > 2 :
            print("Stength = Medium")
        elif self.score >= 5 :
            print("Strength = Strong")


# ------------------------- MAIn programme ----------------------------------------------------

password = input("Enter password : ")
analyse = Analyzer(password)
analyse.letter_counter()
analyse.character_analyzer()
analyse.grading_tool()