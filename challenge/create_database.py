
# For this challenge, you are going to create a database using Python’s SQLite. You will import SQLite into your script. Create a database called movies.db. In that database, you are going to create a table called movies. In that table, you are going to save the following movies:


# year	title	genre
# 2009	Brothers	Drama
# 2002	Spider Man	Sci-fi
# 2009	WatchMen	Drama
# 2010	Inception	Sci-fi
# 2009	Avatar	Fantasy

# a)	Once you create a table, run a SQL query to see all the movies in your table.
# b)	Run another SQL query to select only the movie Brothers from the list.
# c)	Run another SQL query to select all movies that were released in 2009 from your table.
# d)	Run another query to select movies in the fantasy and drama genre.
# e)	Run a query to delete all the contents of your table.

import sqlite3

con = sqlite3.connect('movies.db')
cur = con.cursor()

# Creating a table in the database
cur.execute('CREATE TABLE movies(year,title, genre)')

# Creating a variable of all the movies
movies = [(2009, 'Brothers', 'Drama'),
          (2002, 'Spider-Man', 'Sci-fi'),
          (2009, 'WatchMen', 'Drama'),
          (2010, 'Inception', 'Sci-fi'),
          (2009, 'Avatar', 'Fantasy')]

cur .executemany('''INSERT INTO movies VALUES(?, ?, ?); ''', movies)

# commit and close
con.commit()
con.close()

#a
con = sqlite3.connect('movies.db')
cur = con.cursor()

row = cur.fetchall()
for row in cur.execute('SELECT * FROM Movies;'):
    print(row)

#b
con = sqlite3.connect('movies.db')
cur = con.cursor()

row = cur.fetchall()
for row in cur.execute('SELECT * FROM Movies WHERE '
                       'title ="Brothers";'):
    print(row)

#c
con = sqlite3.connect('movies.db')
cur = con.cursor()

row = cur.fetchall()
for row in cur.execute('SELECT * FROM Movies WHERE '
                       'year = 2009'):
    print(row)
#d

con = sqlite3.connect('movies.db')
cur = con.cursor()

row = cur.fetchall()
for row in cur.execute('SELECT * FROM Movies WHERE '
                       'genre = "Fantasy" OR genre = "Drama";'):
    print(row)

#e
con = sqlite3.connect('movies.db') 
cur = con.cursor() 
cur.execute('DELETE FROM movies;') 
con.commit()

# Creating and saving the movies to the database. The first step is to import SQLite and create a database(movies.db). Then we create a table called movies with all the columns that we need (year, title, and genre). There are two ways to upload data to our database. The first one is using the command cur.execute. This method only uploads one item at a time. Since we want to upload many items at once, we use cur.executemany. To do this we create a list with all the movies that we want to upload (movies variable). Once we upload, we need to commit and close to make those changes permanent.
