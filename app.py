from flask import Flask, request

import result
import product

app = Flask(__name__)


@app.before_request
def before_request():

    result.write_log('info', "User requests info, path: {0}, method: {1}, ip: {2}, agent: {3}"
                     .format(str(request.path), str(request.method), str(request.remote_addr), str(request.user_agent)))

    if 'Content-Type' in request.headers and request.headers['Content-Type'] != "application/json":
        return result.result(406, "requested URL was not found on the server")


@app.after_request
def after_request(response):
    resp = response.get_json()

    if resp is not None:
        code, status, description = resp["code"], resp["status"], resp["description"]
        response_info = "Server response info, code: {0}, status: {1}, description: {2}"

        if code == 500:
            result.write_log('warning', response_info.format(code, status, description))
        else:
            result.write_log('info', response_info.format(code, status, description))

    return response


@app.errorhandler(400)
def method_400(e):
    return result.result(400, "the browser (or proxy) sent a request that this server could not understand")


@app.errorhandler(404)
def method_404(e):
    return result.result(404, "requested URL was not found on the server")


@app.errorhandler(405)
def method_405(e):
    return result.result(405, "http method is not allowed for the requested URL")


@app.errorhandler(500)
def method_500(e):
    return result.result(500, "something has gone wrong on the restful api server")

# --------------------------------------------------------------------------------------


@app.route('/', methods=["GET"])
def hello_world():
    return 'Restful api server v1.0.1'


@app.route('/rest/ping', methods=["GET"])
def ping():
    return result.result(200, "ping successful", "Welcome to restful api server.")

# --------------------------------------------------------------------------------------


def check_integer(input_int, name):

    try:
        if input_int is None or input_int == "":  # if mongoDB start(skip) or limit is 0, it will return all data
            return 0

        return int(input_int) if int(input_int) >= 0 else result.result(400, "{} must be positive integer".format(name))

    except ValueError:
        return result.result(400, "{} is not integer".format(name))


def update_page_params(params, start, limit):

    int_start, int_limit = check_integer(start, "start"), check_integer(limit, "limit")

    if type(int_start) is tuple:
        return int_start

    if type(int_limit) is tuple:
        return int_limit

    params.update({"start": int_start, "limit": int_limit})
    return params

# --------------------------------------------------------------------------------------


@app.route('/rest/product', methods=['GET'])
def product_list():

    params, values = {}, request.values
    introduction, start, limit = values.get('introduction'), values.get('start'), values.get('limit')

    if introduction is not None and introduction != "":
        params["introduction"] = introduction

    page_params = update_page_params(params, start, limit)  # provide paging feature

    if type(page_params) is tuple:
        return page_params

    return product.products_list(**page_params)


@app.route('/rest/product/<product_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def control_product(product_id):

    if request.method == "GET":
        return product.get_product(product_id)

    if request.method == "DELETE":
        return product.delete_product(product_id)

    product_data = request.get_json()

    if "name" not in product_data or product_data["name"] is None:
        return result.result(400, "name is empty or null")

    if "introduction" not in product_data or product_data["introduction"] is None:
        return result.result(400, "introduction is empty or null")

    if "price" not in product_data or product_data["price"] is None:
        return result.result(400, "price is empty or null")

    if "quantity" not in product_data or product_data["quantity"] is None:
        return result.result(400, "quantity is empty or null")

    if request.method == "POST":
        return product.create_product(product_id, **product_data)

    return product.update_product(product_id, **product_data)

# --------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
