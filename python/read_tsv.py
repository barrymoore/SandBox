import sys

def main():
    filename=sys.argv[1]
    IN = open(filename, "r")
    for line in IN:
        cols = line.split('\t')
        row_name = cols.pop(0)
        print row_name
        for col in cols:
            print "\t" + col

main()
