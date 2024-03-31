import tkinter as tk
from random import random, randint, choice
from time import sleep
import numpy as np
from easygui import *
from numpy import floor


def generate_population():
    global population, Population_size
    for i in range(board_size):  #Generate the population based on the given parameters.
        row = []
        for j in range(board_size):
            if random() < P:
                row.append([1, "unbeliever"])
                Population_size += 1
            else:
                row.append([0, None])
        population.append(row)
    return population


def draw_states():
    global population, window, rectangle_size, Population_size


    count_s1 = floor(S1 * Population_size)
    count_s2 = floor(S2 * Population_size)
    count_s3 = floor(S3 * Population_size)
    count_s4 = floor(S4 * Population_size)
    array_state = [1, 2, 3, 4]
    for i in range(board_size):
        for j in range(board_size):
            if population[i][j][0] == 1:
                state = 0
                if count_s1 == 0 and 1 in array_state:
                    array_state.remove(1)
                if count_s2 == 0 and 2 in array_state:
                    array_state.remove(2)
                if count_s3 == 0 and 3 in array_state:
                    array_state.remove(3)
                if count_s4 == 0 and 4 in array_state:
                    array_state.remove(4)

                if array_state:
                    state = choice(array_state)

                if state == 1:
                    population[i][j][0] = state
                    count_s1 -= 1

                elif state == 2:
                    population[i][j][0] = state
                    count_s2 -= 1


                elif state == 3:
                    population[i][j][0] = state
                    count_s3 -= 1


                elif state == 4:
                    population[i][j][0] = state
                    count_s4 -= 1



    population = np.array(population)
    np.random.shuffle(population)


def draw_population():
    global population, canvas, rectangle_size


    invalid = 1
    while invalid:  #Draw the population on the canvas
        X_red_person = randint(0, board_size -1)
        Y_red_person = randint(0, board_size -1)
        if population[X_red_person][Y_red_person][0] != 0:
            invalid = 0
    for i in range(board_size):
        for j in range(board_size):
            if population[i][j][0] != 0:
                if i == X_red_person and j == Y_red_person:
                    population[X_red_person][Y_red_person][1] = "believer"
                    # Paint the selected person yellow
                    paintNdraw(i, j, 'red', population[i][j][0])
                else:
                    paintNdraw(i, j, 'blue', population[i][j][0])


def paintNdraw(i, j, color, state):
    fontSize = 5
    padding = 5
    canvas.create_rectangle(j * rectangle_size, i * rectangle_size, (j + 1) * rectangle_size, (i + 1) * rectangle_size,
                            fill=color, outline="white")
    if color == 'red':
        canvas.create_text((j * rectangle_size + padding, i * rectangle_size + padding), text=str(state),
                       font=["Ariel", fontSize], fill="black")


