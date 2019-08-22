# another attempt, this time putting both the http requests and the calculate_pi function within the same task list
# in order to attempt to establish concurrency.
# I don't understand why the url tasks are able to run concurrently (evidenced by the retrieve_bytes tasks finishing
# in a different order to their starting order), yet they must wait for calculate_pi to finish.

import gevent
from gevent import monkey

monkey.patch_all()

from decimal import *
import requests
import pdb

def task(i):
    urls = ["http://slowwly.robertomurray.co.uk/delay/3000/url/https://www.python.org/" for i in range(10)]
    if i < 10:
        url = urls[i]
        print("Downloading from ", url, "job number", i)
        data = requests.get(url)
        print("bytes downloaded from ", url, " = ", data.raw._fp_bytes_read)
        print("retrieve_bytes task ", i, " done")
    else:
        print("calculating pi")
        j = 2
        estimate = Decimal(3)
        while [jobs[k].ready() for k in range(10)] == [False, False, False, False, False, False, False, False, False, False]:
            print([jobs[k].ready() for k in range(10)])
            if j/2 % 2 == 1:
                estimate = estimate + Decimal(4/((j) * (j + 1) * (j + 2)))
            else:
                estimate = estimate - Decimal(4/((j) * (j + 1) * (j + 2)))
            #print(estimate)
            j = j + 2
        print("estimate_pi done with value ", estimate)


jobs = [gevent.spawn(task, i) for i in range(11)]
url_jobs = jobs[0:9]
print("starting all jobs")

# wait for only the url jobs to complete (because calculating pi could go on for a long time...) - this doesn't have the desired effect.
gevent.wait(url_jobs)

print("finishing all jobs")

pdb.set_trace()
