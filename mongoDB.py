from pymongo import MongoClient, errors

import util
import result
import models.contentProduct as contentProduct

# (Schema) Serialization and Deserialization, method: load(), dump()
ProductSchema = contentProduct.ProductSchema()

# --------------------------------------------------------------------------------------

# connect to mongoDB's collection, set connection timeout = 3s -> use Singleton design-pattern
def connect_collection(host, port, db_name, collection):
    result.write_log("info", "Connect to mongoDB, host: {0}, port: {1}, db: {2}, collection: {3}"
                     .format(host, port, db_name, collection))
    name, pwd = util.MONGO_USERNAME, util.MONGO_PASSWORD

    client = MongoClient(host, username=name, password=pwd, port=port, serverSelectionTimeoutMS=3000, connect=False)
    db = client[db_name]
    return db[collection]


def store_products():
    return connect_collection(util.MONGO_HOST, util.MONGO_PORT, util.MONGO_DB_STORE, util.MONGO_COLLECTION_PRODUCTS)

# --------------------------------------------------------------------------------------


# the type of collection's result is list or dict, [] or {} -> no result, tuple(Response class) -> errors happen
def products_list():

    try:
        products = store_products().find()
        products_data = ProductSchema.dump(products, many=True).data

        return products_data

    except:
        result.write_log("critical", "Failed connect to mongoDB, method: products_list")
        return result.result(500, "Failed connect to mongoDB, method: products_list")


def find_product(id):

    try:
        query, fields = {"_id": id}, {}
        product = store_products().find_one(query)
        product_data = ProductSchema.dump(product).data

        return product_data

    except:
        result.write_log("critical", "Failed connect to mongoDB, method: find_product")
        return result.result(500, "Failed connect to mongoDB, method: find_product")


def create_product(product_data):

    try:
        product = ProductSchema.load(product_data).data
        store_products().insert_one(product)

        return product_data

    except errors.DuplicateKeyError:
        result.write_log("warning", "DuplicateKey error in mongoDB, method: create_product")
        return result.result(409, "already exist product id in the collection")
    except:
        result.write_log("critical", "Failed connect to mongoDB, method: create_product")
        return result.result(500, "Failed connect to mongoDB, method: create_product")

print(create_product(
    {
        'product_id': '4',
        'introduction': 'htc phone',
        'quantity': 50,
        'name': 'htc u12',
        'price': 350
    }
))