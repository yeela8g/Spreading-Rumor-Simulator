# Rumor Spreading Simulator

## Introduction

Welcome to the Rumor Spreading Simulator! This Python project simulates the spread of rumors within a population using different strategies. The simulator aims to model the spread of rumors within a population, considering various factors such as individual beliefs, social interactions, and the effectiveness of different spreading strategies.

## How to Run

To run the simulator, follow these steps:

1. Double-click on the `main.exe` file for the main simulator or `q2.exe` for the second program. 
2. Alternatively, you can execute the Python scripts directly by running `main.py` for the main simulator and `q2.py` for the second program.
3. Follow the prompts to set the parameters for the simulation.
4. Once the simulation is complete, you'll receive a summary of the results.

## Programming Principles

The implementation of this project adheres to several key programming principles. The code is organized into functions, promoting reusability and maintainability. Variable and function names are chosen to be descriptive, enhancing code comprehension. Efficient algorithms and data structures are utilized to handle large populations effectively. The code is well-documented, with clear comments explaining the purpose and functionality of each component.

## Parameters in the Simulator

The simulator offers various parameters that can be adjusted to customize the simulation:

1. **P**: Represents the percentage of settlers in the population.Default value is 0.75.
2. **L**: Represents the number of generations without receiving a rumor. Default value is 2. 
3. **Si**: skepticism levels among individuals.
      + S1: A person with skepticism level S1 will believe every rumor they receive (unless L generations have not passed since their last   rumor).
   + S2: A person with skepticism level S2 will believe a rumor they hear with a probability of 2/3.
   + S3: A person with skepticism level S3 will believe a rumor they hear with a probability of 1/3.
   + S4: A person with skepticism level S4 won't believe any rumors they hear.
   
    For example, setting S1=0.25 means that 25% of the population exhibits the lowest level of skepticism, while the rest exhibit higher      levels of skepticism

    > In case where a resident hears a rumor from more than one neighbor in the same generation, they will tend to believe the rumor more than usual, behaving as if they have slightly lower skepticism. However, generally, the skepticism level of each individual remains constant throughout their life.

Adjusting all these parameters provides insight into the influence of differnet factors on rumor spreading dynamics.

## Examples

The simulation begins with a screen where you can set the default values of the parameters, including P, L, and skepticism levels (S1-S4):

![image](https://github.com/yeela8g/Spreading-Rumor-Simulator/assets/118124478/a0b4db8b-132e-4af0-a998-36db45a23837)

After configuring the parameters, the simulation proceeds, displaying the spread of rumors within the population over multiple generations:

![image](https://github.com/yeela8g/Spreading-Rumor-Simulator/assets/118124478/8b2c33e6-32f1-40e2-a81f-c7348c166622)

The simulation will last until there is no rumor spreading anymore or until 55 generations are passed.
Finally, the simulation concludes with a summary screen presenting the results:

![image](https://github.com/yeela8g/Spreading-Rumor-Simulator/assets/118124478/02135d50-eee9-4716-ad2b-5dfd7cf5a025)


## q2.exe
in this program we wanted to implement a similar BUT more sophisticated strategy aimed at slowing down the spread of rumors in non trivial way. The idea of ​​the strategy is to prevent from people with a low level of skepticism S1 sitting next to each other.
By strategically placing individuals with higher skepticism levels in the population, the program aims to disrupt the spread of rumors.

## Conclusions
Through simulations and analysis, this project offers insights into the dynamics of information propagation within populations. While initially designed to simulate the spread of rumors, the principles and mechanisms employed in this simulator can be adapted to model various phenomena that spread through populations, such as infectious diseases like COVID-19. By adjusting parameters and exploring different spreading strategies, researchers and practitioners can gain valuable insights into the dynamics of contagion and devise effective strategies to mitigate its impact.

Thank you for using the Rumor Spreading Simulator!
