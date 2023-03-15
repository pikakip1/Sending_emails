import smtplib
import os
from dotenv import load_dotenv

load_dotenv('info.env')

smtp_username = os.environ.get('LOGIN')
smtp_password = os.environ.get('PASSWORD')


text = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

ref_link = 'https://dvmn.org/referrals/FtZnPHHDWCtyvpn9MSDT79zrpaw36Hj3qJ4kw4DP/'
text = text.replace('%website%', ref_link)
text = text.replace('%friend_name%','Евгений')
text = text.replace('%my_name%','Влад')
my_email = 'pikakip1@mail.ru'
subject = 'Приглашение!'
email_user = 'pikakip22@yandex.ru'

title = """\
From: {}
To: {}
Subject: {}
Content-Type: text/plain; charset="UTF-8";

Привет, {}! {} приглашает тебя на сайт dvmn.org!

{}""".format(my_email,email_user,subject,'Евгений','Влад',text)

title = title.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.mail.ru:465')

server.login(smtp_username, smtp_password)
server.sendmail(my_email, email_user, title)

server.quit()