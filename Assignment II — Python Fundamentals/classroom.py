# Name - Sparsh Sharma, Student ID - U3315385, Date - 16.09.2025
# Smart Classroom Monitor

# -----------------------
# Initial Data
# -----------------------
# Dictionary to store room state: projector status, capacity, and current topic
room_state = {"projector_on": False, "capacity": 30, "topic": ""}
# Set to track student attendance
attendance = set()
# List to store temperature readings
temperatures = []

# -----------------------
# Functions
# -----------------------
# Toggle the projector ON/OFF
def toggle_projector(state):
    state["projector_on"] = not state["projector_on"]
    print(f"Projector is now {'ON' if state['projector_on'] else 'OFF'}.")

# Set the topic for the class
def set_topic(state):
    topic = input("Enter topic for the class: ").strip()
    state["topic"] = topic
    print(f"Topic set to: {topic}")

# Add a student to the attendance list
def add_student(attendance_set, state):
    name = input("Enter student name to add: ").strip()
    if name:
        attendance_set.add(name)
        print(f"{name} added.")
        if len(attendance_set) > state["capacity"]:
            print("ROOM FULL!")
    else:
        print("Invalid name.")

# Remove a student from the attendance list
def remove_student(attendance_set):
    name = input("Enter student name to remove: ").strip()
    if name in attendance_set:
        attendance_set.remove(name)
        print(f"{name} removed.")
    else:
        print("Student not found.")

# Add a temperature reading and check for warnings
def add_temperature(temp_list):
    try:
        temp = float(input("Enter temperature reading (°C): "))
        temp_list.append(temp)
        if temp < 16 or temp > 28:
            print("Temperature Warning!")
    except ValueError:
        print("Invalid input. Enter a number.")

# Display temperature statistics: min, max, and average
def stats(temp_list):
    if not temp_list:
        print("No temperature data.")
        return
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    avg_temp = sum(temp_list)/len(temp_list)
    print(f"Temperature Stats -> Min: {min_temp:.1f}°C, Max: {max_temp:.1f}°C, Avg: {avg_temp:.1f}°C")

# Generate a full classroom report
def report(state, attendance_set, temp_list):
    print("\n--- Classroom Report ---")
    print(f"Projector: {'ON' if state['projector_on'] else 'OFF'}")
    print(f"Topic: {state['topic'] or 'No topic set'}")
    print(f"Attendance ({len(attendance_set)}/{state['capacity']}): {', '.join(attendance_set) if attendance_set else 'None'}")
    stats(temp_list)
    print("------------------------")

# -----------------------
# Main Loop
# -----------------------
# Main interactive loop for user to manage classroom
def main():
    while True:
        print("\n--- Smart Classroom Monitor ---")
        print("1. Toggle Projector")
        print("2. Set Topic")
        print("3. Add Student")
        print("4. Remove Student")
        print("5. Add Temperature")
        print("6. View Stats")
        print("7. Report / Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            toggle_projector(room_state)
        elif choice == "2":
            set_topic(room_state)
        elif choice == "3":
            add_student(attendance, room_state)
        elif choice == "4":
            remove_student(attendance)
        elif choice == "5":
            add_temperature(temperatures)
        elif choice == "6":
            stats(temperatures)
        elif choice == "7":
            if room_state["topic"] and not room_state["projector_on"]:
                print("Reminder: Projector is OFF while a topic is set!")
            report(room_state, attendance, temperatures)
            break
        else:
            print("Invalid choice. Enter 1-7.")

# -----------------------
# Run Program
# -----------------------
if __name__ == "__main__":
    main()
