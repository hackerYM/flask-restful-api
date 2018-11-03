from flask import jsonify
import logging
import util

logging.basicConfig(level=logging.INFO, format=util.log_format)
logger = logging.getLogger(__name__)

handler = logging.FileHandler(util.log_filename)
handler.setLevel(logging.INFO)

formatter = logging.Formatter(util.log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

# http code status
status = {
    200: 'OK',
    201: "Created",
    204: "No Content",
    400: 'Bad Request',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    409: 'Conflict',
    500: 'Internal Server Error'
}

# http code description (default)
default_description = {
    200: 'Successful standard response',
    201: 'Successful create new resource',
    204: 'Successful process the request and is not returning any content.',
    400: 'Please check paras or query valid, server cannot or will not process the request.',
    404: 'Please read the document to check API, the requested resource could not be found.',
    405: 'Please read the document to check API, the request method is not supported for the requested resource.',
    406: 'Please read the document to check API, the request content not acceptable according to headers.',
    409: 'Request could not be processed because of conflict in the current state of the resource.',
    500: 'Please contact api server manager.'
}


def write_log(level, msg):

    if level == "info":
        logger.info(msg)
    elif level == "warning":
        logger.warning(msg)
    elif level == "critical":
        logger.critical(msg)


def result(code, msg, description=""):

    description = default_description.get(code) if description == "" else description
    response = jsonify({
        "code": code,
        "status": status.get(code),
        "message": msg,
        "description": description
    })

    return response, code, {'Content-Type':'application/json'}