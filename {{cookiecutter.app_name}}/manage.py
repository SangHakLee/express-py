"""
Manage.py
"""
from flask_script import Manager

from .bin import createServer

manager = Manager(createServer)

@manager.command
def run():
    """
    $ python manage.py run
    """
    createServer()


if __name__ == "__main__":
    manager.run()