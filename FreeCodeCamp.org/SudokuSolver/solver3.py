import sys
from itertools import product

xval = list(map(str, range(1, 10)))
c_debug = False


def clean(s):
    return (repr(s).replace(" ", "").replace("'", "") + " " * 19)[:19]


class Group:
    def __init__(self, game, key, xcell):
        self.game = game
        self.key = key
        self.type, *_ = key
        self.xcell = xcell
        # print(key, *self.dposs.items(), sep="\n", file=sys.stderr)
        self.recompute()

    def __repr__(self):
        return repr(self.key).replace(" ", "")

    def recompute(self):
        self.dposs = {}
        self.dmust = {}
        for v in xval:
            xm = [c for c in self.xcell if v == c.must]
            xm = None if xm == [] else xm[0]
            xp = [xm] if xm != None else [c for c in self.xcell if v in c.poss]
            self.dposs[v] = xp
            self.dmust[v] = xm

    def solve(self, debug=None):
        if debug == None:
            t_debug = c_debug
        else:
            t_debug = c_debug or debug
        mod = False
        self.recompute()
        for v, xc in self.dposs.items():
            res = any([c.remove(v) for c in self.xcell if not c in xc])
            mod |= res
            if t_debug and res: print(v, xc, [c for c in self.xcell if not c in xc], file=sys.stderr)
            if len(xc) == 0:
                assert False, (self.key, v, xc)
            if len(xc) == 1:
                res = any([c.set(v) for c in xc if v in c.poss])
                if t_debug and res: print(self.key, "one option:", v, xc, file=sys.stderr)
                mod |= res
            else:
                xx = set([c.gx for c in xc])
                xy = set([c.gy for c in xc])
                xs = set([c.gs for c in xc])
                if len(xx) == 1 and self.type != "X":
                    gv = [c for c in list(xx)[0].dposs[v] if not c in xc]
                    old = repr(self.game)
                    res = any([c.remove(v) for c in gv])
                    if res and t_debug:
                        print(self.key, "Impact on ", xx, "for value", v, file=sys.stderr)
                        print("== OLD==", file=sys.stderr)
                        print(old, file=sys.stderr)
                        print("== NEW ==", file=sys.stderr)
                        print(self.game, file=sys.stderr)
                    mod |= res
                if len(xy) == 1 and self.type != "Y":
                    gv = [c for c in list(xy)[0].dposs[v] if not c in xc]
                    old = repr(self.game)
                    res = any([c.remove(v) for c in gv])
                    if res and t_debug:
                        print(self.key, "Impact on ", xy, "for value", v, file=sys.stderr)
                        print("== OLD==", file=sys.stderr)
                        print(old, file=sys.stderr)
                        print("== NEW ==", file=sys.stderr)
                        print(self.game, file=sys.stderr)

                    mod |= res
                if len(xs) == 1 and self.type != "S":
                    gv = [c for c in list(xs)[0].dposs[v] if not c in xc]
                    old = repr(self.game)
                    res = any([c.remove(v) for c in gv])
                    if res and t_debug:
                        print(self.key, "Impact on ", xs, "for value", v, file=sys.stderr)
                        print("== OLD==", file=sys.stderr)
                        print(old, file=sys.stderr)
                        print("== NEW ==", file=sys.stderr)
                        print(self.game, file=sys.stderr)

                    mod |= res
                # print(self.key, xx,xy,xs,file=sys.stderr)

        if mod: return mod
        return False


