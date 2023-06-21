This file describes the code contained in the template files in this folder:

### base.html

The provided code is a template file named `base.html` that uses Jinja templates in a Flask application. Let's go through the code and explain what each part does:

1. `<title>{% block title %} {% endblock %} - FlaskApp</title>`: This line sets the page title dynamically using the content within the `{% block title %} {% endblock %}`. The actual title will be defined in the child templates that extend this base template.

2. The `<style>` block contains CSS rules that define the styling for various elements in the template.

3. `<nav>`: This is a navigation section of the page, typically containing links to different sections of the application.

4. `<a href="{{ url_for('index') }}">FlaskApp</a>`, `<a href="{{ url_for('create') }}">Create</a>`, `<a href="#">About</a>`: These are links within the navigation section. The `url_for()` function is used to generate the URLs for the specified Flask view functions.

5. `<div class="content">`: This `<div>` element is used as a container for the content of the page.

6. `{% for message in get_flashed_messages() %}`, `{% endfor %}`: This is a loop that iterates over the flashed messages, which are messages stored in the session and displayed to the user. For each message, it creates a `<div>` element with the class "alert" and displays the message.

7. `{% block content %} {% endblock %}`: This is a block tag that defines a placeholder for the child templates to fill in with their own content. The actual content will be defined in the templates that extend this base template.

This `base.html` template provides a basic structure for HTML pages in the Flask application. Child templates can extend this base template and override the `{% block %}` tags to define their specific title and content. The navigation section, flashed messages, and general styling are consistent across the application.

### index.html

The index.html template extends the base.html template, meaning it inherits its structure and styling. Here's an explanation of the code:

```html
{% extends 'base.html' %}
```

- This line indicates that the index.html template extends the base.html template, inheriting its structure, styles, and blocks.

```html
{% block content %}
```

- This defines a block named content. It indicates where the content specific to this template will be inserted within the base.html template.

```html
<h1>{% block title %} Posts {% endblock %}</h1>
```
- This creates an `<h1>` heading for the page title. It also defines a block named title within the h1 tags. The content within the block will be inserted into the page title within the base.html template.

```html
{% for post in posts %}
```
- This starts a loop that iterates over the posts collection. It retrieves each post object one by one.

```html
<div class='post'>
```
- This creates a <div> element with the CSS class post. It represents a container for displaying a single post.

```html
<p>{{ post['created'] }}</p>
```
- This displays the created value of the current post object within a paragraph element.

```html
<h2>{{ post['title'] }}</h2>
```
- This displays the title value of the current post object within an <h2> heading.

```html
<p>{{ post['content'] }}</p>
```
- This displays the content value of the current post object within a paragraph element.

```html
<a href="{{ url_for('edit', id=post['id']) }}">Edit</a>
```
- This creates a link to edit the current post. The url_for function generates the URL for the edit endpoint and passes the id of the current post as a parameter.

```html
{% endfor %}
```
- This marks the end of the for loop that iterates over the posts collection.

```html
{% endblock %}
```
- This marks the end of the content block, indicating that the content specific to this template has ended.

The index.html template extends the base.html template and overrides the content block. It displays a list of posts, including their creation date, title, content, and a link to edit each post. The content of the template will be inserted into the content block of the base.html template when rendered.

### create.html

```html
{% extends 'base.html' %}
```
- This line indicates that the create.html template extends the base.html template, inheriting its structure, styles, and blocks.

```html
{% block content %}
```
- This defines a block named content. It indicates where the content specific to this template will be inserted within the base.html template.

```html
<h1>{% block title %} Add a New Post {% endblock %}</h1>
```
- This creates an `<h1>` heading for the page title. It also defines a block named title within the h1 tags. The content within the block will be inserted into the page title within the base.html template.

```html
<form method="post">
```
- This starts an HTML form. The method attribute is set to "post", indicating that the form will be submitted using the HTTP POST method.

