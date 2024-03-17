import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup

bot = telebot.TeleBot("7151659098:AAHUkvibjLBydfxM-7phco0NBtoUzioUBmY")

#ТУРНИРНАЯ СЕТКА

#ГРУППОВОЙ ЭТАП ЛЧ
response_s = requests.get("https://www.sports.ru/football/tournament/ucl/table/")
text_s = response_s.text
soup_group = BeautifulSoup(text_s, 'html.parser')
tab_group = soup_group.find_all('div', class_='main-column--full-width')

#1/8 ФИНАЛА ЛЧ
response_18 = requests.get("https://matchtv.ru/football/ucl/stats/season_20955/tour_-8")
text_18 = response_18.text
soup_18 = BeautifulSoup(text_18, 'html.parser')
tab_18 = soup_18.find_all('div', class_='statistics-table statistics-table_stats-games')

#1/4 ФИНАЛА ЛЧ
response_14 = requests.get("https://matchtv.ru/football/ucl/stats/season_20955/tour_-4")
text_14 = response_14.text
soup_14 = BeautifulSoup(text_14, 'html.parser')
tab_14 = soup_14.find_all('div', class_='statistics-table statistics-table_stats-games')

#1/2 ФИНАЛА ЛЧ
response_12 = requests.get("https://matchtv.ru/football/ucl/stats/season_20955/tour_-2")
text_12 = response_12.text
soup_12 = BeautifulSoup(text_12, 'html.parser')
tab_12 = soup_12.find_all('div', class_='statistics-table statistics-table_stats-games')

#ФИНАЛ ЛЧ
response_final = requests.get("https://matchtv.ru/football/ucl/stats/season_20955/tour_-final")
text_final = response_final.text
soup_final = BeautifulSoup(text_final, 'html.parser')
tab_final = soup_final.find_all('div', class_='statistics-table statistics-table_stats-games')

#ТОП 5 ИГРОКОВ ЛЧ
response5_lch = requests.get("https://news.sportbox.ru/Vidy_sporta/Futbol/Liga_Chempionov/stats/leaders_1")
text5_lch = response5_lch.text
soup5_lch = BeautifulSoup(text5_lch, 'html.parser')
players5_lch = soup5_lch.find_all('span', class_='player-name')
goals5_lch = soup5_lch.find_all(attrs={'title': 'Голы (Голы с пенальти)'})

#ТОП ПЯТЬ ЛИГ

#АПЛ
response_apl = requests.get("https://matchtv.ru/football/england/stats")
text_apl = response_apl.text
soup_apl = BeautifulSoup(text_apl, 'html.parser')
tab_apl = soup_apl.find_all('table', class_='global-table global-table_mode_modern show-t')

#Ла-Лига
response_spain = requests.get("https://matchtv.ru/football/spain/stats")
text_spain = response_spain.text
soup_spain = BeautifulSoup(text_spain, 'html.parser')
tab_spain = soup_spain.find_all('table', class_='global-table global-table_mode_modern show-t')

#СериаА
response_italy = requests.get("https://matchtv.ru/football/italy/stats")
text_italy = response_italy.text
soup_italy = BeautifulSoup(text_italy, 'html.parser')
tab_italy = soup_italy.find_all('table', class_='global-table global-table_mode_modern show-t')

#Бундеслига
response_germ = requests.get("https://matchtv.ru/football/germany/stats")
text_germ = response_germ.text
soup_germ = BeautifulSoup(text_germ, 'html.parser')
tab_germ = soup_germ.find_all('table', class_='global-table global-table_mode_modern show-t')

#Лига1
response_france = requests.get("https://matchtv.ru/football/france/stats")
text_france = response_france.text
soup_france = BeautifulSoup(text_france, 'html.parser')
tab_france = soup_france.find_all('table', class_='global-table global-table_mode_modern show-t')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Веб-Сайт')
    start = types.KeyboardButton('Начать')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Что?', reply_markup=markup)

