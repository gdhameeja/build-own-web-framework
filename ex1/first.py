def application(environ, start_response):
    req_param = environ.get('QUERY_STRING')
    if req_param:
        name = req_param.split("=")[1]
    else:
        name = 'PyCon'
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf8')]
    start_response(status, headers)
    response_string = f"<h1>Hello, {name}</h1>"
    return [bytes(response_string, encoding='utf-8')]
