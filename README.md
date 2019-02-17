# Flask - RESTful API server
###### tags: `flask` `restful-api` `2018`

**使用 Python Flask 建立一個 RESTful API server**

* Date: 2018-11-03
* Author: Yen-Ming
* Email: hunglow7808@gmail.com
* Code: https://github.com/HackerYenMing/flask-tutorial

## Preface

### Introduction 

![](https://i.imgur.com/snrpqPP.png)

最近公司要建立 api server 去搭建 POC (Proof of concept)，想快速地開發出可行的 server，於是，就踏入了 Flask 的世界。

在開發的過程中踩了許多坑，也翻閱了很多 Document、Blog，想藉這個機會把學習記錄跟開發過程寫成 Blog，不只是方便我自己以後翻閱，網路上也多了一份資訊，讓想要學習 Python Flask 或者 restful api 的人有所收穫。

Blog 之中若是有任何錯誤、有更好的方法，或是想跟我討論相關技術，歡迎來信跟我探討。

### Requests Skills

Development - 需要 Python 程式能力、Web service 基本概念、MongoDB 非關聯式資料庫，沒接觸過或不太熟的朋友們，可以用以下的資源來學習。

- Python

    0. [Python 基礎教程](http://www.runoob.com/python3/python3-tutorial.html)

    1. [Python 實踐指南](https://pythonguidecn.readthedocs.io/zh/latest/index.html)

    2. [HackerRank - Python 練習平台](https://www.hackerrank.com/domains/python)

- Web service

    0. [Web 前端 vs 後端](https://noootown.wordpress.com/2016/03/23/frontend-backend-breakfast/)

    1. [HTTP Request and Response](https://www.webnots.com/what-is-http/)

    2. [Web 開發技術發展歷史](https://www.tianmaying.com/blog/8ab3eda84daf4e54014daf68ff09000b)

- MongoDB

    - Install

        建議使用 Docker 安裝，比較方便省事，記得順便裝 GUI 管理工具 - Robo 3T。
        
        0. [Windows 安裝教學](https://dotblogs.com.tw/explooosion/2018/01/21/040728)

        1. [Ubuntu Linux 安裝教學](https://blog.gtwang.org/linux/install-mongodb-on-ubuntu/)

        2. [Install on Docker with Auth enabled](https://stackoverflow.com/questions/37450871/how-to-allow-remote-connections-from-mongo-docker-container)

    - Auth

        0. [Manual - Enable Auth](https://docs.mongodb.com/manual/tutorial/enable-authentication/)

        1. [MongoDB 加上驗證機制](https://blog.yowko.com/2017/08/mongodb-enable-auth/)

    - Shell
    
        0. [基礎入門教學](https://blog.gtwang.org/programming/getting-started-with-mongodb-shell-1/)
        
        1. [詳細教程](http://www.runoob.com/mongodb/mongodb-tutorial.html)

:::danger
無論是用哪一種平台安裝 MongoDB，因為 noSQL 普遍預設不用帳密就可以使用 db，若是不希望你的重要資料所有人都可以存取修改，一定要加上驗證機制。
:::

Deployment - 需要了解 git 版本控制、Docker 容器化技術。

- git

- Docker

### Awesome Blog

在實際開發之前，建議先讀他們寫的 Blog，寫得非常好，可以幫助理解許多概念

0. [Gevin's Blog - Flask tutorial](https://blog.igevin.info/archive/)

1. [NotFalse Blog - HTTP Research](https://notfalse.net/http-series)

2. [Flask 與 SQLite 架抽籤網站](https://blog.liang2.tw/posts/2015/09/flask-draw-member/)

### Flask Document

官方的查詢文件，詳細的使用手則

0. [Document](http://flask.pocoo.org/docs/1.0/)

1. [Extensions](http://flask.pocoo.org/extensions/)

### Development Enviornment

- OS - Window 10, Ubuntu 18.04 

    * [Windows 安裝 Python3](https://wwssllabcd.github.io/blog/2018/05/21/how-to-install-python-on-windows/)

    * [Linux 安裝 Python3](https://pythonguidecn.readthedocs.io/zh/latest/starting/install3/linux.html)

    * [Virtualenv - venv](https://openhome.cc/Gossip/CodeData/PythonTutorial/PipPyvenvPy3.html)

- Text editor - vim、Notepad++

    當初開發時，直接使用文字編輯器，加上 pip、venv 建立一個虛擬環境，直接在 command line 執行，但遇到許多小麻煩，使用 tab 縮排發生 TabError、要自己控管切割環境、比較難 debug 等等。

- IDE - PyCharm Professional Edition

    後來就決定用 IDE，挑了幾間的使用過後，覺得 PyCharm 最順手，有許多強大的功能，提供程式碼修復建議、自動修改關聯的重構項目 (Refactor)、各式各樣的插件 (Plugins)、支援 git, docker 等等，還有很多功能沒有提及，可以到官方網站認識。
    
    另外，他有兩種版本，Community Edition, Professional Edition，前者免費、後者只能試用一個月之後要收費，但是，他有提供學生專案，用校級信箱註冊可以使用一整年，學校帶來的些許好處之一吧。:smile: 
        
    0. [學生授權申請](https://sales.jetbrains.com/hc/zh-cn/articles/207154369-学生授权申请方式)

    1. [Install PyCharm In Ubuntu](https://itsfoss.com/install-pycharm-ubuntu/)

    2. [PyCharm - Quick Start Guide](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)

    3. [PyCharm - Vedio Resources](https://www.jetbrains.com/pycharm/documentation/)

- API testing - Postman
    
    
    開發 api server 常常需要測試 api 回傳結果是否正確，瀏覽器是一種方法，但是它只能使用 method [GET]，其他 method 就沒辦法了。
    
    因此，介紹一個很棒的工具 Postman，除了可以檢測 api 回傳結果是否正確以外，也能分門別類你的 api 紀錄 (Collections)、編寫自動化測試 (Testing Automation)，幫助開發 api server 更加順利。

    0. [基本教學](https://xenby.com/b/151-推薦-使開發api更方便的工具-postman)

    1. [Tutorial and Hints](https://steelkiwi.com/blog/api-testing-useful-tools-postman-tutorial-and-hints/)

    
## Basis

相信你已經對 python3 和 web service 有一定了解，我們就正式開始吧。

### Hello World

打開 PyCharm 點選 File -> New Project，選擇 Flask 框架，幫你的專案取一個名字

![](https://i.imgur.com/uVszEXX.png)

左邊資料夾的意義

* static: 儲存靜態文件，那些不會改變的文件，比如 CSS, JavaScript 的文件或圖片

* templates: 用來儲存模板 (HTML)，顯示 web 前端頁面，默認會使用 Jinja 模板語言

* venv: PyCharm 用來建立虛擬環境，實際部屬不會使用到此資料夾內容

static, templates 用來寫 web 前端，在 api server 中幾乎不會用到他們 :sweat_smile: 

![](https://i.imgur.com/BLxbeju.png)

在下面點開 Terminal，你會發現路徑前面已經加上了 (venv)，這是 PyCharm 方便的地方，自動建立一個虛擬環境，不會汙染到其他專案的環境。

在此輸入 ```python app.py```，把 server 執行起來，若要關掉輸入 ```Ctrl + C``` 即可。 

![](https://i.imgur.com/wQqPCkB.png)

用瀏覽器輸入這個網址，如果順利看到這個頁面，恭喜你建立一個 server 了 :thumbsup:

![](https://i.imgur.com/rU7jUDL.png)

先修改一些程式碼

@app.route 就是 Flask 的 routing decorator，第一個的參數是 endpoint 的路徑，第二個則是 endpoint 可以接收的 http method，用來裝飾下面的方法 ```hello()```，定義 api 被呼叫後，要回傳的結果 ```'Hello World!'```。

```app.run()``` 中有三個參數，第一個 ```host='0.0.0.0'``` 代表任意機器都可以連接，第二個為使用的 port，所以在 VM 中部屬此 server，並開啟對應的 port，就可以使用 ```<host-ip>:<port>/<endpoint>``` 連接使用 server 。

第三個 ```app.debug=True``` 在 development 環境使用，發生內部錯誤時候，會顯示異常資訊，並自動重新啟動專案，幫助使用者可以快速開發。

:::danger
正式 production 環境中，絕對不要設置 ```app.debug=True```
:::

```python=
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### First API

要打造出我們的第一個 API，功能如下：

* code, status: http 狀態碼
* description: API 的描述、補充訊息
* message: 呼叫 API 要給的資料
* API 需要給其他資訊，可自行添加欄位

```shell=
api: [GET] /rest/ping

request: 
    URL: http://<host>/rest/ping
    Method: GET
    Headers:
        Content-Type: application/json
        Accept: application/json
    
response: 
    Headers:
        Status Code: 200 OK
    Body: 
        {
            "code": 200,
            "status": "OK",
            "message": "ping successful", 
            "description": "Welcome to restful api serever." 
        }
```

於是我們寫了一個 method，來完成這個 API

```python=
@app.route('/rest/ping', methods=["GET"])
def ping():
    return {
        "code": 200,
        "status": "OK",
        "message": "ping successful",
        "description": "Welcome to restful api serever."
    }
```

結果發生 Error :interrobang: 

![](https://i.imgur.com/jvPqz8o.png)

原來 [WSGI](https://zh.wikipedia.org/wiki/Web服务器网关接口) 限制了回傳型態只能是 string, tuple, Response instance, or WSGI callable，所以我們需要轉型態，把 Python 基本資料型態 Dict, List，轉換成 Json 格式的 Response instance。

所以我們使用 Flask 提供的 jsonify 模組，不僅會將 Python 基本資料型態轉換為 json，而且也會修改 ```Content-Type: application/json```。

最後，加上回報 Header - Status Code 資訊，```200 OK```。

- [Flask return json format](https://www.polarxiong.com/archives/Flask设置返回json格式.html)

- [About Responses](http://flask.pocoo.org/docs/1.0/quickstart/#about-responses)

Code:

```python=
@app.route('/rest/ping', methods=["GET"])
def ping():
    response_data = {
        "code": 200,
        "status": "OK",
        "message": "ping successful",
        "description": "Welcome to restful api server."
    }

    # Same as: Response(json.dumps(response_data), mimetype='application/json'), 200
    return jsonify(response_data), 200
```

Result:

![](https://i.imgur.com/M7zARKk.png)

### Error Handler

[HTTP Status Codes](https://notfalse.net/48/http-status-codes) :1234: 

[HTTP Cats](https://http.cat/) :cat2: 

使用者呼叫 api server，有時會呼叫錯誤，常常發生的狀況有 400, 404, 405 等等，Flask 預設是回傳一個錯誤網頁 (HTML)，但是，我們希望回傳 json 格式，因此需要自己定義。

![](https://i.imgur.com/Lat78Kj.png)

![](https://i.imgur.com/PXUiLgQ.png)

首先，結果的 json 格式，每個 api 的回傳欄位都是一樣，所以我們可以把他寫成一個模組，最後，需要回傳結果，在使用這個模組的方法即可。 

```python=
# File: result.py

from flask import jsonify

# http code status
status = {
    200: 'OK',
    400: 'Bad Request',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error'
}

# http code description (default)
default_description = {
    200: 'Successful response',
    400: 'Please check paras or query valid.',
    404: 'Please read the document to check API.',
    405: 'Please read the document to check API.',
    500: 'Please contact api server manager.'
}


def result(code, msg, description=""):

    description = default_description.get(code) if description == "" else description
    response = jsonify({
        "code": code,
        "status": status.get(code),
        "message": msg, 
        "description": description
    })

    return response, code, {'Content-Type':'application/json'}
```

於是，api 的 endpoint 可以改成這樣，變得比較精簡和直觀。

```python=
@app.route('/rest/ping', methods=["GET"])
def ping():
    return result.result(200, "ping successful", "Welcome to restful api server.")
```

需要修改 Flask 原本預設回傳錯誤網頁 (HTML)，可以用裝飾器 ```@app.errorhandler```，裝飾底下的方法，來客製化 error 結果，所以我們添加兩個方法，發生 404,405 時候，回傳 json 的格式。

[@app.errorhandler](http://flask.pocoo.org/docs/1.0/patterns/errorpages/#error-handlers)

Code:

```python=
from flask import Flask
import result

app = Flask(__name__)


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
```

![](https://i.imgur.com/JbPaEjq.png)


## Server Log

api server 要紀錄一些 log，監測 server 的運行情況，方便發生狀況時，管理者可以看 log 去找出問題，比如說連線 database 是否正常。

收集一段時間的 log，可以利用一些套件 ([ELK](https://www.elastic.co/cn/elk-stack))，統計 server 各種資訊，比如說統計 api 回復 status code 2xx 有幾次，異常 4xx, 5xx 有幾次。

最後，注意收集 log 資訊時，使用者隱私的問題。

[Web Server Logs and Internet Privacy](https://www.timeatlas.com/web-server-logs/)

### Python Logging

Python 有自帶的模組 logging，可以自訂 log 的格式，log file 輸出位置， 設定嚴重程度等，主要會運用到三個功能，```紀錄器 Logger```、```處理器 Handler ```、```格式化 Formatter ```。

- [Python 日志功能詳解](https://blog.igevin.info/posts/python-log/)

- [Basic Logging Tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)

我們先設定 log 的輸出格式和檔案名稱，寫在 ```util.py``` 模組裡面。

修改 ```result.py``` 設定 logging，INFO 層級以上會顯示出來，輸出格式使用 ```log_format```，並且 log 會儲存在 ```log_filename``` 裡面，最後，模組中開出一個方法 ```write_log``` 來使用 logging。


Code:

```python=
# util.py

# logger info
log_format = "%(asctime)s - %(levelname)s - %(message)s"
log_filename = "restful-api.log"
```

```python=
# result.py

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

def write_log(level, msg):

    if level == "info":
        logger.info(msg)
    elif level == "warning":
        logger.warning(msg)
    elif level == "critical":
        logger.critical(msg)
```

### Requests & Response

有了 log 功能之後，就可以把每次的 user requests 和 server response 的資訊記錄起來，Flask 有提供裝飾器 ```@app.before_request```、```@app.after_request```，來定義請求上下文。

- before_request: 裝飾一個方法，在每次請求之前執行。

- after_request: 裝飾一個方法，如果沒有未處理的異常拋出，在每次請求之後執行。

- [請求上下文環境](http://www.bjhee.com/flask-ad1.html)

- [Flask 的 Context 機制](https://blog.tonyseek.com/post/the-context-mechanism-of-flask/)

因此，使用者在呼叫 api 時，我們可以用裝飾器把資料紀錄成 log，更可以添加額外功能，比如說想要阻擋特定 ip 的請求。

- Requests: path, method, ip, agent
- Response: code, status, description

Code:

```python=
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
```

![](https://i.imgur.com/ZDstwZ4.png)


## Database

api server 開放了接口給外部使用，把邏輯處理和資料儲存封裝起來，讓使用者單純呼叫 api，而不用考慮這些問題，設計 api 保存資料有很多做法，簡單的使用 ```pickle``` 對物件序列化來打包資料，也可以用 Python 自帶的模組 ```sqlite3``` 使用 sql 語法儲存資料。

但是，單純利用檔案儲存，會遇到很多麻煩和效能問題，於是，為了解決這些問題和效能優化，設計出了 Database 用來儲存資料，主流分成 SQL, NoSQL 兩種類型，這次 api server 選擇 MongoDB 當作 Database。

一來，api 的 json 格式可以跟 MongoDB 的 collection(DB table) 格式很好的 match，二來，在開發 POC 時候，資料儲存格式常常會變動，前期開發很適合用 NoSQL Database。

0. [Database 儲存資料的好處](https://ithelp.ithome.com.tw/articles/10187443)

1. [NoSQL vs SQL](http://www.bmc.com/blogs/sql-vs-nosql/)

2. [MySQL 和 MongoDB 對比](https://hk.saowen.com/a/8cce49c320dfa6867849d1b895917699b8dc88c2119ffdb0526b264cda394a7e)

這邊先建立三筆資料當作範例，Database: Store, Collection: Products

![](https://i.imgur.com/7GUv75j.png)

### Python pymongo

Python 有提供模組 ```pymongo``` 來跟 MongoDB 互動，連接 MongoClient 來使用服務。

- [pymongo Tutorial](https://api.mongodb.com/python/current/tutorial.html#tutorial)

- [pymongo 中文教程](https://github.com/nummy/pymongo-tutorial-cn)

我們先匯入模組，建議有額外匯入的模組都寫在 ```requirements.txt```，方便以後部屬 server

```shell=
flask
pymongo
```

然後在 ```util.py``` 建立 MongoDB 的連接參數

```python=
# util.py

# mongoDB info
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'your_username'
MONGO_PASSWORD = 'your_password'

MONGO_DB_ACCOUNT = 'Store'
MONGO_COLLECTION_ACCOUNT = 'Products'
```

:::danger
重複提醒，MongoDB 架設起來之後，務必要打開 auth，並設定帳密 :warning: 
:::

建立 mongoDB client 要使用 [Singleton design-pattern](https://openhome.cc/Gossip/DesignPattern/SingletonPattern.htm)，不要將 client 建立在 global 變數之中，避免產生相關問題。

在之後的進階用法，使用多進程 (multiprocess) 連線 database，mongoDB client 程式使用同一個會遇到 ```UserWarning: MongoClient opened before fork.``` 。

[pymongo mongoClient can not work in multiprocess ?](https://stackoverflow.com/questions/34782789/pymongo-mongoclient-can-not-work-in-multiprocess)

另外，設定 ```serverSelectionTimeoutMS=3000```，連線時間最多三秒，超過會噴出 exception 出來，可讓我們知道這次連線 database 發生問題，預設連線不到 database 等待時間有點久 :disappointed: ，api server 會停頓太久，所以讓連線有問題就趕噴出 exception。

最後，讓 log 記錄每次連線 database 資訊，和發生連線 database 發生錯誤時，是在哪個方法發生的。

Code:

```python=
# mongoDB.py

from pymongo import MongoClient
import util
import result


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
        product = store_products().find_one(query)

        return products
    except:
        result.write_log("critical", "Failed connect to mongoDB, method: find_product")
        return None


print(products_list())
print("---")
print(find_product('1'))
```

最後三行 code 是測試用的，看是否連線正常並可以拿回資料。

![](https://i.imgur.com/WXM7xlm.png)

### (De)serialization

Serialization 和 Deserialization 即序列化和反序列化。RESTful API 會規範統一格式來傳遞數據，這邊使用 Json 格式。

在 api server 裡面，不會直接使用 Json 字串來處理資料，而會使用 Python 資料型態，如 list, dict, class 等，傳遞給使用者 Json 字串，內部處理則用 Python 資料型態，兩者時常需要變換，所以，我們使用 Serialization 和 Deserialization 做轉換。

- Serialization: Python 資料型態 -> Json 字串

- Deserialization: Json 字串 -> Python 資料型態

別人已經寫好輪子了，就不需要自己重複再造一遍，這是軟體工程很重要的原則 [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)，於是我們使用 ```marshmallow``` 模組來實現功能。

- [marshmallow 文檔](https://www.jianshu.com/p/594865f0681b)

- [Flask restful api 序列化和反序列化](https://blog.igevin.info/posts/flask-rest-serialize-deserialize/)

當系統複雜起來，可能會使用到許多 Schema，因此開一個資料夾管理這些 Schema

![](https://i.imgur.com/VVQxPbi.png)

```__init__.py``` 的作用是將文件夾變為一個 Python 模塊，不太清楚的朋友可以點底下連結學習

- [What is ```__init__.py``` for?](https://stackoverflow.com/questions/448271/what-is-init-py-for)

- [Python 的 Import 陷阱](https://medium.com/pyladies-taiwan/python-的-import-陷阱-3538e74f57e3)

Code:

```python=
# contentProduct.py

from marshmallow import Schema, fields


class ContentProduct(object):
    def __init__(self, product_id, name, introduction, price, quantity):
        self.product_id = product_id
        self.name = name
        self.introduction = introduction
        self.price = price
        self.quantity = quantity


class ProductSchema(Schema):
    product_id = fields.Str(attribute="_id")
    name = fields.Str()
    introduction = fields.Str()
    price = fields.Number()
    quantity = fields.Number()
```

我們修改 ```mongoDB.py``` 加入序列化和反序列化，額外開一個功能，新增一筆產品資料，並要處理例外狀況，key id 重複、連線失敗。

發生錯誤時，使用 Flask 的 Response class (type: tuple)，回傳定義好的錯誤訊息，這樣被其他方法呼叫時，若是類別是 ```tuple```，就可以知道發生問題了，直接傳遞訊息給使用者。

Code:

```python=
# mongoDB.py
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

def products_list():

    try:
        products = store_products().find()
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
```

最後幾行 code 是測試用的，看是否連線正常並可以插入資料。

![](https://i.imgur.com/NKFheDm.png)

![](https://i.imgur.com/kVpvPdi.png)


## RESTful API

**Resource Representational State Transfer (REST)** :hash: 

### Introduce

在微服務 (microservices) 時代的崛起，Application Programming Interface (API) 為 server to server 或 clinet to server 之間的溝通管道，可以對整體的服務解耦合、高內聚，用 API 互相請求時，不需要知道對方的實作細節，呼叫 API 介面就可以完成功能。

那 API 為什麼需要表現層狀態轉移 (REST) 來設計呢，首先，REST 不是一種架構、協定，他是一種網路架構風格，由 HTTP 協定擁有的幾種方法 (Get, Post ...)，轉換對 server 的各種操作，並用位置訊息來請求一份資源 (URL)，最後，資源實體表現出來外在形式 (Json, Xml ...)。

REST = 資源（Resources） + 表現層（Representation） + 狀態轉化（State Transfer)

API 採用 REST 風格設計，可以有以下的優點 [出自 WIKI](https://en.wikipedia.org/wiki/Representational_state_transfer) :

0. 客戶端 - 伺服器（Client-Server）

1. 無狀態（Stateless）

2. 可快取（Cachable）

3. 分層系統（Layered System）

4. 統一接口（Uniform Interface）

底下為其他人寫的 Blog 介紹 Restful API，建議進去看看加深理解。

0. [RESTful API 淺談](https://www.cnblogs.com/imyalost/p/7923230.html)

1.  [RESTful API 編寫指南](https://blog.igevin.info/posts/restful-api-get-started-to-write/)

2.  [RESTful API 設計指南](https://www.jianshu.com/p/29453a0da748)

3.  [RESTful API 最佳實踐](https://juejin.im/entry/59e460c951882542f578f2f0)


### Basic Concept

#### 回報 http status code (狀態碼)

[HTTP Status Codes 詳細介紹](https://notfalse.net/48/http-status-codes)

狀態碼	| 描述 
----- | -------
2xx	| 已接受請求正常處理並返回結果。
3xx	| 使用者代理需採取進一步行動，以完成請求。
4xx	| 客戶端，請求有錯誤。
5xx	| 服務端，內部有錯誤。

#### URL 搭配 Http method 對照表格

/ |POST（新建）| GET（拿取）|PUT（更新）|DELETE（刪除）
------- | ------- | ------- | ------- | -------
/products | 新建一個產品	| 列出所有產品 | 更新全部產品 | 刪除所有產品
/products/2	| x | 拿取2號產品資料 | 更新2號產品 | 刪除2號產品
Status Code | 201 Created | 200 OK | 200 OK | 204 No Content


#### Paging and Filtering ...

若要回傳是一串集合或是大量資料，可以提供分頁 (Paging) 和過濾 (Filtering) 等等機制，增加 API 的效率和可用性。

- Paging

    [GET] /rest/product?start=2&limit=3

- Filtering

    [GET] /rest/product?introduction=samsung phone

#### Python 技巧

這邊使用一個小技巧，用 Python 語法讓方法可傳遞不定數量的參數，```*args``` 和 ```**kwargs```，可以讓程式碼變得更加精簡和直觀。

- [*args, **kwargs 教學](https://eastlakeside.gitbooks.io/interpy-zh/content/args_kwargs/)

簡單來說，*args 對應 Python list，**kwargs 對應 Python dict。

```shell=
args = [
    "name1",
    "name2"
]

*args = ("name1, "name2")

kwargs = {
    arg1: "name1",
    arg2: "name2"
}

**kwargs = (arg1="name1", arg2="name2")
```

#### 基礎架構

REST 基本概念都理解的話，接下來，我們用簡單的三層式架構 (Three-tier architecture) 去開發 restful api server

- [3-Layer 基礎架構](https://dotblogs.com.tw/clark/2014/09/09/146494)

- [5 Benefits of a 3-Tier Architecture (底下圖片來源)](https://www.izenda.com/blog/5-benefits-3-tier-architecture/)

![](https://i.imgur.com/lwqjVgk.png)

### Data Access

負責資料存取，這邊我們使用 MongoDB，先對資料庫基本的 CRUD 操作，以及發生例外狀況 (exception) 的處理。

Code:

```python=
# mongoDB.py
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
```

### Application

把商業邏輯抽象化，並封裝程式碼實作細節，設計輸出結果，表現層只需要呼叫方法即可操做整體系統。

這邊用一個技巧，確定要輸出 API 最終結果，將其包裝成 Flask Response 物件 (type: tuple)，所以，只要被其他物件使用，只要偵測到 return 類別是 tuple，就不繼續執行接下來的過程，直接回傳 Response 即可。

最後，在裡面添加例外狀況，找不到指定資源時，回傳 ```404 Not Found```。

Code:

```python=
# product.py
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
```

### Presentation

提供使用者操作介面和呈現結果，以 restful api server 來講，就是用 URL 和 Http Method，帶著需要的 params, headers, body 資訊，請求 server 取得資源，server 執行後回傳通用的格式 (Json, Xml ...)。

裡面加入一些過濾機制，避免使用者不按規範操作，引起系統內部問題，400 - 409 都是常見的使用者錯誤，這邊使用了以下 4xx 錯誤狀態碼。

```400 Bad Request``` 
```404 Not Found```
```405 Method Not Allowed```
```406 Not Acceptable```
```409 Conflict```

```python=
# app.py
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
```


## Testing

開發系統到這邊，終於寫出一個有基本 CRUD 的 api server :satisfied:，但是，我們要確認每一個 api 或是內部方法、類別，是否都有回傳預期的結果，所以要仔細測試每一項功能。


### API test

首先，我們先針對開出的 api 功能，都能正確回報結果，我們可以之前介紹的工具 Postman，來編寫自動化測試 script。

![](https://i.imgur.com/9F9zwDE.png)

點開 Tests 之後，在旁邊有提供很多選項，點選你想要測試的項目，在修改裡面的參數。

```javascript=
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Status code name has OK", function () {
    pm.response.to.have.status("OK");
});


pm.test("Body's status is OK", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.status).to.eql("OK");
});

pm.test("Body's description correct", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.description).to.eql("The list of products data.");
});


pm.test("Message's product 1 correct", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.message[0]).to.eql(
        {
            "introduction": "htc phone",
            "name": "htc u11",
            "price": 200,
            "product_id": "1",
            "quantity": 10
        });
});
```

發出 request 的時候，Postman 除了會顯示回傳結果以外，也會根據你撰寫的測試，顯示 Tests 通過、失敗幾項以及失敗原因。

![](https://i.imgur.com/DqCtbhg.png)

如果系統有很多 api，要一個個點進去按發送測試，也太辛苦了一點 :anguished:，所以，Postman 提供一個很貼心的功能，把要測試的 API 都放在一個 Collection 裡面，並都每一個寫好 Tests。

![](https://i.imgur.com/5JBP4Cq.png)

在開啟 Collection Runner 的功能，選擇要運行的資料夾、環境變數、執行次數、每個 request 間隔毫秒數。

![](https://i.imgur.com/PyPQgGB.png)

點選 Run 後，Postman 會自動測試 Collection 裡面的每一個項目，顯示 Tests 結果，也可以產生 Json 報表。

![](https://i.imgur.com/3zAZf58.png)

- [利用 POSTMAN 中的 collection 來快速測試](https://blog.yowko.com/postman-collection-runner/)

### health check

當系統正式上線的時候，我們要知道 server 是否有正常運作，所以需要定期給 server 健康檢查 (health check) 一下 :heart:。

網路上有很多種 api monitor open source 工具，你可以挑一個你喜歡的工具，這邊我們使用 Postman 內建的功能 Monitoring。

- [10+ API Monitoring Tools](https://nordicapis.com/10-api-monitoring-tools/)

- [Intro to Postman Monitoring](https://www.getpostman.com/docs/v6/postman/monitors/intro_monitors)

點選 Collection 旁邊的小箭頭，裡面有 Monitors 的功能。

![](https://i.imgur.com/W76JkKu.png)

設定參數，多久頻率需要監測一次，確定之後點選 Create。

![](https://i.imgur.com/RPIqF2D.png)

:::warning
官方文件說，免費帳號一個月只有 1000 次的請求次數，所以不要條太高的頻率。
Each Postman user gets 1,000 monitoring calls for free per month.
:::

![](https://i.imgur.com/H63VyOW.png)

Postman 就會根據你設定頻率，定期幫你的 server 健康檢查。:smirk:

![](https://i.imgur.com/gFRyR1Y.png)

當 request 發生錯誤時候，Postman 會寄信通知你。

最後，產生每日報表 (Monitors Daily Summary)，分析 server 狀況。 :date: 

![](https://i.imgur.com/3g4d9hu.png)

### Stress test


## Deployment

### Gunicorn

### Docker


## Advanced

### Auth


## Continue ...

