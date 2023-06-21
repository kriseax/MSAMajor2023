import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

# make a Flask application object called app
app = Flask(__name__)

app.config["DEBUG"] = True

# flash uses the secret key to secure sessions that remember information from one request to another
# This is for the error messages
app.config['SECRET_KEY'] = 'your secret key'


# Function to open a connection to the database.db file
def get_db_connection():
    # create connection to the database
    conn = sqlite3.connect('database.db')
    
    # allows us to have name-based access to columns
    # the database connection will return rows we can access like regular Python dictionaries
    conn.row_factory = sqlite3.Row

    #return the connection object
    return conn

"""
Function to get a post from the database
Input: post_id
Output: the post from the database
"""
def get_post(post_id):
    #get database connection object
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',(post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    
    return post


# use the app.route() decorator to create a Flask view function called index(). This displayes when the site home age is requested 
@app.route('/')
def index():
    # use the get_db_connection() function to open a database connection
    conn = get_db_connection()

    # execute an SQL query to select all entries from the posts table.
    # use the fetchall() method to fetch all the rows of the query result. returns a list
    posts = conn.execute('SELECT * FROM posts').fetchall()

    # close the connection
    conn.close()

    #send the posts to the index.html template to be displayed
    return render_template('index.html', posts=posts)


# route to create a post
# pass the tuple ('GET', 'POST') to the methods parameter to allow both GET and POST requests
@app.route('/create/', methods=('GET', 'POST'))
def create():

    #If page requested with post, get and validate form data. Insert post to db and redirect to the home page
    if request.method == 'POST':
        # get title and content
        title = request.form['title']
        content = request.form['content']

        # display error message if title or content not submitted
        # else make a database connection and insert content 
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            #Connect to database
            conn = get_db_connection()
            #Run insert query to insert the new post to the database
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            #Commit the insert
            conn.commit()
            #Close the connection
            conn.close()

            #Redirect to the site index after the post is added so it can be displayed
            return redirect(url_for('index'))
    
    #If page requested with GET load the create.html template
    return render_template('create.html')


# Route to edit a post
#pass the tuple ('GET', 'POST') to the methods parameter to allow both GET and POST requests
#The poost id is passed as a url parameter
@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    #id is sent as a url parameter
    post = get_post(id)

    #If page requested with post, get and validate form data. Insert post to db and redirect to the home page
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            #connect to the db
            conn = get_db_connection()
            
            #execute the update query to update the post in the db
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()

            #Redirect to the site index after the post is added so it can be displayed
            return redirect(url_for('index'))
    
    #On GET request send post to edit page to display
    return render_template('edit.html', post=post)

# Route to delete a post
# Delete page can only run with a POST Request
#post id is passed as a url parameter
@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    #get post id
    post = get_post(id)

    #connect to db
    conn = get_db_connection()

    #execute the delete query
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))

    #commit and close the database
    conn.commit()
    conn.close()

    #Flash a success message to the user
    flash('"{}" was successfully deleted!'.format(post['title']))

    #redirect to the index page
    return redirect(url_for('index'))

#run the flask
app.run(host="0.0.0.0")