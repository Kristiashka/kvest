import time

print("Привіт друже! Давай зіграємо в гру.")
time.sleep(2)
print("Відповідай або 1 або 2")
time.sleep(2)
print("Вибери на чіїй ти стороні.")
time.sleep(2)
a = input("1)Сухопутні війська?; Чи 2)Повітряні сили?;")
if a == "1" or a =="2":
    time.sleep(2)
    print("Гарний вибір!")
    time.sleep(1)
    if a == "1":
        print("В тебе сьогодні завдання!")
        time.sleep(3)
        name = input("Придумай назву своєї групи")
        print("Чудово!")
        time.sleep(1)
        print("З тобою в групі ще 4 людини (РОМЕО) (ТАНК) (ЛЕОПАРД) та (КІБОРГ)")
        time.sleep(3)
        name1 = input("Тепер придумай свій позивний!")
        print("Чудово!")
        time.sleep(1)
        print("Тепер більше подробиць про завдання.Є інформація що в Одессі  1 день тому висадилась група ДРГ! Їхнє завдання Підірвати склад боєприпасів! В групі їх теж п'ятеро! В деяких з них є тату на руках з написом 26-а бригада. В них з собою 5 автоматів АК-47, 3 гранати РГД-5 та 10кг тротилу!")
        time.sleep(16)
        print("А, твоє не дати їм підірвати склад та знешкодити всіх п'ятьох!")
        time.sleep(2)
        print("А, тепер збирайся! В тебе є вибір що з собою взяти!")
        time.sleep(2)
        print("Що візьмеш?")
        avtomat = input("1) АК-47; чи 2)М-416?; ")
        print("Прекрасний вибір!")
        time.sleep(1)
        if avtomat == "1":
            avtomat = " Ак-47 "
        else:
            avtomat = " М-416 "
        granata = input(" 1)Ргд-1 чи 2)Ргд-5? ")
        print("Чудовий Вибір!")
        if granata == "1":
            granata = " Ргд-1 "
        else:
            granata = " Ргд-5 "
        print("На данний момент в тебе в інвентарю є "+ avtomat   + "та" + granata + "та бронежелет, шолом та 3 рожки патронів до автомату!.")
        time.sleep(3)
        print("А, тепер спати! Завтра підйом в 3 години ранку")
        time.sleep(5)
        print("Підйом! Ми виїзджаємо! Через 5 хвилин!")
        time.sleep(2)
        print("ну що ти готовий?")
        ready = input("1)Так; 2)Ні;")
        while ready != "1":
            time.sleep(5)
            print("Ну що тепер готовий?")
            ready = input("1)так 2)ні")
        print("Добре, сідай! Ми виїзджаємо!")
        time.sleep(1)
        print(" *Ви сіли в машину. Та через годину прибули на місце призначення. ")
        time.sleep(3)
        print("Ви та ваша команда вийшли з мікробуса. А, сумки  з спорядженням залишили в машині. На данний момент ви одягнені в цивільний одяг.")
        time.sleep(4)
        print("Ви та ваша команда почали ходити по вулиці міста та шукати підозрілих людей")
        time.sleep(5)
        print("Через годину КІБОРГУ по рації повідомили що місцева поліція схопила одного з учасників дрг.")
        time.sleep(4)
        print("Ви прибули в місцевий відділ поліції на допит.")
        time.sleep(3)
        print("Підозрюваний нічого не хоче розповідати доведеться застосувати силу")
        sula = input("1)Зламати палець; 2)Злмати ногу;")
        if sula == "1":
            print("Ви зламали палець але він всеодно нічого не хоче говорити")
            time.sleep(2)
            print("Ви вдарили два раза по голові, та підозрюваний почав щось говорити")
        else:
            print("Ви зламали ногу підозрюваному, та він почав щось говорити")
        time.sleep(4)
        print("Ви поговорил з підозрюваним дві години часу. Та він розповів вам що завтра в 18:00 вони хочуть підірвати склад. Та що його напарники будуть в чорних штанях, та в кепках.")
        time.sleep(7)
        print("Ви розповіли все своїм напарникам та розробили план перехвату. ")
        time.sleep(3)
        print("Завтра в 17:00 ви приходите на місце та переодягаєтесь в спец-одяг та cідаєте в засідку та починаєте чекати коли з'являться люди в чорних штанах та кепках.")
        time.sleep(6)
        print("Ви з напарниками сіли в мікроавтобус та заснули. *Сьогоднішний день був успішним.")
        time.sleep(3)
        print("Ви проснулись в 10:00. Ви поїли та сіли чекати 17:00")
        time.sleep(3)
        print("Ось і настав ваш час ви з напарниками вийшли з автобусу прийшли на місце предягнулись та сіли чекати.")
        time.sleep(15)
        print("Хвилин через 30 ваш напарник РОМЕО передає по рації що побачив двух людей в чорних штанях та з сумками.")
        time.sleep(10)
        print("Хвилин через п'ять ТАНК передає по рації що замітив ще двух людей з сумками. *Ось і всі чотири на місці")
        time.sleep(5)
        print("Ваша команда розділилась  ")
        time.sleep(2)
        print("Ви з ЛЕОПАРДОМ. ТАНК з КІБОРГОМ та РОМЕО")
        time.sleep(3)
        print("Ви пішли прямо та побачили двух людей  з сумками.")
        time.sleep(4)
        print("Що ви будете робити")
        strelka = input("1) Підійти до них ззаду та взяти в полон; 2) Вистрелити в одного з них;")
        if strelka == "1":
            print("Коли ви підійшли ззаду один з них обернувся та вистрелив вам в шию")
            time.sleep(5)
            print("GAME OVER:спробуйте ще раз")
        else:
            print("Ви вистрели в одного з них, він впав, а другий втік за угол")
            time.sleep(4)
            print("*Ви зліва почули звуки машини та стрілянину")
            time.sleep(3)
            print("ТАНК повідомив по рації що інформація штабу не достовірна  що їх в групі не п'ять а більше. Та що тількищо підїхав Синій фургон та з нього розстреляли КІБОРГА та РОМЕО. Вони не вижили.")
            time.sleep(10)
            print("Ви залишилися в трьох")
            time.sleep(2)
            print("Ви з ЛЕОПАРДОМ побачили як перед вами почав проїзджати синій фургон.")
            time.sleep(4)
            print("Що робити?")
            time.sleep(2)
            strelka2 = input("1)Почати стріляти по ньому; 2)кинути гранату під фургон;")
            if strelka2 == "1":
                print("Ви почали стріляти по ньому але він виявився броньованимю. Відкрилося вікно та знього кинули вам гранату.")
                time.sleep(2)
                print("GAME OVER:спробуйте ще раз")
            else:
                print("Ви відірвали чику та кінули гранату перед фургон. Він взірвався.")
                time.sleep(3)
                print("КІБОРГ повідомив по рації що знешкодив того хто втік від вас.")
                time.sleep(3)
                print("Юхууу! Вітаю! Ви пройшли гру! А тепер спробуйте ще раз тільки за Повітряни сили!")
    else:
        print("В тебе сьогодні завдання!")
        time.sleep(3)
        name = input("Придумай назву своєї групи")
        print("Чудова назва!!")
        time.sleep(1)
        print("З тобою в групі ще 2 людини (КОНОПЛЯ) та (ЛЬОН)")
        time.sleep(3)
        name1 = input("Тепер придумай свій позивний!")
        print("Прекрасно!")
        time.sleep(1)
        print("А, тепер більше подробиць про завдання. 2 хвилини тому, 3 чужі винищувачі зайшли в повітряний простір України! Ваше завдання збити всі три!.")
        time.sleep(6)
        print("А, Тепер вибери собі літака!.")
        time.sleep(2)
        litak = input("1) Су-25; 2)Су-27;")
        print("Чудово!")
        time.sleep(1)
        print("*Ви вилітаєте через 15секунд. Ваш літак оснащений 2 прості ракети та 2 інфо-червоні ракети!")
        time.sleep(4)
        print("Для того щоб стреляти простою ракетою потрібно натиснути R; А, для того щоб інфо-червоною потрібно натиснути U")
        time.sleep(5)
        print("Зам'ятали? ")
        pamyaty = input(" 1)так; 2)ні;")
        while pamyaty != "1":
            time.sleep(5)
            print("Ну що тепер запам'ятали?")
            pamyaty = input("1)так; 2)ні;")
        print("Добре. МИ ВІЛИТАЄМО!!!")
        time.sleep(2)
        print("*Ви вилетіли та через 10 хвилин побачили перед собою 1 ворожий літак")
        time.sleep(3)
        print("Що будете робити?")
        raketa = input("1)натиснути R; 2)натиснути U;")
        if raketa == "1":
            print("Ви запустили просту ракету, але ворог відійшов в сторону та ви промазали. Ворог в відповідь запустив інфо-червону ракету по вам.")
            time.sleep(7)
            print("Що робити?")
            uklon = input("1)повернути штурвал в ліво; 2) повернути штурвал  в право;")
            if uklon == "1":
                print("ви повернули штурвал в ліво, але всеоднао ракета влучила в вас та вас збито.")
                print("GAME OVER:спробуйте ща раз")
            else:
                print("Ви повернули штурвал в право, але ракета всеодно ракета влучила в вас та вас збито.")
                print("GAME OVER:спробуйте ща раз")
        else:
            print("Ви запустили інфо-червону ракету в ворога та влучили! Ворога збито!")
            time.sleep(4)
            print("КОНОПЛЯ повідомляє по рації що ЛЬОНА збито")
            time.sleep(3)
            print("У вас на горизонті з'являється ще один ворожий літак.")
            time.sleep(3)
            print("Що будете робити?")
            raketa = input("1)натиснути R; 2)натиснути U;")
            if raketa == "1":
                print("Ви запустили просту ракету, але ворог відійшов в сторону та ви промазали. Ворог в відповідь запустив інфо-червону ракету по вам.")
                time.sleep(7)
                print("Що робити?")
                uklon = input("1)повернути штурвал в ліво; 2) повернути штурвал  в право;")
                if uklon == "1":
                    print("ви повернули штурвал в ліво, але всеоднао ракета влучила в вас та вас збито.")
                    print("GAME OVER:спробуйте ща раз")
                else:
                    print("Ви повернули штурвал в право, але ракета всеодно ракета влучила в вас та вас збито.")
                    print("GAME OVER:спробуйте ща раз")
            else:
                print("Ви натиснули U та запустили інфо-червону ракету! Ви влучили в ворога! Ворога збито!")
                time.sleep(4)
                print("КОНОПЛЯ повідомив що він теж збив одну ворожу ціль")
                time.sleep(3)
                print("Ви чудово виконали місію! Тепер можете повертатись на базу!")
                time.sleep(3)
                print("Вітаю ви пройшли гру!!")
else:
    print("Помилка! Такої команди немає! Перезавантажте гру!")