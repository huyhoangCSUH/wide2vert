import sys

if len(sys.argv) < 2:
    print "Need the filename."
    sys.exit()

filename = sys.argv[1]

line_num = 1
fout = open(filename + '_vert.csv', 'w')

with open(filename + '.csv', 'r') as f:
    for line in f:
        line = line.strip()
        line_arr = line.split(',')
        col_num = 1
        for x in line_arr:
            fout.write(str(line_num) + ',' + str(col_num) + ',' + x + '\n')
            col_num += 1
        line_num += 1
