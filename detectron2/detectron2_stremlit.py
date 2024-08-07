import streamlit as st
from getbikes import bikes_list, get_bikes, get_images_titles, front_tags
from inference_sdk import InferenceHTTPClient
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
            st.experimental_rerun()  # Refresh the interface
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
    st.experimental_rerun()  # Refresh the interface

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
    api_url_input = col1.text_input("Provide your API url")
    api_key_input = col2.text_input("Provide your API key")
    model_id_input = col3.text_input("Provide your Model ID")

    # Hardcoded API data for development/testing
    api_url = "https://detect.roboflow.com"
    api_key = "q46vvAvjgrsSYY732pD2"
    model_id = "bike_detector-ki6j2/1"

    # Initialize the inference client
    CLIENT = InferenceHTTPClient(api_url=api_url, api_key=api_key)

    # Function to predict image using the inference client
    def predict_image(url):
        response = CLIENT.infer(url, model_id=model_id)
        # Assuming response has a method or attribute 'predictions' which returns a list of dictionaries
        predictions = response['predictions']  # Adjust based on actual structure of response
        filtered_results = [result for result in predictions if result['confidence'] > 0.92]
        return filtered_results

    predictions = []

    # Function to execute the search for bikes
    def execute_search():
        # Initialize progress bar and status message
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        total_pages = 220  # Example: Assume we know there are 5 pages to scrape
        total_items = 20  # Example: Assume each page has 20 items
        
        i = 1  # Page number for scraping
        total_progress = total_pages * total_items

        while i <= total_pages:
            get_bikes(i)
            i += 1
            n = 0  # Position of the ad in the page
            for j in bikes_list:
                images, title = get_images_titles(j)
                bike = {
                    "title": title,
                    "url": j,
                    "front_photo": front_tags[n],
                    "images": images,
                }
                n += 1
                # Check if the bike matches and add it to predictions
                for item in images:
                    matches = predict_image(item)
                    if matches:
                        bike['matches'] = matches
                        predictions.append(bike)
                        break

                # Update progress bar and status
                current_progress = ((i - 1) * total_items + n) / total_progress
                progress_bar.progress(current_progress)
                status_text.text(f"Processing page {i} item {n}/{total_items}")

            if i > total_pages:
                break

        # Display predictions
        for idx, prediction in enumerate(predictions):
            with st.container():
                st.write("These are your predictions")
                st.image(
                    caption=prediction["title"],
                    image=prediction["front_photo"],
                    width=500,
                )
                st.write("Matches with confidence above 0.92:")
                for match in prediction['matches']:
                    st.write(f"- Confidence: {match['confidence']}")
                if st.button(prediction["title"], key=f"button_{idx}"):
                    st.write(prediction["url"])

    # Button to start the search
    start_searching = st.button(label="Start Searching")
    if start_searching:
        execute_search()
else:
    st.write("Please login to use the application.")
