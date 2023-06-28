#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st



# In[2]:


##Updating Page Logo and Tab Title
st.set_page_config(page_title='Galileo',
                   page_icon='https://amazon-blogs-brightspot-lower.s3.amazonaws.com/about/00/92/0260aab44ee8a2faeafde18ee1da/amazon-logo-inverse.svg',
                   layout="wide")



##Creating Text format options with base and team colors
def highlight(text):
     st.markdown(f'<p style="text-align: center;color:#013369;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
def color(text):
     st.markdown(f'<p style="color:#013369;font-size:20px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)
def accuracy(text):
     st.markdown(f'<p style="color:#013369;font-size:15px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)
def disclaimer(text):
     st.markdown(f'<p style="color:red;font-size:15px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)




##--------------------------------------------------------Application Displayed Portion-----------------------------------------



##Header and Logo
col_title, col_logo = st.beta_columns([4,1])
with col_title:
  st.title('Galileo')
  st.markdown(' ## Created by Raghu Mallappa, Pranav Varma, and Cole Brandt')
  st.markdown('  Last updated: June 28th, 2023')  
with col_logo:
  st.image("https://amazon-blogs-brightspot-lower.s3.amazonaws.com/about/00/92/0260aab44ee8a2faeafde18ee1da/amazon-logo-inverse.svg")
st.write("#")


st.text_input("Please input your question about device sales and traffic", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")



# Bottom info bar ------------------------------------------------------------------------
st.markdown('___')
about = st.beta_expander('About')
with about:
    '''
    Developed by @colerb, @raghumal, and @prv. For more information, please visit our team's [Wiki] (https://w.amazon.com/bin/view/DDS_Analytics).
    '''
    
st.image("https://amazon-blogs-brightspot-lower.s3.amazonaws.com/about/00/92/0260aab44ee8a2faeafde18ee1da/amazon-logo-inverse.svg",
    width= 100, caption='Powered by DDS @ Amazon')




