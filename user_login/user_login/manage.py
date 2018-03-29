from flask_script import Manager, Server
import sys, os
sys.path.append(os.path.abspath(".."))
from user_login import app



manager = Manager(app)

manager.add_command('runserver', Server(
    use_debugger= True,
    use_reloader= True,
    host = '0.0.0.0',
    port = 5000
))

if __name__ == '__main__':
    manager.run()



