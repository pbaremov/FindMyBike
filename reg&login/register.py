# app.py
import streamlit as st

def main():
    st.title("User Registration Form")

    # Input fields
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        # Validate and process user input (e.g., save to database)
        if username and email and password:
            st.success(f"User {username} registered successfully!")
        else:
            st.error("Please fill in all fields.")

if __name__ == "__main__":
    main()
