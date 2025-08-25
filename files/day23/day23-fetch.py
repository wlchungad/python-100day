import threading
import os
import inspect
import concurrent.futures

import requests
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

# for testing purpose, we will use logging as output 
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='./logs/fetch.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8',
                    level=logging.DEBUG)

def worker(html_element):
    logging.info("Worker thread running")
    place = html_element.find('div', class_='name').get_text()
    value = html_element.find('h5').get_text()
    with open("./output.txt", "a", encoding='utf-8') as file:
        file.writelines(f"{place}\t\t{value}\n")

if __name__ == "__main__": 
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    
    #
    url = 'https://water.taiwanstat.com/'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    reservoir = soup.select('.reservoir')
    for i in reservoir:
        pool.submit(worker, (i))
    pool.shutdown(wait=True)


    logging.info("Main thread continuing to run")
    logging.info('---' * 10)