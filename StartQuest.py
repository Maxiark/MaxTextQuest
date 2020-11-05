
try:
    from tkinter import *
    from tkinter.ttk import *
    import os

    ROOT=Tk()
    ROOTH=800  # ширина и высота окна ТКинтер
    ROOTW=600
    s=Style()
    s.theme_use('clam')
    log_e=open('log.txt','w')
    
    def StrCut(text, lenght):   # Вывод текста с переносом строк (длина строки - lenght). Абзацы вставляюся вместо пробелов
        if len(text) <= lenght:
            res = text
        else:
            n = len(text)//lenght
            
            res=''
            for i in range(n+1):
                si = 0
                si2 = 0
                while si < lenght and si>-1:
                    si2 = si
                    si = text.find(' ',si+1)
                res += text[:si2]+'\n'
                text = text[si2:]
            res = res[:-1]
            res += ' '+text
        return res
    
    class MyWindow:   # основное графическое окно TKinter. 
        def __init__(self,root):
            self.root=root
            self.root.columnconfigure(0,weight=1)
            self.root.rowconfigure(0,weight=1)
            self.root.config(bg='darkblue')
            self.message='message!' 
            
            self.contentFrame = Frame(self.root)
            s.configure("G.TFrame", foreground="black", background="green",relief ='sunken')
            self.contentFrame.config(style='G.TFrame')
            self.contentFrame.grid(row=0, column=0, sticky='nsew')
            self.contentFrame.columnconfigure(0, weight=1)
            self.contentFrame.rowconfigure(0,weight=0)
            self.contentFrame.rowconfigure(1,weight=0)
            self.contentFrame.rowconfigure(2,weight=1)
            self.contentFrame.propagate(0)
            
            # Вверхний блок для консоли. Скрыт по умолчанию. 
            self.topBar = Frame(self.contentFrame, border=2, relief='ridge')
            self.topBar.grid(row=0, column=0, columnspan=1,sticky='we')
            s.configure('D.TFrame',background='black')
            self.topBar.config(style='D.TFrame')
            self.topBar.columnconfigure(0, weight=1)
            
            # Блок с названием программы
            self.NameBar = Frame(self.contentFrame, border=2, relief='ridge')
            self.NameBar.grid(row=1, column=0, columnspan=1,sticky='we')
            s.configure('NameBar.TFrame',background='blue')
            self.NameBar.config(style='NameBar.TFrame')
            self.NameBar.columnconfigure(0, weight=1)
            
            self.NameLab = Label(self.NameBar,text='The Text Game. \t\t Ver: 0.1 \t\t Author: Maxiark', font=('Arial 12'), background='blue', foreground='white')
            self.NameLab.grid(row=0,column=0, padx=10, ipady=0, pady=5)
            
            self.botBar = Frame(self.contentFrame, border=1, relief='ridge',style='D.TFrame')
            self.botBar.grid(row=2,column=0,columnspan=1,sticky='nwes')
            self.botBar.columnconfigure(0,weight=1)
            self.botBar.columnconfigure(1,weight=10)
            self.botBar.rowconfigure(0,weight=1)
            
            self.LabTop = Label(self.topBar,text='Head')
            self.LabTop.grid(row=0,column=0)
            
            # левый блок для меню
            self.leftF = Frame(self.botBar, width=200)
            s.configure('leftF.TFrame',background='navy',relief='groove',width=200)
            s.configure('leftF2.TFrame',background='slateblue',relief='groove')
            self.leftF.config(style='leftF.TFrame')
            self.leftF.columnconfigure(0,weight=1)
            self.leftF.rowconfigure(0,weight=0)
            
            # основной блок для игры
            self.centerF = Frame(self.botBar)
            s.configure('centerF.TFrame',background='red4',relief='groove')
            self.centerF.config(style='centerF.TFrame')
            self.centerF.columnconfigure(0,weight=1)
            self.centerF.rowconfigure(0,weight=0)
        
            
            self.centerF.grid(row=0,column=1,sticky='nsew')
            self.leftF.grid(row=0,column=0,sticky='nswe')
            
            
            self.LabelLeft = Label(self.leftF,text='Меню')
            self.LabelLeft.grid(row=0,column=0)
            
            self.LabelCenter = Label (self.centerF,text='Игра')
            self.LabelCenter.grid(row=0,column=0)
            
            
        def CMDC(self):  # выполнение команд из строки консоли
            self.CMD_L=Label(self.topBar, text='comand console:')
            self.CMD_L.grid()
            
            self.CMD = Entry(self.topBar,width=40)
            self.CMD.grid()
            
            self.CMD_B = Button(self.topBar, text='Run command',command=self.EvalF)
            self.CMD_B.grid()
            
            self.CMD_EL = Label(self.topBar, text='no error')
            s.configure('CMDLE.TLabel',background='yellow')
            self.CMD_EL.config(style='CMDLE.TLabel')
            self.CMD_EL.grid()
            
            self.CMD_hide = Button(self.topBar, text='Hide Console',command=lambda: self.HideTop())
            self.CMD_hide.grid()
        
        def HideTop(self): # скрытие консоли
            self.topBar.grid_remove()
            
        def EvalF(self):  # выполнение команд из строки консоли
            log_e.write(self.CMD.get()+'\n')
            try:
                eval(self.CMD.get())
            except Exception as e:
                print(e)
                self.CMD_EL.config(text=e)
                log_e.write('error: '+str(e))
            else:
                self.CMD_EL.config(text='no error')




    class DataEnt:  # Основные элементы управления для TKinter. 
        def __init__(self,root,root2,PlayerIn):
            self.P = PlayerIn  # ссылка на игрока (если потом захочется сделать несколько пользователей)
            
            self.Curent_Locate = LL[1]  # Текущая локация (комната)
            self.Curent_Quest = self.Curent_Locate.Quests_list[0]   # Текущий квест в локации
            
            self.root=root
            self.root2=root2
            
