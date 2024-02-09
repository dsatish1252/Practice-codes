import turtle

def remove_closer_turtles(turtles, distance):
  """Removes all turtles from the list that are closer than the given distance to the current turtle.

  Args:
    turtles: A list of turtle objects.
    distance: The distance in pixels.

  Returns:
    A list of turtle objects that are further than the given distance from the current turtle.
  """

  current_turtle = turtles[0]
  closer_turtles = []
  for turtle in turtles[1:]:
    if turtle.distance(current_turtle) < distance:
      closer_turtles.append(turtle)

  for turtle in closer_turtles:
    turtles.remove(turtle)

  return turtles


if __name__ == '__main__':
  screen = turtle.Screen()
  turtles = []

  for i in range(10):
    turtle = turtle.Turtle()
    turtle.shape('turtle')
    turtle.color('red')
    turtle.penup()
    turtle.goto(i * 10, 0)
    turtle.pendown()
    turtle.forward(10)
    turtles.append(turtle)

  # Remove all turtles that are closer than 50 pixels to the first turtle.
  turtles = remove_closer_turtles(turtles, 50)

  # Draw a circle around the first turtle.
  turtle.penup()
  turtle.goto(0, 0)
  turtle.pendown()
  turtle.circle(50)

  turtle.hideturtle()
  screen.mainloop()