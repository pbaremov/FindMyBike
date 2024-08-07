import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from inference_sdk import InferenceHTTPClient
from getbikes import bikes_list, get_bikes, get_images_titles, front_tags

from auth import create_user_table, add_user, authenticate_user

# Initialize the user table
create_user_table()

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="FindMyBike WebApp", page_icon=None)

# Application title
st.title("Find your bicycle on pinkbike.com")
st.write("[https://roboflow.com/](https://roboflow.com/)")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Custom CSS for logout button
st.markdown(
    """
    <style>
        .logout-button {
            color: red;
            cursor: pointer;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# User authentication
def login():
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if authenticate_user(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.sidebar.success("Logged in successfully.")
            st.rerun()  # Refresh the interface
        else:
            st.sidebar.error("Invalid credentials")


def signup():
    username = st.sidebar.text_input("New Username")
    password = st.sidebar.text_input("New Password", type="password")
    if st.sidebar.button("Signup"):
        add_user(username, password)
        st.sidebar.success("User created successfully. Please log in.")


def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.rerun()  # Refresh the interface


# Sidebar navigation
if not st.session_state["logged_in"]:
    auth_choice = st.sidebar.radio("Login/Signup", ["Login", "Signup"])
    if auth_choice == "Login":
        login()
    elif auth_choice == "Signup":
        signup()
else:
    st.sidebar.write(f"Logged in as {st.session_state['username']}")
    if st.sidebar.button("Logout"):
        logout()

# Display content if logged in
if st.session_state["logged_in"]:
    # Columns for API inputs
    col1, col2, col3 = st.columns(3)
    api_url = col1.text_input("Provide your API url") or "https://detect.roboflow.com"
    api_key = col2.text_input("Provide your API key") or "RsunSlYyEuNm2g6ifjQB"
    model_id = col3.text_input("Provide your Model ID") or "bike_detector_2-l1bwq/1"

    # setting a confidence score
    confidence_score = st.number_input(
        label="Set a confidence score for your predictions. NB: Lower confidence score equals more FALSE predictions",
        min_value=0.0,  # Optional: minimum value
        max_value=1.0,  # Optional: maximum value
        value=0.91,
        step=0.01,  # Optional: step size
        format="%.2f",  # Optional: format the float number
    )

    # # Hardcoded API data for development/testing
    # api_url = "https://detect.roboflow.com"
    # api_key = "q46vvAvjgrsSYY732pD2"
    # model_id = "bike_detector-ki6j2/1"

    # Initialize the Client
    CLIENT = InferenceHTTPClient(api_url=api_url, api_key=api_key)

    # Function to predict image using the inference client
    def predict_image(url):
        response = CLIENT.infer(url, model_id=model_id)
        predictions = response.get("predictions", [])
        filtered_results = [
            result for result in predictions if result["confidence"] >= confidence_score
        ]
        return filtered_results

    predictions = []
    current_bike = st.empty()
    confidence_score = 0

    # Function to execute the search for bikes
    def execute_search():
        i = 6  # Page number for scraping
        while True:
            get_bikes(i)
            # i += 1
            n = 0  # Position of the ad in the page
            for j in bikes_list:
                images, title = get_images_titles(j)
                bike = {
                    "title": title,
                    "url": j,
                    "front_photo": front_tags[n],
                    "images": images,
                }
                print(n)
                print(f"Current bike is {bike}")

                # Update the current bike display
                with current_bike.container(height=500):
                    st.write("Currently Processing:")
                    st.image(
                        bike["front_photo"],
                        caption=bike["title"],
                        width=300,
                    )
                n += 1
                # Check if the bike matches and add it to predictions
                if title == "Montana Coyote 26 Small":
                    for item in images:
                        match = predict_image(item)
                        print(match)

                        if match:
                            predictions.append(bike)

                            break
            # Display predictions
            for prediction in predictions:
                with st.container():
                    st.write("These are your predictions")
                    st.image(
                        caption=prediction["title"],
                        image=prediction["front_photo"],
                        width=500,
                    )
                    st.link_button(
                        label=prediction["title"],
                        url=prediction["url"],
                    )

    # Button to start the search
    start_searching = st.button(label="Start Searching")
    if start_searching:
        execute_search()
else:
    st.write("Please login to use the application.")
