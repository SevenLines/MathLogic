# coding=utf-8
import random
import string


def gen_task2(s1, s2, s3, s4, s5):
    assert s2[0] == s5[0]
    assert len(set(s1 + s2 + s3 + s4 + s5)) == len(s1 + s2 + s3 + s4 + s5) - 1
    word1 = s1 + s2 + s3
    word2 = s4 + s2
    word3 = s4 + s5
    # print "your words: {}-{}-{}".format(word1, word2, word3)

    x = random.sample(filter(lambda x: x not in word1 + word2 + word3, string.ascii_lowercase), 3)
    alpha = []
    beta = []
    for i in xrange(len(word2) / 2):
        el = random.choice(x)
        if i == 1:
            beta.append((el, s5[1]))
        a = (word2[2 * i], el)
        b = (el, word2[2 * i + 1])
        alpha.append(a)
        beta.append(b)

    for i in xrange(len(word1) / 2):
        if i == 1:
            continue
        el = random.choice(x)
        a = (el, word1[2 * i + 1])
        b = (word1[2 * i], el)
        alpha.append(a)
        beta.append(b)

    gamma = [
        (word3[0], word3[1]),
        (word3[2], word3[3]),
    ]

    random.shuffle(alpha)
    random.shuffle(beta)
    random.shuffle(gamma)

    out = r"$$\begin{{array}}{{l}} " \
          r"\alpha=\{{ {alpha} \}} \\ " \
          r"\beta=\{{ {beta} \}} \\ " \
          r"\gamma=\{{ {gamma} \}} " \
          r"\end{{array}}$$".format(**{
        'alpha': ", ".join(['(%s, %s)' % a for a in alpha]),
        'beta': ", ".join(['(%s, %s)' % a for a in beta]),
        'gamma': ", ".join(['(%s, %s)' % a for a in gamma]),
    })

    return out


task1 = {
    'description': r"Доказать, если $A\,\dot{-}\,B=(A\setminus B)\cup(B\setminus A)$: \\",
    'variants': [
        r"$$A\,\dot{-}\,U=A'$$",
        r"$$A\setminus B = A\,\dot{-}\,(A\cap B)$$",
        r"$$A\,\dot{-}\,\emptyset=A$$",
        r"$$A\setminus B = A\,\dot{-}\,(A\cap B)$$",
    ]
}

task2 = {
    'description': r"Построить отношение $(\alpha\cdot\beta\cup\beta\cdot\alpha)\setminus\gamma$",
    'variants': [
        gen_task2("su", "nd", "ay", "wi", "ne"),
        gen_task2("ge", "ni", "us", "ma", "ny"),
        gen_task2("mo", "nd", "ay", "li", "ne"),
        gen_task2("si", "ng", "le", "ra", "nk"),
    ]
}

task3 = {
    'description': "Привести к предваренной нормальной форме: \\",
    'variants': [
    ]
}


# проверить утверждение
task4 = {
    'description': "Проанализируйте рассуждение: \\",
    'variants': [
        "Все хирурги -- врачи. Некоторые врачи -- герои России. "
        "Следовательно, некоторые хирурги -- Герои России",

        "Всякий метал является твердым веществом. Ртуть не твердое вещество. "
        "Следовательно, ртуть не металл.",

        "Все студенты ИГУ -- жители Иркутской области. Некоторые жители Иркутской области -- пенсионеры. "
        "Следовательно, некоторые студенты ИГУ -- пенсионеры",

        "Все бегуны -- спортсмены. Ни один спортсмен не курит. "
        "Следовательно, ни один курящий не является бегуном",
    ]
}

quantifiers = ['\\forall', '\\exists']

params = [
    'lov',
    'mad',
    'far',
    'git',
]

predicats = [
    'RED',
    'WEB',
    'LSD',
    'CAT',
]

template = r"$${q0} {p0}{l0}({p0},{p1}) \to \neg {q1} {p1}( {l1}({p1},{p0}) " \
           r"\wedge {q2} {p0}{q3} {p2} {l2}({p2}, {p0}))$$"

random.seed(78)
for (param, predicat) in zip(params, predicats):
    quantifier = [random.choice(quantifiers) for _ in xrange(4)]
    task = template.format(**{
        'q0': quantifier[0],
        'q1': quantifier[1],
        'q2': quantifier[2],
        'q3': quantifier[3],
        'p0': param[0],
        'p1': param[1],
        'p2': param[2],
        'l0': predicat[0],
        'l1': predicat[1],
        'l2': predicat[2],
    })
    task3['variants'].append(task)

for i, t in enumerate(zip(task1['variants'], task2['variants'], task3['variants'], task4['variants']), 1):
    print r"Вариант %s" % i
    print r"\begin{enumerate}"
    print r"\item %s" % task1['description']
    print t[0]
    print r"\item %s:" % task2['description']
    print t[1]
    print r"\item %s:\\" % task3['description']
    print t[2]
    print r"\item %s:\\" % task4['description']
    print t[3]
    print r"\end{enumerate}"




