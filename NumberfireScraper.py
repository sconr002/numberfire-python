import httplib2
import json
import os.path
import re
import time

def get_nf_data():
  url = 'http://www.numberfire.com/nba/fantasy/fantasy-basketball-projections'

  try:
    h = httplib2.Http(".cache")
    (resp, content) = h.request(url, "GET")
    m = re.search(r"NF_DATA\s*=\s*(\{.*?\}\}\})\;", content)
    nf_data = json.loads(m.group(1))

    if nf_data:
      # make directory if not exists
      nf_dir = os.path.join(os.path.dirname(__file__), 'nf_data')
      if not os.path.exists(nf_dir):
        os.makedirs(nf_dir)

      # want to save the json data if not already saved
      fn = os.path.join(nf_dir, 'nf_data_' + time.strftime('%Y%m%d') + '.json')

      if not os.path.isfile(fn):
        with open(fn, 'w') as outfile:
          json.dump(nf_data, outfile, sort_keys=True, indent=4)

    return nf_data

  except:
    pass

def get_nf_players(nf_data):

  return nf_data['players']

if __name__ == "__main__":
  nf_data = get_nf_data()
  #pprint.pprint(nf_data)