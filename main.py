import heapq

def parallel_processing(n, m, data):
    output = []
    start_time = [0] * m
    thread_queue = [(0, i) for i in range(n)]

    for job_index, job_time in enumerate(data):
        thread_completion_time, thread_index = heapq.heappop(thread_queue)
        output.append((thread_index, start_time[thread_index]))
        start_time[thread_index] += job_time
        heapq.heappush(thread_queue, (thread_completion_time + job_time, thread_index))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
