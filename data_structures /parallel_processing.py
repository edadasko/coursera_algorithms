'''
Parallel processing
Task. You have a program which is parallelized and uses n independent threads
      to process the given list of m jobs. Threads take jobs in the order they
      are given in the input. If there is a free thread, it immediately takes the
      next job from the list. If a thread has started processing a job, it doesn’t
      interrupt or stop until it finishes processing the job. If several threads
      try to take jobs from the list simultaneously, the thread with smaller index
      takes the job. For each job you know exactly how long will it take any thread
      to process this job, and this time is the same for all the threads. You need to
      determine for each job which thread will process it and when will it start processing.
Input Format. The first line of the input contains integers n and m. The second line contains
              m integers ti — the times in seconds it takes any thread to process i-th job.
              The times are given in the same order as they are in the list from which
              threads take jobs. Threads are indexed starting from 0.
Output Format. Output exactly m lines. i-th line (0-based index is used) should contain
               two space - separated integers — the 0-based index of the thread which
               will process the i-th job and the time in seconds when it will start
               processing that job.
'''

from collections import namedtuple
import math


thread = namedtuple('thread', 'num seconds')


class ThreadsHeap:
    def __init__(self, num):
        self.num_of_threads = num
        self.heap = [thread(i, 0) for i in range(num)]
        self.assigned_jobs = []
    
    def set_free_thread_on_the_job(self, time):
        self.assigned_jobs.append([self.heap[0].num, self.heap[0].seconds])
        self.change_head_priority(time)
    
    def change_head_priority(self, time):
        self.heap[0] = thread(self.heap[0].num, self.heap[0].seconds + time)
        self.sift_thread_down(0)
    
    def sift_thread_down(self, index):
        left_index, right_index = index * 2 + 1, index * 2 + 2
        left_thread = self.heap[left_index] if left_index < self.num_of_threads \
            else thread(left_index, math.inf)
        right_thread = self.heap[right_index] if right_index < self.num_of_threads \
            else thread(right_index, math.inf)
        if left_thread.seconds == math.inf and right_thread.seconds == math.inf:
            return
        current_thread = self.heap[index]
        min_thread = self.get_min_thread(left_thread, right_thread)
        if current_thread.seconds < min_thread.seconds or \
            (current_thread.seconds == min_thread.seconds
             and current_thread.num < min_thread.num):
            return
        min_thread_index = left_index if min_thread == left_thread else right_index
        self.swap_threads(index, min_thread_index)
        self.sift_thread_down(min_thread_index)

    def swap_threads(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def get_min_thread(self, a, b):
        if a.seconds == b.seconds:
            return a if a.num < b.num else b
        return a if a.seconds < b.seconds else b

    def get_report(self):
        return self.assigned_jobs


class JobQueue:
    def __init__(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.queue = []
        assert m == len(self.jobs)
    
    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.queue[i][0], self.queue[i][1])

    def assign_jobs(self):
        heap = ThreadsHeap(self.num_workers)
        for job in self.jobs:
            heap.set_free_thread_on_the_job(job)
        self.queue = heap.get_report()
    
    def solve(self):
        self.assign_jobs()
        self.write_response()


job_queue = JobQueue()
job_queue.solve()
