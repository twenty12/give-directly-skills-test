from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import app, db
from api.commands.seed_database import SeedDB


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('seed_db', SeedDB())

if __name__ == '__main__':
    manager.run()
