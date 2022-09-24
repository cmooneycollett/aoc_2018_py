"""
Solutions for AOC 2018 Day 13.
"""

from copy import deepcopy
from dataclasses import dataclass
from src.utils.cartography import CardinalDirection, Location2D


@dataclass
class Cart:
    """
    Represents a single mine cart characterised by its direction and number of
    intersection turns conducted.
    """
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
        carts = {}
        y = 0
        for line in file.readlines():
            x = 0
            for char in line:
                loc = Location2D(x, y)
                match char:
                    case "<":
                        carts[loc] = Cart(CardinalDirection.WEST, 0)
                        track_map[Location2D(x, y)] = "-"
                    case ">":
                        carts[loc] = Cart(CardinalDirection.EAST, 0)
                        track_map[Location2D(x, y)] = "-"
                    case "^":
                        carts[loc] = Cart(CardinalDirection.NORTH, 0)
                        track_map[Location2D(x, y)] = "|"
                    case "v":
                        carts[loc] = Cart(CardinalDirection.SOUTH, 0)
                        track_map[Location2D(x, y)] = "|"
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
        (new_carts, crash_sites) = conduct_tick(
            track_map, carts, stop_on_first_crash=True)
        if len(crash_sites) == 1:
            return f"{crash_sites[0].x},{crash_sites[0].y}"
        carts = new_carts


def solve_part2(input_data):
    """
    Solves AOC 2018 Day 13 Part 2 // Determines the location of the last mine
    cart remaining at the end of the first tick where it is the last remaining
    mine cart.
    """
    (track_map, carts) = deepcopy(input_data)
    while True:
        (new_carts, _) = conduct_tick(track_map, carts, stop_on_first_crash=False)
        if len(new_carts) == 1:
            loc = list(new_carts.keys())[0]
            return f"{loc.x},{loc.y}"
        carts = new_carts


def update_cart_details(track_map, loc, cart):
    """
    Determines the new location and direction for the cart. Returns a tuple
    containing the new location, and Cart object with updated direction.
    """
    # Adjust direction of cart
    new_loc = loc
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
            new_loc = Location2D(loc.x, loc.y - 1)
        case CardinalDirection.EAST:
            new_loc = Location2D(loc.x + 1, loc.y)
        case CardinalDirection.SOUTH:
            new_loc = Location2D(loc.x, loc.y + 1)
        case CardinalDirection.WEST:
            new_loc = Location2D(loc.x - 1, loc.y)
    return (new_loc, Cart(direction, turns))


def conduct_tick(track_map, carts, stop_on_first_crash=True):
    """
    Conducts a single tick of the mine cart simulation. Returns the updated mine
    cart dict and the list of observed crash locations.
    """
    old_carts = deepcopy(carts)
    new_carts = {}
    crash_sites = set()
    sorted_locs = sorted(old_carts.keys(), key=lambda loc: (loc.y, loc.x))
    for old_loc in sorted_locs:
        crashed = False
        # Skip over old carts that have already been crashed into
        if old_loc in crash_sites:
            continue
        old_cart = old_carts[old_loc]
        # Remove from old carts to prevent spurious crashes
        del old_carts[old_loc]
        # Get updated cart location, direction and turns
        (new_loc, new_cart) = update_cart_details(track_map, old_loc, old_cart)
        # Check if new cart has crashed into another cart
        if new_loc in new_carts:
            crashed = True
            del new_carts[new_loc]
            crash_sites.add(new_loc)
        elif new_loc in old_carts:
            crashed = True
            del old_carts[new_loc]
            crash_sites.add(new_loc)
        # Check if early stop condition has been met
        if crashed and stop_on_first_crash:
            break
        # Don't add crashed cart to the new carts
        if crashed and not stop_on_first_crash:
            continue
        # Add the updated cart to the new carts record
        new_carts[new_loc] = new_cart
    return (new_carts, list(crash_sites))
