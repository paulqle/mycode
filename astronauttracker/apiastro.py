#!/usr/bin/env python3

import requests
  
URL = "http://api.open-notify.org/astros.json"
def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp= requests.get(URL)##.json()
    print(type(resp))
    print(dir(resp))
    #astros = resp.json()
    #print(type(astros))
    #print(astros.key())
#</details>
#People in Space:  7
#Mark Vande Hei is on the ISS.
#Oleg Novitskiy is on the ISS.
#Pyotr Dubrov is on the ISS.
#Thomas Pesquet is on the ISS.
#Megan McArthur is on the ISS.
#Shane Kimbrough is on the ISS.
#Akihiko Hoshide is on the ISS.

main()#need this to print out import
