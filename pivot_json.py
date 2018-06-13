import json
import sys
from pprint import pprint

distance = []

with open('gdmpydemo.json') as f:
  data = json.load(f)
  for row in data["rows"]:
    # pprint(row["elements"])
    for element in row["elements"]:
      # pprint(element["duration"]["text"])
      distance.append(element["duration"]["text"])

print(distance)
