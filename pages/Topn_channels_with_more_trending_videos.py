import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title = "Top_n_Channels",page_icon='▶️')

st.write("""
# Trending Youtube Videos
This app will help you analyse your youtube videos to help your videos appeat on the trending list!
***
""")  # pour faire une ligne

#input the number of channels we want to see
number = st.number_input('Choose the top channels with the most videos on trending list!')
#st.write('you want the top ', number, "channels")

n = int(number)


df = pd.read_csv('GBchannels_with_more_the_most_trending_videos.csv') 


def channel_with_more_trending_videos(n):
    
    chanelsbysize = df.head(n)
   
    top_recommendations = chanelsbysize[['channel_title', 'video_count']]#.reset_index()
    
    fig, ax = plt.subplots(figsize=(8,8))
    
    channel = sns.barplot(x="video_count", y="channel_title", data=top_recommendations,palette=('flare'), ax=ax)
    channel = ax.set(xlabel="number of videos base on the size of the channel", 
                     ylabel="top20 Channels with most trending videos", title = "n Channels with more trending videos")
    
    st.pyplot(fig)
    
    return top_recommendations

#channel_with_more_trending_videos(n)

#st.set_page_config(layout="wide") 
#st.header("click the botun below to display the list of the Top trending Channels")

st.write("""
#### click the bottun below to display the list of the Top trending Channels!
***
""") 

if st.button('Top Channel on Trending') and n != 0:
    
    popul_channels = channel_with_more_trending_videos(n)
    #st.text(channel_choise)
    st.table(popul_channels)
else:
     st.write('Show the the Top trending channels!')
