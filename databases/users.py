import sqlite3


class Admin:
    
    def __init__(self):
        self.db = None
        self.cursor = None
        
    
    def create_table(self):
        """функция для создания таблицы"""
        with sqlite3.connect('./databases/admin.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS Admin (login Text, password Text) """
            self.cursor.execute(query)
            self.db.commit()
            
            
    def change_password(self, new_login, new_password, flag=False):
        self.create_table()
        if flag:
            query = """UPDATE Admin SET password=? WHERE login=?"""
            self.cursor.executemany(query, [(new_password, new_login,)])
            self.db.commit()
        
        else:
            query = """INSERT INTO Admin (login, password) VALUES (?, ?)"""
            self.cursor.executemany(query, [(new_login, new_password,)])
            self.db.commit()
            
            
    def get_login_and_password(self):
        self.create_table()
        query = """SELECT * FROM Admin"""
        self.cursor.execute(query)
        data = {}
        for row in self.cursor:
            data["login"] = row[0]
            data["password"] = row[1]
            
        return data