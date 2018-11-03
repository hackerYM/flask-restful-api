import mongoDB
import result


def products_list(**params):

    products_data = mongoDB.products_list(**params)

    if type(products_data) is tuple:  # happen error on db connection
        return products_data

    if not products_data:
        return result.result(404, "Products data are not exist", "Products are not found in the collection.")

    return result.result(200, products_data, "The list of products data.")


def get_product(product_id):

    product_data = mongoDB.find_product(product_id)

    if type(product_data) is tuple:  # happen error on db connection
        return product_data

    if product_data == {}:
        return result.result(404, "Product data is not exist", "Product is not found in the collection.")

    return result.result(200, product_data, "Get {}'s product data.".format(product_id))


def create_product(product_id, **product_data):

    product_data["product_id"] = product_id
    product_data = mongoDB.create_product(**product_data)

    if type(product_data) is tuple:  # happen error on db connection
        return product_data

    return result.result(201, product_data, "Create {}'s product data.".format(product_id))


def update_product(product_id, **product_data):

    product_data["product_id"] = product_id
    product_data = mongoDB.update_product(**product_data)

    if type(product_data) is tuple:  # happen error on db connection
        return product_data

    if product_data == {}:
        return result.result(404, "Product data is not exist", "Product is not found in the collection.")

    return result.result(200, product_data, "Update {}'s product data.".format(product_id))


def delete_product(product_id):

    product_data = mongoDB.delete_product(product_id)

    if type(product_data) is tuple:  # happen error on db connection
        return product_data

    if product_data == {}:
        return result.result(404, "Product data is not exist", "Product is not found in the collection.")

    return result.result(204, product_data, "Delete {}'s product data.".format(product_id))
