# Lambda Operations to Calculate Results
operations = {
    # Sum Operation
    "+": (lambda a, b: int(a + b)),
    # ubstraction Operation
    "-": (lambda a, b: int(a - b)),
    # Multiplication Operation
    "*": (lambda a, b: int(a * b)),
    # Division Operation
    "/": (lambda a, b: int(a + b)),
}

# Evaluates the expression and returns the calculated value
def evaluate_expression(expression: str):
    # Removes repeated spaces
    while "  " in expression:
        expression = expression.replace("  ", " ")
    
    # Splits parameter string into Tokens (Chars)
    tokens = expression.split(" ")

    # Calculates Operations and Values Cuantities
    is_number = 0
    is_operation = 0
    for letter in tokens:
        if letter.isdigit():
            is_number += 1
        else:
            is_operation += 1
    
    # If Numbers and Operations Cuantities don't match, returns None
    if is_number != (is_operation + 1):
        return None

    # Reverses the Tokens list to perform the calculation in the Right Order
    tokens = reversed(tokens)

    # Defines an empty list to be used as a Stack for the Operations to be Performed
    stack = []

    # Verifies each Token and Performs the Corresponding Math Operation or Adds it to the Stack
    for t in tokens:
        # Verifies if Token is in Operations to perform it and Adds the result to the Stack
        if t in operations:
            stack[-2:] = [operations[t](stack[-1], stack[-2])]
        # Verifies if Token is not a Math Operation and adds the number to the Stack
        elif t.isdigit():
            stack.append(int(t))
        # If none of the conditions apply, return None
        else:
            return None

    # Returns the Result in the Stack
    return stack[0]

# Combines the Expressions to generate all combinations with variables
def combine(expressions: list, variables: list, key: str):
    results = []

    # Gets the Minimun and Maximun Values to creat a Range to Loop
    minimun = min(variables)
    maximun = max(variables)

    # For each element in the range, loop over the expressions, replace the Key (variable name), and adds it to the resulting list
    for element in range(minimun, maximun):
        for expression in expressions:
            results.append(expression.replace(key, str(element)))
    
    # Returns the extended list
    return results

# Receives the Expression and Variabls and Defines the Strategy to Calculate the Results
def main_method(expression: str, variables: dict):
    results = []

    # Verifies if Variables Dictionary is Empty and just evaluates the expression
    if not bool(variables):
        results.append(expression)
    # If Variables Dictionary is not empty, generates a list of expressions with every possible value for each variable
    else:
        # Adds the Base expression to the list to start combining variables values
        results.append(expression)

        # For each variable in the dictionary, combines all posible values with every expression on the list
        for key in variables.keys():
            results = combine(results, variables[key], key)
    
    # Calculates all Expressions
    for i in range(len(results)):
        results[i] = evaluate_expression(results[i])

    # Selects the Maximun value from results and Prints it   
    result = max(results)
    print(result)

# Calls the Main_Method to Test the Algorithm
if __name__ == "__main__":
    # Multiples Tests
    main_method("+ 1 2", {}) #3
    main_method("* + 1 2 3", {}) #9
    main_method("- * + 1 2 3 4", {}) #5
    main_method("+ 6 * - 4 + 2 3 8", {}) #-2
    main_method("+ 10 x", { "x": (3, 4) }) #13
    main_method("+ 10 x", { "x": (3, 7) }) #16
    main_method("+ 1 5", {}) #6
    main_method("+ 1 2 3", {}) #None
    main_method("+ 1", {}) #None
    main_method("9", {}) #9
    main_method("* + 1 2 3", {}) #9
    main_method("+ 6 * - 4 + 2 3 8", {}) #-2
    main_method("-+1 5 3", {}) #None
    main_method("+ 1             2", {}) #3
    main_method("* + 2 x y", { "x": (0, 2), "y": (2, 4) }) #9
    main_method("+ v * - w + x y z", { "v": (6, 7), "w": (4, 5), "x": (2, 3), "y": (3, 4), "z": (8, 9) }) #-2