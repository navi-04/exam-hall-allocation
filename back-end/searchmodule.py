import tkinter as tk

# Data for all 12 halls
hall_1 = [
    ["927623bcs001", "927623bee001", "927623ece001", "927623bcs002", "927623bee002"],
    ["927623ece002", "927623bcs004", "927623bee003", "927623ece003", "927623bcs005"],
    ["927623bee004", "927623ece004", "927623bcs006", "927623bee005", "927623ece005"],
    ["927623bcs007", "927623bee006", "927623ece006", "927623bcs008", "927623bee007"],
    ["927623ece007", "927623bcs009", "927623bee008", "927623ece008", "927623bcs010"]
]
hall_2 = [
    ["927623bcs011", "927623bee011", "927623ece011", "927623bcs012", "927623bee012"],
    ["927623ece012", "927623bcs014", "927623bee013", "927623ece013", "927623bcs015"],
    ["927623bee014", "927623ece014", "927623bcs016", "927623bee015", "927623ece015"],
    ["927623bcs017", "927623bee016", "927623ece016", "927623bcs018", "927623bee017"],
    ["927623ece017", "927623bcs019", "927623bee018", "927623ece018", "927623bcs020"]
]
hall_3 = [
    ["927623bcs021", "927623bee021", "927623ece021", "927623bcs022", "927623bee022"],
    ["927623ece022", "927623bcs024", "927623bee023", "927623ece023", "927623bcs025"],
    ["927623bee024", "927623ece024", "927623bcs026", "927623bee025", "927623ece025"],
    ["927623bcs027", "927623bee026", "927623ece026", "927623bcs028", "927623bee027"],
    ["927623ece027", "927623bcs029", "927623bee028", "927623ece028", "927623bcs030"]
]
hall_4 = [
    ["927623bcs031", "927623bee031", "927623ece031", "927623bcs032", "927623bee032"],
    ["927623ece032", "927623bcs034", "927623bee033", "927623ece033", "927623bcs035"],
    ["927623bee034", "927623ece034", "927623bcs036", "927623bee035", "927623ece035"],
    ["927623bcs037", "927623bee036", "927623ece036", "927623bcs038", "927623bee037"],
    ["927623ece037", "927623bcs039", "927623bee038", "927623ece038", "927623bcs040"]
]
hall_5 = [
    ["927623bcs041", "927623bee041", "927623ece041", "927623bcs042", "927623bee042"],
    ["927623ece042", "927623bcs044", "927623bee043", "927623ece043", "927623bcs045"],
    ["927623bee044", "927623ece044", "927623bcs046", "927623bee045", "927623ece045"],
    ["927623bcs047", "927623bee046", "927623ece046", "927623bcs048", "927623bee047"],
    ["927623ece047", "927623bcs049", "927623bee048", "927623ece048", "927623bcs050"]
]
hall_6 = [
    ["927623bcs051", "927623bee051", "927623ece051", "927623bcs052", "927623bee052"],
    ["927623ece052", "927623bcs054", "927623bee053", "927623ece053", "927623bcs055"],
    ["927623bee054", "927623ece054", "927623bcs056", "927623bee055", "927623ece055"],
    ["927623bcs057", "927623bee056", "927623ece056", "927623bcs058", "927623bee057"],
    ["927623ece057", "927623bcs059", "927623bee058", "927623ece058", "927623bcs060"]
]
hall_7 = [
    ["927623bcs061", "927623bee061", "927623ece061", "927623bcs062", "927623bee062"],
    ["927623ece062", "927623bcs064", "927623bee063", "927623ece063", "927623bcs065"],
    ["927623bee064", "927623ece064", "927623bcs066", "927623bee065", "927623ece065"],
    ["927623bcs067", "927623bee066", "927623ece066", "927623bcs068", "927623bee067"],
    ["927623ece067", "927623bcs069", "927623bee068", "927623ece068", "927623bcs070"]
]
hall_8 = [
    ["927623bcs071", "927623bee071", "927623ece071", "927623bcs072", "927623bee072"],
    ["927623ece072", "927623bcs074", "927623bee073", "927623ece073", "927623bcs075"],
    ["927623bee074", "927623ece074", "927623bcs076", "927623bee075", "927623ece075"],
    ["927623bcs077", "927623bee076", "927623ece076", "927623bcs078", "927623bee077"],
    ["927623ece077", "927623bcs079", "927623bee078", "927623ece078", "927623bcs080"]
]
hall_9 = [
    ["927623bcs081", "927623bee081", "927623ece081", "927623bcs082", "927623bee082"],
    ["927623ece082", "927623bcs084", "927623bee083", "927623ece083", "927623bcs085"],
    ["927623bee084", "927623ece084", "927623bcs086", "927623bee085", "927623ece085"],
    ["927623bcs087", "927623bee086", "927623ece086", "927623bcs088", "927623bee087"],
    ["927623ece087", "927623bcs089", "927623bee088", "927623ece088", "927623bcs090"]
]
hall_10 = [
    ["927623bcs091", "927623bee091", "927623ece091", "927623bcs092", "927623bee092"],
    ["927623ece092", "927623bcs094", "927623bee093", "927623ece093", "927623bcs095"],
    ["927623bee094", "927623ece094", "927623bcs096", "927623bee095", "927623ece095"],
    ["927623bcs097", "927623bee096", "927623ece096", "927623bcs098", "927623bee097"],
    ["927623ece097", "927623bcs099", "927623bee098", "927623ece098", "927623bcs100"]
]
hall_11 = [
    ["927623bcs101", "927623bee101", "927623ece101", "927623bcs102", "927623bee102"],
    ["927623ece102", "927623bcs104", "927623bee103", "927623ece103", "927623bcs105"],
    ["927623bee104", "927623ece104", "927623bcs106", "927623bee105", "927623ece105"],
    ["927623bcs107", "927623bee106", "927623ece106", "927623bcs108", "927623bee107"],
    ["927623ece107", "927623bcs109", "927623bee108", "927623ece108", "927623bcs110"]
]
hall_12 = [
    ["927623bcs111", "927623bee111", "927623ece111", "927623bcs112", "927623bee112"],
    ["927623ece112", "927623bcs114", "927623bee113", "927623ece113", "927623bcs115"],
    ["927623bee114", "927623ece114", "927623bcs116", "927623bee115", "927623ece115"],
    ["927623bcs117", "927623bee116", "927623ece116", "927623bcs118", "927623bee117"],
    ["927623ece117", "927623bcs119", "927623bee118", "927623ece118", "927623bcs120"]
]
import tkinter as tk

