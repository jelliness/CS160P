from flask import Flask

app = Flask(__name__ ,template_folder='views')

# Import controllers
from app.controllers import access_controller, main_controller
