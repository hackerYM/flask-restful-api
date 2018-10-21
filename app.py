from flask import Flask, request
import result

app = Flask(__name__)


@app.before_request
def before_request():
    result.write_log('info', "User requests info, path: {0}, method: {1}, ip: {2}, agent: {3}"
                     .format(str(request.path), str(request.method), str(request.remote_addr), str(request.user_agent)))


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


@app.errorhandler(404)
def method_404(e):
    return result.result(404, "requested URL was not found on the server")


@app.errorhandler(405)
def method_405(e):
    return result.result(405, "http method is not allowed for the requested URL")

# --------------------------------------------------------------------------------------


@app.route('/', methods=["GET"])
def hello_world():
    return 'Restful api server v1.0.1'


@app.route('/rest/ping', methods=["GET"])
def ping():
    return result.result(200, "ping successful", "Welcome to restful api server.")

# --------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
