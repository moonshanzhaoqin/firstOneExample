from flask import Flask ,render_template,request,redirect,url_for,session
import config
from models import User,Question,Answer
from exts import db
from decorator import loin_required


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



@app.route('/')
def index():
    context = {
        'questions':Question.query.order_by('-creat_time').all()
    }
    return render_template('index.html',**context)

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get("phone")
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone,User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return 'user is not exist'


@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method=='GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('phone');
        userName = request.form.get('username');
        password1 = request.form.get('password1');
        password2 = request.form.get('password2');
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return 'user  is  exist'
        else:
            if password1!=password2 :
                return "password is diferent"
            else:
                user = User(telephone=telephone, username=userName, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/loginout/', methods = ['GET', 'POST'])
def loginout():
    session.clear()
    # del session['user_id']
    # session.pop('user_id')
    return redirect(url_for('login'))


@app.route('/question/', methods = ['GET', 'POST'])
@loin_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        context = request.form.get('context')
        question = Question(title=title,content=context)
        user_id =session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author=user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))

@app.route("/detail/<question_id>/",methods=["GET","POST"])
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html',question=question_model)


@app.route("/add_answer/",methods=['GET','POST'])
@loin_required
def add_answer():
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')

    answer = Answer(content=content)
    user_id = session['user_id']
    user = User.query.filter(User.id==user_id).first()
    answer.author = user
    question = Question.query.filter(Question.id==question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail',question_id=question_id))





@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}

if __name__ == '__main__':
    app.run()
