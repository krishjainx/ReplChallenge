#!/usr/bin/env python

import unittest
from ot_validation import isValid

class TestOperationalTransformations(unittest.TestCase):
    def test_transformations(self):
        self.assertTrue(isValid(
            'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
            'Repl.it uses operational transformations.',
            '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
        ))

        self.assertFalse(isValid(
            'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
            'Repl.it uses operational transformations.',
            '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]'
        ))

        self.assertFalse(isValid(
            'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
            'Repl.it uses operational transformations.',
            '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]'
        ))

        self.assertTrue(isValid(
            'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
            'We use operational transformations to keep everyone in a multiplayer repl in sync.',
            '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
        ))

        self.assertTrue(isValid(
            'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
            'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
            '[]'
        ))

if __name__ == '__main__':
    unittest.main()
