# coding: utf-8

from application import create_app

#app initialization & run
if __name__ == '__main__':
    app = create_app('config.py')
    app.run()