class Cell:
    def __init__(self, game, key, value):
        self.game = game
        self.key = key
        self.x, self.y = key
        if value in "0-":
            self.poss = set(xval)
            self.must = None
        else:
            self.poss = set([value])
            self.must = value
        self.bruteforce_hypo = None
        self.gx = self.gy = self.gs = None

    def solution(self):
        return str(self.must) if self.must is not None else "-"

    def __repr__(self):
        return repr(self.key).replace(" ", "") + ":" + str(self).rstrip()

    def __str__(self):
        if self.must is None:
            return clean(self.poss)
        else:
            return clean(self.must)

    def solve(self, debug=False):
        if debug is None:
            t_debug = c_debug
        else:
            t_debug = c_debug or debug

        if self.must is not None: return False
        if len(self.poss) == 1:
            self.must = list(self.poss)[0]
            if t_debug: print("Cell solve:", self.key, self.must, file=sys.stderr)
            x, y = self.key
            for g in [self.gx, self.gy, self.gs]: g.solve(debug=True)
            return True
        return False

    def set(self, v):
        if self.must is None:
            assert v in self.poss, (self, v, self.poss, self.must)
            self.poss = {v}
            self.must = v
            return True
        else:
            assert v == self.must
            return False

    def remove(self, v):
        if v in self.poss:
            self.poss.discard(v)
            return True
        else:
            return False


class Game:
    def __init__(self, grid, hypo=None, title=None):
        self.dcell = {}
        for y, line in enumerate(grid.split("\n")):
            line = (line + " " * 9)[:9]
            for x, v in enumerate(line):
                self.dcell[x, y] = Cell(self, (x, y), v)

    def solution(self):
        return "\n".join(["".join([self.dcell[x, y].solution() for x in range(9)]) for y in range(9)])

    def __repr__(self):
        res = [" ".join([clean("(-)")] + [clean("(%i)" % i) for i in range(9)])]
        for y in range(9):
            res.append(" ".join([clean("(%i)" % y)] + [str(self.dcell[x, y]) for x in range(9)]))
        return "\n".join(res)

    def solve(self):
        self.dgroup = {}
        for y in range(9):
            self.dgroup["Y", y] = g = Group(self, ("Y", y), [self.dcell[x, y] for x in range(9)])
            for c in g.xcell: c.gy = g
        for x in range(9):
            self.dgroup["X", x] = g = Group(self, ("X", x), [self.dcell[x, y] for y in range(9)])
            for c in g.xcell: c.gx = g
        for (x1, y1) in product(range(3), repeat=2):
            self.dgroup["S", x1 * 3, y1 * 3] = g = Group(self, ("S", x1 * 3, y1 * 3),
                                                         [self.dcell[x0 + x1 * 3, y0 + y1 * 3] for (x0, y0) in
                                                          product(range(3), repeat=2)])
            for c in g.xcell: c.gs = g
        cont = True
        loop = 0
        while cont:
            if False:
                print("\n", file=sys.stderr)
                print(self, file=sys.stderr)
            cont = False
            loop += 1
            cont |= any([c.solve() for c in self.dcell.values()])
            cont |= any([g.solve() for g in self.dgroup.values()])
            if False: print(cont, loop, file=sys.stderr)
        if any(c.must == None for c in self.dcell.values()):
            self.solve_bruteforce()

    def solve_bruteforce(self):
        for c in self.dcell.values(): c.bruteforce_hypo = c.must
        xqueue = sorted([c for c in self.dcell.values() if c.bruteforce_hypo == None], key=lambda c: (c.y, c.x))
        if self.solve_bruteforce_queue(xqueue):
            for c in self.dcell.values():
                if c.must is None:
                    c.set(c.bruteforce_hypo)

    def solve_bruteforce_queue(self, xqueue):
        if not xqueue: return True
        cell, *xqueue1 = xqueue
        xvalue = set(cell.poss)
        for gi in [cell.gx, cell.gy, cell.gs]:
            xvalue = xvalue - set([c.bruteforce_hypo for c in gi.xcell])
        # if not xvalue: return False #No option!
        for value in xvalue:
            cell.bruteforce_hypo = value
            if self.solve_bruteforce_queue(xqueue1): return True
        cell.bruteforce_hypo = None
        return False


grid = "\n".join([input() for _ in range(9)])
print(grid.replace("0", "-"), file=sys.stderr)
g = Game(grid)
g.solve()
print(g, file=sys.stderr)
print(g.solution())
