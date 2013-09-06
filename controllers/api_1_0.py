# -*- coding: utf-8 -*-

'''
# Private Function
'''
def __test():
    return "gsagsa"
    
@request.restful()
def index():
    response.view = 'generic.json'
    def GET(*args, **vars):
        return "GET SERVICE"
    def POST(*args, **vars):
        return "POST SERVICE"
    def PUT(*args, **vars):
        return "PUT SERVICE"
    def DELETE(*args, **vars):
        return "DELETE SERVICE"
    return locals()