```html
<label for="title">Title</label>
<br>
<input type="text" name="title"
       placeholder="Post title"
       value="{{ request.form['title'] }}"></input>
<br>
```
- This creates a label and an input field for the post title. The name attribute is set to "title", which is used to identify the input field. The placeholder attribute provides a placeholder text for the input field. The value attribute is populated with the title value from the request.form object, which allows the form to retain the previously submitted title value if there was one.

```html
<label for="content">Post Content</label>
<br>
<textarea name="content"
          placeholder="Post content"
          rows="15"
          cols="60"
          >{{ request.form['content'] }}</textarea>
<br>
```
- This creates a label and a textarea field for the post content. Similar to the title input field, the name attribute identifies the field, the placeholder attribute provides a placeholder text, and the rows and cols attributes define the size of the textarea. The content within the textarea is populated with the content value from the request.form object, which allows the form to retain the previously submitted content value if there was one.

```html
<button type="submit">Submit</button>
```
- This creates a submit button for the form. When clicked, it submits the form data to the server.

```html
</form>
````
 - This marks the end of the HTML form.

```html
{% endblock %}
```
- This marks the end of the content block, indicating that the content specific to this template has ended.

The create.html template extends the base.html template and overrides the content block. It displays a form for creating a new post, including input fields for the post title and content. The form allows users to enter a title and content, and when submitted, the form data is sent to the server for processing. The content of the template will be inserted into the content block of the base.html template when rendered.

### edit.html

The edit.html template is used for editing a post in a Flask application. Here's an explanation of the code:

```html

{% extends 'base.html' %}
```
- This line indicates that the edit.html template extends the base.html template, inheriting its structure, styles, and blocks.

```html

{% block content %}
```
- This defines a block named content. It indicates where the content specific to this template will be inserted within the base.html template.

```html

<h1>{% block title %} Edit "{{ post['title'] }}" {% endblock %}</h1>
```
- This creates an `<h1>` heading for the page title. It also defines a block named title within the h1 tags. The content within the block will be inserted into the page title within the base.html template. In this case, the title will display the text "Edit" followed by the value of post['title'], which represents the title of the post being edited.

```html
<form method="post">
```
- This starts an HTML form. The method attribute is set to "post", indicating that the form will be submitted using the HTTP POST method.

```html
<label for="title">Title</label>
<br>
<input type="text" name="title"
       placeholder="Post title"
       value="{{ request.form['title'] or post['title'] }}"></input>
<br>
```
- This creates a label and an input field for the post title. The name attribute is set to "title", which is used to identify the input field. The placeholder attribute provides a placeholder text for the input field. The value attribute is populated with the title value from the request.form object if it exists, or with the title value from the post object if the form data is not available. This allows the form to display the current title of the post being edited.

```html
<label for="content">Post Content</label>
<br>
<textarea name="content"
          placeholder="Post content"
          rows="15"
          cols="60"
          >{{ request.form['content'] or post['content'] }}</textarea>
<br>
```
- This creates a label and a textarea field for the post content. Similar to the title input field, the name attribute identifies the field, the placeholder attribute provides a placeholder text, and the rows and cols attributes define the size of the textarea. The content within the textarea is populated with the content value from the request.form object if it exists, or with the content value from the post object if the form data is not available. This allows the form to display the current content of the post being edited.

```html

<button type="submit">Submit</button>
```
- This creates a submit button for the form. When clicked, it submits the form data to the server for updating the post.

```html
</form>
```
- This marks the end of the HTML form.

```html
<hr>
<form action="{{ url_for('delete', id=post['id']) }}" method="POST">
    <input type="submit" value="Delete Post"
            onclick="return confirm('Are you sure you want to delete this post?')">
</form>
```
- This section creates a form for deleting the post. The action attribute specifies the URL to which the form will be submitted, using the url_for function with the delete endpoint and the id parameter set to the post['id'] value. When the delete button
