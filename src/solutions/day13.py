"""
Solutions for AOC 2018 Day 13.
"""

from copy import deepcopy
from dataclasses import dataclass
from src.utils.cartography import CardinalDirection, Location2D


@dataclass
class Cart:
    """
    Represents a single mine cart characterised by its location and direction.
    """
    loc: Location2D
    direction: CardinalDirection
    turns: int


def process_input_file(filepath="./input/day13.txt"):
    """
    Processes the AOC 2018 Day 13 input file into the format required by the
    solver functions. Returns a tuple containing: dict mapping Location2D to
    cart track, and list of initial cart locations and directions.
    """
    with open(filepath, encoding="utf-8") as file:
        track_map = {}
        carts = []
        y = 0
        for line in file.readlines():
            x = 0
            for char in line:
                match char:
                    case "<":
                        carts.append(
                            Cart(Location2D(x, y), CardinalDirection.WEST, 0))
                        track_map[Location2D(x, y)] = "~"
                    case ">":
                        carts.append(
                            Cart(Location2D(x, y), CardinalDirection.EAST, 0))
                        track_map[Location2D(x, y)] = "~"
                    case "^":
                        carts.append(
                            Cart(Location2D(x, y), CardinalDirection.NORTH, 0))
                        track_map[Location2D(x, y)] = "~"
                    case "v":
                        carts.append(
                            Cart(Location2D(x, y), CardinalDirection.SOUTH, 0))
                        track_map[Location2D(x, y)] = "~"
                    case " " | "\n" | "\r":
                        pass
                    case _:
                        track_map[Location2D(x, y)] = char
                # Increment to the next character
                x += 1
            # Increment to the next line
            y += 1
    return (track_map, carts)


def solve_part1(input_data):
    """
    Solves AOC 2018 Day 13 Part 1 // Determines the location of the first crash.
    """
    (track_map, carts) = deepcopy(input_data)
    while True:
        # Conduct step for each cart
        new_carts = []
        for cart in carts:
            new_carts.append(update_cart_details(track_map, cart))
        # Check for crashes
        cart_locs = set()
        for cart in new_carts:
            # Check for the location of the first crash
            if cart.loc in cart_locs:
                return f"{cart.loc.x},{cart.loc.y}"
            cart_locs.add(cart.loc)
        # Update the carts list
        carts = new_carts


def solve_part2(input_data):
    """
    Solves AOC 2018 Day 13 Part 2 // Determines the location of the last mine
    cart remaining at the end of the first tick where it is the last remaining
    mine cart.
    """
    (track_map, carts) = deepcopy(input_data)
    carts = {cart.loc: cart for cart in carts}
    while True:
        # Conduct step
        new_carts = {}
        sorted_locs = sorted(carts.keys(), key= lambda loc: (loc.y, loc.x))
        for loc in sorted_locs:
            cart = carts[loc]
            new_cart = update_cart_details(track_map, cart)
            if new_cart.loc in new_carts:
                del new_carts[new_cart.loc]
            else:
                new_carts[new_cart.loc] = new_cart
        if len(new_carts) == 1:
            loc = list(new_carts.keys())[0]
            return f"{loc.x},{loc.y}"
        carts = new_carts


def update_cart_details(track_map, cart):
    """
    Determines the new location and direction for the cart. Returns a new Cart
    object with the updated values.
    """
    # Adjust direction of cart
    loc = cart.loc
    direction = cart.direction
    turns = cart.turns
    match track_map[loc]:
        case "/":
            if direction == CardinalDirection.NORTH:
                direction = CardinalDirection.EAST
            elif direction == CardinalDirection.WEST:
                direction = CardinalDirection.SOUTH
            elif direction == CardinalDirection.SOUTH:
                direction = CardinalDirection.WEST
            else:
                direction = CardinalDirection.NORTH
        case "\\":
            if direction == CardinalDirection.NORTH:
                direction = CardinalDirection.WEST
            elif direction == CardinalDirection.WEST:
                direction = CardinalDirection.NORTH
            elif direction == CardinalDirection.SOUTH:
                direction = CardinalDirection.EAST
            else:
                direction = CardinalDirection.SOUTH
        case "+":
            if turns % 3 == 0:
                direction = direction.rot90_ccw()
            elif turns % 3 == 1:
                pass
            else:
                direction = direction.rot90_cw()
            # Record cart passing through intersection
            turns += 1
    # Update location of cart
    match direction:
        case CardinalDirection.NORTH:
            loc = Location2D(loc.x, loc.y - 1)
        case CardinalDirection.EAST:
            loc = Location2D(loc.x + 1, loc.y)
        case CardinalDirection.SOUTH:
            loc = Location2D(loc.x, loc.y + 1)
        case CardinalDirection.WEST:
            loc = Location2D(loc.x - 1, loc.y)
    return Cart(loc, direction, turns)
