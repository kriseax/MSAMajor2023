import sqlite3

# open a connection to a database file named database.db, which will be created once this script is run
connection = sqlite3.connect("database.db")

# open the schema.sql file and execute its contents using the executescript() method that executes multiple SQL statements at once, 
# this will create the posts table.
with open("schema.sql") as database_schema:
    connection.executescript(database_schema.read())

# create a cursor object which allows us to process rows in a database.
cur = connection.cursor()


# use the cursor’s execute() method to execute the INSERT SQL statements to blog posts to the posts table
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("New Year's Resolutions", "As the new year approaches, I'm starting to think about my resolutions for the coming year. I want to focus on my health and fitness, spend more time with family and friends, and take on new challenges at work. Here's to a great year ahead!"))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("Favorite Recipes", "I love cooking and trying out new recipes. Lately, I've been obsessed with making homemade pasta from scratch. It's surprisingly easy and always impresses my dinner guests. What are some of your favorite recipes to cook?"))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("Music Playlist", "I've been working on a new playlist lately and it's really helping me stay motivated during my workouts. From pop hits to classic rock, there's a little something for everyone. What are some of your favorite songs to listen to while working out?"))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("Favorite Travel Destinations", "I've been lucky enough to travel to some amazing places over the years, but my favorite destination is still Hawaii. There's something so relaxing and peaceful about the islands. What are some of your favorite travel destinations?"))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("Learning to Code", "I've been teaching myself how to code in my spare time and it's been a challenging but rewarding experience. There's always something new to learn and it's exciting to see my skills improve over time. Have you ever tried learning to code?"))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("Binge-worthy TV Shows", "I've been spending way too much time binge-watching TV lately. Some of my recent favorites include Stranger Things, The Queen's Gambit, and Bridgerton. What are some of your favorite TV shows to binge-watch?"))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("Work-from-home Tips", "Working from home has its challenges, but there are a few things that have really helped me stay focused and productive. I make sure to take breaks and get outside for some fresh air, and I try to stick to a regular schedule as much as possible. What are some of your tips for working from home?"))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("Favorite Books", "I'm an avid reader and always on the lookout for a good book. Some of my recent favorites include The Vanishing Half, The Nightingale, and The Immortalists. What are some of your favorite books?"))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("Self-Care Routine", "It's so important to take care of yourself, especially during stressful times. My self-care routine includes yoga, meditation, and taking"))

# commit the changes to the database and close the connection
connection.commit()
connection.close()