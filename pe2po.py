#Shun Fai Lee Lab1
#This is the stack ADT
from Lab1converter.Opstack import Cstack
#This is the function to identify if a char is operators, operand or brackets
from Lab1converter.helper import identify

def pe2po(str_in: str) -> str:
    """
    Convert a prefix input string to postfix format.
    in principle, both prefix and postfix should yield the same expression when evaluated.
    conversion is done by evaluating prefix string, but without actual calculation.
    By using a for loop to do sequential reading of input string from the end backward
    char by char,
    and do pop and push accordingly with the same principle as like evaluating them.
    But we push back the whole combined expression, instead of value, back to the stacks.
    e.g. stacks [A B] [+] will yield AB+ and AB+ will be pushed back to stacks for next concatenation
    The final single combined string piece in the stack will become postfix format
    :argument: The prefix string
    :return: The postfix format of the input.
    """
    """read the length of the input string once and store it"""
    l = len(str_in)
    """This is a stack to store operators"""
    opn = Cstack(l)
    """This is a stack to store operands"""
    opd = Cstack(l)

    for _ in range(l):
        if not identify(str_in[l - _ - 1]) in ["opd", "opn"]:
            print(f'incompatible input "{str_in[l - _ - 1]}" detected. Please only use supported characters')
            print("operators: +, -, *, /, $")
            print("alphabets operands")
            print(f'inside {str_in}')
            return "{bad line/incompatible string detected}"
        else:
            if str_in[l - _ - 1].isalpha():
                opd.push(str_in[l - _ - 1])
            else:
                opn.push(str_in[l - _ - 1])
                while opd.len() > 1 and opn.len() > 0:
                    opd.push(opd.pop() + opd.pop() + opn.pop())
    """when the for loop exit, the while loop is exited too
    there should be no more character inside the two stacks, otherwise it is error scenario
    """
    if opn.len() > 0:
        #when there is still operators in stacks at the end
        #output a msg and do not raise Exception
        return "{bad line/too many operator/incorrect input}"

    elif opd.len() > 1:
        #when there is still operands in stacks at the end
        #output a msg and do not raise Exception
        return "{bad line/insufficient operator/incorrect input}"

    else:
        """nothing go wrong, return the final result string"""
        return opd.pop()