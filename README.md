# 自动化流程分析

自动化处理每一步都将状态写入日志文件，通过日志文件可知当前操作到那一步。也可以作为错误查找；

### 1．	Step1备份数据库

建立 screen 1.1 mysqldump –udata –pabcdefgh data>/*.sql(在python环境下) Gzip /*.sql 压缩文件 写入日志文件

### 2．	Step2执行对原始数据进行标准化处理 , 导入数据

Scp产生的文件路径按照 年/月/数据文件 2011/04/20110402.txt（手动） A. extract.US.custom.original.data.py 2.1获取当前月份，查找月份下的文件 如果存在filename.out.import and filename.out.read 不写入文件task20110426.txt 否则写入文件task20110426.txt 2.2读取task日期.txt python extract.US.custom.original.data.py 对原始数据进行标准化处理 B.Import.transaction.data.py 2.3 查找日期文件（task20110426.txt）下的 文件对应的out.import和.out.read 是否存在

2.4存在，修改task20110426.txt，将文件存储的20110426.txt 改写为 20110426.out.import 文件名为task20110426.import.txt； 2.5不存在写入日志文件； 2.6 python Import.transaction.data.py . task20110426.import.txt文件内的内容； 写入日志执行情况

### 3．	Step3.数据库最近数据导出 Step3.buyer.py step3.seller.py

process.new.data/program/seller/temp.seller.file
process.new.data/program/buyer/ temp.buyer.file

### 4．	Step4. preprocess.seller.info.py preprocess.buyer.info.py buyer seller信息聚类预处理

4.1判断step3产生的文件是否存在 4.2存在，执行对应的buyer。或seller 产生Temp.seller. processed temp.buyer.processed 4.3否则写入执行log，记录错误地址

### 5．	Step5. seller.clustering.py seller.clustering.result

seller信息聚类 （同step4）

python process.new.data/program/buyer/buyer.clustering.py -c process.new.data/program/buyer/temp.buyer.file.preprocessed -s 0.7 0.7 -f process.new.data/program/buyer/temp.buyer.file.preprocessed -o process.new.data/program/buyer/seller.clustering.result

### 6．	Step6 run.clustering.R .py buyer信息聚类

clustering.read.A … clustering.read.Z （同step4）

### 7．	Step7 extract.information.from.clustering.py 提取buyer聚类信息入库 （同step4）

### 8．	Step8 Import.seller.clustering.data.py 提取seller聚类信息入库 （同step4）

### 9．	Step9 extract.keywords.from.description.py 商品描述入库 ，存储过程更新 （同step4）

### 10．	Step10 DecideCountryInformation.py 提取seller国家 （同step4）

### 11．	Step11 Process.Seller.Information.py 公司信息 （同step4）

                                                                       Adair.2011.04.26
