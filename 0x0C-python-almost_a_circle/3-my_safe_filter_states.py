#!/usr/bin/python3
"""Script that lists all states with a name starting with N
safe from injections"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cmd = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(cmd, (
                sys.argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
