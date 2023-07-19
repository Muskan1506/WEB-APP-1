import streamlit as st
from PIL import Image, ImageFilter
import os

#create a folder images
if not os.path.exists ('images'):
    os.makedirs('images')
def save_image(image):
    img=Image.open(image)
    img.save(f'images/{image.name}.png') 

st.title('image processing App')

upload =st.file_uploader(
    label='Upload your image',
    type=['png','jpg','jpeg']
    )
if upload is not None:
    save_image(upload)
    img=Image.open(upload)
    col1,col2=st.columns(2)

filters=['contour','emboss','edge_enhance','blur','smooth','sharpen']
option =st.sidebar.selectbox('select a filter',filters)
col1.image(upload,caption='upload Image',use_column_width=True)
if option=='contour':
   col2.image(img.filter(ImageFilter.CONTOUR),caption='contour filter', use_column_width=True)
if option=='emboss':
    col2.image(img.filter(ImageFilter.EMBOSS),caption='emboss filter',use_column_width=True)

if option =='edge_enhance':
    col2.image(img.Filter(ImageFilter.EDGE_ENHANCE),caption='edge enhance Filter',use_column_width=True)

if option=='blur':
    col2.image(img.Filter(ImageFilter.BLUR),caption ='Blur Filter',use_column_width=True)

    if option=='smooth':
        col2.image(img.Filter(Image.Filter.SMOOTH),caption='Smooth Filter',use_column_width=True)

if option=='Sharpen':
    col2.image(img.Filter(Image.Filter.SHARPEN),caption='Sharpen Filter',use_column_width=True)

    if option=='find edges':
        col2.image(img.Filter(Image.Filter.FIND_EDGES),caption='Find Edges',use_column_width=True)

    message=st.sidebar.text_input("Enter a message",value= "MONDAY")
    font_size=st.sidebar.number_input("Enter font size",value=20)
    font_color=st.sidebar.color_picker("select font color")
    c1,c2=st.sidebar.column(2)
    x=c1.number_input('x coordinate')
    