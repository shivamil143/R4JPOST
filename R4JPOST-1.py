from urllib import response

import mechanize

import os

import datetime

import sys

from time import sleep

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

    msg1=str(input("➣R0ME0 KI MKC K4 2 FECTOR CODE : "))

    print(msg1)

    browser.form['approvals_code'] = msg1

    r=browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()

    

    

def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    r = browser.submit()

print ("[-[ TH3 T00L P00L CREATE BY R4JV33R SINGH4NIY4 ]-]")

emailx=str(input("➣ROMEO KI MKC K4 M4IL : "))

pwx =str(input("➣ROMEO KI MKC K4 P4SSWORD : "))

aclass()

msg4=str(input("➣ENTER ROMEO KI MKC K4 P0ST LINK : "))

np1 = str(input("➣T4TT4 K4 N4M3 LIKH BSDK : "))

msg5=str(input("➣ENTER ROMEO KI MKC K4 N0TEP4D : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣SHIWU KI MKC KO CHODNE KI TIME SPEED : "))

os.system('clear')

sys.stdout.flush()

print('R4JV33R B44P H3R3 v1.0')

count = 0

while True:

    for line in lines:

        if len(line) > 3:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            poct(np1+line)

            print("--> Y3 GY4 MSG SHIWU KI M4 K3 BHOSDE M3 :v ::-->> ", np1, line, "\n")

            count += 1

            if count % 10 == 0:

                sleep(1)

                

                

                
