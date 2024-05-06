from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        with open(r"C:\Users\samsung\New folder (2)\100_days_of_coding\day_20\score.txt") as file:
         data=int(file.read())
        print(data)
        self.highscore=data
        self.penup()
        self.hideturtle()
        self.goto(0,290)
        # self.update_score()
        self.color("white")
        self.increase_score()
    

    def update_score(self):
        self.clear()
        self.write(f"Score-{self.score} || HighScore{self.highscore}-",align="center",font=("Arial",24,"normal"))


    def increase_score(self):
        self.update_score()
        self.score+=1
    # def game_over(self):
    #     self.write("GAME_OVER ",align="center",font=("Arial",24,"normal"))
    #     self.goto(0,0)


    def resret(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open(r"C:\Users\samsung\New folder (2)\100_days_of_coding\day_20\scores.txt",mode="w") as file:
                 file.write(f"{self.highscore}")
        self.score=0
        file.write()
        self.update_score()


     

