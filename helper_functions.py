def create_users_from_file(input_file, collection):
    with open(input_file, 'r', encoding='utf-8') as read_file:
        input_data = read_file.readlines()

    user_list = []

    for i, datum in enumerate(input_data):
        user_list.append({"_id": i, "name": datum[0:-1], "password": str(i)})

    # print(user_list)
    collection.insert_many(user_list)


def create_user(user_id, user_name, user_password, collection):
    collection.insert_one({"_id": int(user_id), "name": user_name, "password": user_password})


def get_user(user_name, user_password, collection):
    x = collection.find_one({"name": user_name, "password": user_password})
    return x


