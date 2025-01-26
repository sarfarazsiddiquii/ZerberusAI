'''
Task 2: Design a Scheduler
'''

def schedule_tasks(tasks, dependencies):
    task_graph = {}
    for task in tasks:
        task_graph[task] = []
    
    in_degree = {}
    for task in tasks:
        in_degree[task] = 0

    for pre, after in dependencies:
        task_graph[pre].append(after)
        in_degree[after] += 1

    queue = []
    for task in tasks:
        if in_degree[task] == 0:
            queue.append(task)
    order = []

    while queue:
        current = queue.pop(0)
        order.append(current)

        for i in task_graph[current]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

    if len(order) == len(tasks):
        return order
    else:
        return("Can't do this course in any possible order")
    
