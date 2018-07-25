# Paper Reviews

### Repository of shorthand paper reviews

Name each file:
([a-z]+_)+[a-z]+.md where the pattern is the title.

Copy the template and fill in the sections.

Use (space separated) keywords to identify the papers.

A script (to write) will parse the domain and keyword section and make folders of symbolic links based on the parsed papers.
This will result in the following layout:
```
./papers
    ./paper_1 # domain CS, keyword ml, graph
    ./paper_2 # domain Biology, CS keywords math, graph
./tree
    ./biology
        ./graph
            ./paper_2 --> ./papers/paper_2
        ./math
            ./paper_2 --> ./papers/paper_2
    ./cs
        ./ML
            ./paper_1 --> ./papers/paper_1
        ./graph
            ./paper_1 --> ./papers/paper_1
            ./paper_2 --> ./papers/paper_2
        ./math
            ./paper_2 --> ./papers/paper_2
```

#### Template
See ./template.md
