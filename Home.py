import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

icon = Image.open("D:\My_webapp\images\home.png")
st.set_page_config(page_title="Aman Sah",
                   page_icon=icon,layout="centered" )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use Local CSS
def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("D:\My_webapp\style.css")

#Load your assets:
# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_aman= Image.open("D:\My_webapp\images\Aman.png")
github = Image.open("D:\My_webapp\images\github.webp")
linkedin = Image.open("D:\My_webapp\images\linkedin.webp")


with st.container():
    st.header("WELCOME !")
    st.subheader("Hi, I am Aman Sah")



#######------About Section ---------------########
with st.container():
    lc_1,rc_1 = st.columns((2,1))
    with lc_1:
        st.header("About Me")
        st.write("---")
        st.write("""Currently, I am engaged in the pursuit of knowledge and innovation as I pursue
                a Master of Technology (M.Tech) in Aerospace Engineering.
                 Specilizing in the field of Aerothermodynamics and Thermal Sciences (ATTS) at 
                [Indian Institute of Technology Kanpur](https://www.iitk.ac.in/).
                Within the Aerospace Department, Under the guidance of  [Prof. Vaibhav Arghode Sir](https://sites.google.com/view/varghode).""")
                 
        
    with rc_1:
        st.image(img_aman,width=200)
        
st.write("---")
with st.container():
    st.title("Education")
    lc_2, rc_2 = st.columns(2)
    st.write("---")
    with lc_2:
        st.subheader("B.E. in Mechanical Engineering")
        st.write("July'2016 - Dec'2020")
        st.write("[Jadavpur University](http://www.jaduniv.edu.in/).")

    with rc_2:
        st.subheader("M.Tech in Aerospace Engineering")
        st.write("Specialization : Aerothermodynamics and Thermal Sciences")
        st.write("July'2022 - Cont.")
        st.write("Advance Combustion and Acoustics Lab (IIT Kanpur)")
        st.write("[web-mail](https://amansah22@iitk.ac.in)")


#---mY FIELD OF INTERESTS-------------
with st.container():
    st.header('Interests')
    st.write("---")
    
    lc,rc =st.columns(2)

    with lc:
        st.write(""" I am immersing myself in cutting-edge research and exploration, particularly focusing on Scaling of PVRF combustors and
                exploring the intersections of Machine Learning, 
                Artificial Intelligence,Data science, Image Processing, Machine Vision, and Autonomous guidance of Unamanned vehicles.""")
    with rc:
        st_lottie(lottie_coding , height=  300, key= "coding")

#Contact Page details
with st.container():
    st.write("---")
    st.header("Get In Touch With me  !")
    st.write("###")


    contact_form = """
<form action="https://formsubmit.co/amansah22@iitk.ac.in" method="POST">
     <input type = "hidden" name= "_captcha" value = "false">
     <input type="text" name=" name" plceholder= "Your Name" required>
     <input type="email" name="email" placeholder = "Your E-mail" required>
     <textarea name = "message" placeholder = "Your Message" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_col,right_col = st.columns(2)
with st.container():
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=
                True)
    
    with right_col:
        st.empty()


st.write("---")
with st.container():
    p,q = st.columns(2)
    with p:
        st.image(linkedin,width=50)
        st.write("[Linkedin Profile](https://www.linkedin.com/in/aman-sah-8a320b14b/)")
    with q:
        st.image(github,width=50)
        st.write("[Github Profile ](https://github.com/AmanSah17)")
