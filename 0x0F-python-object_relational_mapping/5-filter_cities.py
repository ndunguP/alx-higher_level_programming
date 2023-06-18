#!/usr/bin/python3
"""Script that lists all cities of a state from a database"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cmd = """SELECT cities.name FROM cities JOIN states ON
          cities.state_id = states.id WHERE states.name = %s"""
    cur.execute(cmd, (sys.argv[4], ))
    query_rows = cur.fetchall()
    city = []
    for row in query_rows:
        city.append(row[0])
    print(", ".join(i for i in city))
    cur.close()
    conn.close()
