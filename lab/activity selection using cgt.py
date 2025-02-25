start_times = [5, 1, 3, 0, 5, 8]
finish_times = [9, 2, 4, 6, 7, 9]
activities = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']

sorted_activities = sorted(activities_data, key=lambda x: x[2])

def select_activities(activities):
    n = len(activities)
    selected_activities = []

    selected_activities.append(activities[0])
    last_finish_time = activities[0][1]

    for i in range (1,n)
        if finish_times[i] > last_finish_time:
        selected_activities.append(activities[i]):
        last_finish_time = finish_times[i]
        return selected_activities
    



print("Selected activities:")