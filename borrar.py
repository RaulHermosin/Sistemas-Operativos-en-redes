
import requests
import json

dominio = "google.com"

url = f"https://www.virustotal.com/api/v3/domains/{dominio}/comments"

payload = {}
headers = {
  'x-apikey': '3b5bc08c2ae2da7e8289d6535a63487c1f8f0f198ce67458813ca968fdfb0f82'
}

response = requests.request("GET", url, headers=headers, data=payload)
response = json.loads(response.text)

print("Insert into table dominios: ", dominio, " hay ", response['meta']['count'])