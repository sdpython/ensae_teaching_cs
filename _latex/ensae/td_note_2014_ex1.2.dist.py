#coding: latin-1

# énoncé 1, exercice 2 distance de Levenstein

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
print(distance_edition("levenstein", "levenshtein"))    # 1
print(distance_edition("bonbon", "bonbom"))             # 1
print(distance_edition("example", "exemples"))          # 2
print(distance_edition("esche", "eche"))                # 1

# question 2

print("****2*")
print(distance_edition("levenshtein", "levenstein"))    # 1
print(distance_edition("bonbom", "bonbon"))             # 1
print(distance_edition("exemples", "example"))          # 2
print(distance_edition("eche", "esche"))                # 1

# question 3


def distance_edition(mot1, mot2):
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
                if c == d:
                    x = dist[i - 1, j - 1]
                elif c in ['n', 'm'] and d in ['n', 'm']:
                    x = dist[i - 1, j - 1] + 0.5
                else:
                    x = dist[i - 1, j - 1] + 1
                opt.append(x)
            dist[i, j] = min(opt)
    return dist[len(mot1) - 1, len(mot2) - 1]


print("****3*")
print(distance_edition("levenstein", "levenshtein"))    # 1
print(distance_edition("bonbon", "bonbom"))             # 0.5
print(distance_edition("example", "exemples"))          # 2
print(distance_edition("esche", "eche"))                # 1
print(distance_edition("levenshtein", "levenstein"))    # 1
print(distance_edition("bonbom", "bonbon"))             # 0.5
print(distance_edition("exemples", "example"))          # 2
print(distance_edition("eche", "esche"))                # 1

# question 4


def distance_edition(mot1, mot2):
    dist = {(-1, -1): 0}
    for i, c in enumerate(mot1):
        dist[i, -1] = dist[i - 1, -1] + 1
        dist[-1, i] = dist[-1, i - 1] + 1
        for j, d in enumerate(mot2):
            opt = []
            if (i - 1, j) in dist:
                if c == "s":
                    x = dist[i - 1, j] + 0.5
                else:
                    x = dist[i - 1, j] + 1
                opt.append(x)
            if (i, j - 1) in dist:
                if d == "s":
                    x = dist[i, j - 1] + 0.5
                else:
                    x = dist[i, j - 1] + 1
                opt.append(x)
            if (i - 1, j - 1) in dist:
                if c == d:
                    x = dist[i - 1, j - 1]
                elif c in ['n', 'm'] and d in ['n', 'm']:
                    x = dist[i - 1, j - 1] + 0.5
                else:
                    x = dist[i - 1, j - 1] + 1
                opt.append(x)
            dist[i, j] = min(opt)
    return dist[len(mot1) - 1, len(mot2) - 1]


print("****4*")
print(distance_edition("levenstein", "levenshtein"))    # 1
print(distance_edition("bonbon", "bonbom"))             # 0.5
print(distance_edition("example", "exemples"))          # 1.5
print(distance_edition("esche", "eche"))                # 0.5
print(distance_edition("levenshtein", "levenstein"))    # 1
print(distance_edition("bonbom", "bonbon"))             # 0.5
print(distance_edition("exemples", "example"))          # 1.5
print(distance_edition("eche", "esche"))                # 0.5

# question 5


def distance_edition(mot1, mot2):
    dist = {(-1, -1): 0}
    for i, c in enumerate(mot1):
        dist[i, -1] = dist[i - 1, -1] + 1
        dist[-1, i] = dist[-1, i - 1] + 1
        for j, d in enumerate(mot2):
            opt = []
            if (i - 1, j) in dist:
                if c == "s":
                    if i == len(mot1) - 1:
                        x = dist[i - 1, j] + 0.2
                    else:
                        x = dist[i - 1, j] + 0.5
                else:
                    x = dist[i - 1, j] + 1
                opt.append(x)
            if (i, j - 1) in dist:
                if d == "s":
                    if j == len(mot2) - 1:
                        x = dist[i, j - 1] + 0.2
                    else:
                        x = dist[i, j - 1] + 0.5
                else:
                    x = dist[i, j - 1] + 1
                opt.append(x)
            if (i - 1, j - 1) in dist:
                if c == d:
                    x = dist[i - 1, j - 1]
                elif c in ['n', 'm'] and d in ['n', 'm']:
                    x = dist[i - 1, j - 1] + 0.5
                else:
                    x = dist[i - 1, j - 1] + 1
                opt.append(x)
            dist[i, j] = min(opt)
    return dist[len(mot1) - 1, len(mot2) - 1]


print("****5*")
print(distance_edition("levenstein", "levenshtein"))    # 1
print(distance_edition("bonbon", "bonbom"))             # 0.5
print(distance_edition("example", "exemples"))          # 1.2
print(distance_edition("esche", "eche"))                # 0.5
print(distance_edition("levenshtein", "levenstein"))    # 1
print(distance_edition("bonbom", "bonbon"))             # 0.5
print(distance_edition("exemples", "example"))          # 1.2
print(distance_edition("eche", "esche"))                # 0.5
