#!/usr/bin/python3
"""Implementing the lockbox algorithm"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Checks if all boxes can be unlocked.
    
    Args:
        boxes (list): A list of lists, where each sublist contains the keys found in the corresponding box.
    
    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Tracking unlocked boxes
    unlocked[0] = True  # Box 0 is always unlocked initially
    keys = [0]  # Start with the keys from box 0

    # Explore boxes as long as we have new keys to use
    while keys:
        current_key = keys.pop()

        # Check if the current key unlocks a valid box
        if not unlocked[current_key]:
            unlocked[current_key] = True  # Mark the box as unlocked

            # Add all keys found in this newly unlocked box
            for key in boxes[current_key]:
                if key < n and not unlocked[key]:
                    keys.append(key)

    # Return True if all boxes are unlocked
    return all(unlocked)

