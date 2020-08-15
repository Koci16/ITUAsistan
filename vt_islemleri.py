import sqlite3 as sql
from course import Course
from course_grabber import *

with sql.connect("ogrencidb.asistan") as vt:
    im = vt.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS "bilgiler" (
        "fakulte"	TEXT,
        "bolum"	TEXT,
        "dersplani"	TEXT,
        "dersplani_url"	TEXT)""")
    im.execute("""CREATE TABLE IF NOT EXISTS "bolumkodlari" (
        "bolumkodu" TEXT)
        """)
    im.execute("""CREATE TABLE IF NOT EXISTS "dersler" (
        "bolumkodu"	TEXT,
        "crn"	INTEGER,
        "code"	TEXT,
        "title"	TEXT,
        "instructor"	TEXT,
        "building"	TEXT,
        "day"	TEXT,
        "time"	TEXT,
        "room"	TEXT,
        "capacity"	TEXT,
        "enrolled"	TEXT,
        "reservation"	TEXT,
        "restriction"	TEXT,
        "prereq"	TEXT,
        "classrest"	TEXT)""")
    im.execute("""CREATE TABLE IF  NOT EXISTS "dersplani" (
        "kod"	TEXT,
        "ad"	TEXT,
        "donem"	TEXT,
        "harfnotu"	TEXT)""")
    vt.commit()


def bolumkodlari_vt_cek():
    #with sql.connect("ogrencidb.asistan") as __vt:
    pass

def bolumkodlari_vt_kaydet(bolumkodlari):
    with sql.connect("ogrencidb.asistan") as __vt:
        __im = __vt.cursor()
        for __kod in bolumkodlari:
            __im.execute("""INSERT INTO 'bolumkodlari' VALUES ('{}')""".format(__kod))
        __vt.commit()

def dersplani_vt_cek():
    with sql.connect("ogrencidb.asistan") as __vt:
        __im = __vt.cursor()
        __vt.commit()

def dersplani_vt_kaydet():
    with sql.connect("ogrencidb.asistan") as __vt:
        __im = __vt.cursor()
        __vt.commit()

def ogrencibilgileri_vt_cek():
    with sql.connect("ogrencidb.asistan") as __vt:
        __im = __vt.cursor()
        __vt.commit()

def ogrencibilgileri_vt_kaydet():
    with sql.connect("ogrencidb.asistan") as __vt:
        __im = __vt.cursor()
        __vt.commit()
