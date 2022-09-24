"""
Solutions for AOC 2018 Day 14.
"""


def process_input_file(filepath="./input/day14.txt"):
    """
    Processes the AOC 2018 Day 14 input file into the format required by the
    solver functions. Returns the integer value given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return int(file.read().strip())


def solve_part1(num_recipes):
    """
    Solves AOC 2018 Day 14 Part 1 // Determines the scores of the 10 recipes
    immediately after the given number of recipes.
    """
    elf1_i = 0
    elf2_i = 1
    recipes = "37"
    while num_recipes + 10 > len(recipes):
        elf1_recipe = int(recipes[elf1_i])
        elf2_recipe = int(recipes[elf2_i])
        new_recipes = str(elf1_recipe + elf2_recipe)
        recipes += new_recipes
        elf1_i = (elf1_i + 1 + elf1_recipe) % len(recipes)
        elf2_i = (elf2_i + 1 + elf2_recipe) % len(recipes)
    return recipes[num_recipes:num_recipes + 10]


def solve_part2(num_recipes):
    """
    Solves AOC 2018 Day 14 Part 2 // Determines the number of recipes that
    appear to the left of the given score sequence.
    """
    score_sequence = str(num_recipes)
    elf1_i = 0
    elf2_i = 1
    recipes = "37"
    while True:
        left = len(recipes) - len(score_sequence)
        if left >= 0:
            if recipes[left - 1:len(recipes) - 1] == score_sequence:
                return left - 1
            if recipes[left:len(recipes)] == score_sequence:
                return left
        elf1_recipe = int(recipes[elf1_i])
        elf2_recipe = int(recipes[elf2_i])
        new_recipes = str(elf1_recipe + elf2_recipe)
        recipes += new_recipes
        elf1_i = (elf1_i + 1 + elf1_recipe) % len(recipes)
        elf2_i = (elf2_i + 1 + elf2_recipe) % len(recipes)
