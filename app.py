from flask import (
    render_template,
    jsonify,
    request,
    redirect,
    url_for
)
from models import Entry
from server import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/entries')
def entries():
    entries = Entry.query.all()
    return render_template('entries.html', entries=entries)


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
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
