#Shun Fai Lee Lab1
class Cstack:
    def __init__(self, max_height: int):
        """
        This class is used to hold str in a traditional stack.
        :param max_height: The maximum number of items to be held in the stack
        """
        self.max_items = max_height
        self.items = []

    def is_empty(self) -> bool:
        """
        Determines if the stack is currently holding any item
        :return: True if the stack currently has no items
        """
        return len(self.items) == 0

    def is_full(self) -> bool:
        """
        Determines if the stack is currently full.
        :return: True if the stack is full
        """
        return len(self.items) >= self.max_items

    def pop(self) -> str:
        """
        if the stack is not empty
        Removes one item from the top of the stack and returns it.
        :return: The current string item on top of the stack.
        """
        if len(self.items) <= 0:
            raise Exception("stack is empty")
        else: return self.items.pop()

    def push(self, insert_me: str) -> None:
        """
        Pushes a string item on to the stack
        :param insert_me: the string item to insert. NOTE: Must be of type str
        """
        if self.max_items <= len(self.items):
            raise OverflowError("Stack exceeds max height")
        elif type(insert_me) is not str:
            raise AssertionError(f"This is an string stack! Please don't "
                                 f"feed me {type(insert_me)}")
        else : self.items.append(insert_me)

    def peek(self) -> str:
        """
        if the stack is not empty
        Removes one item from the top of the stack and returns it.
        :return: The current string item on top of the stack.
        """
        temp = self.items.pop()
        self.items.append(temp)
        return temp

    def len(self) -> int:
        """
        Determines the number of elements the stack currently
        :return: an int value
        """
        return len(self.items)