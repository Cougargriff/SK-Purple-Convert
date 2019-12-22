import csv
from os import system, name

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

blue_f = open('blue_zero_point_foods.csv')
purple_f = open('purple_zero_point_foods.csv')

blue_csv = csv.reader(blue_f)
purple_csv = csv.reader(purple_f)

diff_foods = []
progress = 0

def print_progress(p):
    progress = ""
    for x in range(0, p / 3):
        progress += "."
    print progress

# loop through purple foods and check if in blue foods
for p in purple_csv:
    clear()
    print_progress(progress)
    in_list = False
    for b in blue_csv:
        diff = p[0].strip().lower() == b[0].strip().lower()
        # print "{} == {} = {}".format(p[0], b[0], diff)
        if diff == True:
            in_list = True
        blue_csv = csv.reader(open('blue_zero_point_foods.csv'))
    print "."
    if in_list == False:
        diff_foods.append(p)
    progress += 1

print "Found {} foods in purple plan not included in blue plan.".format(len(diff_foods))

# output new csv containing the difference of purple
with open('in_purple_not_blue.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow('Diff_Foods')
    for food in diff_foods:
        filewriter.writerow(food)
            

        