from flask import Flask, render_template, request
from databases.questions import Questions
from databases.users import Admin


app = Flask(__name__)


QUESTIONS = Questions()
IF_AUTENTICATED = False


@app.route('/login', methods=['GET', 'POST'])
def login():
    global IF_AUTENTICATED
    if request.method == 'POST':
        user = Admin()
        data = user.get_login_and_password()
        if request.form["login"] == data["login"] and request.form["password"] == data["password"]:
            context = {
                "title": "administrator",
                "message": "",
                "flag": True,
            }
            IF_AUTENTICATED = True
        
            return render_template("login.html", context=context)
        
        else:
            context = {
                "title": "login",
                "message": "Неверный логин или пароль",
                "flag": False,
            }
            
            return render_template('login.html', context=context)
    else:
        if IF_AUTENTICATED:
            context = {
                "title": "administrator",
                "message": "",
                "flag": True,
            }
        
            return render_template("login.html", context=context)
    
        else:
            context = {
                'title': 'login',
                "flag": False
            }
            return render_template('login.html', context=context)
    

@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if IF_AUTENTICATED:
        if request.method == "POST":
            question = request.form["question"]
            option_a = request.form["option_a"]
            option_b = request.form["option_b"]
            option_c = request.form["option_c"]
            option_d = request.form["option_d"]
            option_e = request.form["option_e"]
            QUESTIONS.add_question(question=question, a=option_a, b=option_b, c=option_c, d=option_d, e=option_e)
            context = {
                "titile": "добавление вопроса",
                "message": "вопрос успешно добавлен",
                "info": "добавить еще",
                "url": 'add_question',
                "flag": True,
            }
            
            return render_template('info.html', context=context)
            
        
        else:
            context = {
                "title": "add new question",
                "flag": False,
            }
        
            return render_template('add_question.html', context=context)
    else:
        
        context = {
            "title": "ошибка входа",
            "message": "Вы не авторизованы, пожалуйста войдите в аккаунт",
            "flag": False,
        }
        
        return render_template("info.html", context=context)
    
    
@app.route('/change_question', methods=['GET', 'POST'])
def change_question():
    global IF_AUTENTICATED
    if IF_AUTENTICATED:
        if request.method == 'POST':
            if "question_id" in request.form.keys():
                quest = Questions()
                question = quest.get_question(int(request.form["question_id"]))
                context = {
                    "title": "Изменение вопроса",
                    "question": question,
                    "flag": True,
                }
                
                return render_template("change_question.html", context=context)
            else:
                questions = Questions()
                new_question = request.form["question"]
                option_a = request.form["option_a"]
                option_b = request.form["option_b"]
                option_c = request.form["option_c"]
                option_d = request.form["option_d"]
                option_e = request.form["option_e"]
                answer = request.form["answer"]
                id = request.form["id"]
                questions.change_question(id=id, question=new_question, answer=answer, a=option_a, b=option_b, c=option_c, d=option_d, e=option_e)
                context = {
                    "title": "изменение вопроса",
                    "message": "вопрос успешно изменен",
                    "info": "изменить еще",
                    "url": 'change_question',
                    "flag": True,
                }
                
                return render_template("info.html", context=context)
        else:
        
            context = {
                "title": "Изменение вопроса",
                "flag": False,
            }
        
            return render_template("change_question.html", context=context)    
 
    else:
        context = {
            "title": "ошибка входа",
            "message": "Вы не авторизованы, пожалуйста войдите в аккаунт",
            "flag": False,
        }
        
        return render_template("info.html", context=context)
    