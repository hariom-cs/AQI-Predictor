import os
import time
import requests
import sys

def retrieve_html():
    for year in range(2019, 2025):
        for month in range(1, 13):
            if month < 10:
                url = f"http://en.tutiempo.net/climate/0{month}-{year}/ws-421820.html"
            else:
                url = f"http://en.tutiempo.net/climate/{month}-{year}/ws-421820.html"

            response = requests.get(url)

            # Check if request was successful
            if response.status_code != 200:
                print(f"Failed to retrieve: {url} (Status Code: {response.status_code})")
                continue

            text_utf = response.text.encode('utf-8')

            # Ensure directory exists
            os.makedirs(f"Data/Html_Data/{year}", exist_ok=True)

            with open(f"Data/Html_Data/{year}/{month}.html", "wb") as output:
                output.write(text_utf)

        sys.stdout.flush()

if __name__ == "__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print("Time taken: {:.2f} seconds".format(stop_time - start_time))
