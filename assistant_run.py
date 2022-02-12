from src.assistant import Assistant
from src.time_skill import Time_Skill

bot = Assistant('Janek')
time_skill = Time_Skill()
command = ''
WAKE = 'bot'

bot.respond('Cześć ! Słucham cię !')

while True:
    command = bot.listen().lower()

    #if command.count(WAKE) > 0:
    bot.respond('Gotowy')
    print('Słucham...')
    command = bot.listen().lower()

    if 'dupa' in command:
        bot.respond('ty jesteś ' + command)

    elif 'nazywasz' in command:
        bot.respond('jestem ' + bot.get_name())    

    elif 'dziś dzień' in command:
        bot.respond('Dziś jest ' + str(time_skill.get_date()))

    elif 'godzina' in command:
        bot.respond('Jest ' + str(time_skill.get_time()))

    elif 'tydzień' in command:
        bot.respond('tydzień roku nr. ' + str(time_skill.get_week_number()))

    elif 'wyjście' in command:
        bot.respond('Narazisko')
        break

    else:
        bot.respond('Nie zrozumiałem.')
            

    