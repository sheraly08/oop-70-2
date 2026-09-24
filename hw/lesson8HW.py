import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL
        )
    
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (30) NOT NULL,
    genre VARCHAR (30) NOT NULL
    )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
        )
     
     ''')
conn.commit()



def create_moke_users():
    cursor.executemany(
        'INSERT INTO users(name) VALUES (?)',
        [
            ("ARDAGER",),
            ("ARZY",),
            ("SLAVA",),
            ("VLAD",),
            ("OLEG",),
        ]
    )
    conn.commit()
    print("Пользователи созданы!!")


def create_moke_movies():
    cursor.executemany(
        'INSERT INTO movies(title, genre) VALUES (?, ?)',
        [
            ("Inception", "Science Fiction"),
            ("Gladiator", "Action"),
            ("Alien", "Horror"),
            ("Jaws", "Thriller"),
            ("Coco", "Animation"),

        ]
    )
    conn.commit()
    print('Фильмы добавлены')


def create_moke_reviews():
    cursor.executemany(
        'INSERT INTO reviews(user_id, movie_id, rating) VALUES (?, ?, ?)',
        [
            (2, 3, 7),
            (1, 2,  8),
            (3, 5, 10),
            (1, 4, 8),
            (4, 5, 7),
            (2, 3, 10),
            (4, 4, 4),
            (3, 5, 9),
            (5, 5, 7),
            (1, 4, 10),


        ]
    )
    conn.commit()

def get_user_movie_rating():
    cursor.execute('''
    SELECT users.name, movies.title, reviews.rating
    FROM users
    JOIN reviews ON users.id = reviews.user_id
    JOIN movies ON movies.id = reviews.movie_id

    ''')
    data = cursor.fetchall()
    print(data)

#get_user_movie_rating()


def get_movies():
    cursor.execute('''
    SELECT movies.title, reviews.rating
    FROM movies
    LEFT JOIN  reviews ON movies.id = reviews.movie_id
    ''')
    data = cursor.fetchall()
    print(data)

#get_movies()

def get_average_movie():
     cursor.execute(
    'SELECT  AVG(reviews.rating) FROM movies INNER JOIN reviews ON movies.id = reviews.movie_id'
     )
     data = cursor.fetchall()
     print(data)

#get_average_movie()

def get_min_rating():
    cursor.execute(
    'SELECT movies.title, MIN(reviews.rating) FROM movies INNER JOIN reviews ON movies.id = reviews.movie_id'
    )
    data = cursor.fetchall()
    print(data)
get_min_rating()

def get_max_rating():
    cursor.execute('''
   SELECT movies.title, reviews.rating FROM movies INNER JOIN reviews ON movies.id = reviews.movie_id
         WHERE reviews.rating = (SELECT MAX(rating) FROM reviews)
         
         
        
   ''' )
    data = cursor.fetchall()
    print(data)

get_max_rating()




