import requests, colorama, os, time, json
from colorama import Fore, Back, Style,init
init()

# Example
# proxies = {'https': 'https://johnsmith:PASSWORD@66.78.45.72:2212'}

proxies = {}

def init():
    print(Fore.CYAN + "eBay Viewbot v1.0" + Fore.WHITE)
    eBayURL = input("eBay URL: ")
    eBayViews = input("Amount of views: ")
    os.system('cls')
    print("Sending views to"+Fore.GREEN+" "+eBayURL + Fore.WHITE)
    for i in range(int(eBayViews)):
        if not proxies:
            rq = requests.get(eBayURL)
            print(Fore.GREEN+"[Success] Sent view without using a proxy")
        else:
            rq = requests.get(eBayURL,proxies=proxies)
            print(Fore.GREEN+"[Success] Sent view using a proxy")



init()
