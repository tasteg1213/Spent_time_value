import requests
import pprint
from base64 import b64encode
workspace_id = 7565605
projects_list = []
#data = requests.post('https://api.track.toggl.com/api/v9/me/reset_token', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"dorogovbd@gmail.com:Wgf4fjte").decode("ascii")})
#print(data.json())
#print(data.status_code)
#data = requests.get('https://api.track.toggl.com/api/v9/me/time_entries/current', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"dorogovbd@gmail.com:Wgf4fjte").decode("ascii")})
#print(data.status_code)
#print(data.json())

data2 = requests.post('https://api.track.toggl.com/reports/api/v3/workspace/7565605/projects/summary', json='{"end_date":"2024-01-08", "startTime":"0", "start_date":"2024-01-01"}', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"dorogovbd@gmail.com:Wgf4fjte").decode("ascii")})
#print(data2.status_code)
#pprint.pprint(data2.json())
print(f"тип данных :{type(data2.json())}")
print(data2.json())
print(data2)
str_test = "data2 = requests.post(f'https://api.track.toggl.com/reports/api/v3/workspace/7565605/projects/summary', json='{'end_date':'2024-01-08', 'startTime':'0', 'start_date':'2024-01-01'}', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b'dorogovbd@gmail.com:Wgf4fjte').decode('ascii')})"
print(str_test[83:100])
#"""
#for data_ec in data2.json():
#    projects_list.append(data_ec["project_id"])
#print(f"список проектов: {projects_list}")
#"""