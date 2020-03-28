#!/usr/bin/python3
'''Task 5 display all cities from a state according argument '''

if __name__ == "__main__":

    import MySQLdb
    '''import mysqldb'''

    import sys
    '''import sys for arguments'''

    db_connection = MySQLdb.Connect(host="localhost\
", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db_connection.cursor()
    cursorstr = """
SELECT cities.name
FROM cities
INNER JOIN states ON states.id = cities.state_id
WHERE states.name = %s
ORDER BY cities.id;
"""
    value = str(sys.argv[4])
    cursorstr = cursorstr.format(value=value)
    cursor.execute(cursorstr, (value,))
    myresult = cursor.fetchall()
    for y in range(0, len(myresult)):
        w = str(myresult[y])
        x = str(w.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
        print(x, end="")
        if y != len(myresult) - 1:
            print(", ", end="")
        else:
            print()
    cursor.close()
    db_connection.close()
