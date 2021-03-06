import sys
import re

class Expression():
    
    ALLOWED_OPERATOR = ['+', '-', '*', '/']
    PARANTHESIS = ['(', ')']
    PRECEDENCE = ['*', '/', '+', '-']
    
    def is_existing_greater_precedence(self, token): 
        top = self.operator_stack[-1]
        if (top in self.PARANTHESIS or token in self.PARANTHESIS):
            return False
        
        if token == top:
            return False
        
        if self.get_greater_precedence(top, token) == top:
            return True
        
        return False
        
    def get_greater_precedence(self, top, token): # (*, -)
        return top if self.PRECEDENCE.index(top) < self.PRECEDENCE.index(token) else token
    
    def perform_operation(self, operand_1, operand_2, operator):
        # operator is a string, while operands are integers
        if operator == '+':
            if len(self.operator_stack) > 0 and self.operator_stack[-1]=='-':
                operand_1 = -1 * operand_1
                return abs(operand_1 + operand_2)

            return operand_1 + operand_2
        
        if operator == '-':
            if len(self.operator_stack) > 0 and self.operator_stack[-1]=='-':
                operand_1 = -1 * operand_1
                return abs(operand_1 - operand_2)
                
            return operand_1 - operand_2
        
        if operator == '*':
            if len(self.operator_stack) > 0 and self.operator_stack[-1]=='-':
                operand_1 = -1 * operand_1
                return abs(operand_1 * operand_2)
                
            return operand_1 * operand_2
        
        if operator == '/':
            if len(self.operator_stack) > 0 and self.operator_stack[-1]=='-':
                operand_1 = -1 * operand_1
                return abs(operand_1 // operand_2)
                
            return operand_1 // operand_2
        
        return value
    
    def get_tokens(self):
        regular_expression = re.compile('(\d+|[^ 0-9])')
        return re.findall(regular_expression, self.expression)
        
        
    def prepare_postfix_stacks(self):
        for token in self.get_tokens():
            if token.isdigit():
                
                self.operand_stack.append(int(token))
                continue
            
            if token in self.ALLOWED_OPERATOR:
                if (len(self.operator_stack) > 0 
                       and self.is_existing_greater_precedence(token)) :
                    operator = self.operator_stack.pop()
                    operand_2 = self.operand_stack.pop()
                    operand_1 = self.operand_stack.pop()
                    result = self.perform_operation(operand_1, operand_2, operator)
                    self.operand_stack.append(result)
                    
                self.operator_stack.append(token)           
                continue
                
            if token == '(':
                self.operator_stack.append(token)
                continue
                
            if token == ')':
                while (self.operator_stack[-1] != '('):
                    operator = self.operator_stack.pop()
                    operand_2 = self.operand_stack.pop()
                    operand_1 = self.operand_stack.pop()
                    result = self.perform_operation(operand_1, operand_2, operator)
                    self.operand_stack.append(result)
                self.operator_stack.pop() # discarding the left paranthesis
                continue
        
    def evaluate(self):
        while len(self.operator_stack) > 0:
            if(len(self.operator_stack) == 1 and len(self.operand_stack) == 1):
                val = str(self.operator_stack.pop()) + str(self.operand_stack.pop())
                self.operand_stack.append(val)
                break
            
            operator = self.operator_stack.pop()
            operand_2 = self.operand_stack.pop()
            operand_1 = self.operand_stack.pop()
            result = self.perform_operation(operand_1, operand_2, operator)
            self.operand_stack.append(result)
        return int(self.operand_stack.pop())
    
    def __init__(self, expr):
        self.expression = expr
        self.operand_stack = list()
        self.operator_stack = list()
        self.prepare_postfix_stacks()


def main():
    print("Welcome to the Expression eval solution by Ranjith. Enter the expression(s) or type 'quit' to exit.")
    while True:
        input = sys.stdin.readline().rstrip('\n')
        if input == 'quit':
            break
        else:
            print(Expression(input).evaluate())

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("KeyboardInterrupt")
    sys.exit(1)
