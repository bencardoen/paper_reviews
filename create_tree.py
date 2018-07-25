def read_papers(directory_name='./papers'):
    # open directory
    # for each paper
    # scan domain
    # scan keywords
    # create tree
    # per domain
    # single node
    # per keyword (under domain), leaf node
    # leaf node is symbolic link to paper
    tree = {}
    import os
    for filename in os.listdir(directory_name):
        domains = []
        keywords = []
        dnext = False
        knext = False
        with open(filename, 'r') as f:
            l = f.readline()
            if dnext:
                domains = parseDomains(l)
            if knext:
                keywords = parseKeywords(l)
                break
            dnext = '##### Domain' in l
            knext = '##### Keywords' in l
        for d in domains:
            if d in tree:
                keys = tree[d]
                for k in keywords:
                    if k in keys:
                        keys[k].append(filename)
                    else:
                        keys[k] = [filename]
            else:
                tree[d] = {k: filename for k in keywords}
    return tree


def writeTree(tree):
    for d in tree:
        # mkdir if not exists
        for k, v in d.items():
            # mk d/k subdir if not exists
            # mk symbolic link
            pass


def parseDomains(line):
    return []


def parseKeywords(line):
    return []


def main():
    pass


if __name__ == '__main__':
    main()
