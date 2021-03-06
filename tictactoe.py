def sum(a, b, c):
    # Overriding the inbuilt sum() function
    return a + b + c

def printBoard(xState, zState):

    """
    Ternary operators are also known as conditional expressions. 
    They are operators that evaluate something based on a condition being 
    true or false. It simply allows testing a condition in a single line 
    replacing the multiline if-else making the code compact.
    Python Syntax : [on_true] if [expression] else [on_false] 
    
    References:
    https://www.geeksforgeeks.org/ternary-operator-in-python/
    """

    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    """Literal String Interpolation or F-strings: 
    The idea behind f-strings is to make string interpolation simpler.
    F-strings provide a concise and convenient way to embed python 
    expressions inside string literals for formatting.

    References:
    https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
    https://peps.python.org/pep-0498/
    """

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|--")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(xState, zState):
    # Function with all the winning possibilities for a player
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # turn is 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            # Value is an integer for indexing in the array
            xState[value] = 1 # Change 0 -> 1 in the array
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1 # Change 0 -> 1 in the array
        cwin = checkWin(xState, zState)
        if(cwin != -1):
            print("Match over")
            break
        turn = 1 - turn


"""
References:
https://youtu.be/E8fmDDtaHLU
https://gist.github.com/CodeWithHarry/d83fed6958b7626ef51aa87c2d7130de
"""