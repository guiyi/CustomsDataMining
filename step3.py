# -*- coding: utf-8 -*-
# Filename: step3.py
# Author : Adair
# 
import MySQLdb; 
import re, sys, math, os, curses.ascii, string;
from os.path import walk,join,normpath;
from operator import *; 
global conn, cursor, PATH;

PATH = "process.new.data/";
conn = MySQLdb.connect(host='localhost',user='data',db='data',passwd='abcdefgh');
cursor = conn.cursor();
cursor.execute("select id, seller_name, seller_add from map_seller");
data = cursor.fetchall();
outfile = open(PATH + "program/seller/temp.seller.file","w");
for k in range(0,len(data)):   
    outfile.write(str(data[k][0])+"\t"+data[k][1]+"\t"+data[k][2]+"\n");
    outfile.close();

