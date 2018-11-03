from pymongo import MongoClient, errors

import util
import result
import models.contentProduct as contentProduct

# (Schema) Serialization and Deserialization, method: load(), dump()
ProductSchema = contentProduct.ProductSchema()

# --------------------------------------------------------------------------------------


# connect to mongoDB's collection, set connection timeout = 3s -> use Singleton design-pattern

class Connection(object):
    conn = None

    def __new__(cls, *args):
        if cls.conn is None:
            cls.conn = MongoClient(util.MONGO_HOST, username=util.MONGO_USERNAME, password=util.MONGO_PASSWORD,
                                   port=util.MONGO_PORT, serverSelectionTimeoutMS=3000, connect=False)
        return cls.conn


def connect_collection(db_name, collection):
    result.write_log("info", "Connect to mongoDB, host: {0}, port: {1}, db: {2}, collection: {3}"
                     .format(util.MONGO_HOST, util.MONGO_PORT, db_name, collection))
    return Connection()[db_name][collection]


def store_products():
    return connect_collection(util.MONGO_DB_STORE, util.MONGO_COLLECTION_PRODUCTS)

# --------------------------------------------------------------------------------------


# the type of collection's result is list or dict, [] or {} -> no result, tuple(Response class) -> errors happen

def products_list(**params):

    try:
        start, limit = params.pop("start"), params.pop("limit")

        products = store_products().find(params).skip(start).limit(limit)
        products_data = ProductSchema.dump(products, many=True).data

        return products_data

    except:
        result.write_log("critical", "Failed connect to mongoDB, method: products_list")
        return result.result(500, "Failed connect to mongoDB, method: products_list")


def find_product(product_id):

    try:
        product = store_products().find_one({"_id": product_id})
        product_data = ProductSchema.dump(product).data

        return product_data

    except:
        result.write_log("critical", "Failed connect to mongoDB, method: find_product")
        return result.result(500, "Failed connect to mongoDB, method: find_product")


def create_product(**product_data):

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


def update_product(**product_data):

    try:
        product = ProductSchema.load(product_data).data
        query, update = {'_id': product['_id']}, {'$set': product}

        product = store_products().find_one_and_update(query, update, return_document=True)
        product_data = ProductSchema.dump(product).data

        return product_data

    except:
        result.write_log("critical", "Failed connect to mongoDB, method: update_product")
        return result.result(500, "Failed connect to mongoDB, method: update_product")


def delete_product(product_id):

    try:
        product = store_products().find_one_and_delete({"_id": product_id})
        product_data = ProductSchema.dump(product).data

        return product_data

    except:
        result.write_log("critical", "Failed connect to mongoDB, method: update_product")
        return result.result(500, "Failed connect to mongoDB, method: update_product")
