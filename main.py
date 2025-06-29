from admin import *
from databases.start_questions import *
import random


    
QUESTIONS = []
REPEAT_QUESTIONS = []
ANSWERS_LIST = []

    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        context = {
            'title': 'Python', 
            'flag': True,
        }
    else:
        context = {
            'title': 'Python', 
            'flag': False,
        }
    return render_template('index.html', context=context)


@app.route('/test')
def test():
    global QUESTIONS, REPEAT_QUESTIONS
    questions = Questions()
    last_id = questions.get_last_id()
    while len(QUESTIONS) < 10:
        number = random.randrange(1, last_id+1)
        if number not in QUESTIONS:
            QUESTIONS.append(number)
    REPEAT_QUESTIONS = QUESTIONS
    context = {
        "title": "test",
        'url': 'test_quest'
    }
    
    return render_template('test.html', context=context)
    
    
@app.route('/test_quest', methods=['GET', "POST"])
def test_quest():
    global QUESTIONS
    if len(QUESTIONS) > 0:
        if request.method == 'POST':
            ANSWERS_LIST.append(request.form['answer'])
            id = QUESTIONS[0]
            one_question = Questions().get_question(id=id)
            if len(QUESTIONS) == 1:
                QUESTIONS = []
            else:
                QUESTIONS = QUESTIONS[1:]
                
            context = {
                "question": one_question,
            }

        else:
            id = QUESTIONS[0]
            one_question = Questions().get_question(id=id)
            QUESTIONS = QUESTIONS[1:]
            context = {
                "question": one_question,
            }
        
        return render_template('test.html', context=context)
    else:
        ANSWERS_LIST.append(request.form['answer'])
        answers = 0
        misstakes = 0
        misstake_dict = {
            1: "ошибку",
            2: "ошибки",
            3: "ошибки",
            4: "ошибки",
            5: "ошибок",
            6: "ошибок",
            7: "ошибок",
            8: "ошибок",
            9: "ошибок",
            10: "ошибок"
        }
        for i in range(len(REPEAT_QUESTIONS)):

            if Questions().get_question(REPEAT_QUESTIONS[i])['answer'] == ANSWERS_LIST[i]:
                answers += 1
            else:
                misstakes += 1
        if misstakes > 0:
            result = f"Тест не пройден вы совершили {misstakes} {misstake_dict[misstakes]}"
        else:
            result = "Поздровляем тест сдан"
            
        context = {
            "title": "result",
            "result": result,
            "misstakes": misstakes,
        }
        
        return render_template('result.html', context=context)


@app.route('/show_misstakes')
def show_misstakes():
    global REPEAT_QUESTIONS, ANSWERS_LIST
    question = Questions().get_question(REPEAT_QUESTIONS[0])
    REPEAT_QUESTIONS = REPEAT_QUESTIONS[1:]
    answer = ANSWERS_LIST[0]
    ANSWERS_LIST = ANSWERS_LIST[1:]
    if len(REPEAT_QUESTIONS) > 0:
        url = 'show_misstakes'
        message = "Следующий вопрос"
    else:
        url = 'index'
        message = "На главную"
    context = {
        "title": "show misstakes",
        "question": question,
        "answer": answer,
        "url": url,
        "message": message
    }

    return render_template('answers.html', context=context)


    
    
if __name__ == '__main__':
    id = Questions().get_last_id()
    if id:
        app.run()
    else:
        write_to_db(questions=questions)
        app.run()