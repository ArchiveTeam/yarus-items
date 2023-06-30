import re
import sys


def main(filenames):
    items = {}
    for filename in sorted(filenames):
        print(filename)
        with open(filename, 'r') as f:
            for t, v in re.findall('https?://yarus\.ru/([^/]+)/([0-9]+)', f.read()):
                if t not in items:
                    items[t] = set()
                items[t].add(v)
    for k, v in items.items():
        with open('{}.txt'.format(k), 'w') as f:
            for s in sorted(v):
                f.write(k+':'+s+'\n')

if __name__ == '__main__':
    main(sys.argv[1:])

