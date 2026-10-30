def calculate(first, operator, second):
	"""Return the result of a basic arithmetic operation."""
	if operator == "+":
		return first + second
	if operator == "-":
		return first - second
	if operator == "*":
		return first * second
	if operator == "/":
		if second == 0:
			raise ZeroDivisionError("Cannot divide by zero.")
		return first / second
	raise ValueError("Unsupported operator. Use +, -, *, or /.")


if __name__ == "__main__":
	try:
		first = float(input("First number: "))
		operator = input("Operator (+, -, *, /): ").strip()
		second = float(input("Second number: "))
		print("Result:", calculate(first, operator, second))
	except (ValueError, ZeroDivisionError) as error:
		print("Error:", error)
