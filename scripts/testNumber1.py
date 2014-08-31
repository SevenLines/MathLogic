#coding: utf-8
# Программа генерирует Latex файл,  
# с первой контрольной.
# третей с конца строке в документе
# заменить   \line(1,0){250}\vfill\columnbreak
# на         \line(1,0){250}\vfill
# а то верстка поплывет


import random
import itertools
import collections
import string

# сид для генератора случайных чисел
seed = 777
# кол-во вариантов
tasksCount = 42
# кол-во вариантов в одном столбике Latex документа
tasksPerColumn =3 

# проверка на пренадлежность списку списков
def isContain(elem, st):
    for lst in st:
        if elem in lst:
            return 1
    return 0

# кол-во элементов в списке списков
def Length(st):
    return len(sum(st,[]))

# произведение отношений
def RelationsMul(rel1, rel2):
    out = []
    for el in rel1:
        for el2 in rel2:
            if el[1] == el2[0]:
                if (el[0], el2[1]) not in out:
                    out.append((el[0], el2[1]))
    return out

# задачи на построение фактор множества
def FactorSetsTask():
    '''
    Возвращает список туплов (задача, ответ)
    '''
    global seed
    
    out = []
    sets = [];
    
    n = 5
    maxElementValue = 77
    setLength = 7
    
    random.seed(seed)
    
    for i in range(1,tasksCount+1):
        sets.clear()
         
        for _ in range(0,n) :
            sets.append([])
       
        while( Length(sets) != setLength ):
            rnd = random.randrange(maxElementValue)
            rest = rnd % n
            if not isContain(rnd, sets):
                if len(sets[rest]) < 3:
                    sets[rest].append(rnd)
        lstOfValues = sum(sets, []) 
        lstOfValues.sort()
        
        sets = [el for el in sets if len(el) > 0]
        
        strTask  = ''.join([ 'A = \{ ', ', '.join(map(str, lstOfValues)), ' \}'])
        #print(strTask)
        
        strAnswer = '\n'.join( map(lambda x: '\{'+', '.join(map(str, x)) + '\}', sets) )
        #print(strAnswer)
        
        out.append( (strTask, strAnswer) )
    return out

# задача на построение отношений
# типа alpha*beta / gamma
def RelationsTask():
    '''
    Возвращает тупл (A, alpha, beta, gamma, answer)
    где alpha, beta, gamma - список пар
    answer - одна единственная пара-ответ
    '''
    global seed
    
    out = []
    out2 = []
    
    setLength = 5
    bLength = 6
    
    A = list(range(1,setLength + 1))
    AxA = list(itertools.product(A, A))
    
    random.seed(seed)
    
    # формируем отношение beta, у всех одинаковое
    beta = []
    while len(beta) < bLength:
        rnd = random.choice( AxA )
        if rnd not in beta:
            beta.append(rnd)
    # вывод на экран beta
    s = ' '.join( map ( str,  beta) )
    print(s)
    
    Alphas = []
    alpha = []
    # формируем alpha
    for _ in range(1,tasksCount+1):
        while True:
            alpha.clear()
            while len(RelationsMul(alpha, beta)) < 3:
                rnd = random.choice( AxA )
                if rnd not in alpha:
                    alpha.append(rnd)
            if len(alpha) < 5 and len(alpha) > 3:
                break
        alpha.sort()
        s = ' '.join( map ( str,  alpha) )
        gamma = RelationsMul(alpha, beta)
        indexToRemove = random.randrange( len(gamma) )
        answer = gamma[indexToRemove]
        gamma.pop(indexToRemove)
        out.append( (A, alpha[:], beta, gamma[:], answer) )
    
    for item in out:
        sTask = ''.join( ['$\{ ',
                      ', '.join( map(str, item[0]) ),
                      ' \}$, где\n$$\\begin{array}{l}\n',
                      '\\alpha = \{ ',
                      ', '.join( map(str, item[1]) ),
                      ' \} \\\\ \n',
                      '\\beta = \{ ',
                      ', '.join( map(str, item[2]) ),
                      ' \} \\\\ \n',
                      '\\gamma = \{ ',
                      ', '.join( map(str, item[3]) ),
                      ' \}\n\\end{array}$$',
                       ])
        sAnswer = str( item[4] )
        out2.append( (sTask, sAnswer) )
    
    return out2
    
def SetsTask():
    task1 = '{0} \\cap ({1} \\setminus {2}) \\text{3} ( {0} \\cap {1} ) \\setminus ( {0} \\cap {2} )'
    task2 = '( {0} \\cap {1} ) \\setminus {2} \\text{3} ( {0} \\cap {1} ) \\setminus ( {0} \\cap {2} )'
    task = [task1, task2]
    
    # вместо просто ABC куда веселее использовать слова
    words = ['red', 'how',
             'one', 'car',
             'two', 'nap',
             'kid', 'man',
             'nya', 'can',
             'nom', 'you',
             'let', 'buy',
             'lov', 'yuk',
             'boy', 'his',
             'gym', 'cap',
             'air', 'sun',
             'ink', 'rat',
             'pal', 'owl',
             'cat', 'way',
             'dog', 'use',
             'key', 'new',
             'she', 'raw',
             'old', 'mad',
             'sea', 'kit',
             'day', 'log',
             'who', 'jet',
              ]
    words = list(w.upper() for w in words)
    
    out = []
    
    random.seed(seed)
    
    for i in range(1,tasksCount+1):
        letters = words[i % len(words)]
        out.append(task[i % len(task)].format(letters[0], letters[1], letters[2], '{ и }'))
        
    return out
    
    
if __name__ == '__main__':
   
    factorTasks = FactorSetsTask()
    relationsTasks = RelationsTask()
    setsTasks = SetsTask()
    
    fileTasks = open("tasks.txt", 'w');
    # заголовок латех файла 
    s = '\n'.join(['\documentclass[9pt,a4paper]{article}',
        '\\usepackage[cp1251]{inputenc}',
        '\\usepackage{amsmath}',
        '\\usepackage{amsfonts}',
        '\\usepackage{amssymb}',
        '\\usepackage{multicol}',
        '\\usepackage[russian]{babel}',
        '\\usepackage[left=1.00cm, right=1.00cm, top=1.00cm, bottom=1.00cm]{geometry}',
        '',
        '\setlength{\columnsep}{20mm}',
        '\setlength{\columnseprule}{0.1pt}',
        '\setlength\parindent{0pt}',
        '\pagestyle{empty}',
        '',
        '\\begin{document}',
        '\\begin{multicols}{2}',])
    fileTasks.write(s);
    
    for i in range( len(factorTasks) ):
        s = '\n'.join(  [ '\line(1,0){250}'+ '\\\\\\\\',
                          'Вариант №'+ str(i+1) + '\\\\\\\\',
                          '1. Доказать эквивалентность (графическим и формальным способами):',
                          '$$' + setsTasks[i] + '$$',
                          '2. Построить отношение $(\\alpha\\cdot\\beta) \setminus \\gamma$ на множестве',
                          relationsTasks[i][0],
                          '3. Построить фактор-множество множества\n$$'+ factorTasks[i][0]+'$$',
                          'по отношению $a = b mod 5$',
                          '\n'] )
        if  (i+1) % tasksPerColumn == 0:
            s = s + '\\line(1,0){250}\\vfill\\columnbreak\n\n'
        fileTasks.write(s)
        #print(s)
    # футер латех файла
    fileTasks.write('\end{multicols}\n\end{document}')
    
    fileTasks.close()
        
        