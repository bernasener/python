import turtle
import pandas
import tkinter as tk
from tkinter import messagebox

#BernaŞener180209045


screen = turtle.Screen()


screen.setup(1250,712)
screen.title("")
image = "unnamed.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("81_city.csv")
all_cities = data.city.to_list()
guessed_cities = []

writingScore = turtle.Turtle()
writingScore.color("black")
writingScore.penup()
writingScore.hideturtle()
writingScore.goto(361,300)
writingScore.write('Correct City Number : 0', font=("Bold"))

writingRemains = turtle.Turtle()
writingRemains.color("black")
writingRemains.penup()
writingRemains.hideturtle()
writingRemains.goto(361,320)
writingRemains.write('Remain City Number : 0', font=("Bold"))


a = 82
while len(guessed_cities) < 83:
    answer_city = screen.textinput(title="You can discover the cities!", prompt="City Name: ").title()

    if answer_city == "Exit":
        missing_city = []
        for city in all_cities:
            if city not in guessed_cities:
                missing_city.append(city)
        new_data = pandas.DataFrame(missing_city)
        new_data.to_csv("cities_remain.csv")
        break


    if answer_city in all_cities:
        if answer_city not in guessed_cities:
            guessed_cities.append(answer_city)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            city_data = data[data.city == answer_city]
            t.goto(int(city_data.x), int(city_data.y))
            t.write(answer_city)
            writingScore.clear()
            writingScore.write('Correct City Number : {} '.format(len(guessed_cities)), font=("Bold"))
            a = a - 1
            writingRemains.clear()
            writingRemains.write('Remain City Number : {} '.format(a), font=("Bold"))
            if(a == 0):
                messagebox.showwarning("Warning!","You WON ! Game is over !")

                break

        else:
            messagebox.showwarning("Warning!","This city is already exist in map !")

    else:

        messagebox.showwarning("Warning!", "There is no city you entered !")























