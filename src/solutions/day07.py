"""
Solutions for AOC 2018 Day 7 - "The Sum of Its Parts".
"""

import heapq
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
    (steps_queue, enqueued_steps) = initialise_steps_queue(step_maps)
    while len(steps_queue) > 0:
        # Get next step
        next_step = heapq.heappop(steps_queue)
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
                heapq.heappush(steps_queue, step)
                enqueued_steps.add(step)
    return "".join(steps_completed)


def solve_part2(step_maps):
    """
    Solves AOC 2018 Day 7 Part 2 // Determines the amount of time (in seconds)
    that is needed to complete all steps using five works and the 60+ second
    step durations.
    """
    # Set up the queue
    steps_completed = []
    (steps_queue, enqueued_steps) = initialise_steps_queue(step_maps)
    # Set up the workers
    total_time = 0
    active_workers = {}
    # Keep processing steps until there queue is empty
    while len(steps_queue) > 0 or len(active_workers) > 0:
        activate_workers(steps_queue, active_workers, max_workers=5)
        time_step = process_active_workers(steps_queue, enqueued_steps,
                                           active_workers, steps_completed,
                                           step_maps)
        total_time += time_step
    return total_time


def initialise_steps_queue(step_maps):
    """
    Generates the initial steps queue and set of enqueued steps. Returns the
    heapify-ed steps queue (list) and the set of enqueued steps.
    """
    (steps_forward, _) = step_maps
    # Find all steps that do not have any pre-requisite steps
    all_steps = set(steps_forward.keys())
    sub_steps = set()
    for steps in steps_forward.values():
        sub_steps.update(steps)
    enqueued_steps = all_steps - sub_steps
    steps_queue = []
    heapq.heapify(steps_queue)
    for step in enqueued_steps:
        heapq.heappush(steps_queue, step)
    return (steps_queue, enqueued_steps)


def activate_workers(steps_queue, active_workers, max_workers=5):
    """
    Activates workers from the inactive pool if there are available workers and
    steps ready to be worked on from the steps queue.
    """
    available_workers = max_workers - len(active_workers)
    for _ in range(available_workers):
        if len(steps_queue) > 0:
            next_step = heapq.heappop(steps_queue)
            step_time = 60 + ord(next_step) - ord("A") + 1
            active_workers[next_step] = step_time
        else:
            break


def process_active_workers(steps_queue, enqueued_steps, active_workers,
                           steps_completed, step_maps):
    """
    Processes the active workers by decrementing time by minimum time remaining
    for any worker, completing steps with 0 time remaining, adding following
    steps to the steps queue and incrementing the total time count by the size
    of the time step taken.
    """
    (steps_forward, steps_backward) = step_maps
    steps_to_remove = []
    # Calculate size of time step
    time_step = 1
    if len(active_workers) > 0:
        time_step = min(active_workers.values())
    # Decrease remaining time remaining for workers
    for working_step in active_workers:
        active_workers[working_step] -= time_step
        if active_workers[working_step] == 0:
            steps_to_remove.append(working_step)
            steps_completed.append(working_step)
    # Add completed steps to finished list and add next steps to steps queue
    for step in steps_to_remove:
        del active_workers[step]
        # add next steps to step queue
        if step in steps_forward:
            for next_step in steps_forward.get(step):
                good_step = True
                for previous_step in steps_backward[next_step]:
                    if previous_step not in steps_completed:
                        good_step = False
                        break
                if next_step not in enqueued_steps and good_step:
                    heapq.heappush(steps_queue, next_step)
                    enqueued_steps.add(next_step)
    # Increment total time counter by the size of time step taken
    return time_step
