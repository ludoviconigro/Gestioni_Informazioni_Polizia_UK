from libb import *

#INIZIO  ROTTA PAGINA APERTURA
@app.route('/')
def index():
    session.clear()
    return html_page_inizio
#FINE ROTTA PAGINA APERTURA

# INIZIO ROTTA LOGOUT
@app.route('/logout')
def logout():
        # Rimuovi le informazioni di sessione
        session.clear()

        # Redirect alla homepage o ad un'altra pagina dopo il logout
        return html_page_inizio
# FINE ROTTA LOGOUT
    
#INIZIO  ROTTA LOGIN
@app.route('/login')
def login():
    # Genera l'URL di callback per reindirizzare l'utente dopo l'autorizzazione da parte di GitHub
    callback_url = url_for('authorized', _external=True)
     # Definisce lo scope delle autorizzazioni richieste per l'autenticazione dell'utente
    scope = 'user:email'
    # Reindirizza l'utente a GitHub per l'autenticazione OAuth
    return redirect(f'https://github.com/login/oauth/authorize?client_id={app.config["GITHUB_CLIENT_ID"]}&redirect_uri={callback_url}&scope={scope}')
#FINE  ROTTA LOGIN

#INIZIO ROTTA HOMEPAGE
@app.route('/github/callback')
def authorized():
    # Ottieni il codice di autorizzazione dalla richiesta
    code = request.args.get('code')
    # URL per richiedere il token di accesso da GitHub
    token_url = 'https://github.com/login/oauth/access_token'   
    # Payload per la richiesta del token di accesso
    token_payload = {
        'client_id': app.config['GITHUB_CLIENT_ID'],
        'client_secret': app.config['GITHUB_CLIENT_SECRET'],
        'code': code    }
    # Effettua una richiesta POST per ottenere il token di accesso da GitHub
    token_response = requests.post(token_url, data=token_payload)
    # Analizza la risposta per ottenere il token di accesso
    token_data = dict(x.split('=') for x in token_response.text.split('&'))
    # Verifica se l'accesso è stato autorizzato correttamente
    try:
        access_token = token_data['access_token']
    except KeyError:
        # Se l'accesso non è stato autorizzato, reindirizza all'endpoint di login
        return redirect(url_for('login'))  
    # URL per ottenere le informazioni sull'utente da GitHub
    user_url = 'https://api.github.com/user/emails'
    # Headers per l'autenticazione con il token di accesso
    headers = {
        'Authorization': f'token {access_token}'    }
    # Ottieni le informazioni sull'utente da GitHub
    user_response = requests.get(user_url, headers=headers)
    user_data = user_response.json()
    # Salva l'indirizzo email dell'utente in una sessione
    session['email'] = user_data[0]['email']
    # Ottieni la data dell'ultimo aggiornamento dei dati sulla criminalità
    crime_last_updated_response = requests.get('https://data.police.uk/api/crime-last-updated')
    last_updated = 'N/A'
    if crime_last_updated_response.status_code == 200:
        last_updated = crime_last_updated_response.json()['date']
    # Passa i dati alla homepage come variabili da visualizzare
    return render_template_string(home_html, page_content=None, github_name=session['email'], last_updated=last_updated)
#FINE ROTTA HOMEPAGE

# INIZIO ROTTA FORZE DI POLIZIA
def fetch_police_forces():
    # URL dell'API per ottenere le informazioni sulle forze di polizia
    url = 'https://data.police.uk/api/forces'
    # Effettua una richiesta GET all'API
    response = requests.get(url)
    # Converte la risposta in formato JSON
    data = response.json()
    # Restituisce i dati ottenuti
    return data

@app.route('/List_of_forces')
def police_forces_table():
    # Verifica se l'utente è autenticato tramite sessione
    if 'email' not in session:
        # Se l'utente non è autenticato, reindirizzalo alla pagina di login
        return redirect(url_for('login'))    
    else:
        # Ottieni le informazioni sulle forze di polizia
        forces = fetch_police_forces()        
        # Passa le informazioni recuperate al template della tabella HTML per essere visualizzate
        return render_template_string(table_html, forces=forces)
#FINE ROTTA FORZE DI POLIZIA


#INIZIO ROTTA ELENCO UFFICIALI SUPERIORI
def get_people_data(city):
    try:
        # Costruisce l'URL dell'API per ottenere i dati delle persone per una determinata città
        api_url = f"https://data.police.uk/api/forces/{city}/people"
        # Esegue una richiesta GET all'API
        response = requests.get(api_url)
        # Verifica lo stato della risposta
        if response.status_code == 200:
            # Converte la risposta in formato JSON
            data = response.json()
            # Restituisce i dati ottenuti
            return data
        else:
            # Se la risposta non è 200, la richiesta non è andata a buon fine
            return None
    except Exception as e:
        # Se si verifica un'eccezione durante la richiesta, gestisci l'errore
        print(f"Errore durante la richiesta API: {e}")
        return None

