#Shun Fai Lee Lab1
def identify(in_str: str) -> str:
    """
    identify if a char is operators, operand or brackets, or incompatible
    And at the meanwhile, change all parenthesis, square bracket and curly brace bracket to only parenthesis
    :argument: The input char from the expression string, brackets support ( , ) , [ , ] , { , and }
    :return: An identification phases or the parenthesis equivalent for brackets
    """
    opn = ['+', '-', '*', '/', '$']
    opar = ['(','{','[']
    cpar = [')','}',']']
    if in_str.isalpha():
        return 'opd'
    elif in_str in opn:
        return 'opn'
    elif in_str in opar:
        return '('
    elif in_str in cpar:
        return ')'
    else:
        return 'bad'


def preced_post(optr_in: str, optr_peek: str) -> bool:
    """
    Compare the precedence of two operators for infix to postfix conversion
    :argument: optr_in :input operator from expression optr_peek: operator from top of stack
    :return: True precedence of optr_peek > precedence than optr_in
                      [peekd optr]
                        +- | */ | $
                   +- | T  | T  | T
    input operator */ | F  | T  | T
                    $ | F  | F  | F
    """
    if optr_in in ['+','-']:
        return True
    elif optr_in in ['*','/']:
        if optr_peek in ['+','-']:
            return False
        else: return True
    elif optr_in in ['$']:
        return False

def feed(input_f: input):
    """
    Compare the precedence of two operators for infix to postfix conversion
    :argument: in_path :a file object which contain some expression
    :return: a character at a time
    """
    # for line in input_file:
    # incc = "%r" % line
    # print(incc)
    c = input_f.read(1)
    if c in ['\t', ' ']:
        return feed(input_f)
    else:
        return c