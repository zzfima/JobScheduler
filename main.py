import threading
import time

import schedule


def job1():
    print("I'm JOB1")


def job2():
    print("I'm JOB2")


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(10).seconds.do(run_threaded, job1).tag('job1')
schedule.every(3).seconds.do(run_threaded, job2).tag('job2')
cnt = 0

while True:
    schedule.run_pending()
    time.sleep(1)
    cnt += 1
    if cnt == 15:
        print('Cancel JOB1')
        schedule.clear('job1')
    if cnt == 20:
        print('Cancel JOB2')
        schedule.clear('job2')
