import json


def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]


def deletein_str(string, start, stop):
    if len(string) > stop:
        modified_string = string[0: start:] + string[stop::]
    return modified_string


def isValid(stale, latest, otjson):
    currentString = stale
    operations = json.loads(otjson)
    cursor_index = 0


    for operation in operations:
        if operation['op'] == "insert":
            currentString = insert_str(
                currentString, operation['chars'], cursor_index)
            cursor_index += len(operation['chars'])
        elif operation['op'] == "delete":
            if cursor_index + operation['count'] > len(currentString):
                return False
            else:
                currentString = deletein_str(
                    currentString, cursor_index, cursor_index + operation['count'])

        elif operation['op'] == "skip":
            if cursor_index + operation['count'] > len(currentString):
                return False
                break
            else:
                cursor_index += operation['count']

    if currentString == latest:
        return True

# Tests below --> 


print(isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'Repl.it uses operational transformations.',
  '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
))


print(isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'Repl.it uses operational transformations.',
  '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]'
))


print(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]'
))

print(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'We use operational transformations to keep everyone in a multiplayer repl in sync.',
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
))

print(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    '[]'
))
