from flask import (
    render_template,
    jsonify,
    request
)
from models import Entry
from server import app


@app.route('/')
def home():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)


@app.route('/u')
def data():
    if request.args:
        data = ''
        for key_name, value in request.args.items():
            data += f'{key_name}={value},'
        if 'mcu' not in data:
            return jsonify(success=False, message='Missing important param.')
        try:
            Entry(data=data)
        except Exception as e:
            return jsonify(success=False, message=e)
        return jsonify(success=True)
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
