import os, requests, textwrap
from subprocess import call
from colorama import Fore, Back, Style
from googlesearch import search
from lxml.html import fromstring

call('clear' if os.name =='posix' else 'cls')

print("""
DDDDD      OOOOO    RRRRRR   XX    XX 
DD  DD    OO   OO   RR   RR   XX  XX  
DD   DD  OO     OO  RRRRRR     XXXX   
DD   DD   OO   OO   RR  RR    XX  XX  
DDDDDD     OOOO0    RR   RR  XX    XX 
                                  
                                  ALPHA""")

headers = {"User-Agent":"Mozilla/5.0 (X11; CrOS x86_64 14150.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.124 Safari/537.36"}
dork = str(input(f"dork: ").lower()) #insert dork
n = int(input("num:")) #number of result
t = str(dork+".txt")
s = search(dork,num_results=n)
f = open(t,"w")
f.write("# Dork: "+dork+"\n\n")
url = []

for line in s:
    url.append(line)
    print(Fore.GREEN+" found "+Style.RESET_ALL+" "+line)

for u in url:
    try:
        req = requests.get(u,headers=headers)
        req_s = fromstring(req.content)
        string = req_s.findtext(".//title")
        wrapper = textwrap.TextWrapper(width=47)
        dedented_text = textwrap.dedent(text=string)
        original = wrapper.fill(text=dedented_text)
        shortened = textwrap.shorten(text=original, width=47)
        title = wrapper.fill(text=shortened)
        f.write(u+"\n")
    except TypeError: pass
    except requests.exceptions.InvalidSchema: pass
    except requests.exceptions.ConnectionError: break
    except KeyboardInterrupt: break

f.close()
print(Fore.RED+f"{str(len(url))}"+Style.RESET_ALL+" retrieved as: "+t)
