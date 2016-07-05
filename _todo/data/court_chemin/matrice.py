import os
import codecs


def get_distance():
    li = os.listdir("memory")
    d = {}

    for i, l in enumerate(li):
        if i % 1000 == 0 and i > 100:
            print i, len(li), l
            # break
        spl = l.split("_")
        if len(spl) <= 2:
            continue
        v1 = spl[2]
        v2 = spl[3].split(".")[0]

        f = codecs.open("memory\\" + l, "r", "utf8")
        r = f.read()
        f.close()

        temp = eval(r)
        x = temp["Directions"]["Distance"]["meters"]
        d[v1, v2] = x
        d[v2, v1] = x
    return d


def refine_matrix(mat, th=250000, thr=0.9):
    keys = [_[0] for _ in mat.keys()]
    maxi = max(mat.values()) * 2
    rem = {}
    for i, k in enumerate(keys):
        if i % 100 == 0:
            print i, len(rem), len(keys)
        for k2 in keys:
            x = mat.get((k, k2), maxi)
            if maxi > x > th:
                rem[k, k2] = 0
                rem[k2, k] = 0
    res = {}
    for k, v in mat.iteritems():
        if k not in rem:
            res[k] = v
    return res


def save_matrix(mat, file="matrix_distance.txt"):
    f = open(file, "w")
    for k, v in mat.iteritems():
        f.write("%s\t%s\t%d\n" % (k[0], k[1], v))
    f.close()


if __name__ == "__main__":
    d = get_distance()
    print len(d)
    d = refine_matrix(d)
    print len(d)
    save_matrix(d)
