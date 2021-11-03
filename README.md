# Sample python code 

### Creating virtual environment

creating a virtual environment , can help separating dependencies 
of the project from the system level depencies

Virtual Env :
        
``` bash
PS C:\work\samplepython> python -m venv sampleenv

# This creates a sampleenv folder under the current directory,
# we can also specify specific target location for env too

PS C:\work\samplepython> .\sampleenv\Scripts\activate

# Above will activate the venv, we can see below 
# (sampleenv) at the starting of the cmd

(sampleenv) PS C:\work\samplepython> 

(sampleenv) PS C:\work\samplepython> pip install  requests

# to skip firewall issues
(sampleenv) PS C:\work\samplepython> pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org requests

# we can use pip freeze to see existing libraries in our virtual env

(sampleenv) PS C:\work\samplepython> pip freeze
certifi==2021.10.8
charset-normalizer==2.0.7
idna==3.3
requests==2.26.0
requests-mock==1.9.3
six==1.16.0
urllib3==1.26.7

```
