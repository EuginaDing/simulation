import sys
print(sys.version)
print(sys.executable)
print(sys.path)
import requests
import datetime as dt
#sys.path.append(r'c:\VISSIM\py_ptv')
r=requests.get('https://www.google.com')
print(r.status_code)

git config --global user.email "eugina.ding@gmail.com"
git config --global user.name "Eugina Ding"

git remote add origin git@github.com:EuginaDing/simulation.git
git branch -M main
git push -u origin main