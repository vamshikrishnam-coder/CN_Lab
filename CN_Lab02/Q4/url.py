import requests
req=input('please enter the url')
try:
    request=requests.get(req)
    print(request.status_code)
    print('\n')
    print(request.headers)
    print('\n')
    print(request.history)
    print('\n')
    print(request.encoding)
    print('\n')
    print(request.reason)
    print('\n')
    print(request.cookies)
    print('\n')
    print(request.elapsed)
    print('\n')
    print(request.request)
    
except Exception as e:
    print(e)