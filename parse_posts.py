import csv

def string_to_categories(categories):
    return categories.split(',')

def is_recipe(categories):
    cat_lst = string_to_categories(categories)
    for cat in cat_lst:
        if cat.strip() == 'Recipes':
            return True
    return False

# returns [(title, url),...]
def get_recipes(): 
    f = open('posts.csv')
    posts = csv.reader(f) 
    count = 0
    recipes = []
    for row in posts:
        title = row[0]
        url = row[1]
        cats = row[2]
        
        if is_recipe(cats):
            recipes.append((title, url)) 
            count = count + 1

    print "Found {} Recipes.".format(count)
    return recipes