@bot.message_handler(commands=['start'])
def foo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    webAppTest = types.WebAppInfo("https://ru.uefa.com/")
    my_site = types.KeyboardButton(text='Перейти на сайт UEFA', web_app=webAppTest)
    champ_league = types.KeyboardButton('Лига Чемпионов')
    five_league = types.KeyboardButton('Топ-5 Чемпионатов')
    markup.row(champ_league, five_league)
    markup.row(my_site)
    bot.send_message(message.chat.id, f'Что Вы хотите выбрать?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def champ_league(message):
    if message.text == 'Лига Чемпионов':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        player_lch = types.KeyboardButton('Топ-5 бомбардиров ЛЧ')
        tournament_lch = types.KeyboardButton('Турнирная сетка')
        go_back = types.KeyboardButton('Назад')
        murkup.row(tournament_lch, player_lch, go_back)
        bot.send_message(message.chat.id, 'Выберите, что вы хотите узнать?', reply_markup=murkup)

    elif message.text == 'Топ-5 Чемпионатов':
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        apl = types.KeyboardButton('АПЛ')
        la_liga = types.KeyboardButton('Ла-Лига')
        seria_a = types.KeyboardButton('Серия А')
        bubdes_league = types.KeyboardButton('Бундеслига')
        liga_1 = types.KeyboardButton('Лига 1')
        go_back = types.KeyboardButton('Назад')
        murkup.row(apl, la_liga, seria_a, bubdes_league, liga_1)
        murkup.row(go_back)
        bot.send_message(message.chat.id, 'Выберите лигу', reply_markup=murkup)

    elif message.text == 'Турнирная сетка':                                                                             #ТУРНИРНАЯ СЕТКА
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        group_stage = types.KeyboardButton('Групповой этап')
        one_eight = types.KeyboardButton('1/8')
        quarter_finals = types.KeyboardButton('1/4')
        semi_finals = types.KeyboardButton('1/2')
        final = types.KeyboardButton('Финал')
        go_back = types.KeyboardButton('Назад')
        murkup.row(group_stage, one_eight, quarter_finals, semi_finals, final)
        murkup.row(go_back)
        bot.send_message(message.chat.id, 'Выберите стадию', reply_markup=murkup)


    elif message.text == 'Групповой этап':

        sp_gr = []
        for i in tab_group:
            sp_gr.append(i.text.split())

        sp_group = sp_gr[0][23:]

        cnt_group = 0
        tab_cnt_group = 0
        num_group = 10

        (sp_group.remove('Манчестер'), sp_group.remove('Манчестер'), sp_group.remove('Реал'), sp_group.remove('Реал'),
         sp_group.remove('Д'),
         sp_group.remove('Берлин'), sp_group.remove('Булл'), sp_group.remove('Лейпциг'), sp_group.remove('Янг'),
         sp_group.remove('Звезда'))

        lch_group = ''

        for i in sp_group:
            lch_group += f' {i} '
            cnt_group += 1
            tab_cnt_group += 1
            if i == 'Группа':
                num_group = 10
            if cnt_group == num_group:
                lch_group += '\n'
                cnt_group = 0
                num_group = 9
            if tab_cnt_group == 46:
                lch_group += '\n'
                tab_cnt_group = 0

        bot.send_message(message.chat.id, lch_group)

    elif message.text == '1/8':

        sp_18 = []

        for i in tab_18:
            sp_18.append(i.text.split())
        sp_one_eight = sp_18[0][1:]

        sp_one_eight.remove('Манчестер'), sp_one_eight.remove('Манчестер')
        sp_one_eight.remove('Сосьедад'), sp_one_eight.remove('Сосьедад')
        sp_one_eight.remove('(по'), sp_one_eight.remove('пен.'), sp_one_eight.remove('4:2)')

        lch_18 = ''
        cnt_18 = 0

        for i in sp_one_eight:
            lch_18 += f' {i} '
            cnt_18 += 1
            if cnt_18 == 7:
                lch_18 += '\n'
                cnt_18 = 0

        bot.send_message(message.chat.id, lch_18)

    elif message.text == '1/4':
        if response_final.status_code == 404:
            bot.send_message(message.chat.id, 'К сожалению, данный этап турнира еще не прошёл')
        else:
            bot.send_message(message.chat.id, 'Скоро получим ифнормацию!')

    elif message.text == '1/2':
        if response_final.status_code == 404:
            bot.send_message(message.chat.id, 'К сожалению, данный этап турнира еще не прошёл')
        else:
            bot.send_message(message.chat.id, 'Скоро получим ифнормацию!')

    elif message.text == 'Финал':
        if response_final.status_code == 404:
            bot.send_message(message.chat.id, 'К сожалению, данный этап турнира еще не прошёл')
        else:
            bot.send_message(message.chat.id, 'Скоро получим ифнормацию!')

    elif message.text == 'Топ-5 бомбардиров ЛЧ':

        sp_players = [players5_lch[i].text.split() for i in range(5)]
        sp_goals = [goals5_lch[i].text.split() for i in range(1, 6)]

        top_5_lch_zip = list(zip(sp_players, sp_goals))
        top_5_lch = ('Игрок / Клуб, Г(П)\n'
                     '--------------------------------\n')

        for i, k in top_5_lch_zip:
            top_5_lch += f"{' '.join(i)}, {' '.join(k)}\n"
        bot.send_message(message.chat.id, top_5_lch)

    elif message.text == 'АПЛ':

        lst = [i.text.split() for i in tab_apl]
        lst_base = lst[0][0:8]
        lst_base[2], lst_base[3], lst_base[4], lst_base[5] = 'Игр', 'Выйгрышей', 'Ничья', 'Проигрышей'
        lst_base[6], lst_base[7] = 'Забито-пропущено', 'Очки'
        lst_new = lst[0][8:]

        apl_base = ' | '.join(lst_base)

        apl_s = ''
        apl_cnt = 0

        (lst_new.pop(17), lst_new.pop(25),
         lst_new.pop(49), lst_new.pop(106),
         lst_new.pop(131), lst_new.pop(156))

        for i in lst_new:
            apl_s += f' {i} |'
            apl_cnt += 1
            if apl_cnt == 8:
                apl_s += '\n'
                apl_cnt = 0
        res_apl = apl_base + '\n' + '-------------------------------------------' + '\n' + apl_s
        bot.send_message(message.chat.id, res_apl)

    elif message.text == 'Ла-Лига' or message.text == 'Ла Лига':

        lst = [i.text.split() for i in tab_spain]
        lst_base = lst[0][0:8]
        lst_base[2], lst_base[3], lst_base[4], lst_base[5] = 'Игр', 'Выйгрышей', 'Ничья', 'Проигрышей'
        lst_base[6], lst_base[7] = 'Забито-пропущено', 'Очки'
        lst_new = lst[0][8:]

        spain_base = ' | '.join(lst_base)

        spain_s = ''
        spain_cnt = 0

        lst_new.pop(41), lst_new.pop(122)

        for i in lst_new:
            spain_s += f' {i} |'
            spain_cnt += 1
            if spain_cnt == 8:
                spain_s += '\n'
                spain_cnt = 0

        res_spain = spain_base + '\n' + '-------------------------------------------' + '\n' + spain_s

        bot.send_message(message.chat.id, res_spain)

    elif message.text == 'Серия А':

        lst = [i.text.split() for i in tab_italy]
        lst_base = lst[0][0:8]
        lst_base[2], lst_base[3], lst_base[4], lst_base[5] = 'Игр', 'Выйгрышей', 'Ничья', 'Проигрышей'
        lst_base[6], lst_base[7] = 'Забито-пропущено', 'Очки'
        lst_new = lst[0][8:]

        italy_base = ' | '.join(lst_base)

        italy_s = ''
        italy_cnt = 0

        for i in lst_new:
            italy_s += f' {i} |'
            italy_cnt += 1
            if italy_cnt == 8:
                italy_s += '\n'
                italy_cnt = 0

        res_italy = italy_base + '\n' + '-------------------------------------------' + '\n' + italy_s

        bot.send_message(message.chat.id, res_italy)

    elif message.text == 'Бундеслига':

        lst = [i.text.split() for i in tab_germ]
        lst_base = lst[0][0:8]
        lst_base[2], lst_base[3], lst_base[4], lst_base[5] = 'Игр', 'Выйгрышей', 'Ничья', 'Проигрышей'
        lst_base[6], lst_base[7] = 'Забито-пропущено', 'Очки'
        lst_new = lst[0][8:]

        germ_base = ' | '.join(lst_base)

        lst_new.remove('Д'), lst_new.remove('М')

        germ_s = ''
        germ_cnt = 0

        for i in lst_new:
            germ_s += f' {i} |'
            germ_cnt += 1
            if germ_cnt == 8:
                germ_s += '\n'
                germ_cnt = 0

        res_germ = germ_base + '\n' + '-------------------------------------------' + '\n' + germ_s

        bot.send_message(message.chat.id, res_germ)

    elif message.text == 'Лига 1':

        lst = [i.text.split() for i in tab_france]
        lst_base = lst[0][0:8]
        lst_base[2], lst_base[3], lst_base[4], lst_base[5] = 'Игр', 'Выйгрышей', 'Ничья', 'Проигрышей'
        lst_base[6], lst_base[7] = 'Забито-пропущено', 'Очки'
        lst_new = lst[0][8:]

        france_base = ' | '.join(lst_base)

        france_s = ''
        france_cnt = 0

        for i in lst_new:
            france_s += f' {i} |'
            france_cnt += 1
            if france_cnt == 8:
                france_s += '\n'
                france_cnt = 0

        res_france = france_base + '\n' + '-------------------------------------------' + '\n' + france_s

        bot.send_message(message.chat.id, res_france)

    elif message.text == 'Назад':
        foo(message)


bot.polling(non_stop=True)