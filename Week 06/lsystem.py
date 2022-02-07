# Set initial state of l-system
initial = "AB"

# Rules for the l-system
rules = {
	"A": "AB",
	"B": "A"
}

# l_system requires 3 parameters
def l_system(initial, rules, generation):
	# Set current equal to "AB"
	current = initial

	# Repeat i number of times from the initial for-loop
	for _ in range(0, generation):
		# Initialize string variable "result"
		result = ""

		# Loop through each letter in "AB"
		for state in current:
			# Find the value corresponding to the key in the "rules" dictionary and add it to result
			result += rules.get(state, state)

		# Set current to result
		current = result
	# Return current
	return current

# Print 10 times
for i in range(0, 10):
	# Print the number in the range, and call l_system
	print( "{}: {}".format(i, l_system(initial, rules, i)) )
