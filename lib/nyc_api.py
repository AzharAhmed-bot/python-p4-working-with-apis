
import requests
import json

class GetPrograms:
  def __init__(self,url) -> None:
    self.url=url

  def get_response_body(self):
    response = requests.get(self.url)
    return response.content

  def load_json(self):
    program_list=[]
    programs=json.loads(self.get_response_body())
    for program in programs:
      program_list.append(program["agency"])

    return program_list


# programs = GetPrograms().get_programs()
# print(programs)
programs=GetPrograms("http://data.cityofnewyork.us/resource/uvks-tn5n.json")
programs_schools=programs.load_json()

for school in set(programs_schools):
  print(school)
