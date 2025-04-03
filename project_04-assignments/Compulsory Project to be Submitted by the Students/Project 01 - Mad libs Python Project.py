# Project 1: Mad libs Python Project


def simple_programming_madlib():
    language = input("Enter a programming language: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb (present tense): ")
    noun = input("Enter a noun (plural): ")

    story = f"Learning {language} can be very {adjective}.You need to {verb} a lot of code and debug many {noun}.But in the end, it's a {adjective} skill to have!"

    print("\nYour Programming Mad Libs story:")
    print(story)

if __name__ == "__main__":
    simple_programming_madlib()