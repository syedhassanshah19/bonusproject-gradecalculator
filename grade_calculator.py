import streamlit as st

def calculate_total(marks):
    """Calculate total marks from a list of marks"""
    return sum(marks)

def calculate_percentage(total, num_subjects):
    """Calculate percentage"""
    return total / num_subjects

def determine_grade(percentage):
    """Determine grade based on percentage"""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

st.title("📊 Grade Calculator")
st.write("Enter your marks for each subject to calculate total, percentage, and grade.")

num_subjects = st.number_input("Enter number of subjects:", min_value=1, max_value=10, value=3, step=1)

marks = []
for i in range(1, num_subjects + 1):
    mark = st.number_input(f"Marks for Subject {i}:", min_value=0, max_value=100, step=1)
    marks.append(mark)

if st.button("Calculate Grade"):
    total = calculate_total(marks)
    percentage = calculate_percentage(total, num_subjects)
    grade = determine_grade(percentage)

    st.success(f"✅ Total Marks: {total}")
    st.success(f"📌 Percentage: {percentage:.2f}%")
    st.success(f"🎓 Grade: {grade}")
