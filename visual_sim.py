"""Visual simulation of an Autonomous Thermal Agent in LEO.

This module provides a graphical representation of a satellite utilizing
predictive shielding while orbiting Earth.
"""

import turtle
import random

def draw_space_simulation():
    # Setup the 'Orbital Canvas'
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("#0A0A1A")  # Deep Space Blue
    screen.title("LEO Thermal Autonomy: Survival Instinct Visualizer")

    # Create the Earth
    earth = turtle.Turtle()
    earth.shape("circle")
    earth.shapesize(10)
    earth.color("#1E90FF")  # Earth Blue
    earth.penup()

    # Create the Satellite (The Agent Brick)
    sat = turtle.Turtle()
    sat.shape("square")
    sat.color("white")
    sat.penup()
    sat.speed(0)

    # Create the 'Thermal Shield' Visual
    shield = turtle.Turtle()
    shield.hideturtle()
    shield.penup()

    angle = 0
    print("--- Visualizing Orbital Thermal Autonomy ---")

    while True:
        # Calculate Orbital Path
        x = 250 * turtle.math.cos(turtle.math.radians(angle))
        y = 150 * turtle.math.sin(turtle.math.radians(angle))
        sat.goto(x, y)

        # Simulation: When the satellite is on the 'Sun Side' (Right side)
        if x > 50:
            # Activate Survival Instinct
            sat.color("#FF4500")  # Warning: High Flux
            shield.clear()
            shield.goto(x, y)
            shield.dot(50, "rgba(0, 255, 255, 0.3)") # Cyan Regenerative Shield
            status = "SHIELD ACTIVE"
        else:
            sat.color("white")
            shield.clear()
            status = "NOMINAL"

        angle += 2
        if angle >= 360:
            angle = 0

if __name__ == "__main__":
    try:
        draw_space_simulation()
    except turtle.Terminator:
        print("Simulation closed by Architect.")
