# Google Distance Matrix Python Demo
# ==================================
#
# How to set up (Local part)
# --------------------------
#
# Must have Python (>= 3.4) installed with 'requests' library. On Windows, maybe try
# Anaconda Python? It has a 'conda' package manager, make sure 'requests' is installed.
#
# How to set up (Internet part)
# -----------------------------
#
# Go to https://developers.google.com and sign in using a personal (not university)
# Google account. Search for 'Distance Matrix', its API will be the only choice 
# in the list. Get an API key by creating a new project. Copy the API key to 
# the clipboard.
#
# How to run the program
# ----------------------
#
# > python3 distances.py <KEY>
#
# Debug tips
# ----------
#
# Ask Python not to quit after having run the script, so all variables can be
# inspected interactively. The script will also load pprint function for your
# convenience.
#
# > python3 -i distances.py <KEY>
# 

import json
import requests
import sys

if __name__ == '__main__':
  
  # The API key must be provided on the command line, abort otherwise. 
  api_key = 'insert api key here'
  # if len(sys.argv) != 2:
  # 	print('Usage: distances.py <GOOGLE DISTANCE MATRIX API KEY>')
  # 	exit(1)
  # else:
  # 	api_key = sys.argv[1]

  # Google Distance Matrix base URL to which all other parameters are attached
  base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

  # Google Distance Matrix domain-specific terms: origins and destinations
  origins = [
    # 'Vancouver, BC', 'Seattle',
    '7000 65th St Sacramento, CA 95823'
    ]
  destinations = [
    # 'San Francisco', 'Victoria, BC'
    '7000 65th St Sacramento, CA 95823'
    ]

  # Prepare the request details for the assembly into a request URL
  payload = {
    'origins' : '|'.join(origins),
    'destinations' : '|'.join(destinations), 
    'mode' : 'driving',
    'units': 'imperial',
    # 'traffic_model': 'optimistic',
    # 'arrival_time': '8:00am',
    'api_key' : api_key
  }

  # Assemble the URL and query the web service
  r = requests.get(base_url, params = payload)

  # Check the HTTP status code returned by the server. Only process the response, 
  # if the status code is 200 (OK in HTTP terms).
  if r.status_code != 200:
    print('HTTP status code {} received, program terminated.'.format(r.status_code))
    print(json.dumps(r.json()))
  else:
    try:
      # Try/catch block should capture the problems when loading JSON data, 
      # such as when JSON is broken. It won't, however, help much if JSON format
      # for this service has changed -- in that case, the dictionaries json.loads() produces
      # may not have some of the fields queried later. In a production system, some sort
      # of verification of JSON file structure is required before processing it. In XML
      # this role is performed by XML Schema.
      x = json.loads(r.text)

      # Now you can do as you please with the data structure stored in x.
      # Here, we print it as a Cartesian product.
      # for isrc, src in enumerate(x['origin_addresses']):
      #   for idst, dst in enumerate(x['destination_addresses']):
      #     row = x['rows'][isrc]
      #     cell = row['elements'][idst]
      #     if cell['status'] == 'OK':
      #       print('{} to {}: {}, {}.'.format(src, dst, cell['distance']['text'], cell['duration']['text']))
      #     else:
      #       print('{} to {}: status = {}'.format(src, dst, cell['status']))

      # Of course, we could have also saved the results in a file,
      with open('gdmpydemo.json', 'w') as f:
        f.write(r.text)

      # TODO Or in a database,

      # Or whatever.
      # ???
      # Profit!

    except ValueError:
      print('Error while parsing JSON response, program terminated.')

  # Prepare for debugging, but only if interactive. Now you can pprint(x), for example.
  if sys.flags.interactive:
    from pprint import pprint
