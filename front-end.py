from flask import Flask
from flask import request
import sqlite3


app = Flask(__name__)

@app.route('/')
def root():
    # Connect to db
    db = sqlite3.connect('books.db')  
    cursor = db.cursor()
    #cursor.execute('CREATE TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,topic TEXT, cost INTEGER, ammount INTEGER)')
    # Connect to db
   

    # Insert data into db
    cursor.execute('INSERT INTO books(name,topic, cost, ammount) VALUES("distributed systems","How to get a good grade in DOS in 20 minutes a day",20 ,5 )')
    db.commit()
    cursor.execute('INSERT INTO books(name,topic, cost, ammount) VALUES("distributed systems","RPCs for Dummies", 10,4 )')
    db.commit()
    cursor.execute('INSERT INTO books(name,topic, cost, ammount) VALUES("graduate school","Xen and the Art of Surviving Graduate School",15 ,7 )')
    db.commit()
    cursor.execute('INSERT INTO books(name,topic, cost, ammount) VALUES("graduate school","Cooking for the Impatient Graduate Student",17 ,6 )')
    db.commit()

    # Get data from db
    cursor.execute('SELECT * FROM books')
    data = cursor.fetchall()
    
    # Close db connection
    db.close()
    
    return str(data)
  

@app.route('/create')
def create():
    # Connect to db
    db = sqlite3.connect('posts.db')  
    cursor = db.cursor()
    
    # Get request args
    title = request.args.get('title')
    post = request.args.get('post')
    
    # Insert data into db
    cursor.execute('INSERT INTO posts(title, post) VALUES("%s", "%s")' % (title, post))
    db.commit()
    
    # Close db connection
    db.close()
    return 'title: %s  |  post: %s' % (title, post)

@app.route('/update/<_id>')
def update(_id):
    # Connect to db
    db = sqlite3.connect('posts.db')  
    cursor = db.cursor()
    
    # Get request args
    title = request.args.get('title')
    post = request.args.get('post')
    
    # Update data in db
    cursor.execute('UPDATE posts SET title="%s", post="%s" WHERE id=%s' % (title, post, _id))
    db.commit()
    
    # Close db connection
    db.close()
    return '_id: %s  |  title: %s  |  post: %s' % (_id, title, post)

@app.route('/delete/<_id>')
def delete(_id):
    # Connect to db
    db = sqlite3.connect('posts.db')  
    cursor = db.cursor()
    
    # Update data in db
    cursor.execute('DELETE FROM posts WHERE id=%s' % _id)
    db.commit()
    
    # Close db connection
    db.close()
    return 'deleted _id: %s' % _id


if __name__ == '__main__':
    app.run(debug=True, threaded=True)