"""
    Module name :- answer
    Method(s) :- answer()
"""

from solver import solver


def answer():
    """
    Find the total numbers of letters in words of numbers from 1-1000.

    Return
        Total numbers of letters in words of numbers from 1-1000.
    """
    return solver(1, 1000)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
