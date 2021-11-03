#coding: latin-1

# énoncé 2, exercice 3 distance de Levenstein

# question 1

def distance_edition(mot1, mot2):
    """
    première fonction retrouvée à : http://www.xavierdupre.fr/blog/2013-12-02_nojs.html
    """
    dist = {(-1, -1): 0}
    for i, c in enumerate(mot1):
        dist[i, -1] = dist[i - 1, -1] + 1
        dist[-1, i] = dist[-1, i - 1] + 1
        for j, d in enumerate(mot2):
            opt = []
            if (i - 1, j) in dist:
                x = dist[i - 1, j] + 1
                opt.append(x)
            if (i, j - 1) in dist:
                x = dist[i, j - 1] + 1
                opt.append(x)
            if (i - 1, j - 1) in dist:
                x = dist[i - 1, j - 1] + (1 if c != d else 0)
                opt.append(x)
            dist[i, j] = min(opt)
    return dist[len(mot1) - 1, len(mot2) - 1]


print("****1*")
print(distance_edition("levenstein", "levenstien"))     # 2
print(distance_edition("bonbbon", "bonbon"))            # 1
print(distance_edition("example", "exemples"))          # 2

# question 2

print("****2*")
print(distance_edition("levenstien", "levenstein"))     # 2
print(distance_edition("bonbon", "bonbbon"))            # 1
print(distance_edition("exemples", "example"))          # 2

# question 3


def distance_edition(mot1, mot2):
    """
    première fonction retrouvée à : http://www.xavierdupre.fr/blog/2013-12-02_nojs.html
    """
    dist = {(-1, -1): 0}
    for i, c in enumerate(mot1):
        dist[i, -1] = dist[i - 1, -1] + 1
        dist[-1, i] = dist[-1, i - 1] + 1
        for j, d in enumerate(mot2):
            opt = []
            if (i - 1, j) in dist:
                x = dist[i - 1, j] + 1
                opt.append(x)
            if (i, j - 1) in dist:
                x = dist[i, j - 1] + 1
                opt.append(x)
            if (i - 1, j - 1) in dist:
                x = dist[i - 1, j - 1] + (1 if c != d else 0)
                opt.append(x)
            if (i - 2, j - 2) in dist:
                if c == mot2[j - 1] and d == mot1[i - 1]:
                    x = dist[i - 2, j - 2] + 1
                    opt.append(x)
            dist[i, j] = min(opt)
    return dist[len(mot1) - 1, len(mot2) - 1]


print("****3*")
print(distance_edition("levenstein", "levenstien"))     # 1
print(distance_edition("bonbbon", "bonbon"))            # 1
print(distance_edition("example", "exemples"))          # 2
print(distance_edition("levenstien", "levenstein"))     # 1
print(distance_edition("bonbon", "bonbbon"))            # 1
print(distance_edition("exemples", "example"))          # 2

# question 4


def distance_edition(mot1, mot2):
    """
    première fonction retrouvée à : http://www.xavierdupre.fr/blog/2013-12-02_nojs.html
    """
    dist = {(-1, -1): 0}
    for i, c in enumerate(mot1):
        dist[i, -1] = dist[i - 1, -1] + 1
        dist[-1, i] = dist[-1, i - 1] + 1
        for j, d in enumerate(mot2):
            opt = []
            if (i - 1, j) in dist:
                x = dist[i - 1, j] + 1
                opt.append(x)
            if (i, j - 1) in dist:
                x = dist[i, j - 1] + 1
                opt.append(x)
            if (i - 1, j - 1) in dist:
                x = dist[i - 1, j - 1] + (1 if c != d else 0)
                opt.append(x)
            if (i - 2, j - 2) in dist:
                if c == mot2[j - 1] and d == mot1[i - 1]:
                    x = dist[i - 2, j - 2] + 1
                    opt.append(x)
            if (i - 2, j - 1) in dist and c == d == mot1[i - 1]:
                x = dist[i - 2, j - 1] + 0.45
                opt.append(x)
            if (i - 1, j - 2) in dist and c == d == mot2[j - 1]:
                x = dist[i - 1, j - 2] + 0.45
                opt.append(x)
            dist[i, j] = min(opt)
    return dist[len(mot1) - 1, len(mot2) - 1]


print("****4*")
print(distance_edition("levenstein", "levenstien"))     # 1
print(distance_edition("bonbbon", "bonbon"))            # 0.45
print(distance_edition("example", "exemples"))          # 2
print(distance_edition("levenstien", "levenstein"))     # 1
print(distance_edition("bonbon", "bonbbon"))            # 0.45
print(distance_edition("exemples", "example"))          # 2
