"""
this function compares prices of the sites in list
"""
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import browsercookie
import pandas as pd
import time
import re

# for e-mailing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

try:
    file = 'shops.xls'  # get file with data
    xl = pd.ExcelFile(file)  # make a DataFrame
    dfexcel = xl.parse('Лист1')  # parse Sheet1
except FileNotFoundError:  # if no the file
    print("""there must be the file "shop.xls" somewhere""")

def mailsend():
    """
      sending e-mail
      """
    # create message object instance
    msg = MIMEMultipart()

    message = "Thank you"

    # setup the parameters of the message
    password = ""
    msg['From'] = "nixtaganrog@mail.ru"
    msg['To'] = "mfirsoff@mail.ru"
    msg['Subject'] = "Subscription"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.mail.ru: 465')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print
    "successfully sent email to %s:" % (msg['To'])


def wildberries(soup):
    """
      the price for Wildberries
      input: parsed string
      return: price
      """
    ourprice = soup.find('span', {'class': 'final-cost'})  # Получаем строку с ценой
    ourprice = str(ourprice).replace(u'\xa0', '')  # getout non-breaking spaces
    ourprice = str(ourprice).split()  # split the string
    ourprice = str(ourprice[2])[:-1]  # getting element without last symbol
    ourprice = int(ourprice)  # get our price as number

    return ourprice


def ozon(soup):
    """
      the price for Ozon
      input: parsed string
      return: price
      """
    ourprice = soup.find_all('span', {'class': 'c8q7 c8q8'})  # Получаем строку с ценой
    ourprice = str(ourprice).replace(u'\xa0', '')  # getout non-breaking spaces
    ourprice = str(ourprice).split()
    ourprice = str(ourprice[4]).split('>')
    ourprice = re.findall(r'\d+', str(ourprice[1]))  # getting number from string
    ourprice = int(ourprice[0])
    return ourprice


def yandex(soup):
    """
      the price for Yandex
      input: parsed string
      return: price
      """
    ourprice = soup.find_all('span', {'data-tid': 'c3eaad93'})  # Получаем строку с ценой
    ourprice = str(ourprice).replace(' ', '')  # delete all spaces
    ourprice = str(ourprice).split('>')
    ourprice = str(ourprice[1]).split('<')
    ourprice = int(ourprice[0])
    return ourprice


# mailsend()

