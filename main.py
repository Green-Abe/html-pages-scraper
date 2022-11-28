import json
import time
from time import sleep
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
import json

info=[]
inf=[]
inn=[]
iz=[]
fiz=[]
siz=[]
sev=[]
eig=[]
noin=[]
tan=[]
heb=[]
hec=[]
hed=[]
hee=[]
hef=[]
path=r"C:\Users\abe\Downloads\fb_selnium\fb"
options = FirefoxOptions()
options.add_argument("--headless")
driver =webdriver.Firefox(options=options)

coach='Coaching/Technical Director'
president='President'
registrar='Registrar'
referee='Referee Assignor'
executive='Executive Director'


with open('one.json','r') as f:
    config=json.load(f)

for i in range(261): #261
    k=config['0'][str(i)]
    url = "https://norcalpremier.com/"+f'{k}'
    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(7)
    driver.implicitly_wait(95) 
    html=driver.page_source
#print(html)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    one=soup.select('div.sidebar-contact:nth-child(1) > h2:nth-child(2)')
    tone=soup.select('div.sidebar-contact:nth-child(1) > h5:nth-child(1)')
    eone=soup.select('div.sidebar-contact:nth-child(1) > a:nth-child(3)')

    two=soup.select('div.sidebar-contact:nth-child(2) > h2:nth-child(2)')
    ttwo=soup.select('div.sidebar-contact:nth-child(2) > h5:nth-child(1)')
    etwo=soup.select('div.sidebar-contact:nth-child(2) > a:nth-child(3)')

    three=soup.select('div.sidebar-contact:nth-child(3) > h2:nth-child(2)')
    tthree=soup.select('div.sidebar-contact:nth-child(3) > h5:nth-child(1)')
    ethree=soup.select('div.sidebar-contact:nth-child(3) > a:nth-child(3)')

    four=soup.select('div.sidebar-contact:nth-child(4) > h2:nth-child(2)')
    tfour=soup.select('div.sidebar-contact:nth-child(4) > h5:nth-child(1)')
    efour=soup.select('div.sidebar-contact:nth-child(4) > a:nth-child(3)')

    five=soup.select('div.sidebar-contact:nth-child(5) > h2:nth-child(2)')
    tfive=soup.select('div.sidebar-contact:nth-child(5) > h5:nth-child(1)')
    efive=soup.select('div.sidebar-contact:nth-child(5) > a:nth-child(3)')

    six=soup.select('div.sidebar-contact:nth-child(6) > h2:nth-child(2)')
    tsix=soup.select('div.sidebar-contact:nth-child(6) > h5:nth-child(1)')
    esix=soup.select('div.sidebar-contact:nth-child(6) > a:nth-child(3)')

    seven=soup.select('div.sidebar-contact:nth-child(7) > h2:nth-child(2)')
    tseven=soup.select('div.sidebar-contact:nth-child(7) > h5:nth-child(1)')
    eseven=soup.select('div.sidebar-contact:nth-child(7) > a:nth-child(3)')

    eight=soup.select('div.sidebar-contact:nth-child(8) > h2:nth-child(2)')
    teight=soup.select('div.sidebar-contact:nth-child(8) > h5:nth-child(1)')
    eeight=soup.select('div.sidebar-contact:nth-child(8) > a:nth-child(3)')
    
    nine=soup.select('div.sidebar-contact:nth-child(9) > h2:nth-child(2)')
    tnine=soup.select('div.sidebar-contact:nth-child(9) > h5:nth-child(1)')
    enine=soup.select('div.sidebar-contact:nth-child(9) > a:nth-child(3)')

    ten=soup.select('div.sidebar-contact:nth-child(10) > h2:nth-child(2)')
    tten=soup.select('div.sidebar-contact:nth-child(10) > h5:nth-child(1)')
    eten=soup.select('div.sidear-bcontact:nth-child(10) > a:nth-child(3)')

    eleven=soup.select('div.sidebar-contact:nth-child(11) > h2:nth-child(2)')
    televen=soup.select('div.sidebar-contact:nth-child(11) > h5:nth-child(1)')
    eeleven=soup.select('div.sidebar-contact:nth-child(11) > a:nth-child(3)')

    twelve=soup.select('div.sidebar-contact:nth-child(12) > h2:nth-child(2)')
    ttwelve=soup.select('div.sidebar-contact:nth-child(12) > h5:nth-child(1)')
    etwelve=soup.select('div.sidebar-contact:nth-child(12) > a:nth-child(3)')

    thirteen=soup.select('div.sidebar-contact:nth-child(13) > h2:nth-child(2)')
    tthirteen=soup.select('div.sidebar-contact:nth-child(13) > h5:nth-child(1)')
    ethirteen=soup.select('div.sidebar-contact:nth-child(13) > a:nth-child(3)')

    forteen=soup.select('div.sidebar-contact:nth-child(14) > h2:nth-child(2)')
    tforteen=soup.select('div.sidebar-contact:nth-child(14) > h5:nth-child(1)')
    eforteen=soup.select('div.sidebar-contact:nth-child(14) > a:nth-child(3)')
    
    fifteen=soup.select('div.sidebar-contact:nth-child(15) > h2:nth-child(2)')
    tfifteen=soup.select('div.sidebar-contact:nth-child(15) > h5:nth-child(1)')
    efifteen=soup.select('div.sidebar-contact:nth-child(15) > a:nth-child(3)')

    address=soup.find('h4',{"class":"masthead-subtitle"}).text
    team=soup.find('h1',{"class":"masthead-title"}).text
   
    
    
    try:
        c1=one
        e1=eone
        bgg={'Team':team,
        'location':address,
        'title':tone[0].text.strip(), 
        'name':c1[0].text.strip(),
        'email':e1[0].text.strip(),
         }

        info.append(bgg)
    except:
        bgg={
        'title':' ', 
        'name':' ',
        'email':' ',
      }

        info.append(bgg)
    try:
        c2=two
        e2=etwo
        bvv={
        'title':ttwo[0].text.strip(), 
        'name':c2[0].text.strip(),
        'email':e2[0].text.strip(),
        }

        inf.append(bvv)
    except:
        bvv={
        'title':' ', 
        'name':' ',
        'email':' ',
      }

        inf.append(bvv)

    try:
        c3=three
        e3=ethree

        bzz={
        'title':tthree[0].text.strip(), 
        'name':c3[0].text.strip(),
        'email':e3[0].text.strip(),

      }

        inn.append(bzz)
    except:
        
       
      bzz={
        'title':' ', 
       'name':' ',
        'email':' ',
      }
      inn.append(bzz)
    try:
        c4=four
        e4=efour
        faz={
        'title':tfour[0].text.strip(), 
        'name':c4[0].text.strip(),
        'email':e4[0].text.strip(),

     }
        iz.append(faz)
    except:
      faz={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
      iz.append(faz)

    try:
        c5=five
        e5=efive
        foz={
        'title':tfive[0].text.strip(), 
        'name':c5[0].text.strip(),
        'email':e5[0].text.strip(),

     }
        fiz.append(foz)


    except:
        foz={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        fiz.append(foz)

    try:
        c6=six
        e6=esix
        saz={
        'title':tsix[0].text.strip(), 
        'name':c6[0].text.strip(),
        'email':e6[0].text.strip(),

     }
        siz.append(saz)

    except:
        saz={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        siz.append(saz)

    try :
        c7=seven
        e7=eseven
        sez={
        'title':tseven[0].text.strip(), 
        'name':c7[0].text.strip(),
        'email':e7[0].text.strip(),

        }
        sev.append(sez)
    except:
         sez={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
         sev.append(sez)

    try :
        c8=eight
        e8=eeight
        egh={
        'title':teight[0].text.strip(), 
        'name':c8[0].text.strip(),
        'email':e8[0].text.strip(),

        }
        eig.append(egh)
    except:
        egh={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        eig.append(egh)

    try :
        c9=nine
        e9=enine
        nein={
        'title':tnine[0].text.strip(), 
        'name':c9[0].text.strip(),
        'email':e9[0].text.strip(),

        }
        noin.append(nein)
    except:
        nein={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        noin.append(nein)

    try :
        c10=ten
        e10=eten
        ton={
        'title':tten[0].text.strip(), 
        'name':c10[0].text.strip(),
        'email':e10[0].text.strip(),

        }
        tan.append(ton)
    except:
        ton={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        tan.append(ton)
    try :
        c11=eleven
        e11=eeleven
        hebb={
        'title':televen[0].text.strip(), 
        'name':c11[0].text.strip(),
        'email':e11[0].text.strip(),

        }
        heb.append(hebb)
    except:
        hebb={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        heb.append(hebb)

    try :
        c12=twelve
        e12=etwelve
        hecc={
        'title':ttwelve[0].text.strip(), 
        'name':c12[0].text.strip(),
        'email':e12[0].text.strip(),

        }
        hec.append(hecc)
    except:
        hecc={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        hec.append(hecc)

    try :
        c13=thirteen
        e13=ethirteen
        hedd={
        'title':tthirteen[0].text.strip(), 
        'name':c13[0].text.strip(),
        'email':e13[0].text.strip(),

        }
        hed.append(hedd)
    except:
        hedd={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        hed.append(hedd)
    
    try :
        c14=forteen
        e14=efifteen
        hezz={
        'title':tforteen[0].text.strip(), 
        'name':c14[0].text.strip(),
        'email':e14[0].text.strip(),

        }
        hee.append(hezz)
    except:
        hezz={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        hee.append(hezz)
    
    try :
        c15=fifteen
        e15=efifteen
        heff={
        'title':tfifteen[0].text.strip(), 
        'name':c15[0].text.strip(),
        'email':e15[0].text.strip(),

        }
        hef.append(heff)
    except:
        heff={
        'title':' ', 
        'name':' ',
        'email':' ',
      }
        hef.append(heff)
    dd=pd.DataFrame(info)
    dee=pd.DataFrame(inf)
    dzz=pd.DataFrame(inn)
    doo=pd.DataFrame(iz)   
    dooz=pd.DataFrame(fiz)
    booz=pd.DataFrame(siz)
    bob=pd.DataFrame(sev)
    pop=pd.DataFrame(eig)
    pilo=pd.DataFrame(noin)
    pie=pd.DataFrame(tan)
    pow=pd.DataFrame(heb)
    poz=pd.DataFrame(hec)
    pox=pd.DataFrame(hed)
    lio=pd.DataFrame(hee)
    lizz=pd.DataFrame(hef)
    df=pd.concat([dd, dee,dzz,doo,dooz,booz,bob,pop,pilo,pie,pow,poz,pox,lio,lizz], axis=1)

    df.to_excel("last.xlsx")
    print(i)

    
   


        



