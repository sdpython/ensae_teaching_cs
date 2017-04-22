#-*- coding: utf-8 -*-
"""
@file
@brief First approach for a edit distance between two graphs

See :ref:`l-graph_distance`.
"""
import copy
import re


class Vertex:
    """
    defines a vertex of a graph
    """

    def __init__(self, nb, label, weight):
        """
        constructor
        @param      nb      (int) index of the vertex
        @param      label   (str) label
        @para       weight  (float)
        """
        self.nb = nb         # kind of id
        self.label = label      # label
        self.pair = (None, None)
        self.edges = {}
        self.predE = {}
        self.succE = {}
        self.weight = weight

    def __str__(self):
        """
        usual
        """
        return self.Label

    def is_vertex(self):
        """
        returns True
        """
        return True

    def is_edge(self):
        """
        returns False
        """
        return False

    @property
    def Label(self):
        """
        returns the label
        """
        return self.label


class Edge:
    """
    defines an edge
    """

    def __init__(self, from_, to, label, weight):
        """
        constructor
        @param  from_       (int)
        @param  to          (int)
        @param  label       (str)
        @param  weight      (float)

        ``'00'`` means the beginning of a graph, ``'11'`` the end.
        """
        self.from_, self.to = from_, to
        self.nb = from_, to
        self.label = label
        self.pair = (None, None)
        self.weight = weight
        if self.from_ == "00" and self.to == "00":
            raise AssertionError("should not happen")
        if self.from_ == "11" and self.to == "11":
            raise AssertionError("should not happen")

    def __str__(self):
        """
        usual
        """
        return self.Label

    def is_vertex(self):
        """
        returns False
        """
        return False

    def is_edge(self):
        """
        returns True
        """
        return True

    @property
    def Label(self):
        """
        returns the label
        """
        return self.label


