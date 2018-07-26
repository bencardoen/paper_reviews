import os
from collections import defaultdict


def read_papers(directory_name='papers'):
    tree = defaultdict(lambda: defaultdict(list))
    for filename in os.listdir(directory_name):
        domains = []
        keywords = []
        dnext = False
        knext = False
        with open(os.path.join(directory_name, filename), 'r') as f:
            l = f.readline()
            while l:
                if dnext:
                    domains = parseLine(l)
                if knext:
                    keywords = parseLine(l)
                    break
                dnext, knext = 'Domain' in l, 'Keywords' in l
                l = f.readline()
        for d in domains:
            for k in keywords:
                tree[d][k].append(filename)
    return tree


def writeTree(tree, root='tree', paperdir='papers'):
    try:
        os.mkdir(root)
    except FileExistsError as e:
        pass
    for domain, keywords in tree.items():
        try:
            os.mkdir(os.path.join(root, domain))
        except FileExistsError as e:
            pass
        for keyword, filenames in keywords.items():
            try:
                os.mkdir(os.path.join(root, domain, keyword))
            except FileExistsError as e:
                pass
            for filename in filenames:
                src = os.path.join(paperdir, filename)
                trg = os.path.join(root, domain, keyword, filename)
                try:
                    os.link(src, trg)
                except FileExistsError as e:
                    pass


def parseLine(line):
    return [r.rstrip().lstrip().lower().replace(' ', '_') for r in line.split(',')]

def main():
    writeTree(read_papers())


if __name__ == '__main__':
    main()
