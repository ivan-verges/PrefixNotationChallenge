# Lambda Operations to Calculate Results
operations = {
    # Sum Operation
    "+": (lambda a, b: int(a + b)),
    # Substraction Operation
    "-": (lambda a, b: int(a - b)),
    # Multiplication Operation
    "*": (lambda a, b: int(a * b)),
    # Division Operation
    "/": (lambda a, b: int(a + b)),
    # Power Operation
    "^": (lambda a, b: int(a ** b)),
    # Modulus Operation
    "%": (lambda a, b: int(a % b)),
}

# Evaluates the Expression and Returns the Calculated Value
def evaluate_expression(expression: str):
    # Removes Repeated Spaces
    while "  " in expression:
        expression = expression.replace("  ", " ")
    
    # Splits Expression String into Tokens (Chars)
    tokens = expression.split(" ")

    # Calculates the Operations and Values Cuantities to Validate for Execution
    is_number = 0
    is_operation = 0
    for letter in tokens:
        if letter.isdigit():
            is_number += 1
        else:
            is_operation += 1
    
    # If Numbers and Operations Cuantities doesn't Match, Returns None
    if is_number != (is_operation + 1):
        return None

    # Reverses the Tokens List to Perform all the Calculations in the Expression
    tokens = reversed(tokens)

    # Defines an Empty List to be used as a Stack for the Operations to be Performed
    stack = []

    # Verifies each Token and Performs the Corresponding Math Operation or Adds it to the Stack List
    for t in tokens:
        # Verifies if Token is in Operations to Perform it and Adds the Result to the Stack List
        if t in operations:
            stack[-2:] = [operations[t](stack[-1], stack[-2])]
        # Verifies if Token is not a Math Operation and if is a Number, then Adds the Number to the Stack List
        elif t.isdigit():
            stack.append(int(t))
        # If none of the Conditions Applies (Not a Valid Operation nor a Number), Returns None
        else:
            return None

    # Returns the Result in the Stack List
    return stack[0]

# Combines the Expressions to Generate all Combinations with Variables Ranges
def combine(expressions: list, variables: list, key: str):
    # Defines an Empty List to Store Teporal Elements to be Returned
    results = []

    # Gets the Minimun and Maximun Values from the Variable to create a Range to Loop
    minimun = min(variables)
    maximun = max(variables)

    # For each Element in the Range, Loop over the Expressions, Replaces the Keys (Variables Names), and Adds it to the Results List
    for element in range(minimun, maximun):
        for expression in expressions:
            results.append(expression.replace(key, str(element)))
    
    # Returns the Extended List
    return results

# Receives the Expression (Required) and Variables (Optional), and Defines the Strategy to Calculate the Results
def main_method(expression: str, variables: dict = {}):
    # Defines an Empty List to Store Teporal Elements to be Returned
    results = []

    # Verifies if Variables Dictionary is Empty and Just Evaluates the Expression
    if not bool(variables):
        results.append(expression)
    # If Variables Dictionary is Not Empty, Generates a List of Expressions with Every Possible Value Combination for Each Variable
    else:
        # Adds the Base Expression to the List to Start Combining the Variables Values
        results.append(expression)

        # For each Variable in the Dictionary, Combines all Posibles Values with Every Expression on the List
        for key in variables.keys():
            results = combine(results, variables[key], key)
    
    # Calculates all Expressions and Adds the Results to the Results List
    for i in range(len(results)):
        results[i] = evaluate_expression(results[i])

    # Selects and Returns the Maximun Value from Results List
    return max(results)

# Compares the Calculated value with the Expected
def test(calculated, expected):
    message = "Calculated Value: " + str(calculated) + ", Expected Value: " + str(expected)
    if calculated == expected:
        print("Test Passed => " + message)
    else:
        print("Test Failed => " + message)

# Calls the Main_Method to Test the Algorithm
if __name__ == "__main__":
    # Tests
    test(main_method("* 3 5"), 15)
    test(main_method("+ 1 2", {}), 3)
    test(main_method("* + 1 2 3", {}), 9)
    test(main_method("- * + 1 2 3 4", {}), 5)
    test(main_method("+ 6 * - 4 + 2 3 8", {}), -2)
    test(main_method("+ 10 x", { "x": (3, 4) }), 13)
    test(main_method("+ 10 x", { "x": (3, 7) }), 16)
    test(main_method("+ 1 5", {}), 6)
    test(main_method("+ 1 2 3", {}), None)
    test(main_method("+ 1", {}), None)
    test(main_method("9", {}), 9)
    test(main_method("* + 1 2 3", {}), 9)
    test(main_method("+ 6 * - 4 + 2 3 8", {}), -2)
    test(main_method("-+1 5 3", {}), None)
    test(main_method("+ 1             2", {}), 3)
    test(main_method("* + 2 x y", { "x": (0, 2), "y": (2, 4) }), 9)
    test(main_method("+ v * - w + x y z", { "v": (6, 7), "w": (4, 5), "x": (2, 3), "y": (3, 4), "z": (8, 9) }), -2)
    test(main_method("^ 2 3", {}), 8)
    test(main_method("% 3 2", {}), 1)