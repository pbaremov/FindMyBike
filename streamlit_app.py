import streamlit as st
import inference

from getbikes import bikes_list, get_bikes, get_images_titles, front_tags


# setting some page configurations
st.set_page_config(layout="wide", page_title="FindMyBike WebApp", page_icon=None)

# title
st.title("Find your bicycle on pinkbike.com")

st.write("[https://roboflow.com/](https://roboflow.com/)")
# header
st.header("Please provide details of your RoboFlow detector model")

# upload your detector                //possibly 3 input fields 1. Api key 2. project name 3 version
col1, col2, col3 = st.columns(3)

api_key_1 = col1.text_input("Provide your API url")
project_name = col2.text_input("Provide your API key")
project_version = col3.text_input("Provide your Model ID")

# api data will be hardcoded for the purpose of development and testing 
# api_url = "https://detect.roboflow.com"
# api_key = "q46vvAvjgrsSYY732pD2"
# model_id = "bike_detector-ki6j2/1"

# initialize the client
# CLIENT = InferenceHTTPClient(
#     api_url=api_url, api_key=api_key
# )

model = inference.ge
def predict_image(url):
    result = model_id.infer(url)
    return result.get()
predictions = []



def execute_search():
    i = 1  # This variable is used for getting the page number for scraping through multiple pages

    while True:
        get_bikes(i)
        i += 1
        n = 0  # This variable gives the position of the ad inside the page - usually a number between 0 and 19
        for j in bikes_list:
            images, title = get_images_titles(j)

            bike = {
                "title": title,
                "url": j,
                "front_photo": front_tags[n],
                "images": images,
            }
            # print(n)
            n += 1
            print(bike["title"], bike["url"])

            # Check if the bike title matches the desired one and it hasn't been added yet
            for item in images:
                match = predict_image(item)
                print(match)
                if match:
                    predictions.append(bike)
                    break
        # Print the predictions (you can remove this line if not needed)
        # print(predictions)
        # Display predictions (you can customize this part as needed)
        for prediction in predictions:
            with st.container():
                st.write("These are your predictions")
                st.image(
                    caption=prediction["title"],
                    image=prediction["front_photo"],
                    width=500,
                )
                st.link_button(label=prediction["title"], url=prediction["url"])


# include some sort of a progress bar

start_searching = st.button(
    label="Start Searching",
)
if start_searching:
    print("button is pressed")
    execute_search()
