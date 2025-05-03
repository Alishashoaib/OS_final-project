class Event:
    """
    Represents an event with arrival time and burst time.
    """
    def __init__(self, event_id, arrival_time, burst_time):
        """
        Initializes an Event object.

        Args:
            event_id: The unique identifier for the event.
            arrival_time: The time the event arrives.
            burst_time: The time needed to process the event.
        """
        self.event_id = event_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


class EventScheduler:
    """
    Schedules and processes events using the First-Come, First-Served (FCFS) algorithm.
    """
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def calculate_fcfs_times(self):
        """
        Calculates completion, turnaround, and waiting times for events using FCFS.
        """
        self.events.sort(key=lambda x: x.arrival_time)

        completion_time = 0
        for event in self.events:
            if completion_time < event.arrival_time:
                completion_time = event.arrival_time
            completion_time += event.burst_time
            event.completion_time = completion_time
            event.turnaround_time = completion_time - event.arrival_time
            event.waiting_time = event.turnaround_time - event.burst_time

    def display_event_times(self):
        """
        Displays the completion, turnaround, and waiting times for each event.
        Also calculates and displays the average turnaround time and average waiting time.
        """
        print("\nEvent Processing Details (FCFS):")
        print("------------------------------------------------------------------------------------------")
        print("| Event ID  | Arrival Time | Burst Time  | Completion Time | Turnaround Time | Waiting Time |")
        print("------------------------------------------------------------------------------------------")
        total_turnaround_time = 0
        total_waiting_time = 0
        for event in self.events:
            print(f"| {event.event_id:9} | {event.arrival_time:12} | {event.burst_time:11} | "
                  f"{event.completion_time:15} | {event.turnaround_time:15} | {event.waiting_time:12} |")
            total_turnaround_time += event.turnaround_time
            total_waiting_time += event.waiting_time
        print("------------------------------------------------------------------------------------------")

        average_turnaround_time = total_turnaround_time / len(self.events) if self.events else 0
        average_waiting_time = total_waiting_time / len(self.events) if self.events else 0

        print(f"\nAverage Turnaround Time: {average_turnaround_time:.2f}")
        print(f"Average Waiting Time: {average_waiting_time:.2f}")


def main():
    """
    Main function to run the event scheduling simulation.
    """
    while True:
        num_events = int(input("Enter the number of events: "))
        if num_events <= 0:
            print("Error: Number of events must be greater than zero.")
            continue

        scheduler = EventScheduler()
        for i in range(num_events):
            event_id = input(f"Enter Event ID {i + 1}: ")
            arrival_time = int(input(f"Enter Arrival Time for {event_id}: "))
            burst_time = int(input(f"Enter Burst Time for {event_id}: "))
            event = Event(event_id, arrival_time, burst_time)
            scheduler.add_event(event)

        scheduler.calculate_fcfs_times()
        scheduler.display_event_times()

        another_run = input("Do you want to run the simulation again? (yes/no): ").lower()
        if another_run != "yes":
            break


if __name__ == "__main__":
    main()
