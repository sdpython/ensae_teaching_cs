# coding: latin-1
def get_lines (file) :
    """retourne toutes les lignes d'un fichier, nettoie les fins de lignes et les espaces"""
    f = open (file, "r")
    li = f.readlines ()
    f.close ()
    return [ l.strip ("\r\n") for l in li ]
        
def distance (line1, line2) :
    """construit une distance entre deux tableaux de lignes"""
    d = { (-1,-1):(0,(-1,-1), "") }
    for i in xrange (0, len (line1)) :
        d [ i,-1 ] = (i+1, (i-1,-1), "+ " + line1 [i])
    for j in xrange (0, len (line2)) :
        d [ -1,j ] = (j+1, (-1,j-1), "- " + line2 [j])
    
    for i in xrange (0, len (line1)) :
        l1 = line1 [i]
        for j in xrange (0, len (line2)) :
            l2 = line2 [j]
            c  = abs (cmp (l1, l2))
            i1 = d [i-1,j][0] + 1
            i2 = d [i,j-1][0] + 1
            i3 = d [i-1,j-1][0] + 2*c
            if i1 <= min (i2, i3) :
                d [i,j] = (i1, (i-1,j), "+ " + l1)
            elif i2 <= min (i1, i3) :
                d [i,j] = (i2, (i,j-1), "- " + l2)
            else :
                d [i,j] = (i3, (i-1,j-1), "  " + l1)
            
    last = (len (line1)-1, len (line2)-1)
    pos  = [d [last]]
    pn   = pos [0][1]
    while pn != (-1,-1) :
        p  = pos [len (pos)-1]
        pn = p [1]
        pos.append (d [pn])
    pos.pop ()
    pos.reverse ()
    return [ p [2] for p in pos ]

def distance_file (file1, file2) :
    line1 = get_lines (file1)
    line2 = get_lines (file2)
    return distance (line1, line2)
    
if __name__ == "__main__" :
    file1 = "filedistance.py"
    file2 = "filedistance2.py"
    res   = distance_file (file1, file2)
    for r in res :
        print r