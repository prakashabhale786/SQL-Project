import sqlite3
conn = sqlite3.connect("Collage.db")  
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Student (
    stu_name TEXT,
    stu_rollno INTEGER PRIMARY KEY,
    stu_age INTEGER,
    stu_adress TEXT
)
""")
stu_name = "Krishna"
stu_rollno = 4
stu_age = 25
stu_adress = "Nashik"
cur.execute("INSERT INTO Student (stu_name, stu_rollno, stu_age, stu_adress) VALUES (?, ?, ?, ?)", 
            (stu_name, stu_rollno, stu_age, stu_adress))
cur.execute("SELECT * FROM Student")
data=cur.fetchall()     # fatchall to show all records
data=cur.fetchone()   # to show first record
data=cur.fetchmany(2)   # to show first 2 record
print(data)
## cur.execute("DELETE FROM Student WHERE stu_name = ?", ('Ghansham',))   # delete the record
conn.commit()
conn.close()

