"""
Solutions for AOC 2018 Day 8.
"""


def process_input_file(filepath="./input/day08.txt"):
    """
    Processes the AOC 2018 Day 8 input file into the format required by the
    solver functions. Returns list containing the numbers listed as
    space-separated values in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return [int(val) for val in file.read().strip().split()]


def solve_part1(licence_values):
    """
    Solves AOC 2018 Day 8 Part 1 // Determines the sum of all metadata entries
    for the nodes.
    """
    (metadata_sum, _) = calculate_metadata_sum(licence_values, 0)
    return metadata_sum


def solve_part2(licence_values):
    """
    Solves AOC 2018 Day 8 Part 2 // Determines the value of the root node by
    using the second check method. The second method uses node value calculation
    that depends on whether the node has child nodes.
    """
    (metadata_sum, _) = calculate_metadata_sum(licence_values, 0,
                                               metadata_index=True)
    return metadata_sum


def calculate_metadata_sum(licence_values, start, metadata_index=False):
    """
    Calculates the sum of metadata for the current node and all child nodes.
    Returns the sum of metadata entries and the end index for the node.
    """
    num_child = licence_values[start]
    num_metadata = licence_values[start + 1]
    cursor = start + 2
    metadata_sum = 0
    child_metadata_values = []
    # Add up metadata values from child nodes
    for _ in range(num_child):
        (child_sum, cursor) = calculate_metadata_sum(licence_values, cursor,
                                                     metadata_index)
        child_metadata_values.append(child_sum)
        cursor += 1
    # Metadata values from current node
    for i in range(num_metadata):
        if metadata_index and num_child > 0:
            child_index = licence_values[cursor + i] - 1
            if child_index < 0 or child_index >= len(child_metadata_values):
                continue
            metadata_sum += child_metadata_values[child_index]
        else:
            metadata_sum += licence_values[cursor + i]
    if not metadata_index:
        metadata_sum += sum(child_metadata_values)
    return (metadata_sum, cursor + num_metadata - 1)
