import psycopg2

con = psycopg2.connect(
    host="localhost",
    port=2222,
    database="pbz_2",
    user="postgres",
    password="postgres0609"
)
cur = con.cursor()
# cur.execute("select * from оборудование")
# rows = cur.fetchall()
# for r in rows:
#     print(r[0],r[1],r[2])
# cur.close()
#con.close()