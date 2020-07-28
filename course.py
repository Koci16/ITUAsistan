class Course:
    def __init__(self,
                 crn:int,
                 code:str,
                 title:str,
                 instructor:str,
                 building:str,
                 day:str,
                 time:str,
                 room:str,
                 capacity:str,
                 enrolled:str,
                 reservation:str,
                 restriction:str,
                 prereq:str,
                 classrest:str):
        #['30149', 'FIZ 102E', 'Physics II', 'Yakup  Hundur', '---- ', 'Pazartesi Salı Çarşamba ', '1500/1729 1500/1729 1500/1729 ', '---- ', '150', '87', 'Yok/None', 'BIO, BIOE, BLG, BLGE, CEV, CEVE, CHZ, CHZE, DEN, DENE, DUI, DUIE, EHB, EHBE, ELK, ELKE, END, ENDE, FIZ, FIZM, GEM, GEME, GEMK, GEO, GEOE, GID, GIDE, GMI, GMIE, IML, IMLE, INS, INSE, ISL, ISLE, JDF, JEF, JEFE, JEO, JEOE, KIM, KIME, KMM, KMME, KOM, KOME, MAD, MADE, MAK, MAKE, MAKM, MAT, MATE, MET, METE, MTO, MTOE, PET, PETE, TEK, TEKE, UCK, UCKE, UCKM, UZB, UZBE, UZBM', 'Yok/None', 'Yok/None']
        self.crn=crn
        self.code=code
        self.title=title
        self.instructor=instructor
        self.building=building.strip()
        self.day=day.strip().split(" ")
        self.time=time.strip().split(" ")
        self.room=room.strip()
        self.capacity=capacity
        self.enrolled=enrolled
        self.reservation=reservation
        self.restriction=restriction.split(", ")
        self.prereq=prereq
        self.classrest=classrest

    def __str__(self):
        return str((self.crn,self.code,self.title,self.instructor,self.building,self.day,self.time,self.room,self.capacity,self.enrolled,self.reservation,self.restriction,self.prereq,self.classrest))

#fiz1=Course('30149', 'FIZ 102E', 'Physics II', 'Yakup  Hundur', '---- ', 'Pazartesi Salı Çarşamba ', '1500/1729 1500/1729 1500/1729 ', '---- ', '150', '87', 'Yok/None', 'BIO, BIOE, BLG, BLGE, CEV, CEVE, CHZ, CHZE, DEN, DENE, DUI, DUIE, EHB, EHBE, ELK, ELKE, END, ENDE, FIZ, FIZM, GEM, GEME, GEMK, GEO, GEOE, GID, GIDE, GMI, GMIE, IML, IMLE, INS, INSE, ISL, ISLE, JDF, JEF, JEFE, JEO, JEOE, KIM, KIME, KMM, KMME, KOM, KOME, MAD, MADE, MAK, MAKE, MAKM, MAT, MATE, MET, METE, MTO, MTOE, PET, PETE, TEK, TEKE, UCK, UCKE, UCKM, UZB, UZBE, UZBM', 'Yok/None', 'Yok/None')
#print(fiz1)
