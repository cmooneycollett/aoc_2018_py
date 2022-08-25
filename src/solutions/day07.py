"""
Solutions for AOC 2018 Day 7 - "The Sum of Its Parts".
"""

from queue import PriorityQueue
import re


def process_input_file(filepath="./input/day07.txt"):
    """
    Processes the AOC 2018 Day 7 input file into the format required by the
    solver functions. Returns tuple containing: dict mapping each instruction to
    those directly following it, and dict mapping each instruction to those
    directly before it.
    """
    with open(filepath, encoding="utf-8") as file:
        steps_forward = {}
        steps_backward = {}
        regex_line = re.compile(
            r"^Step ([A-Z]) must be finished before step ([A-Z]) can begin\.$")
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if match_line := regex_line.match(line):
                step_before = match_line.group(1)
                step_after = match_line.group(2)
                # Steps forward
                if step_before not in steps_forward:
                    steps_forward[step_before] = [step_after]
                else:
                    steps_forward[step_before].append(step_after)
                # Steps backward
                if step_after not in steps_backward:
                    steps_backward[step_after] = [step_before]
                else:
                    steps_backward[step_after].append(step_before)
        return (steps_forward, steps_backward)


def solve_part1(step_maps) -> str:
    """
    Solves AOC 2018 Day 7 Part 1 // Determines the order in which the steps
    should be taken, with alphabetical order used to select the next step from
    those available.
    """
    # Extract the step maps
    (steps_forward, steps_backward) = step_maps
    # Find which steps have no pre-requisites
    steps_completed = []
    all_steps = set(steps_forward.keys())
    sub_steps = set()
    for steps in steps_forward.values():
        sub_steps.update(steps)
    enqueued_steps = all_steps - sub_steps
    steps_queue = PriorityQueue()   # Steps sorted by alphabetical order
    for step in enqueued_steps:
        steps_queue.put(step)
    while steps_queue.qsize() > 0:
        # Get next step
        next_step = steps_queue.get()
        steps_completed.append(next_step)
        # Add all following steps into the priority queue
        if next_step not in steps_forward:
            continue
        for step in steps_forward[next_step]:
            # Check if the pre-requisite steps have been completed
            good_step = True
            for previous_step in steps_backward[step]:
                if previous_step not in steps_completed:
                    good_step = False
                    break
            # Add step to queue if pre-reqs done and not already queued
            if step not in enqueued_steps and good_step:
                steps_queue.put(step)
                enqueued_steps.add(step)
    return "".join(steps_completed)


def solve_part2(_step_maps):
    """
    Solves AOC 2018 Day 7 Part 2 // ###
    """
    return NotImplemented
