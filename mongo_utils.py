def add_restaurant(client, data):
    """
    Add data
    :param mongo_host:
    :param data:
    :return:
    """

    db = client['test']  ## Se pone el nombre de la base de datos que se quiera usar
    inserted_id = db.my_restaurants.insert_one(data).inserted_id

    print("ID del restaurante creado ={}".format(inserted_id))
    return inserted_id


def update_restaurant(client, id, data):
    """
    Update restaurant
    :param mongo_host:
    :param id:
    :param data:
    :return:
    """

    db = client['test']
    db.my_restaurants.update_one({'_id': id}, {"$set": data})


def get_restaurant(client, id):
    """
    Get a restaurant by id
    :param mongo_host:
    :param id:
    :return:
    """

    db = client['test']
    result = db.my_restaurants.find({'_id': id})
    # 
    return result[0]


def get_restaurant_with_query(client, query):
    """
    Executes the query
    :param mongo_host:
    :param query:
    :return:
    """

    db = client['test']
    results = db.my_restaurants.find(query)
    # 
    return results