@app.route('/Senior_officers', methods=['GET', 'POST'])
def Senior_officers():
    # Verifica se l'utente è autenticato tramite sessione
    if 'email' not in session:
        # Se l'utente non è autenticato, reindirizzalo alla pagina di login
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            # Se la richiesta è una POST, ottiene il nome della città dalla form
            city = request.form['city']
            # Ottiene i dati delle persone per la città specificata
            people_data = get_people_data(city)
            if people_data is not None:
                # Reindirizza alla pagina 'people_data' con il nome della città come parametro
                return redirect(url_for('people_data', city=city))
            else:
                # Se non ci sono dati disponibili per la città, reindirizza alla pagina 'Senior_officers'
                # con un messaggio di errore
                return render_template_string(Senior_officers_html, error_message="Città non valida o nessun dato disponibile.")
        # Se la richiesta è una GET, restituisce la pagina HTML per inserire il nome della città
        return Senior_officers_html

@app.route('/people_data/<city>')
def people_data(city):
    # Ottiene i dati delle persone per la città specificata
    people_data = get_people_data(city)
    # Verifica se sono stati ottenuti dati validi
    if people_data is not None:
        # Passa i dati delle persone e il nome della città al template HTML per essere visualizzati
        return render_template_string(people_data_html, city=city, people_data=people_data)
    else:
        # Se non ci sono dati disponibili per la città, reindirizza alla pagina 'Senior_officers'
        # con un messaggio di errore
        return render_template_string(Senior_officers_html, error_message="Città non valida o nessun dato disponibile.")
#FINE ROTTA ELENCO UFFICIALI SUPERIORI


#INIZIO ROTTA CONTATTI POLIZIA
@app.route('/force_data', methods=['GET', 'POST'])
def force_data():
    # Verifica se l'utente è autenticato tramite sessione
    if 'email' not in session:
        # Se l'utente non è autenticato, reindirizzalo alla pagina di login
        return redirect(url_for('login'))    
    else:
        # Inizializza le variabili
        force_data = None
        city = None
        # Se la richiesta è una POST
        if request.method == 'POST':
            # Ottieni il nome della città dalla form
            city = request.form.get('city')
            # Ottieni i dati relativi alle forze di polizia per la città specificata
            force_data = get_force_data(city)
        # Rendi il template HTML passando i dati e il nome della città
        return render_template_string(force_data_html, city=city, force_data=force_data)
    
# Funzione per ottenere i dati relativi alle forze di polizia
def get_force_data(city):
    # Costruisci l'URL dell'API per ottenere i dati relativi alle forze di polizia per una determinata città
    api_url = f"https://data.police.uk/api/forces/{city}"
    # Effettua una richiesta GET all'API
    response = requests.get(api_url)    
    # Verifica se la richiesta è andata a buon fine (status code 200)
    if response.status_code == 200:
        # Converte la risposta in formato JSON
        force_data = response.json()
        return force_data
    else:
        return None
        # FINE ROTTA CONTATTI POLIZIA

# INIZIO ROTTA ELENCO DELLE ZONE DI COMPETENZA DI UNA FORZA
def get_quartiere_forze(city):
    try:
        # Costruisce l'URL dell'API per ottenere i dati sui quartieri per una determinata città
        api_url = f"https://data.police.uk/api/{city}/neighbourhoods"
        # Esegue una richiesta GET all'API
        response = requests.get(api_url)
        # Verifica lo stato della risposta
        if response.status_code == 200:
            # Converte la risposta in formato JSON
            data = response.json()
            # Restituisce i dati ottenuti
            return data
        else:
            # Se la risposta non è 200, la richiesta non è andata a buon fine
            return None
    except Exception as e:
        # Se si verifica un'eccezione durante la richiesta, gestisci l'errore
        print(f"Errore durante la richiesta API: {e}")
        return None

@app.route('/quartiere_forze', methods=['GET', 'POST'])
def quartiere_forze():
    # Verifica se l'utente è autenticato tramite sessione
    if 'email' not in session:
        # Se l'utente non è autenticato, reindirizzalo alla pagina di login
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            # Se la richiesta è una POST, ottiene il nome della città dalla form
            city = request.form['city']
            # Ottiene i dati sui quartieri per la città specificata
            quartiere_forze_LISTA = get_quartiere_forze(city)
            if quartiere_forze_LISTA is not None:
                # Reindirizza alla pagina 'quartiere_forze_LISTA' con il nome della città come parametro
                return redirect(url_for('quartiere_forze_LISTA', city=city))
            else:
                # Se non ci sono dati disponibili per la città, reindirizza alla pagina 'quartiere_forze'
                # con un messaggio di errore
                return render_template_string(quartiere_forze_html, error_message="Città non valida o nessun dato disponibile.")
        # Se la richiesta è una GET, restituisce la pagina HTML per inserire il nome della città
        return quartiere_forze_html

@app.route('/quartiere_forze_LISTA/<city>')
def quartiere_forze_LISTA(city):
    # Ottiene i dati sui quartieri per la città specificata
    quartiere_forze_LISTA = get_quartiere_forze(city)
    # Verifica se sono stati ottenuti dati validi
    if quartiere_forze_LISTA is not None:
        # Passa i dati dei quartieri e il nome della città al template HTML per essere visualizzati
        return render_template_string(quartiere_forze_LISTA_html, city=city, quartiere_forze_LISTA=quartiere_forze_LISTA)
    else:
        # Se non ci sono dati disponibili per la città, reindirizza alla pagina 'quartiere_forze'
        # con un messaggio di errore
        return render_template_string(quartiere_forze_html, error_message="Città non valida o nessun dato disponibile.")
# FINE ROTTA ELENCO DELLE ZONE DI COMPETENZA DI UNA FORZA

if __name__ == '__main__':
    app.run(debug=True)