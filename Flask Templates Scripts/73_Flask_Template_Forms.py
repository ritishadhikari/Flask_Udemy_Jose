from flask import Flask, render_template, request

app = Flask(import_name= __name__, static_folder= 'static', template_folder= 'templates')

@app.route(rule = '/')
def index():
    return render_template('Flask_index_73.html')


@app.route(rule = '/signup_form')
def signup_form():
    return render_template('Flask_signup_73.html')

# we can receive get information through the form into our python working file
# we can post information from the python working file to the browser through the ginga template

@app.route(rule = '/thankyou')
def Thank_you():
    first = request.args.get('first') # this recieves the content stored in first from the signup_form
    last  = request.args.get('last') # this recieves the content stored in last from the signup_form
    return render_template('Flask_thankyou_73.html', first = first, last = last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Flask_404_73.html'), 404


if __name__ == '__main__':
    app.run(debug = True, use_reloader = False)
