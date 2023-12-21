from flask import Flask, render_template, request
from postmarker.core import PostmarkClient

app = Flask(__name__)

@app.route('/')
def blog_home():
    return render_template('blog_home.html')

@app.route('/gallery')
def blog_gallery():
    return render_template('blog_gallery.html')

@app.route('/wishlist', methods=['GET', 'POST'])
def blog_wishlist():
    if request.method == 'POST':
        msg = request.form['wishList']
        name = request.form['firstName']
        subj = request.form['subject']
        comment = request.form['comment']
        postmark = PostmarkClient(server_token='59f86335-8ff9-4c21-a132-f2f1a53b3597')
        postmark.emails.send(
            From='sender@example.com',
            To='sshafe928@west-mec.com',
            Subject='Postmark test',
            HtmlBody= f"From: {name}\nSubject: {subj}\nMessage: {msg}\nComment: {comment}"
        )
    return render_template('blog_wishlist.html')

@app.route('/friends')
def blog_friends():
    return render_template('blog_friends.html')





if __name__ == '__main__':
    app.run(debug=True)

