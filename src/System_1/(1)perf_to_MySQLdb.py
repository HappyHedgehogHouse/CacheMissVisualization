import MySQLdb as db
import datetime
import string
import re
import time
import subprocess

while 1:
    test = subprocess.Popen(["perf","stat","-B","-o", "data.txt", "-e", \
        "cache-references,cache-misses", "sleep", "1"],     stdout=subprocess.PIPE)
    test.communicate()[0]
    
    f = open("data.txt", "r")
    f.readline()
    line = 1
    i = 0
    data = [0]*2
    
    while line:

        line = f.readline()
        result = re.findall(r'\s([\d,]+)\s',line)
        if result:
	    data[i] = result[0].replace(',', '')
            data[i] = float(data[i])
            i = i+1

    tmpDB = db.connect('203.246.112.77', 'root', 'net12345', 'Yoon')

    cur = tmpDB.cursor()
    current_time = datetime.datetime.now()

    query = "INSERT INTO Cache(time, reference, miss, missrate)"\
       "VALUES(%s,%s,%s,%s)"
    data = [(current_time, data[0], data[1], data[1]/data[0])]
    rslt = cur.executemany(query,data)
    tmpDB.commit()