#             фрейм состояния (Здоровье и Инвентарь)
            self.StFr=Frame(self.root2)
            s.configure('StFr.TFrame',relief='groove', background='navy')
            self.StFr.config(style='StFr.TFrame')
            self.StFr.columnconfigure(0,weight=1)
            self.StFr.grid(row=0,sticky='WE',padx=5,ipady=1,pady=1)
            
            self.StatLabel = Label(self.StFr,text='Состояние персонажа:', font=('Arial 12 bold'), foreground='white', background='navy')
            self.StatLabel.grid(row=0,column=0,pady=5)
            
            self.StatusFr=Frame(self.StFr)
            s.configure('StatusFr.TFrame', relief='groove', background='cyan4')
            self.StatusFr.config(style='StatusFr.TFrame')
            self.StatusFr.columnconfigure(0,weight=1)
            self.StatusFr.grid(row=1,sticky='WE',padx=10,ipady=0,pady=5)
            
            self.StatusFr1=Frame(self.StatusFr)
            s.configure('StatusFr1.TFrame', relief='groove', background='RoyalBlue2')
            self.StatusFr1.columnconfigure(0,weight=0)
            self.StatusFr1.columnconfigure(1,weight=1)
            self.StatusFr1.columnconfigure(2,weight=2)
            self.StatusFr1.config(style='StatusFr1.TFrame')
            self.StatusFr1.grid(row=0,sticky='WEN',padx=2, pady=2)
            
            self.StatusFr2=Frame(self.StatusFr)
            s.configure('StatusFr2.TFrame', relief='groove', background='gold')
            self.StatusFr2.config(style='StatusFr2.TFrame')
            self.StatusFr2.columnconfigure(0,weight=0)
            self.StatusFr2.columnconfigure(1,weight=2)
            self.StatusFr2.grid(row=1,sticky='WES',padx=2, pady=2)

#             Полоса здоровья
            s.configure("red.Horizontal.TProgressbar", foreground='green', background='red')
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            self.NPB=Progressbar(self.StatusFr1,style="green.Horizontal.TProgressbar",orient='horizontal',length=100,mode='determinate')
            self.NPB['value']=100
            self.NPB.grid(row=0,column=2,sticky='WE')
#             Значок сердца
            self.HeartLb = Label(self.StatusFr1,text='\u2665 Здоровье \u2665', font='Arial 13 bold italic', foreground='gray0', background='RoyalBlue2')
            self.HeartLb.grid(row=0, column=0, padx=1, ipady=0, pady=2)
#             Уровень здоровья
            self.HealthLb = Label(self.StatusFr1,text='100', font='Arial 13 bold italic', foreground='gray0', background='RoyalBlue2')
            self.HealthLb.grid(row=0, column=1)
            
#             Значок инструментов
            self.InstLb = Label(self.StatusFr2,text='\u2692 Вещи: ', background='gold', font='Arial 12 bold')
            self.InstLb.grid(row=1, column=0, padx=1, ipady=0, pady=2)

