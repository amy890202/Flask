#pip install flask_script==2.0.6 --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
from flask_script import Manager
from flask import Flask
from __init__ import app


# 設定你的 app
manager = Manager(app)

# 自訂command
@manager.command
def hello():
    """Print hello"""
    print("hello")

if __name__ == "__main__":
    manager.run()
