import mysql.connector
import pak_fed_ministries_data
from mysql.connector import errorcode
from pak_fed_ministries_data import get_ministries_data

try:
    cnx = mysql.connector.connect(user='root', password='mypassword', host='localhost', database='scrapping')
    insert_sql = ("INSERT INTO pakFedMinistries (name, link) VALUES (%(text)s, %(link)s)")

    ministries_data = get_ministries_data()

    cursor = cnx.cursor()

    for ministry in ministries_data:
        print("Stroing data for %s" % (ministry["text"]))
        cursor.execute(insert_sql, ministry)

    cnx.commit()

    cursor.close()
    cnx.close()

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(error)

else:
    cnx.close()