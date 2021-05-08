import random
import mysql.connector as mysql

class Database:
    def __init__(self):
        with open("db_data.txt","r") as f:
            lines = f.readlines()
            self.host = lines[0]
            self.database = lines[1]
            self.user = lines[2]
            self.password = lines[3]

    def connect(self):
        global db_connection
        global cursor
        db_connection = mysql.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = db_connection.cursor()

    def disconnect():
        db_connection.close()
        cursor.close()

    # PREFIX

    def add_prefix(guild_id, prefix):
        Database.connect(Database())

        insert_query = f"INSERT INTO prefixes (guild_id, prefix) VALUES ({int(guild_id)}, '{str(prefix)}');"
        cursor.execute(insert_query)
        db_connection.commit()

        Database.disconnect()

    def remove_prefix(guild_id):
        Database.connect(Database())

        delete_query = f"DELETE FROM prefixes WHERE guild_id = '{int(guild_id)}';"
        cursor.execute(delete_query)
        db_connection.commit()

        Database.disconnect()

    def replace_prefix(guild_id, prefix):
        Database.connect(Database())

        replace_query = f"UPDATE prefixes SET prefix = '{prefix}' WHERE guild_id = '{int(guild_id)}';"
        cursor.execute(replace_query)
        db_connection.commit()

        Database.disconnect()

    # BLACKLIST

    def add_blacklist(user_id, reason):
        Database.connect(Database())

        insert_query = f"INSERT INTO blacklist (user_id, reason) VALUES ({int(user_id)}, '{reason}');"
        cursor.execute(insert_query)
        db_connection.commit()

        Database.disconnect()

    def remove_blacklist(user_id):
        Database.connect(Database())

        remove_query = f"DELETE FROM blacklist WHERE user_id = '{int(user_id)}';"
        cursor.execute(remove_query)
        db_connection.commit()

        Database.disconnect()

    def find_prefix(guild_id):
        Database.connect(Database())

        cursor.execute(f"SELECT prefix from prefixes where guild_id = '{guild_id}';")
        data = cursor.fetchall()
        
        return data[0]

        Database.disconnect()

    def check_blacklist(user_id):
        Database.connect(Database())

        cursor.execute(f"SELECT reason from blacklist where user_id = '{user_id}';")
        data = cursor.fetchall()

        try:
            d = data[0]

        except:
            return False


    # LOGGING

    def add_log(msg_link):
        Database.connect(Database())

        msg_id = random.randint(10000,99999)

        cursor.execute(f'SELECT msg_link FROM messages WHERE id = {msg_id};')
        check_id_fetch = cursor.fetchone()

        if check_id_fetch != 0:

            insert_query = f"INSERT INTO messages (id, msg_link) VALUES ({int(msg_id)}, '{msg_link}');"

            cursor.execute(insert_query)
            db_connection.commit()

        else:
            Database.add_log(msg_id)
        
        Database.disconnect()
        
        return msg_id


    def remove_log(log_id):
        Database.connect(Database())

        remove_query = f"DELETE FROM messages WHERE id = '{int(log_id)}';"
        cursor.execute(remove_query)
        db_connection.commit()

        Database.disconnect()

    
    def get_log(log_id):
        Database.connect(Database())

        cursor.execute(f"SELECT msg_link from messages where id = '{log_id}';")
        data = cursor.fetchall()
        
        return data[0]

        Database.disconnect()