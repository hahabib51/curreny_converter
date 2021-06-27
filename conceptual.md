### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Python is used for back-end development. JavaScript can be used mostly for front end user side but could also be back end. Developers use Python for a range of scientific applications. They use JavaScript for web development, user-facing functionality, and servers. Python uses snake-case and JavaScript uses CamelCase. The languages have their own specific way of writing code but the idea of the concpet is the same.



- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
    The 1st way is to append "c" to the list. Use .get(c, default). 

- What is a unit test?
    Unit testing is testing the functionality of a module or method.


- What is an integration test?
    Integration testing is making sure that components work together.


- What is the role of web application framework, like Flask?
    Frameworks are the foundation for building web applications. Web frameworks are a collection of the foundational tools necessary for web development. Flask maps URLs to the code they are requesting, connects to a database, creates and serves up customizable HTML templates, stores state information in a session, provides testing and debugging tools, and much much more. 




- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    You use URL parameters when the content feels more like the subject of the page. You use Query parameters when you feel it is more for things like extra info about the page. 



- How do you collect data from a URL placeholder parameter using Flask?
    from flask import request. use request.args is a dict-like object of query parameters. You need to accept POST requests in methods. request.form is a dict-like object of POST parameters.



- How do you collect data from the query string using Flask?
    Use
from flask import flask 

@app.route("/data")
def data():
    # query_string = ???
    return render_template("data.html")
  
    

- How do you collect data from the body of the request using Flask?
    Use
from flask import request

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.data



- What is a cookie and what kinds of things are they commonly used for?
    A cookie store state. Collect personal data. Track website activities. Verification for login credentials. 



- What is the session object in Flask?
    In the flask, a session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values. 


- What does Flask's `jsonify()` do?
    You can export JSON files with Flask, instead of just text. Jsonify an object like a list not a set.
