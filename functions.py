from tabulate import tabulate
from const import *
import os
from datetime import datetime
from fpdf import FPDF

def get_file_content2(file_path: str) -> list:
    list_exercises = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for exercises in f.read().splitlines():
            list_exercises.append(exercises.split(','))
        return list_exercises if list_exercises else ['REST']
    
def read_exercise_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        exercise_data = []
        for line in lines[1:]:  
            exercise_info = line.strip().split(', ')
            exercise = {
                'id': int(exercise_info[0]),
                'name': exercise_info[1],
                'set': int(exercise_info[2]),
                'rep': exercise_info[3]
            }
            exercise_data.append(exercise)
    return exercise_data

all_back=get_file_content2(back_file)
all_chest=get_file_content2(chest_file)
all_biceps=get_file_content2(biceps_file)
all_calves=get_file_content2(calves_file)
all_glutes=get_file_content2(glutes_file)
all_hamstring=get_file_content2(hamstring_file)
all_quads=get_file_content2(quads_file)
all_shoulder=get_file_content2(shoulder_file)
all_triceps=get_file_content2(triceps_file)

def input_choice(data: str, menu:str) -> str:
    while True:
        display_menu(menu)
        choice = input("--> ")
        if choice not in data:
            print("Invalid")
            continue
        else:
            return choice
        
def display_menu(menu:str)->str:
    print(menu)

def display_menu_by_days(choice:str)->str:
    if choice == 'a':
        return input_choice('abc', menu_3days)
    elif choice == 'b':
         return input_choice('ab', menu_4days)
    elif choice == 'c':
         return input_choice('ab', menu_6days)

def display_exercices(exercice_type:str, file_path:str):
    print(f"Here are the {exercice_type} exercices:")
    print(tabulate(file_path, tablefmt="rounded_grid"))
    
def push(destination):
    print("push is composed of:chest shoulder triceps")
    display_exercices("chest", all_chest,)
    choose_and_append_exercises2("chest", chest_file,destination)
    display_exercices("shoulder", all_shoulder)
    choose_and_append_exercises("shoulder", shoulder_file,destination)
    display_exercices("triceps", all_triceps)
    choose_and_append_exercises("triceps", triceps_file,destination)

def pull(destination):
    print("pull is composed of:back biceps")
    display_exercices("back", all_back,)
    choose_and_append_exercises2("back", back_file,destination)
    display_exercices("biceps", all_biceps)
    choose_and_append_exercises("biceps", biceps_file,destination)


def legs_lower(destination):
    print("legs is composed of:calves quads hamstring glutes")
    display_exercices("calves", all_calves,)
    choose_and_append_exercises2("calves", calves_file,destination)
    display_exercices("glutes", all_glutes)
    choose_and_append_exercises("glutes", glutes_file,destination)
    display_exercices("quads", all_quads)
    choose_and_append_exercises("quads", quads_file,destination)
    display_exercices("hamstring", all_hamstring)
    choose_and_append_exercises("hamstring", hamstring_file,destination)
        
def upper(destination):
    print("upper is composed of:chest shoulder triceps back biceps")
    display_exercices("chest", all_chest,)
    choose_and_append_exercises2("chest", chest_file,destination)
    display_exercices("shoulder", all_shoulder)
    choose_and_append_exercises("shoulder", shoulder_file,destination)
    display_exercices("triceps", all_triceps)
    choose_and_append_exercises("triceps", triceps_file,destination)
    print("pull is composed of:back biceps")
    display_exercices("back", all_back,)
    choose_and_append_exercises("back", back_file,destination)
    display_exercices("biceps", all_biceps)
    choose_and_append_exercises("biceps", biceps_file,destination)

def full_body(destination):
    print("full body is composed of:chest shoulder triceps back biceps calves quads hamstring glutes")
    display_exercices("chest", all_chest,)
    choose_and_append_exercises2("chest", chest_file,destination)
    display_exercices("shoulder", all_shoulder)
    choose_and_append_exercises("shoulder", shoulder_file,destination)
    display_exercices("triceps", all_triceps)
    choose_and_append_exercises("triceps", triceps_file,destination)
    print("pull is composed of:back biceps")
    display_exercices("back", all_back,)
    choose_and_append_exercises("back", back_file,destination)
    display_exercices("biceps", all_biceps)
    choose_and_append_exercises("biceps", biceps_file,destination)
    display_exercices("calves", all_calves,)
    choose_and_append_exercises("calves", calves_file,destination)
    display_exercices("glutes", all_glutes)
    choose_and_append_exercises("glutes", glutes_file,destination)
    display_exercices("quads", all_quads)
    choose_and_append_exercises("quads", quads_file,destination)
    display_exercices("hamstring", all_hamstring)
    choose_and_append_exercises("hamstring", hamstring_file,destination)

