from getbikes import bikes_list, get_bikes, get_images_titles, front_tags
# from robo_detector import robo_detector


import streamlit as st
from st_picture_carousel import st_picture_carousel


st.set_page_config(layout="wide", page_title="FindMyBike WebApp", page_icon=None)

# title
st.title("Find your bicycle on pinkbike.com")


# header
st.header("Please provide details of your RoboFlow detector model")

# upload your detector                //possibly 3 input fields 1. Api key 2. project name 3 version
col1, col2, col3 = st.columns(3)

api_key = col1.text_input("Provide your API key")
project_name = col2.text_input("Provide your project name")
project_version = col3.text_input("Provide your project version")

# save your detector // this may be optional


# load the detector

print(api_key)

# upload your images
photo = st.file_uploader(type=["png, jpeg, jpg"], label="upload your file")


# include some sort of a progress bar


# run the code that will scrape through all the HTML and will get the urls of all the images

i = 1
while True:
    # print(f'i is {i}')
    a = len(bikes_list)
    get_bikes(i)

    i += 1

    n = 0
    for i in bikes_list:
        images, title = get_images_titles(i)

        bike = {
            "title": title,
            "url": i,
            "front_photo": front_tags[n],
            "images": images,
        }
        print(n)
        n += 1
        print(len(bike["images"]))

        print(bike)

        st.image(
            caption=bike["title"],
            image=bike["front_photo"],
        )
        st.image(image=bike["images"])
        st.link_button(label=bike["title"], url=bike["url"])
        # for image in images:
        #     display_bicycles_only(image)
        # print(get_front_image(i))

        # this code will show the progress on the screen

        # make predictions

        # image_carousel = st_picture_carousel(img_list=images)

    #     for i in images:
    # #         result = robo_detector(i)
    # #         print(result)
    #         st_picture_carousel(images)
    # # #


    # display the results
