def mad_libs():
    print("Let\'s play Mad Libs! fill in the blanks with your own words")

    name=input("Give me a name: ")
    place=input("Tell me a place: ")
    funny_adj=input("Give me a funny adjective: ")
    random_object = input("Give me a random object: ")
    animal=input ("Give me an animal: ")
    action_verb=input("Give me an action verb: ")
    funny_exclamation=input("Give me a funny exclamation:")
    story =f"""
    Once upon a time, there was a person named {name}. They lived in {place} and one day found something very {funny_adj}.
    Around them were tons of {random_object}. Suddenly, a group of {animal} appeared!
    {name} started to {action_verb}, then laughed and shouted, "{funny_exclamation}!"
    What a day!
     """
    print("\nHere is your madlib story")
    print(story)
if __name__ == "__main__":
    mad_libs()