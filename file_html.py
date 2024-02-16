#INIZIO HTML ROTTA PAGINA APERTURA
html_page_inizio = '''
<!DOCTYPE html>
<html>
<head>
	<title>Sign In</title>
	<style>
		body {
			display: flex;
			flex-direction: column;
			align-items: center;
			height: 100vh;
			margin: 0;
			background-color: #f0f0f0;
			font-family: Arial, sans-serif;
		}
		h1 {
			margin-top: 0;
			margin-bottom: 1rem;
		}
		.github-button {
			display: flex;
			align-items: center;
			justify-content: center;
			background-color: #333;
			color: #fff;
			border: none;
			border-radius: 4px;
			padding: 0.5rem 1rem;
			text-decoration: none;
			font-size: 1rem;
			margin-top: 1rem;
			cursor: pointer;
		}
		.github-button:hover {
			background-color: #444;
		}
		.github-logo {
			height: 2rem;
			margin-right: 0.5rem;
		}
	</style>
</head>
<body>
	<h1>Accedi con:</h1>
	<a href="/login" class="github-button">
		<img src="https://w7.pngwing.com/pngs/914/758/png-transparent-github-social-media-computer-icons-logo-android-github-logo-computer-wallpaper-banner-thumbnail.png" class="github-logo">
		GitHub
	</a>
</body>
</html>
'''
#FINE HTML ROTTA PAGINA APERTURA

#INIZIO HTML ROTTA HOMEPAGE
home_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
    <style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            flex-direction: column;
            font-family: 'Open Sans', sans-serif;
            text-align: center;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        h2 {
            font-size: 1.5rem;
            margin-top: 0;
            margin-bottom: 1rem;
        }
        p {
            font-size: 1.2rem;
            margin-top: 0;
            margin-bottom: 2rem;
        }
        form {
            margin-bottom: 2rem;
        }
        button {
            padding: 0.7rem 2rem;
            background-color: #ffc229;
            color: #fff;
            border: none;
            border-radius: 1rem;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.2s;
        }
        button:hover {
            background-color: #e8b821;
        }
        hr {
            width: 50%;
            margin: 2rem auto;
            border: none;
            height: 2px;
            background-color: #ccc;
        }
        a {
            display: inline-block;
            padding: 0.5rem 1rem;
            background-color: #ffc229;
            color: #fff;
            border: none;
            border-radius: 1rem;
            font-size: 1.2rem;
            text-decoration: none;
            transition: all 0.2s;
        }
        a:hover {
            background-color: #e8b821;
        }
    </style>
</head>
<body>
    <h1>Homepage</h1>
    <p>Benvenuto {{ github_name }}</p>
    <h2>Fare clic sui pulsanti sottostanti per navigare in pagine specifiche:</h2>
    <form action="/List_of_forces" method="get">
        <button type="submit">Elenco delle forze dell'ordine</button>
    </form>
    <hr>
    <h3>Ricerca per citt&agrave:</h3>
    <form action="/Senior_officers" method="get">
        <button type="submit">Ufficiali di alto grado</button>
    </form>
    <form action="/force_data" method="get">
        <button type="submit">Contatti polizia cittadina</button>
    </form>
    <form action="/quartiere_forze" method="get">
        <button type="submit">Zone di competenza</button>
    </form>
    <hr>
    <p><strong>Ultimo aggiornamento:</strong> {{ last_updated }}</p>
    {% if page_content %}
        <div>
            {{ page_content }}
        </div>
    {% endif %}
    <a href="/logout">Logout</a>
