"""
Solutions for AOC 2018 Day 12.
"""

from copy import deepcopy
import re


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

    def calculate_plant_pot_sum(self):
        """
        Calculates the sum of the indices for all plant pots with plants in
        them.
        """
        return sum(pot for (pot, plant) in self.state.items() if plant == "#")


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


def solve_part1(input_plant_sim):
    """
    Solves AOC 2018 Day 12 Part 1 // Determines the plant pot index sum for all
    pots containing plants after 20 generations.
    """
    plant_sim = deepcopy(input_plant_sim)
    for _ in range(20):
        plant_sim.conduct_step()
    return plant_sim.calculate_plant_pot_sum()


def solve_part2(_input_data):
    """
    Solves AOC 2018 Day ## Part 2 // ###
    """
    return NotImplemented
