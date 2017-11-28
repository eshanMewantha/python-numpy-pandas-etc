from flask import Flask, jsonify, request, make_response, abort

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Comics"


@app.route('/eshan/api/v1.0/superheroes', methods=['GET'])
def get_superheroes():
    return jsonify({'superheroes': superheroes})


@app.route('/eshan/api/v1.0/superheroes/powers', methods=['GET'])
def get_powers():
    superhero_name = request.args.get('name', default='', type=str)
    if superhero_name == '':
        return jsonify({'error': 'Error : Empty parameter'})
    else:
        if superhero_name not in superheroes.keys():
            return jsonify({'error': 'Error : Superhero doesn\'t exist'})
        else:
            superhero_details = superheroes[superhero_name]
            return jsonify({'powers': superhero_details['powers']})


@app.route('/eshan/api/v1.0/superheroes/add', methods=['POST'])
def add_superhero():
    if not request.json or 'name' not in request.json:
        abort(400)

    superhero_name = request.json['name']
    details = request.json['details']

    if superhero_name not in superheroes.keys():
        superheroes[superhero_name] = details
        status = 'success'
    else:
        status = 'entry already exists'
    return jsonify({'name': superhero_name, 'details': details, 'status': status})


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


superheroes = {
    'superman': {
        'from': 'Krypton',
        'description': 'Golden standard for superheroes',
        'powers': ['super strength', 'heat vision', 'enhanced senses', 'flight', 'super speed']
    },
    'hulk': {
        'from': 'Earth',
        'description': 'Strongest avenger',
        'powers': ['super strength', 'invulnerability', 'super healing']
    }
}

if __name__ == '__main__':
    app.run(debug=True)
