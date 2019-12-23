import csv

# lst of tuples (title, url)::rest....
def create_single_col_list(lst, fname):
    with open(fname, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Title', 'url'])
        for item in lst:
            filewriter.writerow([item[0], item[1]])