#             Список вещей в инвентаре
            self.InvList = Label(self.StatusFr2,text='', width=10)
            self.InvList.grid(row=1, column=1, sticky='WE')
            
#             Подгрузить последним. Кнопка остановки и консоли
            self.SetFr=Frame(self.root)
            s.configure('SetFr.TFrame',relief='groove', background='khaki3')
            self.SetFr.config(style='SetFr.TFrame')
            self.SetFr.columnconfigure(0,weight=1)
            self.SetFr.columnconfigure(1,weight=1)
            self.SetFr.grid()
            
#             Фрейм для кнопки перезагрузки игры. 
            self.Restart_Frame=Frame(self.SetFr)
            s.configure('Restart_Frame.TFrame',relief='groove')
            self.Restart_Frame.config(style='Restart_Frame.TFrame')
            self.Restart_Frame.columnconfigure(0,weight=1)
            self.Restart_Frame.grid(row=0)
            
#             кнопка перезагрузки игры
            self.RestartBut = Button (self.Restart_Frame, text='Начать игру с начала', command=lambda: self.Restart())
            self.RestartBut.grid()
            
#             кнопка остановки программы и фрейм для неё
            self.But_Stop_Frame=Frame(self.SetFr)
            s.configure('But_Stop_Frame.TFrame',relief='groove')
            self.But_Stop_Frame.config(style='But_Stop_Frame.TFrame')
            self.But_Stop_Frame.columnconfigure(0,weight=1)
            self.But_Stop_Frame.columnconfigure(1,weight=1)
            self.But_Stop_Frame.grid(row=3)
            
            self.ButStop = Button (self.But_Stop_Frame,text='Выйти из игры.',command=lambda: self.Stop())
            self.ButConsole = Button (self.But_Stop_Frame,text='Console',command=lambda: self.TopBar())
            
#             фрейм для найстройки пути к сценариям
            self.SettingFr2=Frame(self.SetFr)
            s.configure('SettingFr2.TFrame',relief='groove')
            self.SettingFr2.config(style='SettingFr.TFrame')
            self.SettingFr2.columnconfigure(0,weight=1)
            self.SettingFr2.grid(row=1)
            
            self.PathLb0 = Label(self.SettingFr2,text='Настройки пути к сценариям')
            self.PathLb0.grid(row=0,column=0,sticky='we')
            
            self.SettingFr=Frame(self.SetFr)
            s.configure('SettingFr.TFrame',relief='groove')
            self.SettingFr.config(style='SettingFr.TFrame')
            self.SettingFr.columnconfigure(0,weight=1)
            self.SettingFr.columnconfigure(1,weight=1)
            self.SettingFr.grid(row=2)
            
            self.PathLb = Label(self.SettingFr,text='Текущий путь:')
            self.PathLb.grid(row=0,column=0)
            
            global pf
            self.pfl=list(pf.split('\\'))
            if len(self.pfl)<4:
                self.pfs=str(pf)
            else:
                self.pfs='...\\{0}\\{1}'.format(str(self.pfl[-2]),str(self.pfl[-1]))
            
            self.PathLb2 = Label(self.SettingFr,text=self.pfs)
            self.PathLb2.grid(row=0,column=1, pady=5, padx=5)
            
#             поле для ввода нового пути к сценариям
            self.PathEn=Entry(self.SettingFr,width=20)
            self.PathEn.insert(0,str(pf))
            self.PathEn.grid(column=0,row=1)
            
#             кнопка установки пути
            self.But_Set_Path = Button (self.SettingFr,text='Ввести путь',command=lambda: self.SetPath(self.PathEn.get()))
            self.But_Set_Path.grid(column=1,row=1)
            
#            размещение кнопок
            self.ButStop.grid(row=1, sticky='WE')
            self.ButConsole.grid(row=0, sticky='WE')
            
#             скрыть верхнюю панель (с консолью)
            MyW.topBar.grid_remove()
            
#             основное окно игры. Установка фона и т.п.
            self.GameFrame = Frame(self.root2)
            s.configure('GameFrame.TFrame',relief='flat', background='red')
            self.GameFrame.config(style='GameFrame.TFrame')
            self.GameFrame.grid(row=1,sticky='SEWN',padx=5)
            
#             текст заданий
            self.RoomInfo = Frame(self.GameFrame)
            s.configure('RoomInfo.TFrame',relief='groove', background='navy')
            self.RoomInfo.config(style='RoomInfo.TFrame')
            self.RoomInfo.grid(row=0,sticky='EWN',padx=0)
            
