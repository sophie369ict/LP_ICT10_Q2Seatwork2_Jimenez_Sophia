from pyscript import document, display

def grade_average(e):
    # List of subjects
    subjects = ["Math", "English", "Science", "Social Studies", "P.E.", "Foreign Languages"]

    # Tuple of corresponding units
    units = (3, 3, 4, 2, 1, 2)

    # Clear previous outputs before displaying new results
    document.getElementById("show_name").innerHTML = ""
    document.getElementById("show_grade").innerHTML = ""
    document.getElementById("show_ave").innerHTML = ""

    # Get student info
    first_name = document.getElementById("fname").value
    last_name = document.getElementById("lname").value

    grades = []
    for i in range(1, 7):
        value = document.getElementById(f"grd{i}").value
        if value.strip() == "": 
            display("⚠️ Please fill in all fields before computing.", target="show_ave")
            return 
        grades.append(float(value))

    # Get grades
    grades = [
        float(document.getElementById("grd1").value),
        float(document.getElementById("grd2").value),
        float(document.getElementById("grd3").value),
        float(document.getElementById("grd4").value),
        float(document.getElementById("grd5").value),
        float(document.getElementById("grd6").value)
    ]

    # Compute weighted average (GWA)
    total_weighted = 0
    total_units = 0

    for i in range(len(subjects)):
        total_weighted += grades[i] * units[i]
        total_units += units[i]

    gwa = total_weighted / total_units

    # Display student information
    display(f"Student Name: {first_name} {last_name}", target="show_name")

    # Build and display grades list
    grade_output = ""
    for i in range(len(subjects)):
        grade_output += f"{subjects[i]} ({units[i]} units): {grades[i]}<br>"
    document.getElementById("show_grade").innerHTML = grade_output
    


    # Display GWA
    display(f"General Weighted Average (GWA): {gwa:.2f}", target="show_ave")
