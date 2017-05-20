from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import glob
import os


all_files = []
with open ("jsondata.json", 'w') as g:
  g.write("[\n")

for root,dirs,files in os.walk("/home/michael/Downloads/lastfm_subset"):
  files = glob.glob(os.path.join(root,'*.json'))
  for f in files:
    all_files.append(f)
for f in all_files:
  dic = {}
  with open(f, 'r') as json_file:
    j = json.load(json_file, parse_float = decimal.Decimal)
    clean_tags = []
    for [tag,weight] in j["tags"]:
      clean_tags.append([str(tag.encode('utf-8')).lower().strip(),str(weight).lower().strip()])
    dic['tags'] = clean_tags
    clean_similars = []
    for [a,weight] in j["similars"]:
      clean_similars.append([str(a).lower().strip(), weight])
    dic['similars'] = clean_similars

    dic['title'] = str(j['title'].encode('utf-8')).lower().strip()
    dic['track_id'] = str(j['track_id']).lower().strip()
    dic['artist'] = str(j['artist'].encode('utf-8')).lower().strip()
  with open("jsondata.json", 'a') as g:
    g.write(str(dic))
    g.write(",\n")
with open("jsondata.json",'a') as g:
  g.write("]")
