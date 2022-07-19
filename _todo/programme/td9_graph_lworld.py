with open("td9_graph_lworld.txt", "r") as f :
    lines = f.readlines()
    
links =[]
for line in lines :
    spl = line.strip("\n\r ").split(",")
    if len(spl) == 2 :
        l = { "source":spl[0],"target":spl[1],"type":"-"}
        links.append(l)
        l = { "source":spl[1],"target":spl[0],"type":"-"}
        links.append(l)
        
with open("td9_graph_lworld.js", "w") as f :
    f.write ("var links = [\n")
    for l in links :
        f.write("{")
        f.write( ",".join ( [ f"{k}:'{v}'" for k,v in l.items() ] ) )
        f.write("},\n")
    f.write("\n];\n")
    