def display_exercices_of_choices(choice1:str,choice2:str):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if (choice1=="a" and choice2=="a"):
        print("So you have choosed Push-Pull-Legs (Push-R-R-Pull-R-R-Leg)")
        push(lundi_file)
        pull(jeudi_file)
        legs_lower(dimanche_file)
    if (choice1=="a" and choice2=="b"):
        print("So you have choosed Upper Lower (Upper-R-R-Lower-R-R-Upper)")
        upper(lundi_file)
        legs_lower(jeudi_file)
        upper(dimanche_file)
    if (choice1=="a" and choice2=="c"):
        print("So you have choosed Full Body (FullBody-R-R-FullBody-R-R-FullBody)")
        full_body(lundi_file)
        full_body(jeudi_file)
        full_body(dimanche_file)
    if (choice1=="b" and choice2=="a"):
        print("So you have choosed Upper Lower (Upper-Lower-R-R-Upper-Lower-R)")
        upper(lundi_file)
        legs_lower(mardi_file)
        upper(vendredi_file)
        legs_lower(samedi_file)
    if (choice1=="b" and choice2=="b"):
        print("So you have choosed Upper Lower (Upper-R-Lower-R-Upper-R-Lower)")
        upper(lundi_file)
        legs_lower(mercredi_file)
        upper(vendredi_file)
        legs_lower(dimanche_file)
    if (choice1=="c" and choice2=="a"):
        print("So you have choosed Push-Pull-Legs (Push-Pull-Leg-R-Push-Pull-Leg)")
        push(lundi_file)
        pull(mardi_file)
        legs_lower(mercredi_file)
        push(vendredi_file)
        pull(samedi_file)
        legs_lower(dimanche_file)
    if (choice1=="c" and choice2=="b"):
        print("So you have choosed Push-Pull-Legs (Push-Pull-Leg-Push-Pull-Leg-R)")
        push(lundi_file)
        pull(mardi_file)
        legs_lower(mercredi_file)
        push(jeudi_file)
        pull(vendredi_file)
        legs_lower(samedi_file) 
    data_to_display={
        'lundi':get_file_content2(lundi_file),
        'mardi':get_file_content2(mardi_file),
        'mercredi':get_file_content2(mercredi_file),
        'jeudi':get_file_content2(jeudi_file),
        'vendredi':get_file_content2(vendredi_file),
        'samedi':get_file_content2(samedi_file),
        'dimanche':get_file_content2(dimanche_file)
    }
    print(tabulate(data_to_display, headers=days_of_week, tablefmt="rounded_grid"))
    generate_week_plan_pdf()

def choose_and_append_exercises(exercice_type:str,file_name:str,days):
    exercise_data = read_exercise_data(file_name)
    chosen_exercises = []
    print(f"Choose three {exercice_type} exercises by entering their IDs:")
    while len(chosen_exercises) < 3:
        user_input = input(f"Enter exercise ID {len(chosen_exercises) + 1}--> ")
        exercise_id = int(user_input) if user_input.isdigit() else None
        exercise = exercise_data[exercise_id - 1] if 1 <= exercise_id <= 6 else None
        if exercise:
            chosen_exercises.append(exercise)
            print(f"Exercise {exercise['name']} added to the list.")
        else:
            print("Invalid ID. Please enter a valid exercise ID.")
    with open(f"{days}", 'a') as file:
        for exercise in chosen_exercises:
            file.write(f"{exercise['id']}, {exercise['name']}, {exercise['set']}, {exercise['rep']}\n")

def choose_and_append_exercises2(exercice_type:str,file_name:str,days):
    exercise_data = read_exercise_data(file_name)
    chosen_exercises = []
    print(f"Choose three {exercice_type} exercises by entering their IDs:")
    while len(chosen_exercises) < 3:
        user_input = input(f"Enter exercise ID {len(chosen_exercises) + 1}--> ")
        exercise_id = int(user_input) if user_input.isdigit() else None
        exercise = exercise_data[exercise_id - 1] if 1 <= exercise_id <= 6 else None

        if exercise:
            chosen_exercises.append(exercise)
            print(f"Exercise {exercise['name']} added to the list.")
        else:
            print("Invalid ID. Please enter a valid exercise ID.")
    with open(f"{days}", 'w') as file:
        for exercise in chosen_exercises:
            file.write(f"{exercise['id']}, {exercise['name']}, {exercise['set']}, {exercise['rep']}\n")

def generate_week_plan_pdf():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_file_path = f'./Factures/week_plan_{timestamp}.pdf'
    pdf = FPDF(orientation='L', unit='mm', format='A3')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(400, 10, txt="Weekly Exercise Plan", ln=True, align='C')
    data_to_display = {
        'Monday': get_file_content2(lundi_file),
        'Tuesday': get_file_content2(mardi_file),
        'Wednesday': get_file_content2(mercredi_file),
        'Thursday': get_file_content2(jeudi_file),
        'Friday': get_file_content2(vendredi_file),
        'Saturday': get_file_content2(samedi_file),
        'Sunday': get_file_content2(dimanche_file),
    }
    min_col_width = 30
    col_widths = {day: max(len(str(exercise)) for exercise in data) + min_col_width for day, data in data_to_display.items()}
    pdf.set_fill_color(0, 0, 255)  
    pdf.set_text_color(255, 255, 255) 
    for day, col_width in col_widths.items():
        pdf.cell(col_width, 10, txt=day, border=1, fill=True)
    pdf.ln(10)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(0, 0, 0)
    for line_number in range(max(len(data) for data in data_to_display.values())):
        for day, col_width in col_widths.items():
            exercises = data_to_display[day]

            if line_number < len(exercises):
                exercises_str = ', '.join(exercises[line_number])
                pdf.cell(col_width, 10, txt=exercises_str, border=1)
            else:
                pdf.cell(col_width, 10, txt='', border=1)

        pdf.ln(10)

    pdf.output(pdf_file_path, 'F')
    print(f"PDF file generated successfully: {pdf_file_path}")