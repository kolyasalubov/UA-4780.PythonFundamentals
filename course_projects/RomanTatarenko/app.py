from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Advertisement(db.Model):
    __tablename__ = 'advertisement'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    ads = Advertisement.query.all()
    return render_template('index.html', ads=ads)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_ad = Advertisement(title=title, content=content)
        db.session.add(new_ad)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    ad = Advertisement.query.get_or_404(id)
    if request.method == 'POST':
        ad.title = request.form['title']
        ad.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', ad=ad)


@app.route('/delete/<int:id>')
def delete(id):
    ad = Advertisement.query.get_or_404(id)
    db.session.delete(ad)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
