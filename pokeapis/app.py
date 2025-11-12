from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.secret_key = "homero"

def obtener_pokemon_api(id_o_nombre):
    """Obtiene un Pokémon de la PokeAPI"""
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{id_o_nombre.lower()}"
        respuesta = requests.get(url, timeout=5)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return {
                'id': datos['id'],
                'name': datos['name'].capitalize(),
                'image': datos['sprites']['other']['official-artwork']['front_default'],
                'types': [t['type']['name'].capitalize() for t in datos['types']],
                'stats': {s['stat']['name'].replace('-', ' ').title(): s['base_stat'] for s in datos['stats']},
                'height': datos['height'] / 10,
                'weight': datos['weight'] / 10,
            }
        return None
    except:
        return None

def obtener_lista_pokemon():
    """Obtiene lista de primeros 151 Pokémon"""
    try:
        url = "https://pokeapi.co/api/v2/pokemon?limit=151&offset=0"
        respuesta = requests.get(url, timeout=5)
        
        if respuesta.status_code == 200:
            pokemons = []
            for p in respuesta.json()['results']:
                id_num = p['url'].split('/')[-2]
                pokemons.append({'id': id_num, 'name': p['name'].capitalize()})
            return pokemons
        return []
    except:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon_seleccionado = None
    apodo = None
    pokemons = obtener_lista_pokemon()

    if request.method == 'POST':
        id_buscado = request.form.get('pokemon_id')
        apodo = request.form.get('apodo', '')
        
        if id_buscado:
            pokemon_seleccionado = obtener_pokemon_api(id_buscado)

    return render_template('index.html', pokemons=pokemons, selected=pokemon_seleccionado, nickname=apodo)

# ...existing code...
@app.route('/lista')
def lista():
    """Página con todos los Pokémon"""
    pokemons = obtener_lista_pokemon()
    return render_template('listas.html', pokemons=pokemons)
# ...existing code...

@app.route('/pokemon/<nombre>')
def pokemon_detalle(nombre):
    """Página de detalle de un Pokémon"""
    pokemon = obtener_pokemon_api(nombre)
    if pokemon:
        return render_template('pokemon.html', pokemon=pokemon)
    return render_template('error.html', mensaje="Pokémon no encontrado"), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)