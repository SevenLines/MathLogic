# coding=utf-8
from tests import Task


class TaskOne(Task):
    title = "Доказать/опровергнуть выполнимость формул, не строя таблиц истинности"

    @classmethod
    def items(cls):
        wrds = [
            "NP",
            "AB",
            "HE",
            "MY",
            "MK",
        ]
        out = []

        for i, (w1, w2) in enumerate(zip(wrds, wrds[::-1]), 1):
            # четный вариант
            p1 = r"\neg({A}\to {B})"
            p2 = r"({B}\vee(\neg {B}\vee({A}\vee({A}\to {B})))"
            if i % 2:
                p1, p2 = p2, p1
            out.append(
                r'$${0}\&{1}$$'.format(p1, p2).format(A=w1[0], B=w1[1])
            )

            # нечетный вариант
            p1 = r"\neg({P})"
            p2 = r"\neg(((({P}\to {Q})\to {Q})\to {Q})\to {Q})"
            if i % 2:
                p1, p2 = p2, p1
            out.append(
                r'$${0}\&{1}$$'.format(p1, p2).format(P=w2[0], Q=w2[1])
            )
        return out


class TaskTwo(Task):
    title = "Доказать/опровергнуть что следующие формулы являются тавтологиями, не строя таблиц истинности"

    @classmethod
    def items(cls):
        out = []
        wrds = [
            "LIFE",
            "CAVE",
            "GIFT",
            "SING",
            "GIRL",
            "SURF",
            "FIRE"
        ]
        for i, (w1, w2) in enumerate(zip(wrds, wrds[::-1])):
            p = r"$$(({P}\to {Q})\&({R}\to {S}))\to(({P}\& {R})\to({Q}\&{S}))$$"
            out.append(p.format(P=w1[0], Q=w1[1], R=w1[2], S=w1[3]))
            p = r"$$(({P}\to {Q})\&(\neg {R}\to {S})\&\neg({Q}\vee {S}))\to\neg({P}\& {R})$$"
            out.append(p.format(P=w2[0], Q=w2[1], R=w2[2], S=w2[3]))
        return out


class TaskThree(Task):
    title = "Доказать/опровергнуть логическое следование"

    @classmethod
    def items(cls):
        out = []
        wrds = [
            "CLAUD",
            "DREAM",
            "FLASH",
            "PLANT",
            "BRUSH",
            "LIGHT"
            "WATER"
        ]
        for i, w in enumerate(wrds):
            p1 = r"{F}\to({G}\to {H})"
            p2 = r"({H}\& {K})\to {L}"
            p3 = r"{M}\to({K}\&\neg {L})"
            p4 = r"{F}\to ({G}\to {M})"
            pi = [p1, p2, p3, p4]
            p = r"\begin{{equation*}}\begin{{split}}%" \
                r"s,\;& %s,\; \\& %s\;\models\; %s" \
                r"\end{{split}}\end{{equation*}}" \
                % (pi[i % 4], pi[(i + 1) % 4], pi[(i + 2) % 4], pi[(i + 3) % 4])
            out.append(p.format(F=w[0], H=w[1], G=w[2], K=w[3], L=w[4], M="M"))
        return out


class TaskFour(Task):
    title = "Найти КНФ(или ДНФ) и достроить до СКНФ(или СДНФ), " \
            "в дополнение найти СКНФ(СДНФ) с помощью таблицы истинности " \
            "и сравнить с полученной с помощью достройки"

    @classmethod
    def items(cls):
        wrds = [
            "SUN",
            "CAT",
            "YES",
            "AIR",
        ]
        out = []
        for w1, w2 in zip(wrds, wrds[::-1]):
            p = r"$$({B}\& {C})\equiv(\neg {A} \vee {B})$$"
            out.append(p.format(A=w1[2], B=w1[0], C=w1[1]))

            p = r"$$(({A}\to {B})\to({B}\& {C}))\wedge(({B}\to {C})\to({A}\to {B}))$$"
            out.append(p.format(A=w1[2], B=w1[0], C=w1[1]))
        return out


