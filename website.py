from bottle import route, run

@route('/tom.com')
def hello():
    return "Hello World! bottle chicken nugget banana"

run(host= 'localhost', port=8080, reloader=True)

