import requests 
import json
class md5_decrypt():
    def __init__(self, cmd):
        # super(md5_decrypt, self).__init__()
        self.cmd = cmd 

    def run(self):
        print(self.cmd)
        response = requests.get(self.cmd)
        result = json.loads(response.content)
        print(result["result"])
        

