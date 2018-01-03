import multiprocessing

from flask import Flask, jsonify, request, make_response, abort

app = Flask(__name__)


def long_running_task(thread_name):
    for i in range(100000000):
        if i % 100000 == 0:
            print('Processing request ' + str(thread_name))


@app.route('/eshan/api/v1.0/superheroes/add', methods=['POST'])
def add_superhero():
    if not request.json or 'id' not in request.json:
        abort(400)

    id = request.json['id']
    thread = multiprocessing.Process(target=long_running_task, args=(id,))
    thread.start()
    print('returning before the process ends. Process will continue in background')
    return jsonify({'status': 'running'})


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