#             блок для ответов
            self.AnswerFrame = Frame(self.GameFrame)
            s.configure('AnswerFrame.TFrame',relief='groove', background='navy')
            self.AnswerFrame.config(style='AnswerFrame.TFrame')
            self.AnswerFrame.columnconfigure(0,weight=1)
            self.AnswerFrame.columnconfigure(1,weight=1)
            self.AnswerFrame.grid(row=1, padx=0, sticky='EWN')
            
#             Тексты названия комнаты, текст заданий, вариантов действий
            self.WelcomeLb = Label(self.RoomInfo,text = 'Приветствие локации', background='navy', foreground='yellow', font='Arial 10 italic')
            self.WelcomeLb.grid(row=0, pady=5, padx=5, sticky='nwe')
            
            self.TextQuestLb = Label(self.RoomInfo,text= 'Текст квеста', width=77, background='navy', foreground='yellow', font='Arial 12 bold')
            self.TextQuestLb.grid(row=1, padx=5, pady=10, sticky='we')
            
            self.AnsListLb = Label(self.AnswerFrame,text='Возможные действия: \n', background='navy', foreground='yellow')
            self.AnsListLb.grid(row=0, padx=5, pady=10, sticky='we')
            
#            строка ввода ответа. И кнопка ввода
            self.AnsEntry=Entry(self.AnswerFrame,width=50)
            self.AnsEntry.insert(0,'Введите действие или номер варианта.')
            self.AnsEntry.grid(row=1, column=0)
            
            self.But_Answer = Button (self.AnswerFrame,text='Выполнить',command=lambda: self.AnswerEnter(self.AnsEntry.get()))
            self.But_Answer.grid(column=1,row=1, sticky='w')
            
#             возможность ввода через Enter
            self.AnsEntry.bind('<Return>', lambda event: self.AnswerEnter(self.AnsEntry.get()))
            
            self.SetInfo()
            
#             Вызов верхней панели с консолью
        def TopBar(self):
            MyW.topBar.grid()
            
#             функция остановки программы.
        def Stop(self):
            ROOT.quit()
            ROOT.destroy()
        
#         Команда установки нового пути к сценариям
        def SetPath(self,path):
            # Установка нового пути к сценариям
            global pf, pf0
            if path == '':
                pf = pf0
            path2 = os.path.join(path,'SL0.qs')
            if os.path.isfile(path2): # Проверка, что в новом пути содержится хотя бы нулевой сценарий: SL0.qs
                pf = path
            else:
                print('Скрипты не найдены! Укажите другой путь или оставьте поле пустым (по умолчанию)')
                self.PathEn.insert(0,'Скрипты не найдены! Укажите другой путь или оставьте поле пустым (по умолчанию)')
                pf = pf0
            log_e.write('path to script: '+str(pf))
            
            self.pfl=list(pf.split('\\'))
#             вывод в строку пути к файлам
            if len(self.pfl)<4:
                self.pfs=str(pf)
            else:
                self.pfs='{0}...\\{1}\\{2}'.format(str(self.pfl[0]), str(self.pfl[-2]), str(self.pfl[-1]))
            
            self.PathLb2['text'] = self.pfs
        
#         запуск сценария (номер локации, номер квеста в ней)
        def Start(self, LNum, QNum):
            global LL
#             дополнительные переменный для нормальной работы команд из сценария (P,L,Q)
            P = self.P
            L = LL[LNum]
            Q = LL[LNum].Quests_list[QNum]
            
#             проверка наличия условий для запуска данного скрипта
            g = 0
            for check in Q.CheckList:
                if check != '':
                    if eval(check[:check.index(':')]) == False:
#                         выполнение иного квеста, если проверка не пройдена:
                        eval('self.'+check[check.index(':')+1:].strip())
                        g=1
                    
#             если условий нет или проверка пройдена, то продолжаем запускать этот квест. 
            if g == 0:
#                 счётчик вызова данного квеста
                Q.count += 1
#                 установка данного квеста как текущего
                self.Curent_Locate = L
                self.Curent_Quest = Q
                
                log_e.write('ok, start QID:'+str(QNum))
                
#                 Применение эффектов при старте квеста. 
                for eff in self.Curent_Quest.Effects:
                    if eff != '':
                        exec(eff.strip())
                        log_e.write('Effects now: '+ eff.strip())
                        
#                 Обновление информации в окне:
                self.SetInfo()
#                 очищение строки ввода:
            self.AnsEntry.delete(0,'end')
            
        
        def SetInfo(self):
            P = self.P
            L = self.Curent_Locate
            Q = self.Curent_Quest
            
