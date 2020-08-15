from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

class Ders(object):
    def __init__(self,derskodu,dersadi,kredi,yariyil):
        self.kod=derskodu
        self.ad=dersadi
        self.kredi=kredi
        self.yariyil=yariyil
        self.__harfnotu="G"

    def __str__(self):
        return "{} {} {} {}".format(self.kod,self.ad,self.yariyil,self.kredi)

    @property
    def harfnotu(self,yeninot):
        self.__harfnotu=yeninot

    @harfnotu.getter
    def harfnotu(self):
        return self.__harfnotu

def dersPlaniCek(plan_url):
    dersler_listesi = []
    dersplani_sayfasi = requests.get(plan_url,headers=headers)
    dersplani_soup = BeautifulSoup(dersplani_sayfasi.content, "lxml")
    donemler = dersplani_soup.findAll("table",attrs={"class":"plan"})
    for donem in donemler:
        satirlar = donem.findAll("tr")
        satirlar.pop(0)
        for satir in satirlar:
            kolonlar = satir.findAll("td")
            if(len(kolonlar[0])>1):
                dersler_listesi.append(Ders(*[kolon.text for i,kolon in enumerate(kolonlar) if (i==0 or i==1 or i==2 or i==9) ]))
            elif("Seçime Bağlı" in kolonlar[1].text):
                secmeliders_url=plan_url[:-11]+kolonlar[1].find("a")['href']
                print(secmeliders_url)
                secmeliders_sayfasi = requests.get(secmeliders_url, headers=headers)
                secmeliders_soup = BeautifulSoup(secmeliders_sayfasi.content, "lxml")
                secmelisatirlar = secmeliders_soup.find("table", attrs={"class": "plan"}).find_all("tr")
                secmelisatirlar.pop(0)
                for secmelisatir in secmelisatirlar:
                    secmelikolonlar = secmelisatir.findAll("td")
                    __kod,__ad,__kredi,__donem="","","",""
                    for secmeli_i,secmelikolon in enumerate(secmelikolonlar):
                        if(secmeli_i==0):
                            __kod=secmelikolon.text
                        elif(secmeli_i==1):
                            __ad=secmelikolon.text
                        elif(secmeli_i==2):
                            __kredi=secmelikolon.text
                    __donem=kolonlar[9].text
                    dersler_listesi.append(Ders(__kod,__ad,__kredi,__donem))


    return dersler_listesi



