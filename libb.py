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
app.config['GITHUB_CLIENT_ID'] = '__GITHUB_CLIENT_ID__'
app.config['GITHUB_CLIENT_SECRET'] = '__GITHUB_CLIENT_SECRET__'
app.config['SECRET_KEY'] = "__SECRET_KEY__"
