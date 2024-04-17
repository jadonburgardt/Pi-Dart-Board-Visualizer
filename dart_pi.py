# Jadon Burgardt - pi dart program

import turtle
import random
import math

# creates a screen
screen = turtle.Screen()

# creates 'turtle' object
t = turtle.Turtle()

# turtle draw speed
t.speed(20)

# each square side length = 500 so I can see. radius will be half this to correspond with the assignment
square_side = 500

# calculate starting position x, y
coord_x = -square_side / 2  # calc x coordinate
coord_y = -square_side / 2  # calc y coordinate

# moves to the starting position x, y
t.penup()
t.goto(coord_x, coord_y)
t.pendown()

# draws the square by using a range function
for side in range(4):
    t.forward(square_side)
    t.left(90)

# for the horizontal line through the square
t.penup()
t.goto(-300, 0)
t.pendown()
t.forward(600)

# for the vertical, also
t.penup()
t.goto(0, -300)
t.setheading(90)  # sets degrees to 90 facing upwards
t.pendown()
t.forward(600)

# draw circle inside of the square
radius = square_side / 2  # radius is half of square side_length
t.penup()
t.goto(250, 0)
t.pendown()
t.circle(radius)  # draws circle using the new radius variable

# function to throw a dart and determine its location
def throw_dart(radius):
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)
    return x, y

# function to estimate pi 
def estimate_pi(num_darts):
    darts_in_circle = []

    for dart in range(num_darts):
        x, y = throw_dart(radius)
        t.speed(1000)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(10)

        # code for finding which points are in which shape
        distance = math.sqrt(x**2 + y**2)  # finds the distance of dart from the origin
        if distance <= radius:
            darts_in_circle.append((x, y))  # add to the circle list

    pi = (len(darts_in_circle) / num_darts) * 4  # Area of square is 4
    return pi

num_darts = 100 # 100 darts seemed to be a decent sample size while not wasting too much time.

while num_darts <= 100: 
    
    # using the estimate_pi function to calculate pi
    pi_estimate = estimate_pi(num_darts)
    print(f"Estimated value of pi for {num_darts} darts: {pi_estimate}")

    num_darts += 1  # Increase the number of darts for the next iteration

# to close the turtle screen when clicked
screen.exitonclick()

## SOME NOTES (that you may or may not read) - 
## 1. I submitted the code with the functionality to calculate the entire circle, not the first quadrant. I wasn't sure which one was expected. To make the first quadrant version work, in variable pi, change 4 to 1, and in the function throw_dart, change the first item in x and y's parenthesis to 0.
## 2. Sometimes testing this gives me a number for pi which is higher than 3.14. I was confused for a long time, after researching, I have come to the conclusion that it is not always guaranteed to get under 3.14 due to the volatility of the monte carlo method. Hopefully I have understood that correctly. 
## 3. when calculating for quad 1 only. I usually get something around .8 or so. when mult. by 4 this comes out to 3.2, which is above 3.14. Like said in #2, I hope this is correct.