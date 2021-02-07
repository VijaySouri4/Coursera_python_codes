def get_event_date(event):
    return event.date()

def current_user(events):
    event.sort(key=get_event_date)
    machines = {}

    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()

        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == 'logout':
            machines[event.machine].remove(event.user)

        return machines

def generate_report(machines):
    for key, values in machines.items():
        if len(users) > 0:
            uesr_list = ", ".join(values)
            print("{}: {}".format(key, uesr_list))

if __name__ == '__main__'