for i in range(0, len(dfexcel)):  # for each row in Excel file
    ourprice = 0

    while ourprice == 0:  # if cookies is old and function get error we signaling about it and cycle
        try:
            try:  # if Firefox exist
                cj = browsercookie.firefox()  # get cookies from firefox
            except:  # if NOT use static cookie string
                cj = '<CookieJar[<Cookie yandexuid=8817021111596999824 for .admetrica.ru/>, <Cookie ymex=1614628396.oyu.8817021111596999824 for .admetrica.ru/>, <Cookie yp=1612122796.yu.8817021111596999824 for .admetrica.ru/>, <Cookie bx_user_id=7a33d13a004e2bcc445731f731bfedea for .bitrix.info/>, <Cookie browser_data=TTqYzV9nc1lIOSUyRnpCJTJGV0NDcTB2bU5EWUQzbjlIWEFYOSUyQkFyd3RCQ2hEbjJ5YU1WeTNWY2klMkJVUk8yT09yWnJoMTlScW1acDdoemxITlhXTXJYUXlWbm4lMkJNMWclM0QlM0Q for .dnacdn.net/>, <Cookie __cfduid=dca12a31b19dfd49e15eb08ee60496d5e1597006397 for .ecponline.ru/>, <Cookie _ym_d=1597006399 for .ecponline.ru/>, <Cookie _ym_isad=2 for .ecponline.ru/>, <Cookie _ym_uid=1597006399124675758 for .ecponline.ru/>, <Cookie _fbp=fb.1.1597006435066.1439233164 for .etp-region.ru/>, <Cookie _ym_d=1597006435 for .etp-region.ru/>, <Cookie _ym_isad=2 for .etp-region.ru/>, <Cookie _ym_uid=1597006435933181780 for .etp-region.ru/>, <Cookie _ym_visorc_48851510=w for .etp-region.ru/>, <Cookie _ym_d=1597086204 for .etprf.ru/>, <Cookie _ym_isad=2 for .etprf.ru/>, <Cookie _ym_uid=1597086204783742702 for .etprf.ru/>, <Cookie _ym_visorc_44856190=w for .etprf.ru/>, <Cookie NID=204=mG-wANPAuuRtJsZ0t2_Y1qtmDToHhXncf3XnOGgRHEQnZXdDYNtjrLWQnId09YcMxu0BlhrlPutpDDBV4sVwj9Tx9lxE2JlNcPUXj9inI8hur6_YBthSoa4CJKihZRzKBFv0sg6ovjnOOALAx3Till9GS5vNzFA7yXdQATJK5PE for .google.com/>, <Cookie _ym_d=1598794979 for .gosuslugi.ru/>, <Cookie _ym_isad=2 for .gosuslugi.ru/>, <Cookie _ym_uid=1598794979814166619 for .gosuslugi.ru/>, <Cookie _ym_visorc_52235404=b for .gosuslugi.ru/>, <Cookie isSpecialVersion=false for .gosuslugi.ru/>, <Cookie userSelectedLanguage=ru for .gosuslugi.ru/>, <Cookie userSelectedRegion=00000000000 for .gosuslugi.ru/>, <Cookie usi_portal=rBBoD1+6b5Susw7Cgk60Ag== for .gosuslugi.ru/>, <Cookie _ga=GA1.2.756351032.1597006730 for .kontur.ru/>, <Cookie _gat=1 for .kontur.ru/>, <Cookie _gid=GA1.2.2125352199.1597006730 for .kontur.ru/>, <Cookie _ym_d=1597006730 for .kontur.ru/>, <Cookie _ym_isad=2 for .kontur.ru/>, <Cookie _ym_uid=1597006730667907364 for .kontur.ru/>, <Cookie _ym_visorc_24728315=w for .kontur.ru/>, <Cookie ngtoken=LhHLZl8wY4qu2V8gA0rsAg== for .kontur.ru/>, <Cookie VID=1u3IF82JefI000000R0sD4I0:::0-0-0-44aa150:CAASEImCxM0-6zpWB1Vh294Ttz4aYEKzeHsJCOn9SBymfbeRWcSuMQQEQxnAhYsz_qrtM0h7zPgq2Jm9eXi2E4bWwoxCNHwbN5L5bHhM6kwg5sWa2rZOgTpO-fAxa_oDxEF6Tms7cmT9_mmz5ugDoG2uvGbhwg for .mail.ru/>, <Cookie amplitude_id_bcbcf0f0c3bc8d4102bb913afbc350c0mail.ru=eyJkZXZpY2VJZCI6ImM0ODg0OWRlLTI0ODQtNDFhMS1hZTc1LTU5M2Q1MmE5ZDM5MlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5OTk3ODU2MjYwMywibGFzdEV2ZW50VGltZSI6MTU5OTk3ODU2MjYwMywiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9 for .mail.ru/>, <Cookie b=4EgEALDlQBUArNZvGQIAACBUTXBQOKTTnHDilW8onNN1XwgA for .mail.ru/>, <Cookie c=I7kVYAIAACcEAAAUAAAACQAwqR4C for .mail.ru/>, <Cookie cto_bundle=qSCGOV9nc1lIOSUyRnpCJTJGV0NDcTB2bU5EWUQzbnNSTldGNWRCcG56QmxLc1hoeGNOaXFJTjVOWGtrSVpOcnhSQjJld2dLdGZqVjN3Qm9jUkVoSlo5d0s1YkFlVmJYbWhYQkhGMTZhJTJGOSUyQjhOSXgxaTJPQWVKcndWSyUyRmdKTnkyV1RsV3JCJTJGNEhrQmdTM25rMnRsd1hhJTJGJTJGZjBvU2h3JTNEJTNE for .mail.ru/>, <Cookie gp=811013 for .mail.ru/>, <Cookie i=AQAiuRVgAgATAAgQBTcHATsHAT0HAcUIAXseAb0HCAQBpgEB for .mail.ru/>, <Cookie mrcu=BD2E5F30488D58858165997EAE5F for .mail.ru/>, <Cookie p=umAEAJ92bQAA for .mail.ru/>, <Cookie rbcnt=956636 for .mail.ru/>, <Cookie s=ww=1366|wh=590|fver=0 for .mail.ru/>, <Cookie searchuid=8817021111596999824 for .mail.ru/>, <Cookie tmr_lvid=cec5d8c26789c63b42dc6db0dbfe1603 for .mail.ru/>, <Cookie tmr_lvidTS=1596999822801 for .mail.ru/>, <Cookie tmr_reqNum=42 for .mail.ru/>, <Cookie _ym_uid=1597006728947393704 for .market.yandex.ru/>, <Cookie dist_hide=0 for .market.yandex.ru/>, <Cookie sync_cookie_csrf=3953031054fake for .mc.admetrica.ru/>, <Cookie sync_cookie_ok=synced for .mc.admetrica.ru/>, <Cookie sync_cookie_csrf=2841735838fake for .mc.yandex.ru/>, <Cookie mdtr_soc=yqtLX18ijT4ApgHOaqes for .mediator.mail.ru/script/>, <Cookie VID=2CyOPi3GpcXz00000R0sD4Hz:::0-0-0-466048e:CAASENq0CXD_lOkpQ2LcxcuC7IAaYOrtQg671s6it7pHllSvoxCziVEyflRz8PFAqJcOJ9dGRRRQWLuAVRgIQFALNeMOcrZz50vTygB7ufaGoDRbv83MGBsWb1tnjQnYiG1WSAAS4f5vC9VdDPPzDT0acz3bDA for .mytopf.com/>, <Cookie _ym_d=1606053771 for .nalog.ru/>, <Cookie _ym_isad=2 for .nalog.ru/>, <Cookie _ym_uid=1606053771142210083 for .nalog.ru/>, <Cookie _ym_visorc=b for .nalog.ru/>, <Cookie _statid=ff140571-49b9-46cf-be75-369a993eefd9 for .ok.ru/>, <Cookie bci=554340309634936588 for .ok.ru/>, <Cookie __Secure-ab-group=45 for .ozon.ru/>, <Cookie __Secure-access-token=3.0.jesAiQ-tR36-KIvCj8wRYw.45.l8cMBQAAAABgFbu0ESG-Y6N3ZWKgAICQoA..20210130220404.W-2TC467Tny6YNzrTkbWmr971fh3x9dmmIaG0DbhsRY for .ozon.ru/>, <Cookie __Secure-ext_xcid=caf40a3fc870e3b2211ba27a6afd1f58 for .ozon.ru/>, <Cookie __Secure-refresh-token=3.0.jesAiQ-tR36-KIvCj8wRYw.45.l8cMBQAAAABgFbu0ESG-Y6N3ZWKgAICQoA..20210130220404.GcxBpgY2lYegA2wsgh4vzG6jf7-BTZDH_R94L9KgH0A for .ozon.ru/>, <Cookie __Secure-user-id=0 for .ozon.ru/>, <Cookie __exponea_etc__=1d7b52b4-2d33-46ff-81e4-73b16696184d for .ozon.ru/>, <Cookie __exponea_time2__=-1.7210087776184082 for .ozon.ru/>, <Cookie _dc_gtm_UA-37420525-1=1 for .ozon.ru/>, <Cookie _ga=GA1.2.1064065215.1612037048 for .ozon.ru/>, <Cookie _gat_UA-37420525-1=1 for .ozon.ru/>, <Cookie _gcl_au=1.1.34265469.1612037047 for .ozon.ru/>, <Cookie _gid=GA1.2.1862244835.1612037048 for .ozon.ru/>, <Cookie cto_bundle=5d6_819nc1lIOSUyRnpCJTJGV0NDcTB2bU5EWUQzaDRjNDRGcTZYTFRPRGZibFZIaGgzYzNyZ295JTJCUktNeGZ3YldJVWxYOGUlMkJNTDB1WlZSNEdwaEVkeksyNXVmcTklMkZtdzhBMW5RSkxKYUpHVlF0THRpNUE3Z0FVSjVGS25oQW5acmdpUWZNU3U3aGJNVVIwZ0ZNczFNOUdsQXdHOUdnJTNEJTNE for .ozon.ru/>, <Cookie tmr_lvid=95268506e3ae32a4f199fb6dcc91da7f for .ozon.ru/>, <Cookie tmr_lvidTS=1612037048049 for .ozon.ru/>, <Cookie tmr_reqNum=2 for .ozon.ru/>, <Cookie visid_incap_1101384=IGmZhCyCSGKohzIiGjzTtbO7FWAAAAAAQUIPAAAAAABDzJV7deA52YWuuPtB+g7W for .ozon.ru/>, <Cookie Cookie_check=checked for .pokupki.market.yandex.ru/>, <Cookie reviews-merge=true for .pokupki.market.yandex.ru/>, <Cookie server_request_id_blue-market:product=1612036411471%2F1c23e882a7893e94c5b4ab7923ba0500 for .pokupki.market.yandex.ru/>, <Cookie visits=1612036411-1612036411-1612036411 for .pokupki.market.yandex.ru/>, <Cookie fsts=1598794693 for .relap.io/>, <Cookie hllc=1 for .relap.io/>, <Cookie lsts=1612036393 for .relap.io/>, <Cookie rlprp=Fe1ANQ&yw5ANQ&LNhANQ--1d4458dcc2016afb9543b195cc0298510e931f11 for .relap.io/>, <Cookie unique=mJ2eVQac for .relap.io/>, <Cookie _fbp=fb.1.1597006608413.635719805 for .tender-rus.ru/>, <Cookie _ga=GA1.2.1433260403.1597006608 for .tender-rus.ru/>, <Cookie _gat=1 for .tender-rus.ru/>, <Cookie _gid=GA1.2.876467307.1599978566 for .tender-rus.ru/>, <Cookie _ym_d=1597006608 for .tender-rus.ru/>, <Cookie _ym_isad=2 for .tender-rus.ru/>, <Cookie _ym_uid=1597006608860508356 for .tender-rus.ru/>, <Cookie _ym_visorc_26633109=w for .tender-rus.ru/>, <Cookie _ym_visorc_26812653=b for .tender-rus.ru/>, <Cookie ___wbs=0cb0f421-b727-4071-8823-cf0058c521fa.1612036862 for .wildberries.ru/>, <Cookie ___wbu=60465753-57ea-4862-8c84-10bbe8d8d406.1612036862 for .wildberries.ru/>, <Cookie __cpns=2_6_7_8_3_19 for .wildberries.ru/>, <Cookie __pricemargin=1.0-- for .wildberries.ru/>, <Cookie __region=68_69_64_48_38_40_70_33_1_4_30_22_31_66 for .wildberries.ru/>, <Cookie __store=119261_1699_119400_116433_117501_507_3158_120762_117986_2737_117413_119781 for .wildberries.ru/>, <Cookie _dc_gtm_UA-2093267-1=1 for .wildberries.ru/>, <Cookie _ga=GA1.1.193451523.1612036863 for .wildberries.ru/>, <Cookie _ga_TW9NLWX9V5=GS1.1.1612036862.1.0.1612037043.60 for .wildberries.ru/>, <Cookie _gcl_au=1.1.2122086680.1612036863 for .wildberries.ru/>, <Cookie _gid=GA1.2.1592514966.1612036863 for .wildberries.ru/>, <Cookie _wbauid=212255801612036862 for .wildberries.ru/>, <Cookie ncache=119261_1699_119400_116433_117501_507_3158_120762_117986_2737_117413_119781%3B68_69_64_48_38_40_70_33_1_4_30_22_31_66%3B1.0--%3B2_6_7_8_3_19 for .wildberries.ru/>, <Cookie stories_uid=17181612036862658 for .wildberries.ru/>, <Cookie __ym_zz_zz=15970063412558968353101061278315 for .yandex.md/>, <Cookie _ym_d=1597006728 for .yandex.ru/>, <Cookie _ym_isad=2 for .yandex.ru/>, <Cookie _ym_uid=1597006728947393704 for .yandex.ru/>, <Cookie _ym_visorc=b for .yandex.ru/>, <Cookie _ym_wasSynced=%7B%22time%22%3A1597006727505%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D for .yandex.ru/>, <Cookie acclinks= for .yandex.ru/>, <Cookie i=4Kc2KG7XWf1cGgk6lAg9jn8mBKZLk2xLe9daFXYYVouKVopiwJPLv75bzQYfzTD7+FvYpTHAuWyayQXu42NPhUGrH+8= for .yandex.ru/>, <Cookie mda=0 for .yandex.ru/>, <Cookie skid=5995705831612036411 for .yandex.ru/>, <Cookie spravka=dD0xNjEyMDM2NDExO2k9OTUuMTc0LjEyNi4xNTM7dT0xNjEyMDM2NDExNDM0OTg5MjQ3O2g9NDVhNjQyMGRhMTMzMmViNDQ2ZmIxZmZiODM0YTNmOTI= for .yandex.ru/>, <Cookie yabs-frequency=/5/0000000000000000/obImS9K00024F200/ for .yandex.ru/>, <Cookie yandexuid=8817021111596999824 for .yandex.ru/>, <Cookie ymex=1912366728.yrts.1597006728 for .yandex.ru/>, <Cookie yp=1628542727.p_sw.1597006727#1597611528.szm.1:1366x768:1366x626 for .yandex.ru/>, <Cookie sq=%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D1%8C%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%8C for .yandex.ru/meta>, <Cookie sq=%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D1%8C%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%8C for .yandex.ru/page>, <Cookie sc_1597006728825=%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D1%8C%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%8C:crypto.kontur.ru:%2Fsearch%2F:1597006727454360-705913648858849704200114-production-app-host-man-web-yp-226 for .yandex.ru/watch>, <Cookie _fbp=fb.1.1612036415005.232991150 for .yastatic.net/>, <Cookie _ga=GA1.2.7719630.1612036414 for .yastatic.net/>, <Cookie _ga_L4FJH9Z6QX=GS1.1.1612036413.1.0.1612036413.0 for .yastatic.net/>, <Cookie _gat_UA-146150221-1=1 for .yastatic.net/>, <Cookie _gcl_au=1.1.1670471436.1612036413 for .yastatic.net/>, <Cookie _gid=GA1.2.496119760.1612036414 for .yastatic.net/>, <Cookie cto_bundle=T5ye019nc1lIOSUyRnpCJTJGV0NDcTB2bU5EWUQzdmI0dEdSWW9JQVVNTGYxOGFLekZOM2ZkT3p0bzhNeWpreGFLQUpzQ1Jka2tqNXo0JTJCOGh5SXlLUHBOSTZiQ3dVN1NPa05tMU11QUhNNkFadjZZemd4JTJGNGhueWtDd3VJemRuJTJCbjQ2RlBiVFAxMlI3bDN1UHR0RldJclVjc0ZNbVhnJTNEJTNE for .yastatic.net/>, <Cookie GPS=1 for .youtube.com/>, <Cookie VISITOR_INFO1_LIVE=qdFRtupPf6M for .youtube.com/>, <Cookie _ym_d=1596999830 for .zakupki.gov.ru/>, <Cookie _ym_isad=2 for .zakupki.gov.ru/>, <Cookie _ym_uid=1596999830916526241 for .zakupki.gov.ru/>, <Cookie _ym_visorc_36706425=w for .zakupki.gov.ru/>, <Cookie __statGroupId=0d6fb9a5-e769-49a0-a438-86504c356ae3 for crypto.kontur.ru/>, <Cookie _pk_id.28.f224=9ccbccbf6a1c696a.1597006730.1.1597006730.1597006730. for crypto.kontur.ru/>, <Cookie _pk_ref.28.f224=%5B%22%22%2C%22%22%2C1597006730%2C%22https%3A%2F%2Fyandex.ru%2F%22%5D for crypto.kontur.ru/>, <Cookie _pk_ses.28.f224=* for crypto.kontur.ru/>, <Cookie location_city=6373 for crypto.kontur.ru/>, <Cookie location_region=61 for crypto.kontur.ru/>, <Cookie referrer=https%3a%2f%2fyandex.ru for crypto.kontur.ru/>, <Cookie utm=utm_source%3dyandex%26utm_medium%3dorganic for crypto.kontur.ru/>, <Cookie ctx_id=ffffffffaf18761e45525d5f4f58455e445a4a423660 for esia.gosuslugi.ru/>, <Cookie idp_id=647a7f09f9549cba6fc801d73ebe593a for esia.gosuslugi.ru/>, <Cookie oauth_id=123841fb5c15c78192b10c42e029af5c for esia.gosuslugi.ru/aas>, <Cookie BX_USER_ID=7a33d13a004e2bcc445731f731bfedea for etp-region.ru/>, <Cookie LogonNameZRF= for etprf.ru/>, <Cookie ouid=1003315479_2703025637 for google-analytics.bi.owox.com/>, <Cookie tmr_detect=0%7C1612036391740 for mail.ru/>, <Cookie tmr_detect=0%7C1598794735861 for news.mail.ru/>, <Cookie xnpe_09568822-e4af-11e7-9f8d-ac1f6b02225e=1d7b52b4-2d33-46ff-81e4-73b16696184d for ozon-api.exponea.com/>, <Cookie font-balloon-loaded=1 for pokupki.market.yandex.ru/>, <Cookie fonts-loaded=1 for pokupki.market.yandex.ru/>, <Cookie last-loaded-page-id=blue-market%3Aproduct for pokupki.market.yandex.ru/>, <Cookie shbt=wCy6RO for shopnetic.com/>, <Cookie shuniq=R7tMpLUfjEagfwFzo3TsoHexO2w for shopnetic.com/>, <Cookie geobase=a%3A7%3A%7Bs%3A7%3A%22inetnum%22%3Bs%3A28%3A%2295.174.96.0+-+95.174.127.255%22%3Bs%3A7%3A%22country%22%3Bs%3A2%3A%22RU%22%3Bs%3A4%3A%22city%22%3Bs%3A16%3A%22%D0%A2%D0%B0%D0%B3%D0%B0%D0%BD%D1%80%D0%BE%D0%B3%22%3Bs%3A6%3A%22region%22%3Bs%3A35%3A%22%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%3Bs%3A8%3A%22district%22%3Bs%3A44%3A%22%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9+%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%BE%D0%BA%D1%80%D1%83%D0%B3%22%3Bs%3A3%3A%22lat%22%3Bs%3A9%3A%2247.221729%22%3Bs%3A3%3A%22lng%22%3Bs%3A9%3A%2238.893318%22%3B%7D for tender-rus.ru/>, <Cookie sid=0ce64q22dekvtev4pl2s00r3mg for tender-rus.ru/>, <Cookie ufrm=0%3A for tender-rus.ru/>, <Cookie LogonNameZRF=A3FFAAF86B8BF06439717C68237F896874FA0EB4B4EFA0A18C65857AB460F12CD2228F24DBBE1B0846DBFF7700AC61207ED4A47D94D100A86A7982AC902B8D58F6BCDFDFC4B2B9C9F07D20599EED11354BA33792F92757C38AF65B2C7746D56FD3DA8932F57945F54E388F0E321D756021D220E4BAAF8521A6D1A20FB34CB6E97D73432DC430F07194EBA8E7724E0C4C0569F836C9A365FBD345118684D7BACD2CD714A0C3EC922C5B18527E35CC29718A9DB8CE0D3AE0C98CAC22B4A18D0F for webppo.etprf.ru/>, <Cookie .AUTHSKB=270CEDB3A1C6005206B7B7C67BA5E4FAB99BE013D0C2DEE7809D78FD5CB83679FF5DD0DE9262817796D6A73DB159BEBC365A4B5512D132548222C02AD543EA560FFDFBA8185189B0CA37450215886FF07F922CEA7C9F14B59F1D92D7BE17415D6177C736442F651C251AE18C208E51B5FC82192C02E27E2DDDAB253E86C2E2CE2C40C404E69942A53FA5EBF0566FF6972A020F6E0E82183F63A69B47DFA6C3933B8C65718C8C4691F0F94DFF048D81553B7C0A50 for widget-product.kontur.ru/>, <Cookie spwuid=bgWeAaKd484wQPiuqWG50Hhd%2fVOPIm8KIhLK9uGCwJehlAHS8SQnJt3sw5r%2bXNTt5huulMv7ejOze2%2fwAi%2bmhYRE3SXkfFqv0%2fTtzNh%2fgXDYy7Lh for widget-product.kontur.ru/>, <Cookie NSC_q00qhvxfc=ffffffffaf18371b45525d5f4f58455e445a4a423df2 for www.gosuslugi.ru/>, <Cookie locationSelectionTypeIsShown=true for www.gosuslugi.ru/>, <Cookie SessionID=jesAiQ-tR36-KIvCj8wRYw for www.ozon.ru/>, <Cookie abGroup=45 for www.ozon.ru/>, <Cookie access_token=3.0.jesAiQ-tR36-KIvCj8wRYw.45.l8cMBQAAAABgFbu0ESG-Y6N3ZWKgAICQoA..20210130220404.W-2TC467Tny6YNzrTkbWmr971fh3x9dmmIaG0DbhsRY for www.ozon.ru/>, <Cookie cnt_of_orders=0 for www.ozon.ru/>, <Cookie isBuyer=0 for www.ozon.ru/>, <Cookie refresh_token=3.0.jesAiQ-tR36-KIvCj8wRYw.45.l8cMBQAAAABgFbu0ESG-Y6N3ZWKgAICQoA..20210130220404.GcxBpgY2lYegA2wsgh4vzG6jf7-BTZDH_R94L9KgH0A for www.ozon.ru/>, <Cookie token_expiration=2021-01-31T01:04:04.287424+03:00 for www.ozon.ru/>, <Cookie userId=0 for www.ozon.ru/>, <Cookie BasketUID=6a5f9cf8-3031-46ac-af47-f5b1b41199b7 for www.wildberries.ru/>, <Cookie __wbl=cityId%3D5729%26regionId%3D61%26city%3D%D0%A2%D0%B0%D0%B3%D0%B0%D0%BD%D1%80%D0%BE%D0%B3%26phone%3D88001007505%26latitude%3D47%2C209574%26longitude%3D38%2C932031 for www.wildberries.ru/>, <Cookie _pk_id.1.034e=7af73503c3f63c7b.1612036863.1.1612036863.1612036863. for www.wildberries.ru/>, <Cookie _pk_ses.1.034e=* for www.wildberries.ru/>]>'

            req = requests.get(dfexcel.iloc[i]['URL'], headers={'User-Agent': UserAgent().Firefox},
                               cookies=cj)  # отправляем HTTP запрос подставляя фэйковый запрос
            req.encoding = 'utf8'  # определяем кодировку
            htmlString = req.text
            soup = BeautifulSoup(htmlString)  # Отправляем полученную страницу в библиотеку для парсинга

            if dfexcel.iloc[i]['Site'] == dfexcel.iloc[i - 1]['Site']:  # if same site again waiting because blocks
                time.sleep(3)

            ourprice = locals()[dfexcel.iloc[i]['Site']](soup)  # get function from string

            print(ourprice)

            if ourprice < dfexcel.iloc[i]['Price']:  # if price decrease
                print('In ', dfexcel.iloc[i]['URL'], ' \n is price decreased \n was ', dfexcel.iloc[i]['Price'], '\n now ',
                      ourprice)
                wait = input("Press Enter to continue.")

        # в цикле получим ответ страницы как она нас видит
        # for key, value in req.request.headers.items():
        #     print(key+": "+value)


        except IndexError:  # if get bann
            print('The Site blocks Your cookies. You need open Firefox and go by link')
            print(dfexcel.iloc[i]['URL'])
            print('Enter the capcha')
            wait = input("And press Enter to continue after that.")

            # print(cj)


