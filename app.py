from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
from vectorizer import vect

app = Flask(__name__)

# 分類器の準備
cur_dir = os.path.dirname(__name__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))
db = os.path.join(cur_dir, 'reviews.sqlite')

# 文書を受け取って分類結果を返す
def classify(document):
    label = {0: 'negative', 1:'positive'}
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = clf.predict_proba(X).max()

    return label[y], proba

# モデルの更新
def train(document, y):
    X = vect.transform([document])
    clf.partial_fit(X, [y])

# 送信された映画レビューをSQLiteデータベースに格納
def sqlite_entry(path, document, y):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("INSERT INTO review_db (review, sentiment, date) VALUES (?, ?, DATETIME('now'))", (document, y))
    conn.commit()
    conn.close()

## 以下FLASK

# レビュー投稿のためのテキストフィールド
class ReviewForm(Form):
    movie_review = TextAreaField('', [validators.DataRequired(), validators.length(min=15)]) #validators.lengthで入力文章の最低字数を指定

@app.route('/')
def index():
    form = ReviewForm(request.form)

    return render_template('reviewform.html', form=form)

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    # 投稿されていたら
    if request.method == 'POST' and form.validate():
        review = request.form['movie_review']
        y, proba = classify(review)

        return render_template('results.html', content = review, prediction = y, probability = round(proba * 100, 2)) # round(p, 2) : pを小数2桁に丸める
    
    # 投稿されていなかったら
    return render_template('reviewform.html', form = form)

@app.route('/thanks', methods = ['POST'])
def feedback():
    feedback = request.form['feedback_button']
    review = request.form['review']
    prediction = request.form['prediction']
    inv_label = {'negative': 0, 'positive': 1}
    y = inv_label[prediction]
    # 予測が不正解の場合、もう一方のラベルに変える
    if feedback == 'Incorrect':
        y = int(not(y))
    # モデルの更新
    train(review, y)
    # データベースに格納
    sqlite_entry(db, review, y)

    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug = True)






