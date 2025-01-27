import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

my_mail = os.getenv("NAME")
friend_mail = "DmitryOgurtsov135@yandex.ru"
password = os.getenv("PASSWORD")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(my_mail, password)

letter = """From: {my_mail}
To: {friend_mail}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8"; 

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(my_mail = my_mail, friend_mail = friend_mail)
friend_name = "Игорь"
my_name = "Дмитрий"
link = "https://dvmn.org/profession-ref-program/id478681245/SPY4Y/"
letter = letter.replace("%friend_name%", friend_name )
letter = letter.replace("%my_name%", my_name)
letter = letter.replace("%website%",link )
letter = letter.encode('UTF-8')
server.sendmail(my_mail, friend_mail, letter)
server.quit()



