import os
import smtplib
from dotenv import load_dotenv
load_dotenv()
login=os.getenv('LOGIN_YA')
password=os.getenv('PASSWORD_YA')
server=smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login,password)
letter="""From: {mail_from}
To: {mail_to}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name} {my_name} приглашает тебя на сайт {link}!

{link} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {link}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {link}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(mail_from= "YaFEzzz@yandex.ru", mail_to= "YaFEzzz@yandex.ru", subject= "Приглашение!", friend_name= "Мария!", my_name= "Александр", link= "https://dvmn.org/profession-ref-program/iiiiiiiiiiiiiyyyyyyy/NDvX2/")
letter=letter.encode("UTF-8")
server.sendmail("YaFEzzz@yandex.ru", "YaFEzzz@yandex.ru", letter)
server.quit()