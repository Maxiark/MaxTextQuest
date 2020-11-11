try:
    import tkinter as TK
    from tkinter import filedialog
    import tkinter.ttk as ttk
    import os

    ROOT=TK.Tk()
    ROOTH=800  # ширина и высота окна ТКинтер
    ROOTW=600
    s=ttk.Style()
    s.theme_use('clam')

    # Вывод текста с переносом строк (длина строки - lenght). 
    #     (Абзацы вставляюся вместо пробелов)
    def StrCut(text, lenght):
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
        
    #     Создание фреймов функцией
    def Frame(root, NameStyle='StFrame', fg="black", bg="darkgreen",
              relf ='sunken', cols=[0], rows=[0],
              grids=[], stick='', colspan=1,
              pdx=0, ipdx=0, pdy=0, ipdy=0):
        
        res = ttk.Frame(root)
        s.configure(NameStyle+'.TFrame', foreground=fg,
                    background=bg,relief =relf)
        res.config(style=NameStyle+'.TFrame')
        for i in range(len(cols)):
            res.columnconfigure(i, weight=cols[i])
        for i in range(len(rows)):
            res.rowconfigure(i,weight=rows[i])
        if len(grids)>0:
            res.grid(row=grids[0], column=grids[1],
                     sticky=stick, columnspan=colspan,
                     padx=pdx, ipadx=ipdx, pady=pdy, ipady=ipdy)
        else:
            res.grid(sticky=stick, columnspan=colspan)
        res.propagate(True)
        return res
        
            

    class MyWindow:   # основное графическое окно TKinter. 
        def __init__(self,root):
            self.root=root
            self.root.columnconfigure(0,weight=0)
            self.root.rowconfigure(0,weight=0)
            self.root.config(bg='darkblue')
            self.message='message!'
            self.root.propagate(True)
            
            self.contentFrame = Frame(self.root, NameStyle='contentFrame',
                                      cols=[0], rows=[0,0,1], stick='news')
            self.contentFrame.propagate(True)
            
            # Вверхний блок для консоли. Скрыт по умолчанию. 
            self.topBar = Frame(self.contentFrame, grids=[0,0], cols=[1],
                                bg='black', stick='nwe')
            
            self.LabTop = ttk.Label(self.topBar,text='Head console')
            self.LabTop.grid(row=0,column=0)
            
            # Блок с названием программы
            self.NameBar = Frame(self.contentFrame, NameStyle='NameBar',
                                 bg='blue', grids=[1,0],stick='news')
            
            self.NameLab = ttk.Label(self.NameBar, font=('Arial 12'), 
                                     text='The Text Game. \t\t Ver: 0.1 '+
                                     '\t\t Author: Maxiark', 
                                     background='blue', foreground='white')
            self.NameLab.grid(row=0,column=0, padx=10, ipady=0, pady=5)
            
            self.botBar = Frame(self.contentFrame, NameStyle='BotBar', 
                                grids=[2,0], cols=[1,0], rows=[1],
                                stick='nwes',bg='darkblue')
            
            
            # верхний блок для меню
            self.MenuFr = Frame(self.botBar, NameStyle='MenuFr',
                               bg='darkblue', cols=[0], rows=[0],
                               grids=[0,0], stick='nwes')
            
            self.LabelLeft = ttk.Label(self.MenuFr,text='Меню')
            self.LabelLeft.grid(row=0,column=0)
            
            # основной блок для игры
            self.centerF = Frame(self.botBar, NameStyle='centerF',
                                 bg='darkblue', rows=[0], cols=[1],
                                 grids=[1,0], stick='nswe')
            
            self.LabelCenter = ttk.Label (self.centerF,text='Игра')
            self.LabelCenter.grid(row=0,column=0)
            
            
        def CMDC(self):  # выполнение команд из строки консоли
            self.CMD_L=ttk.Label(self.topBar, text='comand console:')
            self.CMD_L.grid()
            
            self.CMD = ttk.Entry(self.topBar,width=40)
            self.CMD.grid()
            
            self.CMD_B = ttk.Button(self.topBar, text='Run command',
                                    command=self.EvalF)
            self.CMD_B.grid()
            
            self.CMD_EL = ttk.Label(self.topBar, text='no error')
            s.configure('CMDLE.TLabel',background='yellow')
            self.CMD_EL.config(style='CMDLE.TLabel')
            self.CMD_EL.grid()
            
            self.CMD_hide = ttk.Button(self.topBar, text='Hide Console',
                                       command=lambda: self.HideTop())
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
                with open(dir0+'log.txt','a') as log_e:
                    log_e.write('error: '+str(e)+'\n')
            else:
                self.CMD_EL.config(text='no error')




    class DataEnt:  # Основные элементы управления для TKinter. 
        def __init__(self,root,root2,PlayerIn):
            self.P = PlayerIn  # ссылка на игрока 
            
            self.root=root
            self.root2=root2
            
    #             фрейм состояния (Здоровье и Инвентарь)
            self.StFr = Frame(self.root2, NameStyle='StFr', cols=[1],
                              bg='navy', stick='we',grids=[0,0],
                              rows=[0,0,0], pdx=2) 
            
            self.StatLabel = ttk.Label(self.StFr,text='Состояние персонажа:',
                                       font=('Arial 12 bold'),
                                       foreground='white', background='navy')
            self.StatLabel.grid(row=0,column=0,pady=5)
            
    #         Фрейм для здоровья
            self.HealthFr = Frame(self.StFr, NameStyle='HealthFr',
                                  bg='RoyalBlue2', cols=[0,1,2],
                                  grids=[0,0], stick='wen', pdx=5, pdy=2)
            
    #             Полоса здоровья
            s.configure("red.Horizontal.TProgressbar",
                        foreground='green', background='red3')
            s.configure("green.Horizontal.TProgressbar",
                        foreground='green', background='green')
            self.NPB = ttk.Progressbar(self.HealthFr,
                                       style="green.Horizontal.TProgressbar",
                                       orient='horizontal', length=100,
                                       mode='determinate')
            self.NPB['value']=100
            self.NPB.grid(row=0,column=2,sticky='WE')
    #             Значок сердца
            self.HeartLb = ttk.Label(self.HealthFr,text='\u2665 Здоровье \u2665',
                                     font='Arial 13 bold italic',
                                     foreground='gray0', background='RoyalBlue2')
            self.HeartLb.grid(row=0, column=0, padx=1, ipady=0, pady=2)
            
    #             Уровень здоровья
            self.HealthLb = ttk.Label(self.HealthFr,text='100',
                                      font='Arial 13 bold italic',
                                      foreground='gray0', background='RoyalBlue2')
            self.HealthLb.grid(row=0, column=1)
            
            
            self.InventoryFr = Frame(self.StFr, NameStyle='InventoryFr',
                                     bg='gold', cols=[0,2],
                                     grids=[1,0], stick='wes', pdx=5, pdy=2)
            
    #             Значок инструментов
            self.InstLb = ttk.Label(self.InventoryFr,text='\u2692 Вещи: ',
                                    background='gold', font='Arial 12 bold')
            self.InstLb.grid(row=1, column=0, padx=1, ipady=0, pady=2)

    #             Список вещей в инвентаре
            self.InvList = ttk.Label(self.InventoryFr, text='', width=10)
            self.InvList.grid(row=1, column=1, sticky='WE', padx=10, pady=2)
            
            
    #             Фрейм для кнопки перезагрузки игры. 
            self.Restart_Frame = Frame(self.root, cols=[0], rows=[0],
                                       grids=[1,0], stick='n',
                                       pdx=15, pdy=10)
            
    #             кнопка перезагрузки игры
            self.RestartBut = ttk.Button (self.Restart_Frame,
                                          text='Начать игру с начала',
                                          command=lambda: self.Restart())
            self.RestartBut.grid()
            
    #             кнопка остановки программы и фрейм для неё
            self.But_Stop_Frame = Frame(self.root, cols=[1,1],
                                        grids=[1,2], stick='n',
                                        pdx=20, pdy=10)
            
            self.ButStop = ttk.Button (self.But_Stop_Frame,text='Выйти из игры.',
                                       command=lambda: self.Stop())
            self.ButConsole = ttk.Button (self.But_Stop_Frame,text='Console',
                                          command=lambda: self.TopBar())
            
            self.ButConsole.grid(row=0, sticky='WE')
            self.ButStop.grid(row=1, sticky='WE')
            
            self.Menu_hide = ttk.Button(self.root, text='Hide Menu',
                                       command=lambda: self.HideMenu())
            self.Menu_hide.grid(row=1, column=3, sticky='WE')
            
            
    #             фрейм для найстройки пути к сценариям
            self.SettingFr = Frame(self.root, grids=[1,1],cols=[0,1])
            
            self.PathLb0 = ttk.Label(self.root,text='Настройки пути к сценариям')
            self.PathLb0.grid(row=0, column=1, sticky='n', pady=5)
            
            self.PathLb = ttk.Label(self.SettingFr,text='Текущий путь:')
            self.PathLb.grid(row=0, column=0)
            
            global pf
            self.pfl=pf.split(os.sep)
            if len(self.pfl)<3:
                self.pfs=str(pf)
            else:
                self.pfs='...{0}/{1}'.format(str(self.pfl[-2]),str(self.pfl[-1]))
            
            self.PathLb2 = ttk.Label(self.SettingFr,text=self.pfs)
            self.PathLb2.grid(row=0,column=1, pady=5, padx=5)
            
    #             кнопка установки пути
            self.But_Set_Path = ttk.Button (self.SettingFr,text='Выбрать папку',
                                            command=lambda: self.SetPath())
            self.But_Set_Path.grid(column=0,row=1, columnspan=2)
            
    #             скрыть верхнюю панель (с консолью)
            MyW.topBar.grid_remove()
            
            
    #             основное окно игры. Установка фона и т.п.
            self.GameFrame = Frame(self.root2, grids=[2,0],
                                       pdx=5, stick='news')
            
    #             текст заданий
            self.RoomInfo = Frame(self.GameFrame, rows=[0],
                                  grids=[0,0], stick='EWN', bg='navy')
            
    #             блок для ответов
            self.AnswerFrame = Frame(self.GameFrame, cols=[0,1],
                                         grids=[1,0], stick='EWN', bg='navy')
            
    #             Тексты названия комнаты, текст заданий, вариантов действий
            self.WelcomeLb = ttk.Label(self.RoomInfo,text = 'Приветствие локации',
                                       background='navy', foreground='yellow',
                                       font='Arial 10 italic')
            self.WelcomeLb.grid(row=0, pady=5, padx=5, sticky='nwe')
            
            self.TextQuestLb = ttk.Label(self.RoomInfo,text= 'Текст квеста',
                                         width=77, background='navy',
                                         foreground='yellow', font='Arial 12 bold')
            self.TextQuestLb.grid(row=1, padx=5, pady=10, sticky='we')
            
            self.AnsListLb = ttk.Label(self.AnswerFrame, background='navy',
                                       foreground='yellow',
                                       text='Возможные действия: \n')
            self.AnsListLb.grid(row=0, padx=5, pady=10, sticky='we')
            
    #            строка ввода ответа. И кнопка ввода
            self.AnsEntry = ttk.Entry(self.AnswerFrame,width=50)
            self.AnsEntry.insert(0,'Введите действие или номер варианта.')
            self.AnsEntry.grid(row=1, column=0, sticky='w', padx=10)
            
            self.But_Answer = ttk.Button (self.AnswerFrame,text='Выполнить',
                                          command=lambda: self.AnswerEnter(self.AnsEntry.get()))
            self.But_Answer.grid(column=1, row=1, sticky='w', pady=5)
                    
    #             возможность ввода через Enter
            self.AnsEntry.bind('<Return>', lambda event: self.AnswerEnter(self.AnsEntry.get()))
            
    #         Инструкция
            self.ManualFr = Frame(self.GameFrame, cols=[0,1],
                                  grids=[2,0], stick='WEN', bg='navy',
                                  pdx=1, pdy=1)
            self.Manual = ttk.Label(self.ManualFr, background='navy',
                                    foreground='white',
                                    text='Вводите действия или их номер. \n'+
                                    ' Ввод через Кнопку или нажатие Enter.')
            self.Manual.grid(column=0, row=0, pady=2, padx=20)
            
            self.But_Menu = ttk.Button (self.ManualFr,text='Меню',
                                          command=lambda: self.OpenMenu())
            self.But_Menu.grid(row=0, column=1, pady=5, padx=20, sticky='w')
            
            self.ButStop = ttk.Button (self.But_Stop_Frame,
                                       text='Выйти из игры.',
                                       command=lambda: self.Stop())
                    
            self.Start(1,0)
            self.HideMenu()
            
        def HideMenu(self):
            MyW.MenuFr.grid_remove()
            
        def OpenMenu(self):
            MyW.MenuFr.grid()
            
    #             Вызов верхней панели с консолью
        def TopBar(self):
            MyW.topBar.grid()
            
    #             функция остановки программы.
        def Stop(self):
            ROOT.quit()
            ROOT.destroy()
        
    #         Команда установки нового пути к сценариям
        def SetPath(self):
            # Установка нового пути к сценариям
            global pf, pf0
            path = os.path.normpath(filedialog.askdirectory())
            
            if path == '':
                pf = pf0
            path2 = os.path.join(path,'SL0.qs')
            # Проверка, что в новом пути содержится хотя бы нулевой сценарий: SL0.qs
            if os.path.isfile(path2): 
                pf = path
            else:
                print('Скрипты не найдены!'+
                      ' Укажите другой путь или оставьте '+
                      'поле пустым (по умолчанию)')
                self.PathEn.insert(0,'Скрипты не найдены!'+
                                   ' Укажите другой путь или '+
                                   'оставьте поле пустым (по умолчанию)')
                pf = pf0
                
            with open(dir0+'log.txt','a') as log_e:
                log_e.write('path to script: '+str(pf)+'\n')
            
    #             вывод в строку пути к файлам
            self.pfl=pf.split(os.sep)
            if len(self.pfl)<3:
                self.pfs=str(pf)
            else:
                self.pfs='...{0}/{1}'.format(str(self.pfl[-2]),str(self.pfl[-1]))
            
            self.PathLb2['text'] = self.pfs
            Reset()
        
    #         запуск сценария (номер локации, номер квеста в ней)
        def Start(self, LNum, QNum):
            global LL
    #             дополнительные переменный для нормальной работы команд из сценария (P,L,Q)
            P = self.P
            NextLocate = list(filter(lambda x: int(x.ID) == int(LNum), LL))[0]
            L = NextLocate
            NextQuest = list(filter(lambda x: int(x.ID) == int(QNum), L.Quests_list))[0]
            Q = NextQuest
            
    #             проверка наличия условий для запуска данного скрипта
            g = 0
            for check in Q.CheckList:
                if check != '':
                    if eval(check[:check.index(':')]) == False:
    #                         выполнение иного квеста, если проверка не пройдена:
                        eval('self.'+check[check.index(':')+1:].strip())
                        g=1
                    
    #       если условий нет или проверка пройдена, то продолжаем запускать этот квест. 
            if g == 0:
    #                 счётчик вызова данного квеста
                Q.count += 1
    #                 установка данного квеста как текущего
                self.Curent_Locate = L
                self.Curent_Quest = Q
                with open(dir0+'log.txt','a') as log_e:
                    log_e.write('ok, set Quest:'+str(LNum)+' - '+str(QNum)+'\n')
                
    #                 Применение эффектов при старте квеста. 
                for eff in self.Curent_Quest.Effects:
                    if eff != '':
                        exec(eff.strip())
                        with open(dir0+'log.txt','a') as log_e:
                            log_e.write('\t\t Effects now: '+ eff.strip()+'\n')
                        
    #                 Обновление информации в окне:
                self.SetInfo()
    #                 очищение строки ввода:
            self.AnsEntry.delete(0,'end')
            
        
        def SetInfo(self):
            P = self.P
            L = self.Curent_Locate
            Q = self.Curent_Quest
            
            
    #             Проверка снижения здоровья до нуля.
            if P.Health <= 0 and P.Status == 'Жив':
                P.Dead()
                self.Start(0,0)
            
    #       применение эффекта Токсин - снижение здоровья на 1 каждое действие. 
            if 'Toxin' in P.Effects:
                P.Health -= 1
    #       Установка шкалы здоровья. А также моргание красным цветом для визуальности. 
            if self.NPB['value'] != self.P.Health:
                self.NPB['value'] = self.P.Health
                self.NPB['style']="red.Horizontal.TProgressbar"
                self.HealthLb['text'] = self.P.Health
            
    #             установка значений в окне
            self.WelcomeLb['text'] = (self.Curent_Locate.Name)
            
            self.TextQuestLb['text'] = StrCut(self.Curent_Quest.Text, 75)
            
            StrInv=''
            for thing in self.P.Inventory:
                StrInv += str(thing)+' \t'
            self.InvList['text'] = StrInv
            
    #             установка списка вариантов ответа
            S=''
            n=1
            self.CurentAnsList = []
    #             проверка доступности варианта
            for Ans1 in self.Curent_Quest.AnsName:
                CheckCond = self.Curent_Quest.AnsCheck[
                            self.Curent_Quest.AnsName.index(Ans1)].replace('"','\'')
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
    #                     print(LocID, list(filter(lambda x: x.ID == LocID, LL)), [x.ID for x in LL])
                    NextLocate = list(filter(lambda x: int(x.ID) == int(LocID), LL))[0]
                    self.Curent_Locate = NextLocate
                    qnid = int(qnid[qnid.index('-')+1:])
                    NextQuest = list(filter(lambda x: int(x.ID) == int(qnid), self.Curent_Locate.Quests_list))[0]
                    self.Curent_Quest = NextQuest
                    
                    
    #                 если квест в этой локации:
                else:
                    qnid = int(qnid.replace('.0', ''))
                    with open(dir0+'log.txt','w') as log_e:
                        log_e.write('ok, go to QID:'+str(qnid)+'\n')
                    
    #                     установка нужного квеста текущим:
                    NextQuest = list(filter(lambda x: x.ID == qnid, self.Curent_Locate.Quests_list))[0]
                    self.Curent_Quest = NextQuest
                    
    #                 запуск найденного квеста
                self.Start(self.Curent_Locate.ID, self.Curent_Quest.ID)
            
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
            self.Inventory = []
            self.Effects = []
        
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
            self.Effects = (info[info.find('QEffect={')+9:info.find('}',info.find('QEffect={'))]).split(';')
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
    DE=DataEnt(MyW.MenuFr, MyW.centerF, Player1)
    ROOT.geometry('1000x600+900+50')
    ROOT.mainloop()
    #    ROOT.destroy()
    
except Exception as e:
    print(e)
    with open(dir0+'log.txt','w') as log_e:
        log_e.write('ERROR! '+str(e))
