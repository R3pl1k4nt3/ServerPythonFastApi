from wsgiref.simple_server import make_server

#env = dicc q almacena info de las peticiones del cliente (incluye peticion, headers...)
# start_response = callback que recibe 2 argumentos (statuscode y headers que envia el server al cli)

#creo constante html donde alojo web
HTML ="""
<!DOCTYPE html>
<html>
    <head>
        <title>SERVIDOR EN PYTHON</title>
    </head>
    <body>
        <h1>Hola desde el server ligero python</h1>
    </body>
</html>
        
"""

def application(env, start_response):
    headers=[('Content-Type', 'text/html')]
    start_response('200 OK', headers)
    # devuelvo bytes con codificacion utf-8 y la web alojada en constante html
    return [bytes(HTML,'utf-8')]

# creamos el servidor
#make_server recibe obligaotiriamente 3 argumentos
## 1. la direccion donde se va a ejecutar nuestro server
## 2. El puerto donde escucha el server
## 3. La funcion que se encarga de responder a las peticiones

server = make_server('localhost',8000,application)
# ahora ejecutamos el metodo
server.serve_forever()