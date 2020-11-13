LID=[1]
LName=[DarkRoom]
LHello=[Вы в Мрачной комнате. ]
LVar=[Win:0; Pos:0; Done:0]
\Quest
QID=[0]
QCheck=[]
QText=[Вы проснулись в Мрачной комнате. Вы без малейшего понятия как здесь оказались и что вообще вас сюда могло привести. Вы сидите на холодной лавочке, с трудом различая холодные каменные стены комнаты, окно со слабым лунным светом в нём и что-то похожее на дверь в другом конце комнаты. Что вы будете делать?]
QEffect=[P.Reset()]
QVar=[]
\qa [1] 	qatext=[Бежать к двери]
qacheck=[] 	qn=[2.0]
\qa [2] 	qatext=[Бежать к окну]
qacheck=[] 	qn=[4.0]
\qa [3] 	qatext=[Осмотреться]
qacheck=[] 	qn=[9.0]
\Quest
QID=[1]
QCheck=[]
QText=[Вы сели на уже родную холодную лавку. Продышитесь и продолжайте. ]
QEffect=[L.Var.update({'Pos':0})]
QVar=[]
\qa [1] 	qatext=[К двери]
qacheck=[L.Var.get('Done') == 0] 	qn=[2.0]
\qa [2] 	qatext=[К окну]
qacheck=[] 	qn=[7.0]
\qa [3] 	qatext=[Осмотреться]
qacheck=[] 	qn=[9.0]
\qa [4] 	qatext=[Покрутить осколок]
qacheck=["Осколок" in P.Inventory] 	qn=[19.0]
\qa [5] 	qatext=[Выйти в дверь]
qacheck=[L.Var.get('Done') == 1] 	qn=[2-0]
\Quest
QID=[2]
QCheck=[Q.count==0: Start(1,3)]
QText=[Вы с разбегу влетаете в дверь, пытаясь её вышибить, поворачиваете ручку, колотите по петлям - всё без толку. Дверь не поддаётся. Кажется, она даже не сотрясается от ваших ударов.]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\qa [2] 	qatext=[Колотить]
qacheck=[] 	qn=[3.0]
\qa [3] 	qatext=[Покрутить осколок]
qacheck=["Осколок" in P.Inventory] 	qn=[19.0]
\Quest
QID=[3]
QCheck=[]
QText=[Вы снова бьёте в дверь. Дверь не поддаётся. Кажется, она даже не сотрясается от ваших ударов. Вы разбиваете кулаки в кровь. Вам не надоело?]
QEffect=[P.Health-=5]
QVar=[]
\qa [1] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\qa [2] 	qatext=[Колотить]
qacheck=[] 	qn=[3.0]
\qa [3] 	qatext=[Ощупать дверь]
qacheck=[] 	qn=[14.0]
\qa [4] 	qatext=[Покрутить осколок]
qacheck=["Осколок" in P.Inventory] 	qn=[19.0]
\qa [5] 	qatext=[Выйти в дверь]
qacheck=[L.Var.get('Done') == 1] 	qn=[2-0]
\Quest
QID=[4]
QCheck=[Q.count==0: Start(1,7)]
QText=[Вы подбегаете к окну. Это старое грязное окно в деревяной раме. Вы пытаетесь его открыть, но оно заколочено. Что же делать?]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Разбить окно]
qacheck=[] 	qn=[5.0]
\qa [2] 	qatext=[Швырнуть железку]
qacheck=["Железка" in P.Inventory] 	qn=[51.0]
\qa [3] 	qatext=[Швырнуть подкову]
qacheck=["Подкова" in P.Inventory] 	qn=[51.0]
\qa [4] 	qatext=[Осмотреть окно]
qacheck=[] 	qn=[6.0]
\qa [5] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\Quest
QID=[5]
QCheck=[]
QText=[Вы разбиваете окно и получаете кучу порезов осколками стекла. Вам следует быть аккуратнее, если не хотите истечь кровью. Ну и что дальше? ]
QEffect=[P.Health-=50; L.Var.update({'Win':1})]
QVar=[]
\qa [1] 	qatext=[Выглянуть]
qacheck=[] 	qn=[11.0]
\qa [2] 	qatext=[Осмотреть окно]
qacheck=[] 	qn=[6.0]
\qa [3] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\qa [4] 	qatext=[Рассмотреть железку]
qacheck=["Железка" in P.Inventory] 	qn=[13.0]
\qa [5] 	qatext=[Взять осколок]
qacheck=[not "Осколок" in P.Inventory] 	qn=[52.0]
\Quest
QID=[51]
QCheck=[]
QText=[Вы разбиваете окно, осколки стекла разлетаются во все стороны, хорошо, что вы отошли и кинули издалека. Ну и что дальше? ]
QEffect=[L.Var.update({'Win':1})]
QVar=[]
\qa [1] 	qatext=[Выглянуть]
qacheck=[] 	qn=[11.0]
\qa [2] 	qatext=[Осмотреть окно]
qacheck=[] 	qn=[6.0]
\qa [3] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\qa [4] 	qatext=[Рассмотреть железку]
qacheck=["Железка" in P.Inventory] 	qn=[13.0]
\qa [5] 	qatext=[Взять осколок]
qacheck=[not "Осколок" in P.Inventory] 	qn=[52.0]
\Quest
QID=[52]
QCheck=[]
QText=[Вы подбираете осколок стекла. Вы конечно пытались осторожно, но… в общем не умеете вы обращаться с острыми предметами. Свыкнитесь)]
QEffect=[P.Health-=3; P.Inventory.append('Осколок')]
QVar=[]
\qa [1] 	qatext=[Продолжить]
qacheck=[] 	qn=[7.0]
\qa [2] 	qatext=[Покрутить осколок]
qacheck=["Осколок" in P.Inventory] 	qn=[19.0]
\Quest
QID=[6]
QCheck=[]
QText=[На подоконнике вы видете надпись: «Очень старое стекло, не стоит его трогать»]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Назад]
qacheck=[] 	qn=[7.0]
\Quest
QID=[7]
QCheck=[L.Var.get('Win') == 0 : Start(1,8)]
QText=[Вы подходите к старому окну. Зачем?]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Разбить окно]
qacheck=[L.Var.get('Win') == 0] 	qn=[5.0]
\qa [2] 	qatext=[Швырнуть железку]
qacheck=["Железка" in P.Inventory] 	qn=[51.0]
\qa [3] 	qatext=[Швырнуть подкову]
qacheck=["Подкова" in P.Inventory] 	qn=[51.0]
\qa [4] 	qatext=[Осмотреть окно]
qacheck=[] 	qn=[6.0]
\qa [5] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\qa [6] 	qatext=[Рассмотреть железку]
qacheck=["Железка" in P.Inventory] 	qn=[13.0]
\qa [7] 	qatext=[Покрутить осколок]
qacheck=["Осколок" in P.Inventory] 	qn=[19.0]
\Quest
QID=[8]
QCheck=[]
QText=[Вы подходите к разбитому окну. Острожнее с осколками! Ай! Вы опять порезались - чтож вы такой неуклюжий? ]
QEffect=[P.Health-=5]
QVar=[]
\qa [1] 	qatext=[Осмотреть окно]
qacheck=[] 	qn=[6.0]
\qa [2] 	qatext=[Выглянуть]
qacheck=[] 	qn=[11.0]
\qa [3] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\qa [4] 	qatext=[Рассмотреть железку]
qacheck=["Железка" in P.Inventory] 	qn=[13.0]
\qa [5] 	qatext=[Взять осколок]
qacheck=[not "Осколок" in P.Inventory] 	qn=[52.0]
\Quest
QID=[9]
QCheck=[Q.count==0: Start(1,10)]
QText=[Осматривая, а скорее даже ощупывая комнату, вы находите и открываете шкаф. Двери тяжёлые и жутко скрипят в полной тишине, от чего вы вздрагиваете, но выдохнув, открываете шкаф доконца. Вы ощупываете все полки, но чувствуете только холодное дерево. На нижней полке вы всё таки находите какой-то холодный, наверное железный, предмет. Положим его пока в карман. ]
QEffect=[P.Inventory.append('Железка')]
QVar=[]
\qa [1] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\Quest
QID=[10]
QCheck=[]
QText=[Осмотр комнаты ничего нового не дал. Вы всё в той же мрачной комнате и это уже действует вам на нервы. ]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\Quest
QID=[11]
QCheck=[]
QText=[В слабом свете луны вы видите каменную стену с парой окон ниже вашего. Кажется вы находитесь в каком-то здании (может в замке?) на третьем этаже. Внизу растёт ряд больших кустов, за ними поле выской травы, а вдаль до горизонта уходит тёмный лес, над которым возвышается полная луна. ]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Выпрыгнуть]
qacheck=[] 	qn=[0-0]
\qa [2] 	qatext=[Кинуть железку]
qacheck=["Железка" in P.Inventory] 	qn=[12.0]
\qa [3] 	qatext=[Кинуть подкову]
qacheck=["Подкова" in P.Inventory] 	qn=[12.0]
\qa [4] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\Quest
QID=[12]
QCheck=[]
QText=[Вы выкинули железку из окна и наблюдаете за её полётом, всё равно больше вам смотреть не на что. Красиво летит…. СТОП. ЧТО?! Она приближается??!! Чёрт, она летит обратно! АЙ!!! *Ваша голова раскалывается от боли, боюсь, эта шишка на долго...*]
QEffect=[P.Health-=30]
QVar=[]
\qa [1] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\Quest
QID=[13]
QCheck=[]
QText=[Вы пытаетесь осмотреть железку на слабом свету, это что-то похожее на… Подкову? Хм, ну ладно. ]
QEffect=[P.Inventory.remove('Железка'); P.Inventory.append('Подкова')]
QVar=[]
\qa [1] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\Quest
QID=[14]
QCheck=[]
QText=[Проведя по шершавой деревянной двери рукой, вы натыкаетесь на гвоздь чуть выше вашей головы. Интересно, а можно ли вбить его?]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Ударить гвоздь]
qacheck=[] 	qn=[15.0]
\qa [2] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\qa [3] 	qatext=[Покрутить осколок]
qacheck=["Осколок" in P.Inventory] 	qn=[19.0]
\Quest
QID=[15]
QCheck=[]
QText=[Ай! Больно же! Руки для этого не предназначены. Может есть что покрепче? Кстати, кровь на гвозде странно светится… Ну да ладно. ]
QEffect=[P.Health-=5; L.Var.update({'Pos':"Door"})]
QVar=[]
\qa [1] 	qatext=[Ударить головой]
qacheck=[] 	qn=[0-0]
\qa [2] 	qatext=[Ударить железкой]
qacheck=["Железка" in P.Inventory] 	qn=[16.0]
\qa [3] 	qatext=[Покрутить осколок]
qacheck=["Осколок" in P.Inventory] 	qn=[19.0]
\qa [4] 	qatext=[Повесить подкову]
qacheck=["Подкова" in P.Inventory] 	qn=[21.0]
\qa [5] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\Quest
QID=[16]
QCheck=[]
QText=[Вы ударяете железкой, но она неожиданно приклеивается к двери. Вы пытаетесь оторвать её, но это бесполезно - она как будто приварена к двери. Вы бьёте по двери ещё раз и железка падает. Хм, что-то тут не так.]
QEffect=[L.Var.update({'Pos':0})]
QVar=[]
\qa [1] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
\Quest
QID=[17]
QCheck=[]
QText=[Вы вешаете окровавленную подкову на дверь. Она сама поворачивается вокруг своей оси и замирает...  
Неожиданно раздаётся скрип и дверь открывается. 
Из-за двери разливается красное свечение, у вас темнеет в глазах и кружится голова от столь яркого света.... ]
QEffect=[P.Inventory.remove('Подкова'); L.Var.update({"Done":1})]
QVar=[]
\qa [1] 	qatext=[Войти]
qacheck=[] 	qn=[2-0]
\Quest
QID=[18]
QCheck=[]
QText=[Не, ну ты видел? Видел?! Фух, надо что-то придумать. ]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Сесть на лавку]
qacheck=[] 	qn=[1-1]
\qa [2] 	qatext=[Войти в дверь]
qacheck=[] 	qn=[2-0]
\Quest
QID=[19]
QCheck=[]
QText=[Ауч! Вы порезались, кровь капает на пол, ваши руки в крови. Ух, ваши руки остаются липкими от крови на пару секунд. Уберём-ка пока стекло в карман, а]
QEffect=[P.Health-=13]
QVar=[]
\qa [1] 	qatext=[Сесть отдохнуть]
qacheck=[] 	qn=[1.0]
\qa [2] 	qatext=[Взять в руки подкову]
qacheck=["Подкова" in P.Inventory] 	qn=[20.0]
\Quest
QID=[20]
QCheck=[]
QText=[Вы берёте подкову своей окровавленной рукой. Подкова начинается ярко светиться от взаимодействия с кровью. Не сильно понятно что с этим делать. Свечение тускнеет по мере застывания крови…]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Сесть подумать]
qacheck=[] 	qn=[1.0]
\qa [2] 	qatext=[Повесить подкову]
qacheck=[L.Var.get('Pos') == "Door"] 	qn=[17.0]
\Quest
QID=[21]
QCheck=[]
QText=[Хм, подкова вроде пришлась по месту, но… Дверь всё ещё закрыта. Чего-то тут не хватает…]
QEffect=[]
QVar=[]
\qa [1] 	qatext=[Вернуться]
qacheck=[] 	qn=[1.0]
