import concurrent.futures

import requests as requests


class DataProcessingWithMT:

    @staticmethod
    def setup():
        urls = ["https://jsonplaceholder.typicode.com/todos/1",
                "https://jsonplaceholder.typicode.com/todos/2",
                "https://jsonplaceholder.typicode.com/todos/3",
                "https://jsonplaceholder.typicode.com/todos/4" ]
        return urls

    @staticmethod
    def process(url):
        response = requests.get(url)
        return response.json()


if __name__ == "__main__":
    dp = DataProcessingWithMT()
    data = dp.setup()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        results = pool.map(dp.process, data)
    print(list(results))