def update_population(population):
    global L_matrix, canvas, rectangle_size
    # Create a copy of the population to update
    updated_population = np.copy(population)

    for i in range(board_size):
        for j in range(board_size):
            if population[i][j][1] == "believer":

                # Check all 8 neighboring cells
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        # Skip the current cell
                        if x == 0 and y == 0:
                            continue

                        # Get the neighbor's coordinates
                        neighbor_x = i + x
                        neighbor_y = j + y

                        # Check if the neighbor is within the grid
                        if neighbor_x >= 0 and neighbor_x < board_size and neighbor_y >= 0 and neighbor_y < board_size:
                            #check if the unbelievers neighbors can spread the rumor + check they've already passed L generations
                            if population[neighbor_x][neighbor_y][1] == "unbeliever" and L_matrix[neighbor_x][neighbor_y] == 0 :
                                # Get the type of the unbeliever neighbor
                                neighbor_type = population[neighbor_x][neighbor_y][0]
                                if is2neighbors(population, neighbor_x, neighbor_y) and neighbor_type != 1:
                                    neighbor_type -= 1
                                # Implement the logic based on the type of unbeliever neighbor
                                if neighbor_type == 1:
                                    # S1: Always become a believer
                                    updated_population[neighbor_x][neighbor_y][1] = "believer"
                                    # Paint cell red
                                    paintNdraw(neighbor_x, neighbor_y, 'red', population[neighbor_x][neighbor_y][0])


                                elif neighbor_type == 4:
                                    # S4: Stay as unbeliever
                                    pass
                                elif neighbor_type == 2:
                                    # S2: Become a believer with 2/3 probability
                                    if random() < 2 / 3:
                                        updated_population[neighbor_x][neighbor_y][1] = "believer"
                                        # Paint cell red
                                        paintNdraw(neighbor_x, neighbor_y, 'red', population[neighbor_x][neighbor_y][0])


                                elif neighbor_type == 3:
                                    # S3: Become a believer with 1/3 probability
                                    if random() < 1 / 3:
                                        updated_population[neighbor_x][neighbor_y][1] = "believer"
                                        # Paint cell red
                                        paintNdraw(neighbor_x, neighbor_y, 'red', population[neighbor_x][neighbor_y][0])

                updated_population[i][j][1] = "unbeliever"
                paintNdraw(i, j, 'blue', population[i][j][0])
                L_matrix[i][j] = L
            else:
                if L_matrix[i][j] > 0:
                    L_matrix[i][j] -= 1
    return updated_population


def is2neighbors(population, i, j): # Check if the current cell has a more than one believer neighbor
    bool = 0
    sum = 0
    for x in range(max(0, i - 1), min(i + 2, len(population))):
        for y in range(max(0, j - 1), min(j + 2, len(population[0]))):
            if (x, y) != (i, j) and population[x][y][1] == "believer":
                sum += 1
    if sum > 1 :
        bool = 1
    return bool

rectangle_size = 8
population = []
board_size = 100
L_matrix = np.zeros((board_size, board_size))
Generation = 55
P, L, S1, S2, S3, S4 = 0, 0, 0, 0, 0, 0
valid = 1
tolerance = 1e-6

while valid:
    msg = "Please set the following parameters:"
    title = "rumor spreading simulation"
    fields = ["P (Percentage of settlers in the population) ", "L (#generation without receiving a rumor)", "s1", "s2", "s3", "s4"]
    default_values = ["0.75", "2", "0.25", "0.25", "0.25", "0.25"]
    menu = multenterbox(msg, title, fields, default_values)
    P = float(menu[0])
    L = int(menu[1])
    S1 = float(menu[2])
    S2 = float(menu[3])
    S3 = float(menu[4])
    S4 = float(menu[5])
    if 1 > P > 0 and L >= 0 and abs((S1 + S2 + S3 + S4) - 1) < tolerance:
        valid = 0
Population_size = 0
# Create Tkinter window
window = tk.Tk()
window.title("Rumor spreading simulation")
canvas = tk.Canvas(window, width=board_size*rectangle_size, height=board_size*rectangle_size)
canvas.grid()

# Generate and draw the population
generate_population()
draw_states()
draw_population()
window.update()

for generation in range(2, Generation + 1):
    population = update_population(population)
    window.update()
window.destroy()
#find number of rumormongers
normal = 0
rumormongers = 0
for i in range(board_size):
    for j in range(board_size):
        if population[i][j][1] == "believer":
            rumormongers += 1
        elif population[i][j][1] == "unbeliever":
            normal += 1

rumormongersPer = (rumormongers / Population_size) * 100
normalPer = (normal/Population_size) * 100

msg = "rumor spreading simulation"
title = "SUMMARY"
fields = ["rumormongers", "normal / not rumormonger ", "rumormongers %: ", "normal / not rumormonger %", "P", "L", "s1", "s2", "s3", "s4"]
values = [rumormongers, normal, str(rumormongersPer), str(normalPer), str(P), str(L), str(S1), str(S2), str(S3), str(S4)]
# creating a integer box
summary = multenterbox(msg, title, fields, values)


