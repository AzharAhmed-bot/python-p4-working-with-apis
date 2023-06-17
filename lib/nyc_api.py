
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content

  def program_school(self):
    program_list=[]
    programs=json.loads(self.get_programs())
    for program in programs:
      program_list.append(program["agency"])

    return program_list


# programs = GetPrograms().get_programs()
# print(programs)
programs=GetPrograms()
programs_schools=programs.program_school()

for school in set(programs_schools):
  print(school)
