# Flask Template Tutorial

Read the following content to learn about the project templating system 

## Project Template Structure

The `templates` folder contains the HTML templates for this Python Flask project. The templates are used to generate the dynamic web pages of the application.

## Template Files

- `base.html`: This is the base template that provides the common structure and styling for all pages in the project. It includes a navigation bar, displays flashed messages, and defines a content block that child templates can fill in.

- `index.html`: This template extends `base.html` and displays a list of posts. It uses the `{% block content %}` tag to override the content block and render the posts with their titles, content, and edit links.

- `create.html`: This template also extends `base.html` and provides a form for creating a new post. It includes input fields for the post's title and content, and a submit button.

- `edit.html`: This template extends `base.html` and allows editing of an existing post. It pre-fills the form fields with the current post's title and content, and provides a submit button for updating the post. It also includes a delete form to remove the post.

## Usage

To use these templates in a Flask application, you can render them using the Flask framework and pass the necessary data to populate the dynamic content from the flask `routes/views` in the app.py file. The templates extend the `base.html` template to ensure consistent styling and structure across the application.

## Template Elements
There are a number of elements available in the flask templates that make creating dynamic content possible.

### Dynamic Content
In Flask, the `{{ }}` syntax is used for inserting dynamic values or expressions into HTML templates using the Jinja templating engine. Jinja is the default templating engine in Flask and allows you to generate dynamic content based on variables, expressions, or function calls.

Here are some common use cases for `{{ }}` in Flask templates:

1. Variable Substitution: You can use `{{ }}` to insert the value of a variable into the HTML template. For example:

```html
<h1>{{ title }}</h1>
```
In this case, the value of the title variable will be dynamically substituted into the HTML output.

2. Expressions: You can use `{{ }}` to evaluate and display expressions. For example:

```html
<p>The total is: {{ price * quantity }}</p>
```

Here, the expression price * quantity will be evaluated and the result will be inserted into the HTML output.

3. Function Calls: You can call functions within {{ }} to perform more complex operations. For example:

```html
<p>The current date is: {{ datetime.now() }}</p>
```
In this case, the datetime.now() function will be called, and the current date and time will be displayed in the HTML output.

4. Filters: Flask templates also support filters, which are used to modify or format the displayed data. Filters can be applied to values within {{ }} using the | (pipe) symbol. For example:

```html
<p>{{ description | capitalize }}</p>
```

Here, the capitalize filter will convert the description value to capitalize the first letter.

The `{{ }}` syntax allows you to integrate dynamic values and expressions into your Flask templates, making it easier to generate dynamic HTML content based on the data and logic in your application.

### Flash messages

In Flask, flashed messages are a way to store temporary messages or notifications that can be displayed to the user. They are typically used to provide feedback or alerts after certain actions, such as submitting a form or completing an operation.

Flashed messages are stored in the user's session, which is a way to store data that persists across multiple requests. The flashed messages are cleared from the session after they are displayed to the user, ensuring that they are only shown once.

Here's how the process works:

In the Flask application, you can use the flash() function to add a message to the flashed messages. For example:

```python
flash('Login successful!')
```

The flashed message is stored in the user's session temporarily.

When a response is sent to the user, typically when rendering a template, the flashed messages can be accessed using the `get_flashed_messages()` function. This function returns a list of all flashed messages stored in the session.

In the template file, you can iterate over the flashed messages and display them to the user. For example, using a for loop to display each message in a <div> element:

```python
{% for message in get_flashed_messages() %}
  <div class="alert">{{ message }}</div>
{% endfor %}
```

The flashed messages are then rendered in the template and displayed to the user.

Flashed messages provide a convenient way to provide feedback or notifications to the user during their interaction with the Flask application. They can be used to display success messages, error messages, informational messages, or any other type of message that needs to be communicated to the user temporarily.

### Using Programming Structures in Templates

In Flask, the {% %} syntax is used for control flow statements and other template directives in the Jinja templating engine. Jinja is the default templating engine in Flask and provides a set of tags and control structures for conditional statements, loops, template inheritance, and more.

Here are some common use cases for {% %} in Flask templates:

1. Control Flow Statements: You can use {% %} to define control flow statements such as if-else conditions and loops. For example:

```html
{% if condition %}
  <p>This is true.</p>
{% else %}
  <p>This is false.</p>
{% endif %}
```

In this case, the content within the {% if %} block will be rendered if the condition is true, otherwise, the content within the {% else %} block will be rendered.

2. Loops: You can use {% %} to iterate over a collection or perform repetitive tasks. For example:

```html
<ul>
  {% for item in items %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```

In this case, the {% for %} loop will iterate over the items collection and render an `<li>` element for each item in the collection.

3. Template Inheritance: Flask templates support template inheritance, allowing you to create a base template and extend or override specific sections in child templates. This is achieved using the {% extends %} and {% block %} directives. For example:

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Welcome to My Website</h1>
  <p>Here is some content.</p>
{% endblock %}
```

In this case, the child template extends the base.html template and overrides the content block with its own content.

4. Template Includes: You can include reusable code snippets or sub-templates within a template using the {% include %} directive. For example:

```html
{% include 'header.html' %}
<p>Page content goes here.</p>
{% include 'footer.html' %}
```

In this case, the header.html and footer.html templates are included within the main template.

The `{% %}` syntax in Flask templates allows you to incorporate control flow statements, loops, template inheritance, and other advanced features, making it easier to organize and structure your templates and customize their behavior based on different conditions and data.
