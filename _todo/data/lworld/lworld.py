def build_graph():
    relation = """
    yolanda candace bette coleman frank agatha toni teri marilyn peggy
    amy jodi bette nadia
    josh tina eric
    henry tina helena isabella
    valerie leigh helena dylan danny
    winnie helena catherine
    amy jodi bette alice sean
    april alice andrew
    alice tasha eva-papi kit benjamin
    hazel angus kit
    gregg alice phyllis leonard
    joyce phyllis
    tayo alice lisa
    uta alice nina brooke heather mandy shane lacey
    paige shane lenore
    cherie shane carmen eva-papi
    robin carmen lucia pablo
    carmen jenny dona tonya melissa
    heather melanie dana alice lara garby alice tayo
    lara dana ralph
    lara claybourne robin marina manfredi
    shane cherie
    lacey shane paige
    nick jenny gene
    robin jenny claude marina jenny
    jenny moira-max billie
    grace moira-max
    jenny tim trish
    becky tim
    helena isabella
    josh tina helena winnie
    helena catherine
    francesca marina
    """

    relation = [_.split() for _ in relation.split("\n")]
    arcs = []
    for rel in relation:
        for i in range(1, len(rel)):
            a = [rel[i - 1], rel[i]]
            a.sort()
            arcs.append(a)
    arcs.sort()
    temp = arcs
    arcs = []
    for t in temp:
        if len(arcs) == 0 or t != arcs[-1]:
            arcs.append(t)

    for a in arcs:
        print(",".join(a))

    noeuds = {}
    for a, b in arcs:
        noeuds[a] = min(len(noeuds), noeuds.get(a, 100000))
        noeuds[b] = min(len(noeuds), noeuds.get(b, 100000))

    import sys
    sys.path.append(r"D:\Dupre\_data\program\hal\hal_Python")
    import hal_python as HAL
    HAL.Begin()

    vertices = [(b, a) for a, b in noeuds.iteritems()]
    edges = [(noeuds[a], noeuds[b]) for a, b in arcs]
    im = HAL.ArcGraphDraw(vertices, edges)
    im.Display()
    HAL.Pause()

    """
    char *argv2 [6] = { "_graphviz_draw.exe",
    ".",
    "../_hal_data/hal_graph/tmp_DrawGraph.graph",
    "tmp_DrawGraph.png",
    "png",
    "neato"} ;
    """

if __name__ == "__main__":
    build_graph()