class GraphDistance:
    """
    defines a graph

    See :ref:`l-graph_distance`.
    """

    # graph is a dictionary
    @staticmethod
    def get_list_of_vertices(graph):
        edges = [edge[:2] for edge in graph]
        unique = {}
        for i, j in edges:
            unique[i] = unique[j] = 1
        vertices = list(unique.keys())
        vertices.sort()
        return vertices

    def __init__(self, edge_list, vertex_label={}, add_loop=False,
                 weight_vertex=1., weight_edge=1.):
        """
        constructor

        @param      edge_list        list of edges
        @param      add_loop         automatically add a loop on each vertex (an edge from a vertex to itself)
        @param      weight_vertex    weight for every vertex
        @param      weight_edge      weight for every edge
        """
        if type(edge_list) is str:
            self.load_from_file(edge_list, add_loop)
        else:
            self.vertices = {}
            self.edges = {}
            self.labelBegin = "00"
            self.labelEnd = "11"
            vid = GraphDistance.get_list_of_vertices(edge_list)
            for u in vid:
                self.vertices[u] = Vertex(
                    u, vertex_label.get(u, str(u)), weight_vertex)
            for e in edge_list:
                i, j = e[:2]
                ls = "" if len(e) < 3 else e[2]
                self.edges[i, j] = Edge(i, j, str(ls), weight_edge)
            self._private__init__(add_loop, weight_vertex, weight_edge)

    def __getitem__(self, index):
        """
        returns a vertex or an edge if no vertex with the given index was found
        @param      index   id (index) to look for
        @return             Vertex or Edge
        """
        if isinstance(index, str):
            return self.vertices[index]
        elif isinstance(index, tuple):
            return self.edges[index]
        else:
            raise KeyError("unable to get element " + str(index))

    @staticmethod
    def load_from_file(filename, add_loop):
        """
        loads a graph from a file
        @param      filename        file name
        @param      add_loop         @see me __init__
        """
        lines = open(filename, "r").readlines()
        regV = re.compile("\\\"?([a-z0-9_]+)\\\"? *[[]label=\\\"(.*)\\\"[]]")
        regE = re.compile("\\\"?([a-z0-9_]+)\\\"? *-> *\\\"?" +
                          "([a-z0-9_]+)\\\"? *[[]label=\\\"(.*)\\\"[]]")
        edge_list = []
        vertex_label = {}
        for line in lines:
            line = line.strip("\r\n ;")
            ed = regE.search(line)
            ve = regV.search(line)
            if ed:
                g = ed.groups()
                edge_list.append((g[0], g[1], g[2]))
            elif ve:
                g = ve.groups()
                vertex_label[g[0]] = g[1]
        if len(vertex_label) == 0 or len(edge_list) == 0:
            raise OSError("unable to parse file " + filename)
        return GraphDistance(edge_list, vertex_label, add_loop)

    def _private__init__(self, add_loop, weight_vertex, weight_edge):
        if add_loop:
            for k, v in self.vertices.items():
                if k != self.labelBegin and k != self.labelEnd:
                    self.edges[k, k] = Edge(k, k, "", weight_edge)
        self.connect_root_and_leave(weight_vertex, weight_edge)
        self.compute_predecessor()
        self.compute_successor()

    def connect_root_and_leave(self, weight_vertex, weight_edge):
        order = self.get_order_vertices()
        roots = [v for v, k in order.items() if k == 0]
        vert = {}
        for o in order:
            vert[o] = 0
        for k, v in self.edges.items():
            if k[0] != k[1]:
                vert[k[0]] += 1
        for r in roots:
            if self.labelBegin not in self.vertices:
                self.vertices[self.labelBegin] = Vertex(
                    self.labelBegin, self.labelBegin, weight_vertex)
            if r != self.labelBegin:
                self.edges[self.labelBegin, r] = Edge(
                    self.labelBegin, r, "", weight_edge)

        leaves = [k for k, v in vert.items() if v == 0]
        for r in leaves:
            if self.labelEnd not in self.vertices:
                self.vertices[self.labelEnd] = Vertex(
                    self.labelEnd, self.labelEnd, weight_vertex)
            if r != self.labelEnd:
                self.edges[r, self.labelEnd] = Edge(
                    r, self.labelEnd, "", weight_edge)

    def get_order_vertices(self):
        edges = self.edges
        order = {}
        for k, v in edges.items():
            order[k[0]] = 0
            order[k[1]] = 0

        modif = 1
        while modif > 0:
            modif = 0
            for k, v in edges.items():
                i, j = k
                if i != j and order[j] <= order[i]:
                    order[j] = order[i] + 1
                    modif += 1

        return order

    def __str__(self):
        li = []
        for k, v in self.vertices.items():
            li.append(str(v))
        for k, e in self.edges.items():
            li.append(str(e))
        return "\n".join(li)

    def compute_predecessor(self):
        """
        usual
        """
        pred = {}
        for i, j in self.edges:
            if j not in pred:
                pred[j] = {}
            pred[j][i, j] = 0
        for k, v in pred.items():
            for n in v:
                self.vertices[k].predE[n] = self.edges[n]

    def compute_successor(self):
        succ = {}
        for i, j in self.edges:
            if i not in succ:
                succ[i] = {}
            succ[i][i, j] = i, j
        for k, v in succ.items():
            for n in v:
                self.vertices[k].succE[n] = self.edges[n]

    def get_matching_functions(self, function_mach_vertices, function_match_edges,
                               cost=False):
        """
        returns default matching functions between two vertices and two edges
        @param      function_mach_vertices   if not None, this function is returned, othewise, it returns a new fonction.
                                             See below.
        @param      function_match_edges     if not None, this function is returned, othewise, it returns a new fonction.
                                             See below.
        @param      cost                     if True, the returned function should return a float, otherwise a boolean
        @return                              a pair of functions

        Example for * if cost is False:

        ::

            lambda v1,v2,g1,g2,w1,w2 : v1.label == v2.label

        Example for *function_mach_vertices* if cost is True:

        ::

            def tempF1 (v1,v2,g1,g2,w1,w2) :
                if v1 is not None and not v1.is_vertex() : raise TypeError("should be a vertex")
                if v2 is not None and not v2.is_vertex() : raise TypeError("should be a vertex")
                if v1 is None and v2 is None : return 0
                elif v1 is None or v2 is None :
                    return v2.weight*w2 if v1 is None else v1.weight*w1
                else :
                    return 0 if v1.label == v2.label else 0.5*(v1.weight*w1 + v2.weight*w2)

        Example for *function_match_edges* if cost is False:

        ::

            lambda e1,e2,g1,g2,w1,w2 : e1.label == e2.label and
                        (e1.from_ != e1.to or e2.from_ != e2.to) and
                        (e1.from_ != self.labelBegin or e1.to != self.labelBegin) and
                        (e1.from_ != self.labelEnd or e1.to != self.labelEnd)

        Example if cost is True:

        ::

            def tempF2 (e1,e2,g1,g2,w1,w2) :
                if e1 is not None and not e1.is_edge() : raise TypeError("should be an edge")
                if e2 is not None and not e2.is_edge() : raise TypeError("should be an edge")
                if e1 is None and e2 is None : return 0
                elif e1 is None or e2 is None :
                    return e2.weight*w2 if e1 is None else e1.weight*w1
                elif e1.label != e2.label : return 0.5*(e1.weight*w1 + e2.weight*w2)
                else :
                    lab1 = g1.vertices [e1.from_].label == g2.vertices [e2.from_].label
                    lab2 = g1.vertices [e1.to].label == g2.vertices [e2.to].label
                    if lab1 and lab2 : return 0
                    else :  return e1.weight*w1 + e2.weight*w2

        """
        if cost:

            if function_mach_vertices is None:
                def tempF1(v1, v2, g1, g2, w1, w2):
                    if v1 is not None and not v1.is_vertex():
                        raise TypeError("should be a vertex")
                    if v2 is not None and not v2.is_vertex():
                        raise TypeError("should be a vertex")
                    if v1 is None and v2 is None:
                        return 0
                    elif v1 is None or v2 is None:
                        return v2.weight * w2 if v1 is None else v1.weight * w1
                    else:
                        return 0 if v1.label == v2.label else 0.5 * (v1.weight * w1 + v2.weight * w2)
                function_mach_vertices = tempF1

            if function_match_edges is None:
                def tempF2(e1, e2, g1, g2, w1, w2):
                    if e1 is not None and not e1.is_edge():
                        raise TypeError("should be an edge")
                    if e2 is not None and not e2.is_edge():
                        raise TypeError("should be an edge")
                    if e1 is None and e2 is None:
                        return 0
                    elif e1 is None or e2 is None:
                        return e2.weight * w2 if e1 is None else e1.weight * w1
                    elif e1.label != e2.label:
                        return 0.5 * (e1.weight * w1 + e2.weight * w2)
                    else:
                        lab1 = g1.vertices[
                            e1.from_].label == g2.vertices[e2.from_].label
                        lab2 = g1.vertices[
                            e1.to].label == g2.vertices[e2.to].label
                        if lab1 and lab2:
                            return 0
                        else:
                            return e1.weight * w1 + e2.weight * w2

                function_match_edges = tempF2
        else:
            if function_mach_vertices is None:
                def function_mach_vertices(v1, v2, g1, g2, w1, w2):
                    return v1.label == v2.label
            if function_match_edges is None:
                def function_match_edges(e1, e2, g1, g2, w1, w2):
                    return e1.label == e2.label and \
                        (e1.from_ != e1.to or e2.from_ != e2.to) and \
                        (e1.from_ != self.labelBegin or e1.to != self.labelBegin) and \
                        (e1.from_ != self.labelEnd or e1.to != self.labelEnd)
        return function_mach_vertices, function_match_edges

    def common_paths(self, graph2,
                     function_mach_vertices=None,
                     function_match_edges=None,
                     noClean=False):
        function_mach_vertices, function_match_edges = \
            self.get_matching_functions(
                function_mach_vertices, function_match_edges)
        g = GraphDistance([])
        vfirst = Vertex(self.labelBegin, "%s-%s" % (self.labelBegin, self.labelBegin),
                        (self.vertices[self.labelBegin].weight +
                         graph2.vertices[self.labelBegin].weight) / 2)
        g.vertices[self.labelBegin] = vfirst
        vfirst.pair = self.vertices[
            self.labelBegin], graph2.vertices[self.labelBegin]

        modif = 1
        while modif > 0:
            modif = 0
            add = {}
            for k, v in g.vertices.items():

                v1, v2 = v.pair
                if len(v.succE) == 0:
                    for e1 in v1.succE:
                        for e2 in v2.succE:
                            oe1 = self.edges[e1]
                            oe2 = graph2.edges[e2]
                            if function_match_edges(oe1, oe2, self, graph2, 1., 1.):
                                tv1 = self.vertices[oe1.to]
                                tv2 = graph2.vertices[oe2.to]
                                if function_mach_vertices(tv1, tv2, self, graph2, 1., 1.):
                                    # we have a match
                                    ii = "%s-%s" % (tv1.nb, tv2.nb)
                                    if tv1.nb == self.labelEnd and tv2.nb == self.labelEnd:
                                        ii = self.labelEnd
                                    lab = "%s-%s" % (tv1.label, tv2.label) \
                                        if tv1.label != tv2.label else tv1.label
                                    tv = Vertex(
                                        ii, lab, (tv1.weight + tv2.weight) / 2)
                                    lab = "%s-%s" % (oe1.label, oe2.label) \
                                        if oe1.label != oe2.label else oe1.label
                                    ne = Edge(v.nb, tv.nb, lab,
                                              (oe1.weight + oe2.weight) / 2)
                                    add[tv.nb] = tv
                                    g.edges[ne.from_, ne.to] = ne
                                    ne.pair = oe1, oe2
                                    tv.pair = tv1, tv2
                                    v.succE[ne.from_, ne.to] = ne
                                    modif += 1
            for k, v in add.items():
                g.vertices[k] = v

        if not noClean:
            # g.connect_root_and_leave()
            g.compute_predecessor()
            g.clean_dead_ends()
        return g

    def clean_dead_ends(self):
        edgesToKeep = {}
        verticesToKeep = {}
        if self.labelEnd in self.vertices:
            v = self.vertices[self.labelEnd]
            verticesToKeep[v.nb] = False

            modif = 1
            while modif > 0:
                modif = 0
                add = {}
                for k, v in verticesToKeep.items():
                    if v:
                        continue
                    modif += 1
                    verticesToKeep[k] = True
                    for pred, vv in self.vertices[k].predE.items():
                        edgesToKeep[pred] = True
                        add[vv.from_] = verticesToKeep.get(vv.from_, False)
                for k, v in add.items():
                    verticesToKeep[k] = v

            remove = {}
            for k in self.vertices:
                if k not in verticesToKeep:
                    remove[k] = True
            for k in remove:
                del self.vertices[k]

            remove = {}
            for k in self.edges:
                if k not in edgesToKeep:
                    remove[k] = True
            for k in remove:
                del self.edges[k]
        else:
            self.vertices = {}
            self.edges = {}

    def enumerate_all_paths(self, edges_and_vertices, begin=[]):
        if len(self.vertices) > 0 and len(self.edges) > 0:
            if edges_and_vertices:
                last = begin[-1] if len(begin) > 0 \
                    else self.vertices[self.labelBegin]
            else:
                last = self.vertices[begin[-1].to] if len(begin) > 0 \
                    else self.vertices[self.labelBegin]

            if edges_and_vertices and len(begin) == 0:
                begin = [last]

            for ef in last.succE:
                e = self.edges[ef]
                path = copy.copy(begin)
                v = self.vertices[e.to]
                if e.to == e.from_:
                    # cycle
                    continue
                else:
                    path.append(e)
                    if edges_and_vertices:
                        path.append(v)
                    if v.label == self.labelEnd:
                        yield path
                    else:
                        for p in self.enumerate_all_paths(edges_and_vertices, path):
                            yield p

    def edit_distance_path(self, p1, p2, g1, g2,
                           function_mach_vertices=None,
                           function_match_edges=None,
                           use_min=False,
                           debug=False):
        """
        Tries to align two paths from two graphs
        @param      p1                      path 1 (from g1)
        @param      p2                      path 2 (from g2)
        @param      g1                      graph 1
        @param      g2                      graph 2
        @param      function_mach_vertices  function which gives a distance bewteen two vertices,
                                            if None, it take the output of @see me get_matching_functions
        @param      function_match_edges    function which gives a distance bewteen two edges,
                                            if None, it take the output of @see me get_matching_functions
        @param      use_min                 the returned is based on a edit distance, if this parameter is True, the returned value will be:

                                            ::

                                                if use_min :
                                                    n = min (len(p1), len(p2))
                                                    d = d*1.0 / n if n > 0 else 0

        @param      debug                   unused
        @return                             2-uple: distance, aligned path
        """
        function_mach_vertices, function_match_edges = \
            self.get_matching_functions(
                function_mach_vertices, function_match_edges, True)
        dist = {(-1, -1): (0, None, None)}

        w1 = 1.0 / len(p1) if use_min else 1.
        w2 = 1.0 / len(p2) if use_min else 1.

        for i1, eorv1 in enumerate(p1):
            for i2, eorv2 in enumerate(p2):
                np = i1, i2
                posit = [((i1 - 1, i2), (eorv1, None)),
                         ((i1, i2 - 1), (None, eorv2)),
                         ((i1 - 1, i2 - 1), (eorv1, eorv2)), ]

                if eorv1.is_edge() and eorv2.is_edge():
                    func = function_match_edges
                elif eorv1.is_vertex() and eorv2.is_vertex():
                    func = function_mach_vertices
                else:
                    def func(x, y, g1, g2, w1, w2):
                        return 0.5 * (x.weight * w1 + y.weight * w2) if x is not None and y is not None \
                            else (x.weight * w1 if y is None else y.weight * w2)

                for p, co in posit:
                    if p in dist:
                        c0 = dist[p][0]
                        c1 = func(co[0], co[1], g1, g2, w1, w2)
                        c = c0 + c1
                        if np not in dist:
                            dist[np] = (c, p, co, (c0, c1))
                        elif c < dist[np][0]:
                            dist[np] = (c, p, co, (c0, c1))

        last = dist[len(p1) - 1, len(p2) - 1]
        path = []
        while last[1] is not None:
            path.append(last)
            last = dist[last[1]]

        path.reverse()

        d = dist[len(p1) - 1, len(p2) - 1][0]
        if use_min:
            n = min(len(p1), len(p2))
            d = d * 1.0 / n if n > 0 else 0
        return d, path

    def private_count_left_right(self, valuesInList):
        countLeft = {}
        countRight = {}
        for k, v in valuesInList:
            i, j = v
            if i not in countRight:
                countRight[i] = {}
            countRight[i][j] = countRight[i].get(j, 0) + 1
            if j not in countLeft:
                countLeft[j] = {}
            countLeft[j][i] = countLeft[j].get(i, 0) + 1
        return countLeft, countRight

    def private_kruskal_matrix(self, matrix, reverse):
        countLeft, countRight = self.private_count_left_right(matrix)
        cleft, cright = len(countLeft), len(countRight)
        matrix.sort(reverse=reverse)
        count = max(max([sum(_.values()) for _ in countRight.values()]),
                    max([sum(_.values()) for _ in countLeft.values()]))
        while count > 1:
            k, v = matrix.pop()
            i, j = v
            countRight[i][j] -= 1
            countLeft[j][i] -= 1
            count = max(max([max(_.values()) for _ in countRight.values()]),
                        max([max(_.values()) for _ in countLeft.values()]))

        mini = min(cleft, cright)
        if len(matrix) < mini:
            raise Exception("impossible: the smallest set should get all" +
                            "its element associated to at least one coming from the other set")

    def _private_string_path_matching(self, path, skipEdge=False):
        temp = []
        for p in path:
            u, v = p[2]
            if skipEdge and ((u is not None and u.is_edge()) or
                             (v is not None and v.is_edge())):
                continue
            su = "-" if u is None else str(u.nb)
            sv = "-" if v is None else str(v.nb)
            s = "(%s,%s)" % (su, sv)
            temp.append(s)
        return " ".join(temp)

    def distance_matching_graphs_paths(self, graph2,
                                       function_mach_vertices=None,
                                       function_match_edges=None,
                                       noClean=False,
                                       store=None,
                                       use_min=True,
                                       weight_vertex=1.,
                                       weight_edge=1.):
        """
        compute an alignment between two graphs
        @param      graph2                  the other graph
        @param      function_mach_vertices   function which gives a distance bewteen two vertices,
                                            if None, it take the output of @see me get_matching_functions
        @param      function_match_edges      function which gives a distance bewteen two edges,
                                            if None, it take the output of @see me get_matching_functions
        @param      noClean                 if True, clean unmatched vertices and edges
        @param      store                   if None, does nothing, if it is a dictionary, the function will store here various
                                            information about how th matching was operated
        @param      use_min                  @see me edit_distance_path
        @param      weight_vertex            a weight for every vertex
        @param      weight_edge              a weight for every edge
        @return                 2 tuple:
                                    - a distance
                                    - a graph containing the aligned paths between the two graphs

        See :ref:`l-graph_distance`.
        """

        function_mach_vertices, function_match_edges = \
            self.get_matching_functions(
                function_mach_vertices, function_match_edges, True)

        paths1 = list(self.enumerate_all_paths(True))
        paths2 = list(graph2.enumerate_all_paths(True))

        if store is not None:
            store["nbpath1"] = len(paths1)
            store["nbpath2"] = len(paths2)

        matrix_distance = {}
        for i1, p1 in enumerate(paths1):
            for i2, p2 in enumerate(paths2):
                matrix_distance[i1, i2] = self.edit_distance_path(p1, p2, self, graph2,
                                                                  function_mach_vertices, function_match_edges, use_min=use_min)

        if store is not None:
            store["matrix_distance"] = matrix_distance
        reduction = [(v[0], k) for k, v in matrix_distance.items()]
        if store is not None:
            store["path_mat1"] = copy.deepcopy(reduction)
        self.private_kruskal_matrix(reduction, False)
        if store is not None:
            store["path_mat2"] = copy.deepcopy(reduction)

        pair_count_edge = {}
        pair_count_vertex = {}
        for k, v in reduction:
            res, path = matrix_distance[v]
            for el in path:
                n1, n2 = el[2]
                if n1 is not None and n2 is not None:
                    if n1.is_edge() and n2.is_edge():
                        add = n1.nb, n2.nb
                        pair_count_edge[add] = pair_count_edge.get(add, 0) + 1
                    elif n1.is_vertex() and n2.is_vertex():
                        add = n1.nb, n2.nb
                        pair_count_vertex[
                            add] = pair_count_vertex.get(add, 0) + 1

        if store is not None:
            store["pair_count_vertex"] = pair_count_vertex
            store["pair_count_edge"] = pair_count_edge

        reduction_edge = [(v, k) for k, v in pair_count_edge.items()]
        if store is not None:
            store["edge_mat1"] = copy.copy(reduction_edge)
        self.private_kruskal_matrix(reduction_edge, True)
        if store is not None:
            store["edge_mat2"] = copy.copy(reduction_edge)

        reduction_vertex = [(v, k) for k, v in pair_count_vertex.items()]
        if store is not None:
            store["vertex_mat1"] = copy.copy(reduction_vertex)
        self.private_kruskal_matrix(reduction_vertex, True)
        if store is not None:
            store["vertex_mat2"] = copy.copy(reduction_vertex)

        count_edge_left, count_edge_right = self.private_count_left_right(
            reduction_edge)
        count_vertex_left, count_vertex_right = self.private_count_left_right(
            reduction_vertex)

        res_graph = GraphDistance([])
        doneVertex = {}
        done_edge = {}

        for k, v in self.vertices.items():
            newv = Vertex(v.nb, v.label, weight_vertex)
            res_graph.vertices[k] = newv
            if v.nb in count_vertex_right:
                ind = list(count_vertex_right[v.nb].keys())[0]
                newv.pair = (v, graph2.vertices[ind])
                doneVertex[ind] = newv
                if newv.pair[0].label != newv.pair[1].label:
                    newv.label = "%s|%s" % (
                        newv.pair[0].label, newv.pair[1].label)
            else:
                newv.pair = (v, None)

        for k, v in graph2.vertices.items():
            if k in doneVertex:
                continue
            newv = Vertex("2a.%s" % v.nb, v.label, weight_vertex)
            res_graph.vertices[newv.nb] = newv
            newv.pair = (None, v)

        for k, e in self.edges.items():
            newe = Edge(e.from_, e.to, e.label, weight_edge)
            res_graph.edges[k] = newe
            if e.nb in count_edge_right:
                ind = list(count_edge_right[e.nb].keys())[0]
                newe.pair = (e, graph2.edges[ind])
                done_edge[ind] = newe
            else:
                newe.pair = (e, None)

        for k, e in graph2.edges.items():
            if k in done_edge:
                continue
            from_ = list(count_vertex_left[e.from_].keys())[0] if e.from_ in count_vertex_left \
                else "2a.%s" % e.from_
            to = list(count_vertex_left[e.to].keys())[0] if e.to in count_vertex_left \
                else "2a.%s" % e.to
            if from_ not in res_graph.vertices:
                raise RuntimeError("should not happen " + from_)
            if to not in res_graph.vertices:
                raise RuntimeError("should not happen " + to)
            newe = Edge(from_, to, e.label, weight_edge)
            res_graph.edges[newe.nb] = newe
            newe.pair = (None, e)

        res_graph.compute_predecessor()
        res_graph.compute_successor()

        allPaths = list(res_graph.enumerate_all_paths(True))

        temp = [sum([0 if None in _.pair else 1 for _ in p]) * 1.0 / len(p)
                for p in allPaths]
        distance = 1.0 - 1.0 * sum(temp) / len(allPaths)

        return distance, res_graph

    def draw_vertices_edges(self):
        vertices = []
        edges = []
        for k, v in self.vertices.items():
            if v.pair == (None, None) or (v.pair[0] is not None and v.pair[1] is not None):
                vertices.append((k, v.label))
            elif v.pair[1] is None:
                vertices.append((k, "-" + v.label, "red"))
            elif v.pair[0] is None:
                vertices.append((k, "+" + v.label, "green"))
            else:
                raise Exception("?")

        for k, v in self.edges.items():
            if v.pair == (None, None) or (v.pair[0] is not None and v.pair[1] is not None):
                edges.append((v.from_, v.to, v.label))
            elif v.pair[1] is None:
                edges.append((v.from_, v.to, "-" + v.label, "red"))
            elif v.pair[0] is None:
                edges.append((v.from_, v.to, "+" + v.label, "green"))
            else:
                raise Exception("?")

        return vertices, edges
