from flask import (
    render_template,
    jsonify,
    request
)
from models import Entry
from server import app


@app.route('/')
def home():
    if request.args:
        data = ''
        for key_name, value in request.args.items():
            data += f'{key_name}={value},'
        try:
            Entry(data=data)
        except Exception as e:
            return jsonify(success=False, message=e)
        return jsonify(success=True)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