#             применение эффекта Токсин - снижение здоровья на 1 каждое действие. 
            if 'Toxin' in P.Effects:
                P.Health -= 1
            
#             Проверка снижения здоровья до нуля.
            if P.Health <= 0 and P.Status == 'Жив':
                P.Dead()
                self.Start(0,0)
            
#             Установка шкалы здоровья. А также моргание красным цветом для визуальности. 
            if self.NPB['value'] != self.P.Health:
                self.NPB['value'] = self.P.Health
                self.NPB['style']="red.Horizontal.TProgressbar"
                self.HealthLb['text'] = self.P.Health
            
#             установка значений в окне
            self.WelcomeLb['text'] = (self.Curent_Locate.Name)
            
            self.TextQuestLb['text'] = StrCut(self.Curent_Quest.Text, 75)
            
            self.InvList['text'] = self.P.Inventory
            
#             установка списка вариантов ответа
            S=''
            n=1
            self.CurentAnsList = []
#             проверка доступности варианта
            for Ans1 in self.Curent_Quest.AnsName:
                CheckCond = self.Curent_Quest.AnsCheck[self.Curent_Quest.AnsName.index(Ans1)].replace('"','\'')
                if CheckCond == '':
                    S+=str(n)+'. '+Ans1+'\n'
                    n+=1
                    self.CurentAnsList.append(Ans1)
                elif eval(CheckCond) == True:
                    S+=str(n)+'. '+Ans1+'\n'
                    n+=1
                    self.CurentAnsList.append(Ans1)
            self.AnsListLb['text'] = ('Возможные действия: \n'+S[:-1])
            
#             возвращение шкалы здоровья к нормальному цвету
            self.root.after(700, self.ColorNormalize)
            
#             функция нормализации цвета
        def ColorNormalize(self):
            self.NPB['style']="green.Horizontal.TProgressbar"
            self.AnsEntry['background']='white'
            self.AnsEntry['foreground']='black'
        
#         приём ответа 
        def AnswerEnter(self, ans):
#             убираем лишние пробелы
            ans = ans.strip()
            qi = None # индекс выбранного варианта
#             проверяем наличие текстового варианта (без учёта регистра)
            if ans.upper() in self.Curent_Quest.AnsName:
                qi = self.Curent_Quest.AnsName.index(ans.upper())
#             проверка численного ввода варианта
            elif ans.isdigit():
                if int(ans) in range(1,len(self.CurentAnsList)+1):
                    qi = self.Curent_Quest.AnsName.index(self.CurentAnsList[int(ans)-1])
                    
#                 если варианта нет, то вывод ошибки. 
                else:
                    print('Wrong!')
                    self.AnsEntry['background']='red'
                    self.AnsEntry['foreground']='red'
                    self.AnsEntry.delete(0,'end')
                    self.AnsEntry.insert(0,'Неизвестное действие')
                    self.root.after(700, self.ColorNormalize)
            else:
                print('Wrong!')
                self.AnsEntry['background']='red'
                self.AnsEntry['foreground']='red'
                self.AnsEntry.delete(0,'end')
                self.AnsEntry.insert(0,'Неизвестное действие')
                self.root.after(700, self.ColorNormalize)
                
#                 Если вариант всё же найден - запуск следующего квеста
            if qi != None:
                qnid = self.Curent_Quest.AnsNextQ[qi] # ID следующего квеста
                
#                 проверка на пересылку в другую локацию (другой сценарий)
                if '-' in qnid:
                    LocID = int(qnid[:qnid.index('-')])
                    self.Curent_Locate = LL[LocID]
                    qnid = int(qnid[qnid.index('-')+1:])
                    self.Curent_Quest = self.Curent_Locate.Quests_list[qnid]
                    
#                 если квест в этой локации:
                else:
                    qnid = int(qnid.replace('.0', ''))
                    log_e.write('ok, go to QID:'+str(qnid))
#                     установка нужного квеста текущим:
                    self.Curent_Quest = self.Curent_Locate.Quests_list[qnid]
                    
#                 запуск найденного квеста
                self.Start(LL.index(self.Curent_Locate), self.Curent_Locate.Quests_list.index(self.Curent_Quest))
            
#         Перезагрузка игры:
        def Restart(self):
            self.P.Reset()
            Reset()
            self.Start(1,0)
        
