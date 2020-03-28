#!/usr/bin/python3
'''Task 2 display states according argument '''

if __name__ == "__main__":

    import MySQLdb
    '''import mysqldb'''

    import sys
    '''import sys for arguments'''

    db_connection = MySQLdb.Connect(host="localhost\
", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db_connection.cursor()
    cursorstr = """
SELECT *
FROM states
WHERE BINARY states.name = '{value}'
ORDER BY states.id;
"""
    value = str(sys.argv[4])
    cursorstr = cursorstr.format(value=value)
    cursor.execute(cursorstr)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    cursor.close()
    db_connection.close()
