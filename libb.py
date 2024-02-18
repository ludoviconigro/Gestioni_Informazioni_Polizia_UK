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
app.config['GITHUB_CLIENT_ID'] = '3a9b3f9a8286b8ca5bea'
app.config['GITHUB_CLIENT_SECRET'] = '1afb3f072f82a40767da6cbf7664c060523d6a84'
app.config['SECRET_KEY'] = "chiave"
