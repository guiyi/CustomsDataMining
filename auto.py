# -*- coding: utf-8 -*-
# Filename: auto.py
# Author : Adair
# 
import MySQLdb;
import os, string, sys,re,string;
import time;
global PATH,conn,cursor;

LogPath="process.new.data/run.result/";
DataBackUpPath="process.new.data/databackup/BackUp";
DataPath ="process.new.data/program/";
BuyerPath = DataPath+"buyer/";
SellerPath = DataPath+"seller/";
OutFile = open(LogPath + "/"+"runlogs29"+".txt","a");
print OutFile;
DateTime =time.strftime('%Y.%m.%d %H.%m.%s',time.localtime(time.time())).replace(" ",".");
print DateTime;
OutFile.write("\n\n*************************************"+DateTime+"***************************************************************************************************************************\n");
OutFile.write("This program for Customs data mining, development by  adair, Updated on Apil 25, 2011." + time.asctime().replace(" ",".") + "\n\n\n");

def PrintUsage():              
    print "\nThis program development  adair, Updated on Apil 25, 2011."
    print "\nThis program is automatic data. \nIf the input file is infile, then the output file is infile.out.import and infile.out.read.";
    print "The file infile.out.read is for visual check and infile.out.import is for importation."
    print "Usage: program infile\nGood luck.\n\n";



def connectDB():
    global conn, cursor;
    try:
        conn = MySQLdb.connect(host='localhost',user='data',db='data',passwd='abcdefgh');
    except Exception, e:
        print e
        sys.exit();
    cursor = conn.cursor();



