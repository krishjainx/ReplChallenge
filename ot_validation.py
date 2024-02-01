#!/usr/bin/env python

import json

def apply_operations(stale, operations):
    current_string = stale  # Keep the string intact for efficient manipulation
    cursor = 0

    for op in operations:
        if op['op'] == 'insert':
            # Insert the characters at the current cursor position
            current_string = current_string[:cursor] + op['chars'] + current_string[cursor:]
            cursor += len(op['chars'])  # Move cursor forward by the length of the inserted string
        elif op['op'] == 'delete':
            # Ensure delete operation does not exceed the string's bounds
            if cursor + op['count'] > len(current_string):
                return False, None  # Invalid operation
            # Delete the specified number of characters from the current cursor position
            current_string = current_string[:cursor] + current_string[cursor + op['count']:]
        elif op['op'] == 'skip':
            cursor += op['count']  # Move cursor forward
            # Ensure cursor does not go beyond the current string length
            if cursor > len(current_string):
                return False, None  # Invalid operation

    return True, current_string

def isValid(stale, latest, otjson):
    operations = json.loads(otjson)
    valid, result = apply_operations(stale, operations)
    return valid and result == latest