</body>
</html>
   '''
#FINE HTML ROTTA HOMEPAGE

#INIZIO HTML ROTTA FORZE DI POLIZIA
table_html = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Elenco delle forze dell'ordine</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
  <div class="container mt-5">
    <h1>Elenco delle forze dell'ordine</h1>
    <p>Un elenco di tutte le forze di polizia disponibili, ad eccezione della British Transport Police, che è esclusa dall'elenco restituito.</p>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Nome dell' Arma</th>
        </tr>
      </thead>
      <tbody>
        {% for force in forces %}
          <tr>
            <td>{{ force['id'] }}</td>
            <td>{{ force['name'] }}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
    <form action="/github/callback" method="get" >
        <button type="submit">Homepage</button>
    </form>
  </body>
</html>
"""
#FINE HTML ROTTA FORZE DI POLIZIA

#INIZIO HTML ROTTA ELENCO UFFICIALI SUPERIORI
Senior_officers_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ufficiali di alto grado</title>
    <style>
<style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
    </style>        
                </head>
<body>
    <h1>Inserire il nome della città per ottenere le informazioni degli Ufficiali di alto grado:</h1>
    <form method="post">
        <label for="city">Citt&agrave:</label>
        <select id="city" name="city" required>
        <option value>
        <option value="avon-and-somerset">Avon and Somerset Constabulary</option>
        <option value="bedfordshire">Bedfordshire Police</option>
        <option value="cambridgeshire">Cambridgeshire Constabulary</option>
        <option value="cheshire">Cheshire Constabulary</option>
        <option value="city-of-london">City of London Police</option>
        <option value="cleveland">Cleveland Police</option>
        <option value="cumbria">Cumbria Constabulary</option>
        <option value="derbyshire">Derbyshire Constabulary</option>
        <option value="devon-and-cornwall">Devon & Cornwall Police</option>
        <option value="dorset">Dorset Police</option>
        <option value="durham">Durham Constabulary</option>
        <option value="dyfed-powys">Dyfed-Powys Police</option>
        <option value="essex">Essex Police</option>
        <option value="gloucestershire">Gloucestershire Constabulary</option>
        <option value="greater-manchester">Greater Manchester Police</option>
        <option value="gwent">Gwent Police</option>
        <option value="hampshire">Hampshire Constabulary</option>
        <option value="hertfordshire">Hertfordshire Constabulary</option>
        <option value="humberside">Humberside Police</option>
        <option value="kent">Kent Police</option>
        <option value="lancashire">Lancashire Constabulary</option>
        <option value="leicestershire">Leicestershire Police</option>
        <option value="lincolnshire">Lincolnshire Police</option>
        <option value="merseyside">Merseyside Police</option>
        <option value="metropolitan">Metropolitan Police Service</option>
        <option value="norfolk">Norfolk Constabulary</option>
        <option value="north-wales">North Wales Police</option>
        <option value="north-yorkshire">North Yorkshire Police</option>
        <option value="northamptonshire">Northamptonshire Police</option>
        <option value="northumbria">Northumbria Police</option>
        <option value="nottinghamshire">Nottinghamshire Police</option>
        <option value="northern-ireland">Police Service of Northern Ireland</option>
        <option value="south-wales">South Wales Police</option>
        <option value="south-yorkshire">South Yorkshire Police</option>
        <option value="staffordshire">Staffordshire Police</option>
        <option value="suffolk">Suffolk Constabulary</option>
        <option value="surrey">Surrey Police</option>
        <option value="sussex">Sussex Police</option>
        <option value="thames-valley">Thames Valley Police</option>
        <option value="warwickshire">Warwickshire Police</option>
        <option value="west-mercia">West Mercia Police</option>
        <option value="west-midlands">West Midlands Police</option>
        <option value="west-yorkshire">West Yorkshire Police</option>
        <option value="wiltshire">Wiltshire Police</option>
    </select>
        <input type="submit" value="Ricerca">
    </form>
        <form action="/github/callback" method="get" >
        <button type="submit">Homepage</button>
    </form>

</body>
</html>
"""

people_data_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ufficiali di alto grado presenti  a {{ city }} </title>
</head>
<body>
    <h1>Ufficiali di alto grado presenti  a {{ city }} </h1>
    <table border="1">
        <tr>
            <th>Nome</th>
            <th>Grado</th>
            <th>Bio</th>
        </tr>
        {% for person in people_data %}
            <tr>
                <td>{{ person['name'] }}</td>
                <td>{{ person['rank'] }}</td>
                <td>{{ person['bio'] }}</td>
            </tr>
        {% endfor %}
    </table>
    <form action="/Senior_officers" method="get" >
        <button type="submit">Indietro</button>
    </form>
    </body>
</html>
"""
#FINE HTML ROTTA ELENCO UFFICIALI SUPERIORI

#INIZIO HTML ROTTA CONTATTI POLIZIA
force_data_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dati sulla forza dell'ordine</title>
</head>
<body>
        <h1>Inserire il nome della città per ottenere i contatti delle forza dell'ordine in una citt&agrave:</h1>
    <form action="/force_data" method="post">
        <label for="city">Citt&agrave:</label>
        <select id="city" name="city" required>
        <option value>
        <option value="avon-and-somerset">Avon and Somerset Constabulary</option>
        <option value="bedfordshire">Bedfordshire Police</option>
        <option value="cambridgeshire">Cambridgeshire Constabulary</option>
        <option value="cheshire">Cheshire Constabulary</option>
        <option value="city-of-london">City of London Police</option>
        <option value="cleveland">Cleveland Police</option>
        <option value="cumbria">Cumbria Constabulary</option>
        <option value="derbyshire">Derbyshire Constabulary</option>
        <option value="devon-and-cornwall">Devon & Cornwall Police</option>
        <option value="dorset">Dorset Police</option>
        <option value="durham">Durham Constabulary</option>
        <option value="dyfed-powys">Dyfed-Powys Police</option>
        <option value="essex">Essex Police</option>
        <option value="gloucestershire">Gloucestershire Constabulary</option>
        <option value="greater-manchester">Greater Manchester Police</option>
        <option value="gwent">Gwent Police</option>
        <option value="hampshire">Hampshire Constabulary</option>
        <option value="hertfordshire">Hertfordshire Constabulary</option>
        <option value="humberside">Humberside Police</option>
        <option value="kent">Kent Police</option>
        <option value="lancashire">Lancashire Constabulary</option>
        <option value="leicestershire">Leicestershire Police</option>
        <option value="lincolnshire">Lincolnshire Police</option>
        <option value="merseyside">Merseyside Police</option>
        <option value="metropolitan">Metropolitan Police Service</option>
        <option value="norfolk">Norfolk Constabulary</option>
        <option value="north-wales">North Wales Police</option>
        <option value="north-yorkshire">North Yorkshire Police</option>
        <option value="northamptonshire">Northamptonshire Police</option>
        <option value="northumbria">Northumbria Police</option>
        <option value="nottinghamshire">Nottinghamshire Police</option>
        <option value="northern-ireland">Police Service of Northern Ireland</option>
        <option value="south-wales">South Wales Police</option>
        <option value="south-yorkshire">South Yorkshire Police</option>
        <option value="staffordshire">Staffordshire Police</option>
        <option value="suffolk">Suffolk Constabulary</option>
        <option value="surrey">Surrey Police</option>
        <option value="sussex">Sussex Police</option>
        <option value="thames-valley">Thames Valley Police</option>
        <option value="warwickshire">Warwickshire Police</option>
        <option value="west-mercia">West Mercia Police</option>
        <option value="west-midlands">West Midlands Police</option>
        <option value="west-yorkshire">West Yorkshire Police</option>
        <option value="wiltshire">Wiltshire Police</option>
    </select>
        <button type="submit">Ricerca</button>
    </form>

    {% if force_data %}
        <h2>Informazioni sulla forza per la citt&agrave {{ city }}</h2>
        <p><strong>Descrizione:</strong> {{ force_data.get('description', 'N/A') }}</p>
        <p><strong>Sito Web:</strong> <a href="{{ force_data.get('url', '#') }}" target="_blank">{{ force_data.get('url', 'N/A') }}</a></p>
        <p><strong>Telefono:</strong> {{ force_data.get('telephone', 'N/A') }}</p>

        <h3>Link utili:</h3>
        <ul>
            {% for method in force_data.get('engagement_methods', []) %}
                <li>
                    <strong>{{ method.get('title', 'N/A') }}:</strong> {{ method.get('description', 'N/A') }} - <a href="{{ method.get('url', '#') }}" target="_blank">{{ method.get('url', 'N/A') }}</a>
                </li>
            {% endfor %}
        </ul>
    {% endif %}
    <form action="/github/callback" method="get" >
        <button type="submit">Homepage</button>
    </form>
    </body>
</html>
'''
#FINE HTML ROTTA CONTATTI POLIZIA

