import numpy as np

def greedy_assignment(C):
    num_people, num_jobs = C.shape
    assignment = []
    assigned_jobs =[]

    for _ in range(num_people):
        min_cost = float('inf')
        min_job = -1

        for person in range(num_people):
            if person not in assignment:
                for job in range(num_jobs):
                    if C[person][job] < min_cost:
                        min_cost = C[person][job]
                        min_job = job
                        min_person = person
        if min_job != -1:
            assignment.append(min_person)
            assigned_jobs.append(min_job)

    total_cost = sum(C[i][assigned_jobs[i]] for i in range(num_people))
    return total_cost, assigned_jobs

# Ma trận chi phí C
C = np.array([
    [4, 0, 2, 3],
    [7, 4, 3, 4],
    [3, 2, 1, 5],
    [6, 7, 8, 9]
])

min_cost, assignned_job = greedy_assignment(C)
print(f"Tổng chi phí nhỏ nhất là: {min_cost}")
print("Phân công tối ưu:")
for person, job in enumerate(assignned_job):
    print(f"Người {person + 1} -> Công việc {job + 1}")
