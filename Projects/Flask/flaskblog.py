from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # vs __main__

app.config['SECRET_KEY'] = '21c95e12b20377bd122c49a189ffe36c'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home') # both routes handled by same func
def home():
    # return '<h1>Home Page</h1>' but this can get messy!!!
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


# make sure you cd to Flask dir
# write 'set FLASK_APP=flaskblog.py' (whatever the file is called)
# then write 'flask run'
# Since we do not want to always stop the app to make changes
# We can run the app in DEBUG mode and just click refresh to see changes
# just write 'set FLASK_DEBUG=1'`

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__': # can skip the above steps!
    app.run(debug=True)
