import pandas as pd


def main():
    print("Starting program")
    # # Read cvs file as pandas dataframe
    df = pd.read_csv("./Test_recipe_book.csv")
    # # Prompt user to select what recipes they want to include
    print(df["Recipe Title"])
    recipeNums = input("Select the recipes you want to cook this week by typing the recipe numbers in one line separate by spaces.\n")
    recipes = recipeNums.split(" ")
    for entry in recipes:
        print(df.at[entry, 0]) # FIX
    print(recipes)
    # # Add together ingredients into recipe list
    # # Output recipe list as print out (maybe CVS later)
    #
    print("Ending program")


if __name__ == "__main__":
    main()
