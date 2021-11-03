import requests

def test_sampleget(requests_mock):
    '''
    Using the mocking library ,we can mock the url to get the desired output
    '''
    requests_mock.get('https://httpbin.org/get', json={'data':'sample'})
    assert {'data':'sample'} == requests.get('https://httpbin.org/get').json()

def test_samplefailingtest(requests_mock):
    requests_mock.get('https://httpbin.org/get', json={'data':'sample'})
    assert {'data':'s'} == requests.get('https://httpbin.org/get').json()