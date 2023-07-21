from wsgiref.simple_server import make_server

#env = dicc q almacena info de las peticiones del cliente (incluye peticion, headers...)
# start_response = callback que recibe 2 argumentos (statuscode y headers que envia el server al cli)
def application(env, start_response):
    headers=[('Content-Type', 'text/plain')]
    start_response('200 OK', headers)
    
    return 'Hola desde el server ligero python'.encode('utf-8')