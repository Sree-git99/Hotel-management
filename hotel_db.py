import sqlite3
def hotel_db():
    con=sqlite3.connect(database="hotelmanagement.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Customer(ref INTEGER PRIMARY KEY AUTOINCREMENT,name text,gender text,postcode text,mobile text,email text,nationality text,idproof text,idnumber text,address text)")
    con.commit()
    #cur.execute("DROP TABLE room;")
    cur.execute("CREATE TABLE IF NOT EXISTS room(contact text,checkin text,checkout text,roomtype text,roomavailable text PRIMARY KEY,meal text,noofdays text)")
    con.commit()
    #cur.execute("DROP TABLE details;")
    cur.execute("CREATE TABLE IF NOT EXISTS details(Floor text ,Roomno text PRIMARY KEY,RoomType text )")
    con.commit()
    #cur.execute("DROP TABLE register;")
    
    
    
hotel_db()



    