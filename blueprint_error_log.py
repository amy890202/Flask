from flask import Flask, render_template,redirect,abort
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import SMTPHandler

from flask.helpers import url_for

#from simple_page import simple_page
from page.personal import person

app = Flask(__name__)
app.register_blueprint(person, url_prefix='/personal')


def func():
    try:
        x = 5 / 0
        print(x)
    except:
        app.logger.error("Catch an exception in func.", exc_info=True)
        abort(500)


@app.route('/error')
def error():
    return render_template('404.html')

@app.route('/')
def hello_world():
    # app.logger.info("Info message")
    # app.logger.warning("Warning msg")
    # app.logger.error("Error msg----1")
    try:
        x = 5 / 1
        print(x)
        func()
    except:
        app.logger.error("Catch an exception.", exc_info=True)
        abort(500)
    return 'Hello, World!'
 
@app.errorhandler(404)
def page_not_found(e): 
    return render_template('404.html')
@app.errorhandler(500)
def Internal_Server_Error(e): 
    return render_template('500.html')#500 Internal Server Error



if __name__ == '__main__':
 
    # File and Console handler & formtter
    formatter = logging.Formatter(
        "[%(asctime)s][%(module)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    handler = TimedRotatingFileHandler(
        "flask.log", when="D", interval=1, backupCount=15,
        encoding="UTF-8", delay=False, utc=True)
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)
    app.run(debug=True)
    # # Email Handler
    # mail_handler = SMTPHandler(
    #     mailhost='0.0.0.0',
    #     fromaddr='...@....com',
    #     toaddrs=['....@....com'],
    #     subject='Flask Application Error'
    # )
    # mail_handler.setLevel(logging.ERROR)
    # mail_handler.setFormatter(logging.Formatter(
    #     "[%(asctime)s][%(module)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s"
    # ))
    # app.logger.addHandler(mail_handler)
 
    #app.run()
 
