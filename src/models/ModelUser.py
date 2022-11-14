from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection
            cur = cursor.cursor()
            sql = "SELECT id, firstname, lastname, email, password FROM `user` WHERE email = '{}'".format(user.email) 
            cur.execute(sql)
            data = cur.fetchone()
            print(data)
            if data != None:
                return User(data["id"], data["email"], User.check_password(data["password"], user.password), data["firstname"], data["lastname"])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection
            cur = cursor.cursor()
            sql = "SELECT id, firstname, lastname, email, password FROM `user` WHERE id = '{}'".format(id) 
            cur.execute(sql)
            data = cur.fetchone()
            print(data)
            if data != None:
                return User(data["id"], data["email"], None, data["firstname"], data["lastname"])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)