
class Student:
    def __init__(self):
        self.name = "Oleg"
        self.money = 100
        self.mood = 100
        self.smartness = 90
        self.hunger = 100
        self.food = 50
        self.sleep = 100
        self.health = 100

    def attend_academy(self):
        self.mood += 5
        self.smartness += 10
        print(f"{self.name} attends academy.")

    def doing_bad(self):
        self.mood -=5
        self.smartness -= 10
        print(f"{self.name} doing bad at academy.")

    def work(self):
        self.money += 10
        print(f"{self.name} works.")

    def made_project(self):
        self.money +=30
        self.mood -= 10
        self.sleep -= 5
        print(f"{self.name} made a project.")

    def overwork(self):
        self.sleep -= 20
        self.mood -=15
        self.smartness += 15
        print(f"{self.name} does more work than usuall.")

    def daily_stuff(self):
        self.money -= 20
        self.food += 15
        print(f"{self.name} buys daily stuff.")

    def eat(self):
        self.food -= 5
        self.hunger += 10
        print(f"{self.name} ate some food.")

    def sleep(self):
        self.sleep += 20
        print(f"{self.name} slept.")
