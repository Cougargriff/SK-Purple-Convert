import csv
from parse_posts import get_recipes
import re
from create_csv import create_single_col_list

recipe_t = get_recipes() # returns [(title, url),...]

def get_diff_csv():
    return csv.reader(open('in_purple_not_blue.csv'))

def in_diff(tok):
    diff_csv = get_diff_csv()

    for z_food in diff_csv:
        expl_z_food = re.split('-|,|\s', z_food[0].lower())
        
        for part in expl_z_food:
            if tok == part:
                return True
    return False


affected_recipes = []
other_recipes = []

for recipe in recipe_t:
    title = recipe[0]
    url = recipe[1]
    affected = False
    title_exploded = re.split('-|,|\s', title.lower())

    for tok in title_exploded:
        if in_diff(tok) == True:
            affected = True

    if affected == True:
        affected_recipes.append(recipe)
    else:
        other_recipes.append(recipe)

print "Found {} recipes affected by the purple plan zero point foods.".format(len(affected_recipes))
# print affected_recipes
print "Found {} recipes un-affected by purple plan zero point foods.".format(len(other_recipes))

create_single_col_list(affected_recipes, 'affected-purple-recipes.csv')
    
        




