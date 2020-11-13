import xlrd as xl
import os

dir0 = os.getcwd()
pf = os.path.join(dir0,'Data.xlsx')
pf1 = os.path.join(dir0,'Scripts')
pf0 = pf
    
# открыть ексель файл и взять первый лист
F = xl.open_workbook(pf)
FSht = F.sheet_by_index(0)

# количество строк в файле
N = FSht.nrows

# список локаций (L = Location) по их номерам 
Llist = list(set(FSht.col_values(0)[1::]))
Llist.remove('')
print('Локации: ', Llist)
Llist.sort()

# список номеров строк локаций и извлечение информации о них
LLocID = []
LLocInfo = []
for Loc in Llist:
    LocID = FSht.col_values(0).index(Loc)
    LocInfo = FSht.row_values(LocID)[0:4]
    LLocID.append(LocID)
    LLocInfo.append(LocInfo)
# + добавим в список кол-во строк как конец файла. 
LLocID.append(N)

for i in LLocInfo:
    i[0]=int(i[0])

# Формируем список с инфомрацией о квестах
LQInfo = []
LocQuests = []
for i in range(len(LLocID)-1):
#     Запишем файл с информацией о Локации
    LocatePart = ['LID', 'LName', 'LHello', 'LVar']
    S=''
    for ii in range(4):
        S+=LocatePart[ii]+'=['+str(LLocInfo[i][ii])+']\n'
    with open(os.path.join(pf1,'SL{}.qs'.format(i)),'w',
              encoding='utf-8') as SL:
        SL.write(S)
    
#     срез столбца с номерами квестов и их список
    Slise1 = FSht.col_values(4)[LLocID[i] : LLocID[i+1]]
    Slise = list(filter(lambda x: x!='', Slise1))
    
    for ii in range(len(Slise)):
#         запись информации о квесте в файл. 
#         (В эффектах пишется команда, которую можно вызвать, а Var словари)
        QIID = FSht.col_values(4).index(Slise[ii], LLocID[i])
        A=FSht.row_values(QIID)[4:9]
        A[0]=int(A[0])
        QuestPart = ['QID', 'QCheck', 'QText', 'QEffect', 'QVar']
        S=''
        for iii in range(5):
            S+=QuestPart[iii]+'=['+str(A[iii])+']\n'
        with open(os.path.join(pf1,'SL{}.qs'.format(i)),'a',
                  encoding='utf-8') as SL:
            SL.write('\\Quest\n'+S)
#         далее найдём индексы квестов, где искать варианты ответов
        Qind = FSht.col_values(4).index(Slise[ii],LLocID[i])
        if ii+1 == len(Slise):
            Qind2 = LLocID[i+1]
        else:
            Qind2 = FSht.col_values(4).index(Slise[ii+1],LLocID[i])
        
#         Запишем все варианты ответов на квест
        AnsList = []
        AnsCol = FSht.col_values(9)[Qind:Qind2]
        AnsCol = list(filter(lambda x: x!='', AnsCol))
        
        for iii in range(Qind2 - Qind): 
            AnID = FSht.col_values(9).index(AnsCol[iii], Qind)
            AnI=FSht.row_values(AnID)[9:13]
            
            AnsList.append(AnI)
            with open(os.path.join(pf1,'SL{}.qs'.format(i)),'a',
                      encoding='utf-8') as SL:
                SL.write('\\qa ['+str(int(AnI[0]))+'] \t'+
                         'qatext=['+str(AnI[1])+']\n'+
                         'qacheck=['+str(AnI[2])+'] \t'+
                         'qn=['+str(AnI[3])+']\n')
        
        LQInfo.append([A, AnsList.copy()])
    LocQuests.append(LQInfo.copy())
    LQInfo = []
