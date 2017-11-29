from flask import Flask,request,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.secret_key='hard to guess string'

class SearchForm(FlaskForm):
    keywords=StringField('电影关键词',validators=[DataRequired('电影关键词不能为空')])
    search=SubmitField('搜索')

@app.route('/',methods=['GET','POST'])
def index():
    form=SearchForm()
    if form.validate_on_submit():
        keywords=form.keywords.data
        url='https://api.douban.com/v2/movie/search?q={}'.format(keywords)
        response=requests.get(url)
        data=response.json()['subjects']
        return render_template('search.html',form=form,data=data)
    print(form.errors)
    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
