import curses.ascii, re, pdb, string;
from operator import *;


def editDistance(a, b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current = range(n+1)
    for i in range(1, m+1):
        previous, current = current, [i] + [0] * n
        for j in range(1,n+1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def chooseOneClosetoOthers(mylist):
    n = len(mylist);
    result = "";

    if n > 2:
        minScore = 10000;
        minIndex = 0;
        for i in range(1,n):
            score = 0;
            for j in range(1,n):
                score = score + editDistance(mylist[i], mylist[j]);
            if score < minScore:
                minScore = score;
                minIndex = i;
        result = mylist[minIndex];
    else:
        result = mylist[0];

    return result;
        

def InitRegex(path):
    lines = open(path).readlines();
    mlist = [];
    for str in lines:
        str = str.rstrip('\n');
        str = str.rstrip('\r');
        if len(str) < 3:
            continue;
        try:
            regex = re.compile(str.lower());
            mlist.append(regex);
        except:
            print "regex have error:",str;
            return [];
    return mlist;



def InitRegexfromList(lines):
    mlist = [];
    for str in lines:
        str = str.rstrip('\n');
        str = str.rstrip('\r');
        try:
            regex = re.compile(str.lower());
            mlist.append(regex);
        except:
            print "regex have error:",str;
            return [];
    return mlist;



def stringDistance(str1,str2):
    if len(str1) != len(str2):
        dis = -1;
    else:
        dis = 0;
        strLen = len(str1);
        for k in range(1,strLen):
            if str1[k] != str2[k]:
                dis = dis + 1;
                print dis;
    return dis;


def CutToWords(line):
    strs = line.split();
    words = [];
    for str in strs:
        newstr = "";
        for a in str:
            if curses.ascii.isalpha(a) or curses.ascii.isdigit(a):
                newstr = newstr + a;
        if len(newstr) != 0:
            words.append(newstr);
    return words;



def CleanString(line):
    strs = line.split();
    if len(strs) == 0: return line;
    if len(strs) == 1: return strs[0];
    newline = "";
    for str in strs[:-1]:
        newline = newline + str + " ";
    newline = newline + strs[-1];
    return newline.lower();


def sort_by_value(m):
    alist=[];
    blist=[];
    for key,value in m.iteritems():
        alist.append((key,value));
    rankitem=itemgetter(1);
    for each in (sorted(alist,key=rankitem,reverse=True)):
        blist.append(each[0]);
    return blist;