def exportMapSellerInfo():
    global conn, cursor;
    connectDB();

    sql = "select id, seller_name, seller_add from map_seller where cluster_right=1;";
    cursor.execute(sql);
    data = cursor.fetchall();
    outfile = open(DataPath + "seller/temp.seller.file","w");
    for k in range(0,len(data)):
        outfile.write(str(data[k][0])+"\t"+data[k][1]+"\t"+data[k][2]+"\n");
    OutFile.write(" step3  temp.seller.file  "+sql+"  runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    outfile.close();



def exportMapBuyerInfo():
    global conn, cursor;
    connectDB();

    sql = "select id, buyer_name, buyer_add from map_buyer where cluster_right=1;";
    cursor.execute(sql);
    data = cursor.fetchall();
    outfile = open(DataPath + "buyer/temp.buyer.file","w");
    print outfile;
    for k in range(0,len(data)):
        outfile.write(str(data[k][0])+"\t"+data[k][1]+"\t"+data[k][2]+"\n");
    OutFile.write(" step3  temp.buller.file  "+sql+"  runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    outfile.close();

def my_fork(): 
    child_pid = os.fork() 
    if child_pid == 0: 
        os.system("python aa.py")
	print DateTime;
    else: 
        os.system("python bb.py")
	print DateTime;


def wholeProcedurePartI():
   

 # STEP ONE
    # Data backup in folder process.new.data/data.backup
    print "Step 1: Backup the whole database ...",
    DataBackUpFile = DataBackUpPath+"."+ DateTime[0:10]+".SQL.gz";
    #os.system("screen");
    RmPath ="rm "+DataBackUpFile ; 
    # print DataBackUpFile;
    if os.path.exists(DataBackUpFile):   
       #os.system(RmPath);
       OutFile.write("Warning: Step1 You had been BackUp One time ..." + time.asctime().replace(" ",".") + "\n");
       
    else:
       file = DataBackUpPath+"."+DateTime[0:10]+ ".SQL"; 
       command = "mysqldump -udata -pabcdefgh -R data > " + file;
       print command;
       os.system(command);
       os.system("gzip " + file);
    
    OutFile.write("STEP1  Backup the whole database  runing ..." + time.asctime().replace(" ",".") + "\n");
    print "Finished.";

 # STEP TWO
    # New Data  in folder /home/hongdai.zou/2011/04/
    print "Step 2: extract.US.custom.original.data.py  Import.transaction.data.py ...\n",

    OutFile.write("step1  Finised!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP2 extract.US.custom.original.data.py  Import.transaction.data.py ..." + time.asctime().replace(" ",".") + "\n");
  
    NewDataYear=DateTime[0:4];
    NewDataMonth=DateTime[5:7];
    NewDataYear='2012';
    NewDataMonth='02';
    NewDataPath =str(NewDataYear)+"/"+str(NewDataMonth);
    TaskPath = open(NewDataPath+ "/"+"task"+".txt","w"); #orginal path  2011/04/20110426.txt edit 2011/04/20110426.txt.did
    ImportPath = open(NewDataPath+ "/"+"Import"+".sh","w");
    for item in os.listdir(NewDataPath):
        if len(item)==12 and item[-1]=='t': 
           print item;       
           TaskPath.write(item+"\n");
           ImportPath.write(item+".out.import"+"\n");

           command1_A = "python process.new.data/program/extract.US.custom.original.data.py"+"  "+NewDataPath+"/"+item;
           RmDataTxt ="mv"+"  "+NewDataPath+"/"+item+"   " +NewDataPath+"/"+item+".did";
	   OutFile.write(" step2   "+command1_A+"  runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
           OutFile.write(" step2   "+RmDataTxt+"  runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");

           os.system(command1_A);
           os.system(RmDataTxt);
	   
           command1_B ="python  process.new.data/program/import.transaction.data.py -f  "+NewDataPath+"/"+item+".out.import" ;
           os.system(command1_B);
           OutFile.write(" step2   "+command1_B+"  runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
         


    print 'Finshed.'        


 # STEP THREE
    # Export map_seller information and map_buyer information.
    print "Step 3: Export Map_buyer/Map_seller information ...",
    OutFile.write("step2 Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP3 SELECT * FROM  Export Map_buyer/Map_seller information Running ..." + time.asctime().replace(" ",".") + "\n");
    exportMapSellerInfo();
    exportMapBuyerInfo();
    OutFile.write(" step3   exportMapSellerInfo  runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    OutFile.write(" step3   exportMapBuyerInfo  runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
	
    print "Finished.";


 #STEP FOUR      
    # Preprecess data
    print "Step 4: Preprocess the data for buyer seller  ...";
    OutFile.write("step3  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP4   Preprocess the data for buyer seller  ..." + time.asctime().replace(" ",".") + "\n"); 
    seller_PATH = "/home/hongdai.zou/process.new.data/program/seller";
    pre_seller  = " python PreprocessSellerInfo.py  -i temp.seller.file -o temp.seller.file.preprocessed ";
    print seller_PATH;
    print pre_seller;
    os.chdir(seller_PATH);
    os.system(pre_seller);
    OutFile.write(" step4 "+pre_seller+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");

    os.chdir("/home/hongdai.zou");
 
    buyer_PATH = "/home/hongdai.zou/process.new.data/program/buyer";
    command = "python preprocess.buyer.info.py";
    command = command + " -alpha us.alpha.conf.txt  ";
    command = command + " -beta us.beta.conf.txt  ";  
    command = command + " -gamma us.gamma.conf.txt  ";
    command = command + " -i  temp.buyer.file -o temp.buyer.file.preprocessed";
    os.chdir(buyer_PATH);
    os.system(command);
    OutFile.write(" step4 "+command+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");

    print "Finished."



 #STEP FIVE
    print "Step 5: Clustering seller's informations ...",
    OutFile.write("step4  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP5 Clustering seller's informations ..." + time.asctime().replace(" ",".") + "\n");
    os.chdir("/home/hongdai.zou");              
    command = "python "+DataPath+"seller/seller.clustering.py  -s 0.7 0.7 -f "+DataPath+"seller/temp.seller.file.preprocessed -o "+DataPath+"seller/seller.clustering.result";
    print command;
    os.system(command);
    OutFile.write(" step5 "+command+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    print "Finished";



 #STEP SIX                 
    print "Step 6: Clustering buyer's information ...",
    OutFile.write("step5  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP6  Clustering buyer's information ..." + time.asctime().replace(" ",".") + "\n");
    my_fork()
    print "Finshed!"


 #Step Seven
    print "Step 7: extract information from buyer's clustering results ...",
    OutFile.write("step6  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP7   extract information from buyer's clustering results  ..." + time.asctime().replace(" ",".") + "\n");
    os.chdir("/home/hongdai.zou/process.new.data/program/buyer");
    command = "python extract.information.from.clustering.py";
    print  command;
    OutFile.write(" step7 "+command+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    os.system(command);
    print "Finished.";


 #Step Eight
    print "Step 8: extract information from Seller's clustering results ...",
    OutFile.write("step7  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP8  extract information from Seller's clustering results ..." + time.asctime().replace(" ",".") + "\n");
    os.chdir("/home/hongdai.zou/process.new.data/program/seller");
    command = "python import.seller.clustering.data.py -f  seller.clustering.result ";
    print  command;
    OutFile.write(" step8 "+command+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n"); 
    os.system(command);
    print "Finished.";



 #Step Nine
    print "Step 9: Extract keywords from description ...",
    OutFile.write("step8  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP9  Extract keywords from description ..." + time.asctime().replace(" ",".") + "\n");
    command = "python "+DataPath+"extract.keywords.from.description.py";
    print command;
    OutFile.write(" step9 "+command+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    os.system(command);
    print "Finished.";




 #Step Ten
    print "Step 10: Run procedure step10.call4 (update_buyer_id,update_seller_id,update_category_buyer,update_category_seller) ...",
    OutFile.write("step9  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP10   Run procedure step10.call4  ..." + time.asctime().replace(" ",".") + "\n");
    
    global conn, cursor;
    connectDB();
         
 
    sql = "CALL test";
    OutFile.write(" step10 "+sql+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    print sql;      
    cursor.execute(sql);
    #data=cursor.fetchall();
    #if data:  
       #for rec in data:  
          #accname=rec[0];  
          #print accname;
    #OutFile.write(" step10 "+accname+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    cursor.close()  
 
    print "Finished.";


    print "\nWe have finished step 1-10. Please check if the country_id in Map_depart_port table is processed."
    print "You need to finish this step before you can further process sellers' information."
    #print "Do you want to proceed to process seller? (y/n): "
    print "Good-bye and have a good day.\n";




def wholeProcedurePartII():

 #Step Eleven 
    print "Step 11: Compute the country information for each seller in Map_seller table ...",
    OutFile.write("step10  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP11   Compute the country information for each seller in Map_seller table ..." + time.asctime().replace(" ",".") + "\n");
    os.chdir("/home/hongdai.zou/process.new.data/program/seller");
    command = "python DecideSellerCountryInformation.py ";
    print command;
    os.system(command);
    OutFile.write(" step10 "+command+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");
    print "Finished.";




 #Step Twelve
    print "Step 12: Extract seller's information automatically ...";
    OutFile.write("step11  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP12 Extract seller's information automatically  ..." + time.asctime().replace(" ",".") + "\n");
    countryCode = [115,41,83,193,13,64,70,86,92,94,180,36];
    for k in range(0,len(countryCode)):
        os.chdir("/home/hongdai.zou/process.new.data/program/seller");
        command = "python  Process.Seller.Information.py -c " + str(countryCode[k]) + " > log.country." + str(countryCode[k]);
        print command;
        os.system(command);            
        print "\t\tCountry " + str(countryCode[k]) + " is finished ...";
        OutFile.write(" step12 "+command+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");


#Step Thirteen
    print "Step 13: Extract buyer's information automatically ...";
    OutFile.write("step12  Finshed!"+"\t" + time.asctime().replace(" ",".") + "\n\n"+"STEP13 Extract seller's information automatically  ..." + time.asctime().replace(" ",".") + "\n");
    os.chdir("/home/hongdai.zou/process.new.data/program/seller");
    command = "python  DecideBuyerCountryInformation.py";
    print command;
    os.system(command);            
      
    OutFile.write(" step13 "+command+ " runing ..."+"\t" + time.asctime().replace(" ",".") + "\n");

    
    OutFile.write("\n\n  We finished all steps. Thanks for using the program."+"\t" + time.asctime().replace(" ",".") + "\n");
    print "All Countries are processed."
    print "We finished all steps. Thanks for using the program."
    OutFile.write("\n\n****************************************************************************************************************************************************************\n");
	













if __name__=="__main__": 

    if len(sys.argv) != 2:            
        PrintUsage();
        wholeProcedurePartI();
        wholeProcedurePartII();

        sys.exit(0);
    print "\n\nExtraction starts and it will take about half a minute for one day data ...",
    ProcessOneFile(sys.argv[1]);
    print "Thanks for using the program. Good-bye.\n\n";

