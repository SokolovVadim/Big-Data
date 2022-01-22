import json

with open('logDataset.json') as jsonfile:
    data = json.load(jsonfile)
    with open('logDataset.jsonl', 'w') as outfile:
        for entry in data:
            json.dump(entry, outfile)
            outfile.write('\n')