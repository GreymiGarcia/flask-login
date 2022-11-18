from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection
            cur = cursor.cursor()
            sql = "SELECT id, firstname, lastname, email, password FROM `user` WHERE email = %s" 
            cur.execute(sql,(user.email,))
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
            sql = "SELECT id, firstname, lastname, email, password FROM `user` WHERE id = %s" 
            cur.execute(sql,(id,))
            data = cur.fetchone()
            print(data)
            if data != None:
                return User(data["id"], data["email"], None, data["firstname"], data["lastname"])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)