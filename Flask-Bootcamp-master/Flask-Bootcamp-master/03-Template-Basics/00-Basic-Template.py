from flask import Flask, render_template
app = Flask(import_name=__name__, template_folder= '../templates')


@app.route('/')
def index():
    # Connecting to a template (html file)
    return render_template('00-Basic-Template.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
