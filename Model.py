# To run the script :
# 1) Install streamlit :
#                       a) For Windows : pip install streamlit
# 2) Test it using streamlit hello : This opens up a demo app.
# 3) Type in cmd : streamlit run Model.py 

# Importing libraries
import cv2
import streamlit as st
import numpy as np
import mediapipe as mp
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageFilter
import os

## Function to save the image in the same folder as the project folder
def get_image_download_link(image_file,filename,text):
    file_details = {"FileName":filename,"FileType":"png"}
    st.write(file_details)
    img =np.array(image_file)
    cv2.imwrite(filename+".png",cv2.cvtColor(img, cv2.COLOR_RGB2BGR))        
    st.success("Saved File")

# To change the cotents of the screen
placeholder=st.empty()

# The default screen
with placeholder.container():
        st.title("Hackathon Badge Generator")
        st.subheader("This App Takes A Photo And Generates A Custom Badge For The Participant")
        st.write("This app is made by Harshavardhan Bajoria")

# The selection bar
add_selectbox = st.sidebar.selectbox(
    "What Operation You Would Like To Perform :",
    ("About","Badge Generator")
)

#The About Section
if add_selectbox=="About":
    st.write()
    st.write("This App Uses PIL library and streamlit library to generate a badge")
    st.write("On the right hand side you may choose the tasks you wish to perform.")
    st.write("Thanks For Visting. Hope You Have A Great Day. ")
    st.write()
    st.subheader("You May Report Bugs By Using Any Contact Method Listed Below.")
    st.subheader("Email :")
    st.write("hvbajoria@hotmail.com")
    st.subheader("LinkedIn:")
    st.write("https://www.linkedin.com/in/harshavardhan-bajoria")

# To get the image from the user
image=st.sidebar.file_uploader("Upload Image")
if image is not None:
    image=Image.open(image)
    image1=np.array(image)
    st.sidebar.image(image1)

# The Badge Generator Section
    if add_selectbox=="Badge Generator":
        placeholder.empty()
        with placeholder.container():
              st.title("Let's Generate Your Awesome Badge :")
              st.write("Don't forget to share this on your social media")
              st.subheader("Note :")
              st.write("It Supports Image Only In .png Format")
              # For selection of badge
              add_selectbox2 = st.selectbox(
               "Choose A Badge:",
               ("The Ray of Code", "Ocean of Possibilities", "The Coding World","The Entry Gate","Start of Journey")
            )
              # To resize the image and give it a circular appearence
              h,w = image.size
              lum_img = Image.new('L',[h,w] ,0) 
              draw = ImageDraw.Draw(lum_img)
              draw.pieslice([(0,0),(h,w)],0,360,fill=255)
              img_arr = np.array(image)
              lum_img_arr = np.array(lum_img)
              final_img_arr = np.dstack((img_arr, lum_img_arr))
              result=Image.fromarray(final_img_arr)
              # To ask for the user name and add it to the badge
              message = st.text_input('Enter Your Name')
              if message:
                name = message
                color = 'rgb(255,255,255)' 
                font = ImageFont.truetype('arial.ttf', size=30)
                # If user chooses The Ray of Code Badge
                if add_selectbox2=="The Ray of Code":
                    template = cv2.imread('template.png')
                    template = Image.open("template.png")
                    resized_image = result.resize((190,180))
                    Image.Image.paste(template,resized_image, (158, 143))
                    draw = ImageDraw.Draw(template)
                    
                    W, height = template.size
                    w, h = draw.textsize(message)
                    draw.text(((W/2)-w,420), message, fill=color, font=font)
                    st.image(template)

                    # To give the user an option to download the image
                    if(st.sidebar.button('Download')) :
                        result = template
                        img_file='The Ray of Code Badge'
                        st.markdown(get_image_download_link(result,img_file,'Download '+img_file), unsafe_allow_html=True)
                # If user chooses Ocean of Possibilities Badge
                if add_selectbox2=="Ocean of Possibilities":
                    template = cv2.imread('template2.png')
                    template = Image.open("template2.png")
                    resized_image = result.resize((190,180))
                    Image.Image.paste(template,resized_image, (158, 143))
                    draw = ImageDraw.Draw(template)
                    
                    W, height = template.size
                    w, h = draw.textsize(message)
                    draw.text(((W/2)-w,430), message, fill=color, font=font)
                    st.image(template)

                    # To give the user an option to download the image
                    if(st.sidebar.button('Download')) :
                        result = template
                        img_file='Ocean of Possibilities Badge'
                        st.markdown(get_image_download_link(result,img_file,'Download '+img_file), unsafe_allow_html=True)
                # If user chooses The Coding World Badge
                if add_selectbox2=="The Coding World":
                    template = cv2.imread('template3.png')
                    template = Image.open("template3.png")
                    resized_image = result.resize((190,180))
                    Image.Image.paste(template,resized_image, (158, 159))
                    draw = ImageDraw.Draw(template)
                    
                    W, height = template.size
                    w, h = draw.textsize(message)
                    color='rgb(0,0,0)'
                    draw.text(((W/2)-w,430), message, fill=color, font=font)
                    st.image(template)

                    # To give the user an option to download the image
                    if(st.sidebar.button('Download')) :
                        result = template
                        img_file='The Coding World Badge'
                        st.markdown(get_image_download_link(result,img_file,'Download '+img_file), unsafe_allow_html=True)
                # If user chooses The Entry Gate Badge
                if add_selectbox2=="The Entry Gate":
                    template = cv2.imread('template4.png')
                    template = Image.open("template4.png")
                    resized_image = result.resize((190,180))
                    Image.Image.paste(template,resized_image, (158, 143))
                    draw = ImageDraw.Draw(template)
                    
                    W, height = template.size
                    w, h = draw.textsize(message)
                    draw.text(((W/2)-w,443), message, fill=color, font=font)
                    st.image(template)

                    # To give the user an option to download the image
                    if(st.sidebar.button('Download')) :
                        result = template
                        img_file='The Entry Gate Badge'
                        st.markdown(get_image_download_link(result,img_file,'Download '+img_file), unsafe_allow_html=True)
                # If user chooses Start of Journey Badge
                if add_selectbox2=="Start of Journey":
                    template = cv2.imread('template5.png')
                    template = Image.open("template5.png")
                    resized_image = result.resize((190,180))
                    Image.Image.paste(template,resized_image, (158, 143))
                    draw = ImageDraw.Draw(template)
                    
                    W, height = template.size
                    w, h = draw.textsize(message)
                    color = 'rgb(0,0,0)'
                    draw.text(((W/2)-w,420), message, fill=color, font=font)
                    st.image(template)

                    # To give the user an option to download the image
                    if(st.sidebar.button('Download')) :
                        result = template
                        img_file='Start of Journey Badge'
                        st.markdown(get_image_download_link(result,img_file,'Download '+img_file), unsafe_allow_html=True)
