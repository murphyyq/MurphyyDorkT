# -*- coding: utf-8 -*- 
from colorama import Fore , Back , Style 
import sys
import time
import os


#--------------------------------------------------------
#-----------------Yazma efekti fonksiyonu----------------
def yaziyor(yazi):
    for karakter in yazi:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.05)
def yaziyor1(yazi):
    for karakter in yazi:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.1)
#--------------------------------------------------------




os.system('apt install figlet')
os.system('apt install toilet')
os.system('clear')
baslik = (os.system('toilet -f smblock --filter metal "murphyyDorkT v0.1"'))

print(yaziyor(Fore.YELLOW+"Kontrolleri sağlıyorum , Sqlmap yüklümü ? Değilse Yüklüyorum..."+Style.RESET_ALL))
print(time.sleep(2))
os.system('apt install sqlmap && clear')
print(os.system('toilet -f smblock --filter metal "murphyyDorkT v0.1"'))
print(yaziyor1(Fore.YELLOW+'\n\n\nHerşey yüklü , Başlıyorum'+Style.RESET_ALL))
print(yaziyor1(Back.BLACK+"Taramak istediğiniz Dork'u Yazınız: "+Style.RESET_ALL))
cevap = input(Fore.LIGHTGREEN_EX+""+Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX+ cevap + Style.RESET_ALL , yaziyor(' Dork Taranıyor...'))
os.system('sqlmap -g'+ cevap)


