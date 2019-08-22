I have made two attempts at the homework exercise.
In each case, I have been able to estimate the value of pi using the Nilakantha series, and used gevent and requests to run parallel url requests.
The integrity of the data from the HTTP requests is verified by SHA256.

However, I have not been able to get the pi calculation to run in parallel with the url requests; the url requests only complete after the pi calculation is completed, so I have had to set a manual timeout to the pi calculation to prevent an infinite loop.

I'm looking forward to discussing my attempts with you and learning how to improve the control flow of the program, so that the pi calculation can be terminated by the successful completion of the 10 parallel get requests.

Best,

Jeremy
