import sys
import requirements
import requests

INDENT = 40

if len(sys.argv) > 1:
  file = sys.argv[1] 
else:
  file = 'requirements.txt'

lines = open(file, 'r') 
reqs = requirements.parse(lines)
for req in reqs:
  
  # bail early if req is a URL
  if req.uri:
    print(req.line)
    continue
  
  # get summary from PyPi
  res = requests.get(f'https://pypi.org/pypi/{req.name}/json')
  json = res.json()
  summary = json['info']['summary']
  
  # e.g. requirements-parser==0.2.0
  name_with_version_range = f'{req.name}{req.specs[0][0]}{req.specs[0][1]}'

  # figure out how much to indent the summary
  indent_remainder = max(3, INDENT - len(name_with_version_range))
  spaces = " " * indent_remainder

  # print line with summary comment
  print(f"{name_with_version_range}{spaces} # {summary}")