#         Класс игрока. Вообще используется 1, но можно добавить профили. 
    class Player:
        def __init__(self, Name='Безымянный'):
            self.Name = Name
            self.Health = 100
            self.Inventory = []
            self.Progress = {}
            self.Status = 'Жив'
            self.Effects = []
        
        def Dead(self):
            self.Health = 0
            self.Status = 'Мёртв'
        
        def Reset(self):
            self.Health = 100
            self.Inventory = []
            self.Progress = {}
            self.Status = 'Жив'
            self.Effects = []
            
            
#             Класс квеста (текущих заданий в локации)
    class Quest:
        def __init__(self, info, answers):
            self.ID = int(info[info.find('QID={')+5:info.find('}',info.find('QID={'))])
            self.CheckList = list(info[info.find('QCheck={')+8 : info.find('}',info.find('QCheck={'))].split(';'))
            self.Text = info[info.find('QText={')+7 : info.find('}',info.find('QText={'))]
            self.Effects = (info[info.find('QEffect=[')+9:info.find(']',info.find('QEffect=['))]).split(';')
            self.count = 0
            self.Var = (info[info.find('QVar={')+6 : info.find('}', info.find('QVar='))])
            if self.Var == '':
                self.Var = {}
            else:
                d = {}
                self.Var = list(self.Var.split(';'))
                for vari in self.Var:
                    vari = list(vari.split(':'))
                    d.update({vari[0]:vari[1]})
                self.Var = d
                
            self.AnsName = []
            self.AnsCheck = []
            self.AnsNextQ = []
            for ans in answers:
                self.AnsName.append(ans[ans.find('qatext={')+8 : ans.find('}', ans.find('qatext={'))].upper())
                self.AnsCheck.append(ans[ans.find('qacheck=[')+9 : ans.find(']', ans.find('qacheck=['))])
                self.AnsNextQ.append(str(ans[ans.find('qn={')+4 : ans.find('}', ans.find('qn={'))]))
                
            
#     Класс локаций (в т.ч. чтение сценариев и формирование квестов данной локации в init)
    class Location:
        def __init__(self, File):
            with open(File, 'r', encoding='utf-8') as F:
                LocalStr=F.read()
                        
            self.Location_info = LocalStr.split('\\Quest')[0]
            self.Quests_Info_list=LocalStr.split('\\Quest')[1::]
            self.Quests_list=[]
            for questinfo in self.Quests_Info_list:
                q_ans_list = questinfo.split('\qa')[1::]
                q_info = questinfo.split('\qa')[0]
                self.Quests_list.append(Quest(q_info, q_ans_list))
            
            self.ID = self.Location_info[self.Location_info.find('LID={')+5 : self.Location_info.find('}', self.Location_info.find('LID='))]
            self.Name = self.Location_info[self.Location_info.find('LHello={')+8 : self.Location_info.find('}', self.Location_info.find('LHello='))]
            self.ID_Name = self.Location_info[self.Location_info.find('LName={')+7 : self.Location_info.find('}', self.Location_info.find('LName='))]
            self.Var = (self.Location_info[self.Location_info.find('LVar={')+6 : self.Location_info.find('}', self.Location_info.find('LVar='))])
            
            if self.Var == '':
                self.Var = {}
            else:
                d = {}
                self.Var = list(self.Var.split(';'))
                for vari in self.Var:
                    vari = list(vari.strip().split(':'))
                    if vari[1].isdigit():
                        vari[1] = int(vari[1].strip())
                    d.update({vari[0]:vari[1]})
                self.Var = d
        
#     Перезагрузка игры. Чтение сценариев заново, формирование нового списка локаций. 
    def Reset():
        print('Reset!')
        fi=0
        for f in os.listdir(pf):
            scriptf = os.path.join(pf,f)
            LL[fi] = Location(scriptf)
            fi+=1
            
    # path to programm and scripts defolt
    dir0 = os.getcwd()
    pf = os.path.join(dir0,'Scripts')
    pf0 = pf
    
#     Объявление игрока и формирование списка локаций (чтение сценариев)
    Player1 = Player()
    LL=[]
    for f in os.listdir(pf):
        scriptf = os.path.join(pf,f)
        LL.append(Location(scriptf))
    
#     Запуск среды TKinter (окна игры):
    MyW=MyWindow(ROOT)
    MyW.CMDC()
    DE=DataEnt(MyW.leftF, MyW.centerF, Player1)
    ROOT.geometry('1000x600+900+50')
    ROOT.mainloop()
#    ROOT.destroy()

except Exception as e:
    print(e)
    log_e.write('ERROR! '+str(e))