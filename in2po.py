#Shun Fai Lee Lab1
#This is the stack ADT
from Lab1converter.Opstack import Cstack
#This is the function to identify if a char is operators, operand or brackets
from Lab1converter.helper import identify
#This is a function to compare precedence of operands
from Lab1converter.helper import preced_post

def in2po(str_in: str) -> str:
    """
    Convert an infix input string to postfix format.
    by sequential reading of each char in input string
    following the principle of left to right rule, precedence rule and parenthesis handling
    of postfix format
    :argument: The infix string
    :return: The postfix format of the input.
    """
    l = len(str_in)
    if l == 0:
        return ""
    """This is a stack to store operators"""
    opn = Cstack(l)
    parc = 0
    output = ''
    for _ in range(l):
        if identify(str_in[_]) == "opd":
            output = output + str_in[_]        #operands will be appended to output direct

        elif identify(str_in[_]) == "(":
            parc += 1                          #open bracket types will increase a counter by 1
            opn.push(identify(str_in[_]))                #then get pushed into the operations stack

        elif (identify(str_in[_]) == ")") and (opn.is_empty()) == False:
            tempopn = opn.pop()
            if parc > 0:
                while tempopn != '(':
                    output = output + tempopn
                    tempopn = opn.pop()
            else:
                # when there is no brackets in stacks in the middle
                # output a msg and do not raise Exception
                print(f'insufficient open parenthesis/brackets in "{str_in}" detected.')
                return "{bad line/insufficient open parenthesis/brackets}"
            parc -= 1

        elif identify(str_in[_]) == 'opn':
            if opn.is_empty():
                opn.push(str_in[_])
            else:
                while (not opn.is_empty()) and (opn.peek() != '(') and (preced_post(str_in[_],opn.peek())):
                    output = output + opn.pop()
                opn.push(str_in[_])

        elif identify(str_in[_]) == 'bad':
            print(f'incompatible input "{str_in[_]}" detected. Please only use supported characters')
            print("operators: +, -, *, /, $")
            print("alphabets operands")
            print("for infix to prefix/postfix only: brackets: ( ),{},[]")
            print(f'inside {str_in}')
            return "{bad line/incompatible string detected}"

    while not opn.is_empty():
        output = output + opn.pop()
    if parc != 0:
        #when there is still brackets in stacks at the end
        #output a msg and do not raise Exception
        print(f'insufficient close parenthesis/brackets in "{str_in}" detected.')
        return "{bad line/insufficient close parenthesis/brackets}"
    return output