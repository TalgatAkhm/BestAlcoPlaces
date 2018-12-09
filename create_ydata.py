#!/usr/bin/python3
import sys
import json

if len(sys.argv) < 5:
    print("Error input: datasets count input file, output file, weight")
    exit()

count = int(sys.argv[1])
out_name = sys.argv[-1]
output = {}
output['type'] = 'FeatureCollection'
output['features'] = []

for j in range(count):
    in_name = sys.argv[2+j*2]
    weight = sys.argv[3+j*2]
    features = []

    with open(in_name) as f:
        data = json.loads(f.read())
        for i, x in enumerate(data):
            obj = {}
            obj['id'] = 'id' + str(i + 1)
            obj['type'] = 'Feature'
            obj['geometry'] = {'type':'Point', 'coordinates':[x['lat'], x['lon']]}
            obj['properties'] = {'weight':weight}
            features.append(obj)
    output['features'] += features
json_data = json.dumps(output)
with open(out_name, "w") as f:
    f.write(json_data)
