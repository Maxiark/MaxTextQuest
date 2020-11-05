from xlrd import *
import xlwt

# открыть ексель файл и взять первый лист
F = open_workbook('Data.xlsx')
FSht = F.sheet_by_index(0)

# количество строк в файле
N = FSht.nrows

# список локаций (L = Location) по их номерам 
Llist = list(set(FSht.col_values(0)[1::]))
Llist.remove('')
print('Локации: ', Llist)
Llist.sort()

# список номеров строк локаций и извлечение информации о них (LocInfo), LLocInfo = List of LocInfo
LLocID = []
LLocInfo = []
for Loc in Llist:
    LocID = FSht.col_values(0).index(Loc)
    LocInfo = FSht.row_values(LocID)[0:4]
    LLocID.append(LocID)
    LLocInfo.append(LocInfo)
# + добавим в список кол-во строк как конец файла. 
LLocID.append(N)

# Формируем список с инфомрацией о квестах
LQInfo = []
LocQuests = []
for i in range(len(LLocID)-1):
#     Запишем файл с информацией о Локации
    with open('Scripts/SL{}.qs'.format(i),'w', encoding='utf-8') as SL:
        SL.write('LID={'+str(int(LLocInfo[i][0]))+'}\n'+
                 'LName={'+str(LLocInfo[i][1])+'}\n'+
                 'LHello={'+str(LLocInfo[i][2])+'}\n'+
                 'LVar={'+str(LLocInfo[i][3])+'}\n')
    
#     срез столбца с номерами квестов и их список
    Slise1 = FSht.col_values(4)[LLocID[i] : LLocID[i+1]]
    Slise = list(filter(lambda x: x!='', Slise1))
    
    for ii in range(len(Slise)):
#         запись информации о квесте в файл. Для удобства всё записываеться с [] или {}
#         (В эффектах пишется команда, которую можно вызвать, а Var словари)
        QIID = FSht.col_values(4).index(ii, LLocID[i])
        A=FSht.row_values(QIID)[4:9]
        with open('Scripts/SL{}.qs'.format(i),'a', encoding='utf-8') as SL:
            SL.write('\\Quest\n'+
                     'QID={'+str(int(A[0]))+'}\n'+
                     'QCheck={'+str(A[1])+'}\n'+
                     'QText={'+str(A[2])+'}\n'+
                     'QEffect=['+str(A[3])+']\n'+
                     'QVar={'+str(A[4])+'}\n')
#         далее найдём индексы квестов, чтобы понять где искать варианты ответов
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
            with open('Scripts/SL{}.qs'.format(i),'a', encoding='utf-8') as SL:
                SL.write('\\qa {'+str(int(AnI[0]))+'} \t'+
                         'qatext={'+str(AnI[1])+'}\n'+
                         'qacheck=['+str(AnI[2])+'] \t'+
                         'qn={'+str(AnI[3])+'}\n')
        
        LQInfo.append([A, AnsList.copy()])
    LocQuests.append(LQInfo.copy())
    LQInfo = []    
    
