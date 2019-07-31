import sqlite3
conn = sqlite3.connect('..\db.sqlite3')
cursor = conn.cursor()
print("Opened database successfully")

# try to fetch data from DB
#try:
#    cQrCodesExisting = cQrCode.objects.all()
#    #no exception means object preesent and can be filtered against auth to redirect to Welcome Page
#    if cQrCodesExisting.isAuthenticated == True : 
#        print ("auth Done")
#except ObjectDoesNotExist:
#    print("do nothing for now")


uniqueId = 124247


Query = "UPDATE polls_cqrcode set isAuthenticated = 0 where uniqueId = " + str(uniqueId)
conn.execute(Query)
conn.commit()


# for row in cursor.execute("SELECT uniqueId, isAuthenticated   from polls_cqrcode"):
    # print("uniqueId = ", row[0])
    # print("isAuthenticated = ", row[1])

    

conn.commit()
conn.close()