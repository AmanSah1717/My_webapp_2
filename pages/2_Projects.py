import requests
from PIL import Image
import streamlit as st



st.set_page_config(page_title="Projects",
                   page_icon= "D:\My_webapp\images\sample 3d 1.png ",layout="centered" )

img_1 = Image.open("D:\My_webapp\images\s1.png")
img_2 = Image.open("D:\My_webapp\images\sample 3d 1.png")
pvrf_vid= "D:\My_webapp\images\PVRF_16_11_23.mp4"
img_RP = Image.open("D:\My_webapp\images\RP.png")       # Note: the video of the combustor taken on 16th November 2023
img_cdu = Image.open("D:\My_webapp\images\cdu.jpg")
img_cdu_result = Image.open("D:\My_webapp\images\iterations.jpg")
img_box = Image.open("D:\\My_webapp\\images\\amazon.jpg")
img_machine = Image.open("D:\My_webapp\images\RE_pac_machine.jpg")
img_val = Image.open("images/validation_img.jpg")
img_coutee = Image.open("D:\My_webapp\images\coutee_flow.jpg")


#-----PROJECTS-------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("---")
    img_col_1,text_col_1 = st.columns((2,4))

    with img_col_1:
        img_col_3,vid_col = st.columns((1,1))
        with img_col_3:
            #insert the image
            st.image(img_RP,caption="Prototype Model")
            


        with vid_col:
            st.image(img_2,caption="ANSYS (Combustion simulation) of Scaled Model"
                     )
           
    
    with text_col_1:
        st.header("M.Tech Thesis")
        st.subheader(" Design and Scaling of High Thermal Intensity Porous Media PVRF Combustor for Jet-Engines ")
        st.write("Mentor : Prof. vaibhav Arghode")
        st.write(
            """Inegration of advanced porous media, including SiC and Al2O3, into combustor designs.
              Aimed at substantial reduction of CO,CO2 and Nox emissions, while concurrently tackling operational noise levels.
              A proactive approach to continuously enhancing combustion technology for superior environmental impact.""")
        st.write("""Designed and Assembled comprehensive 3D model of PVRF Combustor using Creo Parametric.  
                 Compared combustion CFD Simulation results with the experimental setup to draw research backed inferences from the  various data collected. 

            """
        )
    st.write("---")


with st.container():
    st.write("#####")
    img_col_2,text_col_2 = st.columns((2,1))

    with img_col_2:
        in_col_r,in_col_left = st.columns(2)
        with in_col_left:
            st.image(img_cdu,caption= "Conditional Delay Units")
        with in_col_r:
            st.image(img_cdu_result,caption= "Iteration Convergence Plots with different learning rates")
    
    
    
    with text_col_2:
        st.subheader("Cracking Binary PUF Hardware Security Using Machine Learning")
        st.write(
            """ • Research Project based on how the 1980s 2048 randomly connected PUF-CDU Hardware Encryption can be cracked using
                Linear Regression.""")
        
        st.write("""
                 • Out of Millions of Combinations our model can crack it   
                 within 0.3 secondsusing minibatch gradient descent, NAG acceleration, 
                 and ISTA to enhance the accuracy of input prediction."""
        )

st.write("---")
with st.container():
    img_col_3,text_col_3 = st.columns((2,1))
    with img_col_3:
        in_col_r , in_col_left = st.columns(2)
        with in_col_left:
            st.image(img_box)
        with in_col_r:
            st.image(img_machine)

    with text_col_3:
        st.subheader("RE- PAC (Packaging Material Classification Application )")
        st.write("""
                 Developed by a team from IIT Kanpur, our project leverages cutting-edge technologies for precise packaging material classification. Using Deep Neural Networks (DNN), Convolutional Neural Networks (CNN), 
                 Optical Character Recognition (OCR), and Image Processing with OpenCV, our solution ensures accurate classification of texts, barcodes, logos, and object images on packaging materials. The application, built on Streamlit, offers a real-time interface for easy visualization of classification results. Deployable on Raspberry Pi 4B, it's versatile for various environments.
                 """)
        st.write("[Github >](https://github.com/AmanSah17/RE-PAC_Web_app)")
        st.write("[Demo video of application > ](https://drive.google.com/file/d/1dGSNv3476IUgJBPe76PbpMyRCVrmBQgV/view?usp=sharing)")


st.write("---")
with st.container():
    img_col_4,text_col_4 = st.columns((2,1))
    with img_col_4:
        in_col_l,in_col_r = st.columns(2)
        with in_col_l:
            st.image(img_coutee,caption = " Coutee-Flow without and with the prssure gradient")
        with in_col_r:
            st.image(img_val,caption= " Finite Difference Method(FDM) solution convergence with iterations")

    with text_col_4:
        st.subheader ("""Numerical analysis of unsteady Couette flow with a pressure gradient.""")
        st.write("""
                 Couette flow is a classical problem that comes under very few flow problems for which an exact analytical
                solution exists. Couette flow has vast practical applications and is used to model the flow of magma in
                the earth’s mantle, atmospheric circulations, and flow in a lightly loaded journal bearing. In this report,
                a numerical approach was used to study the flow physics for in-compressible Couette flow. The finite
                difference method was used to solve the governing equations. A comparative study between explicit and
                implicit methods of the solution was done. Also, a simple parallel implementation was executed which resulted
                in a visible performance boost. Also, a parametric study on the effect of pressure gradient and Reynolds
                number on the flow profile was done.
                 """)
        st.write("[Google Drive >](https://accounts.google.com/v3/signin/rejected?continue=https://drive.google.com/file/d/1Ze62KU4DDzLbCSxBtHqi_zFw93ApqZx2/view?usp%3Ddrive_link&dsh=S268696828:1687195689446354&flowEntry=ServiceLogin&flowName=WebLiteSignIn&followup=https://drive.google.com/file/d/1Ze62KU4DDzLbCSxBtHqi_zFw93ApqZx2/view?usp%3Ddrive_link&ifkv=Af_xneGFPmoIJKWZdvYfIT5Frj-yUYtxSLzV136wKOqCECeTgKgDgAQDn4qyO-n-0s0nNTRGL9w96A&osid=1&rhlk=js&rrk=47&service=wise)")

















