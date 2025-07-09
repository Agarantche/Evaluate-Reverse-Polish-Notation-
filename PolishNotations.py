class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # nums will act as our stack to store operands
        nums = []
        # Define the set of valid operators
        operators = {"+", "-", "*", "/"}

        # Iterate through each token in the input array
        for token in tokens:
            # If the token is not an operator, it must be an integer
            if token not in operators:
                # Convert the string token to an integer and push it onto the stack
                nums.append(int(token))
            else:
                # If it's an operator, pop the last two operands from the stack
                # The order is crucial for subtraction and division: operand2 is the most recent
                operand2 = nums.pop()
                operand1 = nums.pop()

                # Perform the corresponding arithmetic operation
                if token == "+":
                    nums.append(operand1 + operand2)
                elif token == "-":
                    nums.append(operand1 - operand2)
                elif token == "*":
                    nums.append(operand1 * operand2)
                elif token == "/":
                    # For division, integer division truncates toward zero
                    nums.append(int(operand1 / operand2))

        # After processing all tokens, the single remaining element on the stack is the result
        return nums[0]
