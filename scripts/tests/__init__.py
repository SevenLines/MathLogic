# coding=utf-8
from StringIO import StringIO


class Task:
    def __init__(self):
        pass

    title = ""

    @classmethod
    def items(cls):
        return []


class Test:
    def __init__(self):
        pass

    @staticmethod
    def gen(*tasks):
        s = StringIO()
        for i, p in enumerate(zip(*[t.items() for t in tasks]), 1):
            print >> s, "Вариант %s" % i
            print >> s, r"\begin{enumerate}"
            for k, t in enumerate(tasks):
                print >> s, r"\item %s" % t.title
                print >> s, r"%s" % p[k]
            print >> s, r"\end{enumerate}"
        return s.getvalue()