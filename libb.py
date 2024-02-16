try: 
  from flask import *
  import requests
  import random
  import json
  from time import time
  from random import random
  from flask_dance.contrib.github import make_github_blueprint, github
  from file_html import *
  from flask_login import logout_user
except Exception as e:
    print("Mancano alcuni moduli {}".format(e))
    
app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = '71a6e1bbc25d5250abee'
app.config['GITHUB_CLIENT_SECRET'] = '5a45b659b0ff82bd3fb205dac4e3a32a0385d18e'
app.config['SECRET_KEY'] = "chiave"
