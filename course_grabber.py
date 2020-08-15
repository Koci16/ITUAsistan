from bs4 import BeautifulSoup
import requests
from course import Course

courseMainURL = "http://www.sis.itu.edu.tr/tr/ders_programlari/LSprogramlar/prg.php"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}


def getCourseCodes():
    courseCodeList = []
    page = requests.get(courseMainURL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    courseCodes = soup.find("select",attrs={"name":"bolum"}).findAll("option")
    courseCodeList = [c.text.strip() for c in courseCodes]
    courseCodeList.pop(0)
    return courseCodeList

def getCourseClasses(req):
    classes=[]
    coursePageURL = courseMainURL +"?fb="+req
    coursePage = requests.get(coursePageURL,headers=headers)
    courseSoup = BeautifulSoup(coursePage.content, "lxml")
    coursePrg = courseSoup.find("table",attrs={"class":"dersprg"}).findAll("tr")
    coursePrg.pop(0)
    coursePrg.pop(0)
    for row in coursePrg:
        columns = row.findAll("td")
        classes.append(Course(*[c.text for c in columns]))
    return classes

