import sqlite3


class Questions:
    """Класс который хранит в базе данных вопросы и варианты ответов"""
    
    def __init__(self):
        self.db = None
        self.cursor = None
        self.id = 1
        
    
    def create_table(self):
        """функция для создания таблицы"""
        with sqlite3.connect('./databases/questions.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS questions (id INTEGER, question TEXT, answer TEXT, a TEXT, b TEXT, c TEXT, d TEXT, e TEXT) """
            self.cursor.execute(query)
            self.db.commit()
            
            
    def get_last_id(self):
        """функция для получения последнего id"""
        self.create_table()
        query = """SELECT MAX(id) FROM questions"""
        self.cursor.execute(query)
        for row in self.cursor:
            if  row[0]:
                self.id = int(row[0]) + 1
        return self.id - 1
        
    
    
    def add_question(self, question, answer, a, b, c, d=None, e=None):
        """функция для добавления вопроса в бд"""
        self.create_table()
        self.get_last_id()
        query = """INSERT INTO questions (id, question, answer, a, b, c, d, e) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        insert_payments = [
            (self.id, question, answer, a, b, c, d, e,)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
        
    
    def change_question(self, id, question, answer, a, b, c, d=None, e=None):
        """функция для измениния вопроса либо вариантов ответа"""
        self.create_table()
        query = """UPDATE questions SET question=?, answer=?, a=?, b=?, c=?, d=?, e=? WHERE id=? """
        insert_payments = [
            (question, answer, a, b, c, d, e, id)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
        

    def get_all_question(self):
        """функция для получения всех вопросов из бд"""
        self.create_table()
        query = """ SELECT * FROM questions """
        self.cursor.execute(query)
        questions = {}
        count = 1
        for row in self.cursor:
            questions[count] = {"id": row[0], 
                         "question": row[1], 
                         "answer": row[2], 
                         "a": row[3], 
                         "b": row[4], 
                         "c": row[5], 
                         "d": row[6], 
                         "e": row[7]}
            count += 1
        return questions
    
    
    def get_question(self, id):
        """функция для получения конкретного вопроса"""
        self.create_table()
        query = """ SELECT * FROM questions WHERE id=? """
        self.cursor.execute(query, (id,))
        question = {}
        
        for row in self.cursor:
            question['id'] = row[0]
            question['question'] = row[1]
            question['answer'] = row[2]
            question['a'] = row[3]
            question['b'] = row[4]
            question['c'] = row[5]
            question['d'] = row[6]
            question['e'] = row[7]
            
        return question
        
        
    
