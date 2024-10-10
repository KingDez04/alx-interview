#!/usr/bin/python3
"""Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    opened_boxes = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in opened_boxes:
            opened_boxes.add(current_box)
            for key in boxes[current_box]:
                if key not in opened_boxes and key < len(boxes):
                    stack.append(key)

    return len(opened_boxes) == len(boxes)
