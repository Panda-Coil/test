from collections import deque

#stack = deque()
#stack.append("first")
#stack.append("second")
#stack.append("third")

#print(stack[-1])
#stack.pop()
#print(stack[-1])
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    

def reverse_string(string):
    reversed_string = deque()
    for letter in string:
        reversed_string.append(letter)
    new_string = ""
    for x in range(0, len(string)):
        new_string += reversed_string.pop()
    return new_string

def is_balanced(paranthesis):
    stack1 = Stack
    for letter in paranthesis:
        if letter == "(" or ")" or "[" or "]" or "{" or "}":
            stack1.push(letter, letter)
    open_circle = 0
    open_square = 0
    open_curley = 0
    for paranth in stack1:
        if paranth == "(":
            open_circle += 1
        elif paranth == "[":
            open_square += 1
        elif paranth == "{":
            open_curley += 1
        elif paranth == ")" and open_circle > 0:
            open_circle -= 1
        elif paranth == "[" and open_square > 0:
            open_square -= 1
        elif paranth == "{" and open_curley > 0:
            open_curley -= 1
        else:
            return False
            break
    if open_curley == 0 and open_circle == 0 and open_square == 0:
        return True
    else:
        return False
            
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced_real(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False
    return stack.size()==0

    
    
print(is_balanced_real("({a+b})"))
print(is_balanced_real("))((a+b}{"))
print(is_balanced_real("((a+b))"))
print(is_balanced_real("((a+g))"))
print(is_balanced_real("))"))
print(is_balanced_real("[a+b]*(x+2y)*{gg+kk}"))
        

