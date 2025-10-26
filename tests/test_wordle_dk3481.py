from wordle_dk3481 import validate_guess, check_guess

def test_validate_guess():
		tests = [
				('words', True),  # correct 5 words input
				('word', False),  # incorrect 4 words input
				('WORDS', False), # incorrect capitalized input
				('word3', False), # incorrect input with non-alpha
				(12345, False),   # incorrect input of numbers
				(None, False)
		]
		for guess, expected in tests:
				result = validate_guess(guess)
				assert result == expected, f"input invalid: {guess}"


def test_check_guess_basic():
		tests = [
				('apple', 'apple'),    # correct guess
				('brain', 'hello'),    # incorrect guess with no match
				('eerie', 'keeps'),    # incorrect guess with some green, yello, gray
				('hello', 'helloo'),   # incorrect guess with wrong input (empty list expected)
		]
		results = [
				[('a', 'green'), ('p', 'green'), ('p', 'green'), ('l', 'green'), ('e', 'green')],
				[('h', 'gray'), ('e', 'gray'), ('l', 'gray'), ('l', 'gray'), ('o', 'gray')],
				[('k', 'gray'), ('e', 'green'), ('e', 'yellow'), ('p', 'gray'), ('s', 'gray')],
				[]
		]
		for i in range(len(tests)):
				guess, target = tests[i]
				output = check_guess(guess, target)
				assert output == results[i], f"Result incorrect for {guess}, {target}: {output}"