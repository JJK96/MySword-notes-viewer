import sqlite3
con = sqlite3.connect('versenotes.mybible')

def replace(table):
    cur = con.cursor()
    res = cur.execute(f"select * from {table} where data LIKE '%efeze %' or data LIKE '%Efeze %'")
    rows = res.fetchall()
    for row in rows:
        text = row[5].replace('efeze ', 'efe ').replace('Efeze ', 'Efe ')
        if table == "commentary":
            cur.execute(f"update {table} set data = ? where id = ?", (text, row[0]))
        else:
            cur.execute(f"update {table} set data = ? where book = ? and chapter = ? and fromverse = ?", (text, row[0], row[1], row[2]))
    con.commit()
    print("replaced ", len(rows))

replace("commentary")
replace("commentary2")
