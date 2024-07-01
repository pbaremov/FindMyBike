import time
import streamlit as st

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button("Rerun")


# import streamlit as st
# import time

# "Starting a long computation..."

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)
# list = [
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
#     "1",
#     "2",
#     "3",
#     "",
# ]
# for i in range(len(list)):
#     # Update the progress bar with each iteration.
#     if bar.progress == len(list):
#         break
#     latest_iteration.text(f"Iteration {i+1}")
#     bar.progress(i + 1)
#     time.sleep(0.1)
#     print(type(bar.progress))


# "...and now we're done!"
