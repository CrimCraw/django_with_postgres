import requests
from datetime import datetime


def send_msg(**kwargs):
    token = "6318300722:AAGmc_jB5t-CDHe-FPiHUmw4mLTnRmH98R4"  # bot token

    user_id = "5158861192"  # user id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {kwargs}</b>')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())
