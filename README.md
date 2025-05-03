This Python code implements a simulation of event scheduling using the First-Come, First-Served (FCFS) algorithm. Let's break down each part of the code:

1. The Event Class:

Python

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
This class defines the structure of an "event." Think of an event as a task or a process that needs to be scheduled.
__init__(self, event_id, arrival_time, burst_time): This is the constructor of the Event class. When you create a new Event object, you need to provide:
event_id: A unique identifier for this specific event (e.g., "P1", "Task A", "Event 3").
arrival_time: The time at which this event arrives in the system.
burst_time: The amount of time required to process this event to completion.
The constructor also initializes three other attributes to 0:
completion_time: The time at which the event finishes its execution.
turnaround_time: The total time an event spends in the system (from arrival to completion). It's calculated as completion_time - arrival_time.
waiting_time: The time an event spends waiting in the ready queue before it starts its execution. It's calculated as turnaround_time - burst_time.
2. The EventScheduler Class:

Python

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
        print("| Event ID \t| Arrival Time | Burst Time \t| Completion Time | Turnaround Time | Waiting Time |")
        print("------------------------------------------------------------------------------------------")
        total_turnaround_time = 0
        total_waiting_time = 0
        for event in self.events:
            print(f"| {event.event_id:9} \t| {event.arrival_time:12} | {event.burst_time:11} \t| "
                  f"{event.completion_time:15} | {event.turnaround_time:15} | {event.waiting_time:12} |")
            total_turnaround_time += event.turnaround_time
            total_waiting_time += event.waiting_time
        print("------------------------------------------------------------------------------------------")

        average_turnaround_time = total_turnaround_time / len(self.events) if self.events else 0
        average_waiting_time = total_waiting_time / len(self.events) if self.events else 0

        print(f"\nAverage Turnaround Time: {average_turnaround_time:.2f}")
        print(f"Average Waiting Time: {average_waiting_time:.2f}")
This class is responsible for managing and scheduling the Event objects using the FCFS algorithm.
__init__(self): The constructor initializes an empty list called self.events. This list will store the Event objects that need to be processed.
add_event(self, event): This method takes an Event object as input and adds it to the self.events list.
calculate_fcfs_times(self): This is the core of the FCFS scheduling logic:
self.events.sort(key=lambda x: x.arrival_time): The first step in FCFS is to process events based on their arrival time. This line sorts the self.events list in ascending order of their arrival_time.
completion_time = 0: A variable completion_time is initialized to 0. This will keep track of the time when the currently executing event finishes.
The code then iterates through the sorted list of events:
if completion_time < event.arrival_time:: If the current completion_time is earlier than the arrival_time of the next event, it means the CPU was idle. In this case, the completion_time is updated to the arrival_time of the current event, as the event has to wait until it arrives to start.
completion_time += event.burst_time: The completion_time is updated by adding the burst_time of the current event. This represents the time when the current event finishes executing.
event.completion_time = completion_time: The calculated completion_time is stored in the completion_time attribute of the current Event object.
event.turnaround_time = completion_time - event.arrival_time: The turnaround_time for the current event is calculated.
event.waiting_time = event.turnaround_time - event.burst_time: The waiting_time for the current event is calculated.
display_event_times(self): This method neatly prints a table showing the details of each processed event:
It displays the Event ID, Arrival Time, Burst Time, Completion Time, Turnaround Time, and Waiting Time for each event in the self.events list.
It also calculates and prints the average turnaround time and average waiting time for all the processed events.
3. The main() Function:

Python

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
This function serves as the entry point of the program and handles the user interaction.
while True:: This creates a loop that allows the user to run the simulation multiple times.
num_events = int(input("Enter the number of events: ")): It prompts the user to enter the number of events they want to simulate.
Input Validation: It checks if the entered number of events is greater than zero. If not, it displays an error message and continues to the next iteration of the loop.
scheduler = EventScheduler(): An instance of the EventScheduler class is created.
Event Input Loop: It iterates num_events times to get the details (ID, arrival time, burst time) for each event from the user. For each event, it creates an Event object and adds it to the scheduler using the add_event() method.
scheduler.calculate_fcfs_times(): It calls the calculate_fcfs_times() method of the scheduler object to compute the completion, turnaround, and waiting times for all the added events based on the FCFS algorithm.
scheduler.display_event_times(): It calls the display_event_times() method to display the calculated times in a formatted table and show the average turnaround and waiting times.
Run Again Prompt: It asks the user if they want to run the simulation again. If the user enters anything other than "yes" (case-insensitive), the loop breaks, and the program ends.
4. if __name__ == "__main__"::

Python

if __name__ == "__main__":
    main()
This is a standard Python construct. It ensures that the main() function is called only when the script is executed directly (not when it's imported as a module into another script).
In Summary:

This code provides a clear and functional implementation of the First-Come, First-Served (FCFS) event scheduling algorithm. It allows users to input event details (arrival time and burst time), simulates the FCFS scheduling process, and then displays important performance metrics like completion time, turnaround time, waiting time, and their averages. This makes it a valuable tool for understanding and demonstrating the FCFS scheduling concept.
