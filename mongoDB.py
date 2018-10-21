from pymongo import MongoClient
import util
import result


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


def products_list():

    try:
        products = store_products().find()

        return [product for product in products]
    except:
        result.write_log("critical", "Failed connect to mongoDB, method: products_list")
        return None


def find_product(id):

    try:
        query, fields = {"_id": id}, {}
        products = store_products().find_one(query)

        return products
    except:
        result.write_log("critical", "Failed connect to mongoDB, method: find_product")
        return None


print(products_list())
print("---")
print(find_product('1'))