# INIZIO HTML ROTTA ELENCO DELLE ZONE DI COMPETENZA DI UNA FORZA
quartiere_forze_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elenco delle zone di competenza di una forza dell'ordine</title>
    <style>
<style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
    </style>
        
                </head>
<body>
    <h1>Elenco delle zone di competenza di una forza dell'ordine:</h1>
    <form method="post">
        <label for="city">Citt&agrave:</label>
        <select id="city" name="city" required>
        <option value>
        <option value="avon-and-somerset">Avon and Somerset Constabulary</option>
        <option value="bedfordshire">Bedfordshire Police</option>
        <option value="cambridgeshire">Cambridgeshire Constabulary</option>
        <option value="cheshire">Cheshire Constabulary</option>
        <option value="city-of-london">City of London Police</option>
        <option value="cleveland">Cleveland Police</option>
        <option value="cumbria">Cumbria Constabulary</option>
        <option value="derbyshire">Derbyshire Constabulary</option>
        <option value="devon-and-cornwall">Devon & Cornwall Police</option>
        <option value="dorset">Dorset Police</option>
        <option value="durham">Durham Constabulary</option>
        <option value="dyfed-powys">Dyfed-Powys Police</option>
        <option value="essex">Essex Police</option>
        <option value="gloucestershire">Gloucestershire Constabulary</option>
        <option value="greater-manchester">Greater Manchester Police</option>
        <option value="gwent">Gwent Police</option>
        <option value="hampshire">Hampshire Constabulary</option>
        <option value="hertfordshire">Hertfordshire Constabulary</option>
        <option value="humberside">Humberside Police</option>
        <option value="kent">Kent Police</option>
        <option value="lancashire">Lancashire Constabulary</option>
        <option value="leicestershire">Leicestershire Police</option>
        <option value="lincolnshire">Lincolnshire Police</option>
        <option value="merseyside">Merseyside Police</option>
        <option value="metropolitan">Metropolitan Police Service</option>
        <option value="norfolk">Norfolk Constabulary</option>
        <option value="north-wales">North Wales Police</option>
        <option value="north-yorkshire">North Yorkshire Police</option>
        <option value="northamptonshire">Northamptonshire Police</option>
        <option value="northumbria">Northumbria Police</option>
        <option value="nottinghamshire">Nottinghamshire Police</option>
        <option value="northern-ireland">Police Service of Northern Ireland</option>
        <option value="south-wales">South Wales Police</option>
        <option value="south-yorkshire">South Yorkshire Police</option>
        <option value="staffordshire">Staffordshire Police</option>
        <option value="suffolk">Suffolk Constabulary</option>
        <option value="surrey">Surrey Police</option>
        <option value="sussex">Sussex Police</option>
        <option value="thames-valley">Thames Valley Police</option>
        <option value="warwickshire">Warwickshire Police</option>
        <option value="west-mercia">West Mercia Police</option>
        <option value="west-midlands">West Midlands Police</option>
        <option value="west-yorkshire">West Yorkshire Police</option>
        <option value="wiltshire">Wiltshire Police</option>
    </select>
        <input type="submit" value="Ricerca">
    </form>
                <form action="/github/callback" method="get" >
        <button type="submit">Homepage</button>
    </form>
</body>
</html>
"""

quartiere_forze_LISTA_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elenco dei quartieri per una forza del’ordine  nella citt&agrave di {{ city }} </title>
    <style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;
        

            text-align: center;
            flex-direction: column;
        }
        table {
            width: 80%;
            border-collapse: collapse;
            margin: 0 auto;
        }
        th, td {
            padding: 10px;
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <h1>Elenco dei quartieri per una forza del’ordine  nella citt&agrave di {{ city }} </h1>
    <table border="1" >
        <tr>
            <th>ID</th>
            <th>Quartiere</th>
        </tr>
        {% for person in quartiere_forze_LISTA %}
            <tr>
                <td>{{ person['id'] }}</td>
                <td>{{ person['name'] }}</td>
            </tr>
        {% endfor %}
    </table>
        <form action="/quartiere_forze">
        <button type="submit">Indietro</button>
    </form>

</body>
</html>
"""
# FINE HTML ROTTA ELENCO DELLE ZONE DI COMPETENZA DI UNA FORZA
