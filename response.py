import gevent
from gevent import monkey

monkey.patch_all()

from decimal import *
import requests
import hashlib
import pdb

urls = ["http://slowwly.robertomurray.co.uk/delay/3000/url/https://www.python.org/" for i in range(10)]

# function to send a get request to a url and print the number of bytes collected
def retrieve_bytes(url):
    print("Downloading from %s" % url)
    data = requests.get(url)
    encoded = data.text.encode()
    print("bytes downloaded from ", url, " = ", data.raw._fp_bytes_read)
    # use sha256 to verify data integrity between requests of same web page
    print("Hash: ", hashlib.sha256(encoded).hexdigest())
    print("retrieve_bytes task done")

def calculate_pi():
    print("calculating pi")
    i = 2
    estimate = Decimal(3)
    while i < 10000000: # sets an effective timeout on the estimate
        # attempt to query the status of the other threads, if they're all finished we want to exit calculate_pi
        status = [url_jobs[k].ready() for k in range(10)]
        if False in status: # keep iterating the pi calculation until all the url threads are complete
            if i/2 % 2 == 1:
                estimate = estimate + Decimal(4/((i) * (i + 1) * (i + 2)))
            else:
                estimate = estimate - Decimal(4/((i) * (i + 1) * (i + 2)))
            i = i + 2
        else: # if url threads are complete, print the estimate of pi
            print("estimate_pi done with value ", estimate)
            return 0
    print("timeout reached. Estimate of pi: ", estimate)
    return 0

# spawn the calculate_pi process
gevent.spawn(calculate_pi)

# spawn the set of url querying processes
url_jobs = [gevent.spawn(retrieve_bytes, url) for url in urls]
gevent.joinall(url_jobs)
