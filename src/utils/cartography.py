"""
This module contains classes and functions to represent and operate on points
and objects in N-dimensional space.
"""

from dataclasses import dataclass
from enum import Enum, auto, unique


@unique
class CardinalDirection(Enum):
    """
    Represents the four different cardinal directions of north, east, south and
    west.
    """
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def rot90_cw(self, times=1):
        """
        Returns the CardinalDirection resulting from rotating by 90 degrees in
        the clockwise direction, repeating the specified number of times.
        """
        direction = self
        for _ in range(times):
            match direction:
                case CardinalDirection.NORTH:
                    direction = CardinalDirection.EAST
                case CardinalDirection.EAST:
                    direction = CardinalDirection.SOUTH
                case CardinalDirection.SOUTH:
                    direction = CardinalDirection.WEST
                case CardinalDirection.WEST:
                    direction = CardinalDirection.NORTH
                case _:
                    direction = None
        return direction

    def rot90_ccw(self, times=1):
        """
        Returns the CardinalDirection resulting from rotating by 90 degrees in
        the counter-clockwise direction, repeating the specified number of
        times.
        """
        direction = self
        for _ in range(times):
            match direction:
                case CardinalDirection.NORTH:
                    direction = CardinalDirection.WEST
                case CardinalDirection.EAST:
                    direction = CardinalDirection.NORTH
                case CardinalDirection.SOUTH:
                    direction = CardinalDirection.EAST
                case CardinalDirection.WEST:
                    direction = CardinalDirection.SOUTH
                case _:
                    direction = None
        return direction


@dataclass(frozen=True, eq=True)
class Location2D:
    """
    Represents a point location on a two-dimensional plane. Instances of this
    dataclass will be immutable, and can be safely hashed and added to
    collections like dicts (as keys) and sets.
    """
    x: int
    y: int