# Data for all 12 halls (same as your original data)
# [Keep the hall data here...]

# List of all halls
halls = [hall_1, hall_2, hall_3, hall_4, hall_5, hall_6, hall_7, hall_8, hall_9, hall_10, hall_11, hall_12]

# Function to search the roll number
def search_roll_number():
    roll_number = entry.get()
    found = False
    # Clear previous canvas content
    canvas.delete("all")
    
    # Iterate over the halls and check for the roll number
    for hall_index, hall in enumerate(halls):
        for row_index, row in enumerate(hall):
            if roll_number in row:
                found = True
                hall_num = hall_index + 1
                row_num = row_index + 1
                seat_num = row.index(roll_number) + 1
                
                # Draw visual representation
                draw_hall_layout(hall_num, row_num, seat_num, roll_number)
                break
        if found:
            break
    if not found:
        result_label.config(text="Roll number not found!")
        canvas.create_text(200, 200, text="Roll number not found!", font=("Arial", 14), fill="red")

# Function to draw hall layout
def draw_hall_layout(hall_num, row_num, seat_num, roll_number):
    hall_width = 300
    hall_height = 200
    seat_size = 30

    # Create the outer boundary for the hall
    canvas.create_rectangle(50, 50, 50 + hall_width, 50 + hall_height, outline="black", width=2)
    
    # Draw the rows
    for row in range(1, 6):  # There are 5 rows in each hall
        for seat in range(1, 6):  # There are 5 seats in each row
            x1 = 50 + (seat - 1) * seat_size
            y1 = 50 + (row - 1) * seat_size
            x2 = x1 + seat_size
            y2 = y1 + seat_size
            canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=1)
            canvas.create_text(x1 + seat_size / 2, y1 + seat_size / 2, text=f"{row}-{seat}", font=("Arial", 8))

    # Highlight the seat where the roll number was found
    x1 = 50 + (seat_num - 1) * seat_size
    y1 = 50 + (row_num - 1) * seat_size
    x2 = x1 + seat_size
    y2 = y1 + seat_size
    canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=2)
    canvas.create_text(x1 + seat_size / 2, y1 + seat_size / 2, text=f"Roll: {roll_number}", font=("Arial", 10, "bold"), fill="red")

    # Display hall number, row, and seat
    result_label.config(text=f"Roll number found in Hall {hall_num}, Row {row_num}, Seat {seat_num}")
    
    # Display the person allocated to the hall
    allocated_label.config(text=f"Person Allocated: Roll Number {roll_number} - Hall {hall_num}")

# Creating the main window
root = tk.Tk()
root.title("Roll Number Search with Visual Representation")

# Create a label for instructions
label = tk.Label(root, text="Enter Roll Number:")
label.pack(pady=10)

# Create an entry widget to input the roll number
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a search button
search_button = tk.Button(root, text="Search", command=search_roll_number)
search_button.pack(pady=10)

# Create a label to display the search result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Create a Canvas widget for drawing the hall layout
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(pady=20)

# Create a label to display the allocated person and hall below the canvas
allocated_label = tk.Label(root, text="", font=("Arial", 12))
allocated_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
