#!/usr/bin/python3
'''Task 1 get all name of the states starting with N'''

if __name__ == "__main__":

    import MySQLdb
    '''import mysqldb'''

    import sys
    '''import sys for arguments'''

    db_connection = MySQLdb.Connect(host="localhost\
", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE '\
N%' ORDER BY states.id;")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    cursor.close()
    db_connection.close()
