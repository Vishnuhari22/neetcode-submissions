class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(int(i))
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if i == "+":
                    stack.append(num2+num1)
                elif i == "-":
                    stack.append(num2-num1)
                elif i == "*":
                    stack.append(num1*num2)
                elif i == "/":
                    stack.append(int(num2/num1))
                else:
                    return False
        return stack[-1]