from pymongo import MongoClient
import time

connection = MongoClient('localhost', 27017)
# france = connection.France
# communes = france.communes

# nom = "Clamart2"

# start = time.time()
# commune = communes.find_one({"nom_commune_postal" : nom})
# exec_time = time.time() - start
# print(commune)
# print(exec_time)
def get_mailing_list(name):
    db = connection.mailing
    liste = db.lists.find_one({'name' : name})
    print(liste)
    user_ids = liste["users"]
    users = [ db.users.find_one({'_id' : id}) for id in user_ids ]
    return { 'name' : liste["name"],
             'users' : users}

liste = get_mailing_list("ma liste")
print(liste)






