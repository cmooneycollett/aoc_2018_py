"""
Solutions for AOC 2018 Day 12.
"""

from copy import deepcopy
import re
from collections import deque


class PlantSim:
    """
    Represents a simulation of plant pots.
    """

    def __init__(self, initial_state_raw, recipes_raw):
        # Initialse the state
        self.state = {
            -2: ".",
            -1: ".",
            len(initial_state_raw): ".",
            len(initial_state_raw) + 1: "."
        }
        self.leftmost_pot_index = -2
        self.rightmost_pot_index = len(initial_state_raw) + 1
        for (i, char) in enumerate(initial_state_raw):
            self.state[i] = char
        # Initialise the plant pot recipes
        self.recipes = {}
        for (from_note, to_note) in recipes_raw:
            self.recipes[from_note] = to_note
        # Initialise steps
        self.steps = 0

    def conduct_step(self):
        """
        Conducts one step of the plant simulation.
        """
        # Add two empty plant pots as padding to current and new states
        new_state = {}
        for delta_left in (-1, -2):
            new_state[self.leftmost_pot_index + delta_left] = "."
            self.state[self.leftmost_pot_index + delta_left] = "."
        for delta_right in (1, 2):
            new_state[self.rightmost_pot_index + delta_right] = "."
            self.state[self.rightmost_pot_index + delta_right] = "."
        # Determine the new state for each non-padding plant in current state
        for pot in range(self.leftmost_pot_index, self.rightmost_pot_index + 1):
            # Generate matching pattern
            pattern = ""
            for delta in (-2, -1, 0, 1, 2):
                pattern += self.state[pot + delta]
            new_state[pot] = self.recipes[pattern]
        # Update the current state to the new state
        self.state = new_state
        # Record the expansion of plant pots
        self.leftmost_pot_index -= 2
        self.rightmost_pot_index += 2
        self.steps += 1

    def calculate_plant_pot_sum(self):
        """
        Calculates the sum of the indices for all plant pots with plants in
        them.
        """
        return sum(pot for (pot, plant) in self.state.items() if plant == "#")

    def get_steps(self):
        """
        Gets the total number of steps conducted by the PlantSim.
        """
        return self.steps


def process_input_file(filepath="./input/day12.txt"):
    """
    Processes the AOC 2018 Day 12 input file into the format required by the
    solver functions. Returns a PlantSim object populated with the initial state
    and plant pot recipes given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        regex_state = r"initial state: ([.#]*)"
        regex_recipe = r"([.#]{5}) => ([.#])"
        input_raw = file.read().strip()
        match_state = re.findall(regex_state, input_raw)
        match_recipes = re.findall(regex_recipe, input_raw)
        return PlantSim(match_state[0], match_recipes)


def solve_part1(input_plant_sim: PlantSim) -> int:
    """
    Solves AOC 2018 Day 12 Part 1 // Determines the plant pot index sum for all
    pots containing plants after 20 generations.
    """
    plant_sim = deepcopy(input_plant_sim)
    for _ in range(20):
        plant_sim.conduct_step()
    return plant_sim.calculate_plant_pot_sum()


def solve_part2(input_plant_sim: PlantSim) -> int:
    """
    Solves AOC 2018 Day 12 Part 2 // Determines the plant pot index sum for all
    pots containing plants after 50 billion generations.
    """
    step_cap = 50000000000  # 50 billion generations
    plant_sim = deepcopy(input_plant_sim)
    previous_sum = 0
    current_sum = plant_sim.calculate_plant_pot_sum()
    delta_queue = deque([])
    for _ in range(step_cap):
        plant_sim.conduct_step()
        temp_sum = plant_sim.calculate_plant_pot_sum()
        previous_sum = current_sum
        current_sum = temp_sum
        delta = current_sum - previous_sum
        # Break if the delta matches the previous three, indicating stability
        if len([val for val in delta_queue if val == delta]) == 3:
            break
        delta_queue.append(delta)
        if len(delta_queue) > 3:
            delta_queue.popleft()
    return current_sum + delta_queue[0] * (step_cap - plant_sim.get_steps())
