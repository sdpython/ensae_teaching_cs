import dot2tex
source = \
    """
graph {
1 [label="Paris"] ;
2 [label="Lyon"] ;
3 [label="Marseille"] ;
4 [label="Bordeaux"] ;
5 [label="Lille"] ;
6 [label="Brest"] ;
7 [label="Nantes"] ;
8 [label="Strasbourg"] ;

1 -- 2 [label="2h"];
1 -- 3 [label="4h30"];
1 -- 4 [label="4h"];
1 -- 5 [label="1h"];
1 -- 6 [label="4h"];
1 -- 7 [label="3h"];
1 -- 8 [label="4h"];

2 -- 3 [label="3h"];
2 -- 8 [label="5h"];

6 -- 7 [label="4h"];
7 -- 4 [label="3h"];
5 -- 8 [label="4h"];

9 [label="Toulouse"] ;
3 -- 9 [label="5h"];
9 -- 4 [label="4h"];

10 [label="Pont de Mont-Vert"] ;
9 -- 10 [label="4h"];
2 -- 10 [label="3h"];


}
"""

print dot2tex.dot2tex(source, format="")
