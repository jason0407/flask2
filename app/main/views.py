from datetime import  datetime
from flask import render_template,session,redirect,url_for,request,flash


from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/')
def index():
    #获取浏览器信息
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html',user_agent=user_agent,current_time = datetime.utcnow())

@main.route('/change',methods=['GET','POST'])
def change():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('好像你改名了！')
        session['name'] = form.name.data
        return redirect(url_for('.change'))
    return render_template('change.html',form=form,name = session.get('name'))

@main.route('/addUser',methods=['GET','POST'])
def addUser():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.addUser'))
    return render_template('addUser.html',form=form,name = session.get('name'),known = session.get('known',False))
