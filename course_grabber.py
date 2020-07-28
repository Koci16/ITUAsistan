from bs4 import BeautifulSoup
import requests

courseMainURL = "http://www.sis.itu.edu.tr/tr/ders_programlari/LSprogramlar/prg.php"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

page = requests.get(courseMainURL,headers=headers)
if page.status_code == 200:
    print('Success!')
elif page.status_code == 404:
    print('Not Found.')

soup = BeautifulSoup(page.content, "html.parser")
courseCodes = soup.find("select",attrs={"name":"bolum"}).findAll("option")
courseCodeList = [c.text.strip() for c in courseCodes]
courseCodeList.pop(0)
courseCodeList=['AKM', 'ATA', 'ALM', 'BEB', 'BED', 'BEN', 'BIL', 'BIO', 'BLG', 'BLS', 'BUS', 'CAB', 'CEV', 'CHE', 'CHZ', 'CIE', 'CIN', 'CMP', 'COM', 'DAN', 'DEN', 'DFH', 'DGH', 'DNK', 'DUI', 'EAS', 'ECO', 'ECN', 'EHA', 'EHB', 'EHN', 'EKO', 'ELE', 'ELH', 'ELK', 'ELT', 'END', 'ENE', 'ENG', 'ENR', 'ESL', 'ESM', 'ETK', 'EUT', 'FIZ', 'FRA', 'FZK', 'GED', 'GEM', 'GEO', 'GID', 'GLY', 'GMI', 'GMK', 'GSB', 'GSN', 'GUV', 'GVT', 'HUK', 'HSS', 'ICM', 'ILT', 'IML', 'ING', 'INS', 'ISE', 'ISH', 'ISL', 'ISP', 'ITA', 'ITB', 'JDF', 'JEF', 'JEO', 'JPN', 'KIM', 'KMM', 'KMP', 'KON', 'LAT', 'MAD', 'MAK', 'MAL', 'MAT', 'MEK', 'MEN', 'MET', 'MCH', 'MIM', 'MKN', 'MST', 'MTM', 'MOD', 'MRE', 'MRT', 'MTH', 'MTK', 'MTO', 'MTR', 'MUH', 'MUK', 'MUT', 'MUZ', 'NAE', 'NTH', 'PAZ', 'PEM', 'PET', 'PHE', 'PHY', 'RES', 'RUS', 'SBP', 'SEN', 'SES', 'SNT', 'SPA', 'STA', 'STI', 'TDW', 'TEB', 'TEK', 'TEL', 'TER', 'TES', 'THO', 'TRZ', 'TUR', 'UCK', 'ULP', 'UZB', 'YTO']
print(*courseCodeList)

while True:
    print()
    req=input("Select a course code for grabbing or just take em all. (code/ALL) Ex.: GMI ").strip().upper()
    if req in courseCodeList:
        break
    elif req=="ALL":
        break
    else:
        print("Invalid input.")

coursePageURL = courseMainURL +"?fb="+req
coursePage = requests.get(coursePageURL,headers=headers)
if coursePage.status_code == 200:
    print('Success!')
elif coursePage.status_code == 404:
    print('Not Found.')

courseSoup = BeautifulSoup(coursePage.content, "lxml")

coursePrg = courseSoup.find("table",attrs={"class":"dersprg"}).findAll("tr")

# for index,row in enumerate(coursePrg):
#     if not row.has_attr("onmouseover"):
#         print(row)
#     else:
#         coursePrg.pop(index)
coursePrg.pop(0)
coursePrg.pop(0)
# print(coursePrg)

for row in coursePrg:
    print(row)
    columns = row.findAll("td")
    print([c.text for c in columns])

course=['30149', 'FIZ 102E', 'Physics II', 'Yakup  Hundur', '---- ', 'Pazartesi Salı Çarşamba ', '1500/1729 1500/1729 1500/1729 ', '---- ', '150', '87', 'Yok/None', 'BIO, BIOE, BLG, BLGE, CEV, CEVE, CHZ, CHZE, DEN, DENE, DUI, DUIE, EHB, EHBE, ELK, ELKE, END, ENDE, FIZ, FIZM, GEM, GEME, GEMK, GEO, GEOE, GID, GIDE, GMI, GMIE, IML, IMLE, INS, INSE, ISL, ISLE, JDF, JEF, JEFE, JEO, JEOE, KIM, KIME, KMM, KMME, KOM, KOME, MAD, MADE, MAK, MAKE, MAKM, MAT, MATE, MET, METE, MTO, MTOE, PET, PETE, TEK, TEKE, UCK, UCKE, UCKM, UZB, UZBE, UZBM', 'Yok/None', 'Yok/None']
