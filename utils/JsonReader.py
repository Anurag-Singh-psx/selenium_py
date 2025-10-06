import json


class JsonReader:

    def read_json(self,file):
        with open(file) as json_file:
            data = json.load(json_file)
            return data