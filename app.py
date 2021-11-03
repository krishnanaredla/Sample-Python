import requests
from typing import Dict,List

def sampleget(url:str)->List[Dict]:
    '''
    Sample documentation explaining about the code 
    In function definition , its not required to mention 
    the input and return data types
    '''
    try:
        r = requests.get(url,verify=False)
        print(r.status_code)
        return r.json()
    except Exception as e:
        raise RuntimeError(e)

if __name__ == "__main__":
    '''
    Good to have __name__ ==  "__main__",
    which is kind of starting point of execution.
    These comments are called doc strings ,
    which can be used to generate documentation
    '''
    getResponse = sampleget('https://httpbin.org/get')
    print(getResponse)