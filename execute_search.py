# run the code that will scrape through all the HTML and will get the urls of all the images
import streamlit as st 
from getbikes import bikes_list, get_bikes, get_images_titles, front_tags

def execute_search():
    i = 1
    while True:
        # print(f'i is {i}')
        a = len(bikes_list)
        get_bikes(i)

        i += 1

        n = 0
        for j in bikes_list:
            images, title = get_images_titles(j)

            bike = {
                "title": title,
                "url": j,
                "front_photo": front_tags[n],
                "images": images,
            }
            # print(f"bike number {n}")
            n += 1
            # print(f'Len(bike[images]) is {len(bike["images"])}')

            # print(bike)

            # for image in images:
            #     display_bicycles_only(image)
            # print(get_front_image(i))

            # this code will show the progress on the screen

            # make predictions

            #     for i in images:
            # #         result = robo_detector(i)
            # #         print(result)
            #         st_picture_carousel(images)
            # # #

            # display the results
            with st.container():
                st.write("this are your predictions")
                st.image(
                    caption=bike["title"],
                    image=bike["front_photo"],
                    width=500,
                )  # this displays the front photo0,

                # st.image(image=bike["images"])  # this displays the list of internal images
                st.link_button(
                    label=bike["title"], url=bike["url"]
                )  # this button is a link to the web page of the bicycle

            # if len(bike["images"]) != 0:
            #     img = image_select(
            #         label=bike["title"],
            #         images=bike["images"],
            #     )