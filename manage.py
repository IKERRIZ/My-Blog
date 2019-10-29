#!/usr/bin/env python
from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app.models import User,Comments,Blog,UpVote,DownVote,BlogCategory, Quote



# Creating app instance
app = create_app('development')

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    '''
    Run the unittest
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Comments = Comments, Blog = Blog, BlogCategory = BlogCategory, Quote=Quote)


if __name__ == '__main__':
    app.secret_key = 'faithikerriz'
    manager.run()
