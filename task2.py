from pymongo import MongoClient

def get_database():
    # Замініть '<your_connection_string>' на ваш MongoDB URI
    client = MongoClient("<your_connection_string>")
    return client["cats_db"]

db = get_database()

# Читання (Read)
def get_all_cats():
    cats = db.cats.find()
    for cat in cats:
        print(cat)

def get_cat_by_name(name):
    cat = db.cats.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Cat with name {name} not found.")


# Оновлення (Update)

def update_cat_age(name, new_age):
    result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Updated age of {name} to {new_age}")
    else:
        print(f"Cat with name {name} not found.")

def add_feature_to_cat(name, feature):
    result = db.cats.update_one({"name": name}, {"$push": {"features": feature}})
    if result.matched_count > 0:
        print(f"Added feature to {name}: {feature}")
    else:
        print(f"Cat with name {name} not found.")


# Видалення (Delete)

def delete_cat_by_name(name):
    result = db.cats.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Deleted cat {name}")
    else:
        print(f"Cat with name {name} not found.")

def delete_all_cats():
    result = db.cats.delete_many({})
    print(f"Deleted {result.deleted_count} cats")


# Запуск функцій

# Приклад викликів функцій:
get_all_cats()
get_cat_by_name("barsik")
update_cat_age("barsik", 5)
add_feature_to_cat("barsik", "спить на ліжку")
delete_cat_by_name("barsik")
delete_all_cats()


# Коментарі та обробка винятків

try:
    # Виклики CRUD функцій
except Exception as e:
    print(f"An error occurred: {e}")
