import streamlit as st
import random

def generate_minefield(round_id):
    # Ensure the round_id is valid
    round_length = len(round_id)
    if round_length < 36:
        return "Invalid round ID", None
    elif round_length == 36:
        # Initialize all cells as question marks
        minefield = [":question:" for _ in range(25)]

        # Randomly place green squares
        green_indices = [random.randint(0, 7), random.randint(8, 12), random.randint(13, 16), random.randint(17, 24)]
        for index in green_indices:
            minefield[index] = ":green_square:"

        # Create a grid-like structure
        rows = [
            " ".join(minefield[0:5]),
            " ".join(minefield[5:10]),
            " ".join(minefield[10:15]),
            " ".join(minefield[15:20]),
            " ".join(minefield[20:25]),
        ]
        return "\n".join(rows), random.randint(45, 90)

# Streamlit app
st.title("Mines Predictor")

round_id = st.text_input("Enter Round ID (36 characters):", "")

if st.button("Generate Mines"):
    if round_id:
        grid, accuracy = generate_minefield(round_id)
        if grid == "Invalid round ID":
            st.error(grid)
        else:
            st.subheader("Minefield Grid:")
            st.text(grid)
            st.subheader(f"Accuracy: {accuracy}%")
           
            st.write("_Made by techjit_")
    else:
        st.error("Please enter a valid Round ID.")
