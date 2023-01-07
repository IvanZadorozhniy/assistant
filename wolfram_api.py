import wolframalpha
from dotenv.main import load_dotenv
import os
class WolframApi():
    def __init__(self):
        self.client = wolframalpha.Client(os.environ.get("WOLFRAM_API_KEY"))
    
    def get_answer_for_query(self, query=""):
        return self.client.query('random fact')


if __name__ == "__main__":
    wolfram = WolframApi()
    res = wolfram.get_answer_for_query()
    for pod in res.pods:
        for sub in pod.subpods:
            print(sub.plaintext)