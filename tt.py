# -*- coding: utf-8 -*-
# Filename: tt.py
# Author : Adair
#import MySQLdb;
import os, string, sys,re,string;
import time;
global PATH,conn,cursor;

LETTER="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
letter="abcdefghijklmnopqrstuvwxyz";
os.chdir("/home/hongdai.zou/process.new.data/program/buyer");
#backupfile = "cp -f temp.buyer.file.preprocessed temp.file.a";
#os.system(backupfile);
for i in range(0, 12) :
    command1 =  'awk -F \"\t\" \'{print $2\"\t\"$1\"\t\"$3\", \"$4\", \" $5\", \"$6}\' yellow.page.and.info.USA.for.clustering.with.label |grep \"^'+LETTER[i]+'\" | awk -F \"\t\" \'{print $2\"\t\"$1\"\"$1\"\t\"$3}\' > temp.external.a'
    print command1;
    command2 =  'awk -F \"\t\" \'{print $2\"\t\"$1\"\t\"$3}\' temp.buyer.file.preprocessed |grep \"^'+letter[i]+'\" |awk -F \"\t\" \'{print  $2\"\t\"$1\"\t\"$3}\'> temp.real.data.a'
    #print command2;
    command3 = "cat  temp.real.data.a  temp.external >clustering.ready."+LETTER[i]
    print command3;
    command4 = "python  buyer.clustering.py  -c clustering.del.reg.rules.USA -s 0.9 0.7 -f clustering.ready."+LETTER[i]+"  -o  temp.buyer.file.preprocessed.clustering.result."+LETTER[i]
    #print command4;
    

    os.system(command1);
    #os.system(command2);
    os.system(command3);
    #os.system(command4);
