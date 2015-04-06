while 1 :
    import MySQLdb as db
    import time
    tmpDB = db.connect('203.246.112.77', 'root', 'net12345', 'Yoon')

    cur = tmpDB.cursor()

    query = "SELECT * FROM Cache ORDER BY time DESC LIMIT 100"
    cur.execute(query)

    data=cur.fetchall()
    #print data

    f = open("d3.json", 'w')
    f.write ("{\n\t\"record\": [\n")

    for ent in data :
        f.write ("\t\t{\n")
        f.write ("\t\t\t\"time\": \""+ ent[0]+ "\",\n")
        f.write ("\t\t\t\"reference\": "+ str(ent[1])+ ",\n")
        f.write ("\t\t\t\"miss\": "+ str(ent[2])+ ",\n")
        f.write ("\t\t\t\"missrate\": "+ str(ent[3])+ "\n")
        f.write ("\t\t},\n")

    f.seek(f.tell()-2)
    f.write ("\n\t]\n}")
    f.close()
    time.sleep(1)