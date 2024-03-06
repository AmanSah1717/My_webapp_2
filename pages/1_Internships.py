import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Internships",
    page_icon="D:\My_webapp\images\home.png", 
    layout="centered"
)

# Load images
img_metric = Image.open("D:\My_webapp\images\metric_errors.jpg")
img_pred = Image.open("D:\My_webapp\images\plot.jpg")
img_inuron = Image.open("D:\My_webapp\credentials\Ineuron_ai.jpg")
dnn_trash = Image.open("D:\\My_webapp\\images\\trash_det.jpg")
fin_cert = Image.open("D:\My_webapp\images\Finlatics_Cert.jpg")
fin_lor = Image.open("D:\My_webapp\images\Finlatics_LOR.jpg")


st.header("Internships")
st.subheader("Data Science Analyst") 
lc, rc = st.columns((2,1))

with st.container():
    
    
    with lc:
    
            st.image(img_metric,width=400,caption="Table : Various Model Performace ")
            st.image(img_pred,width=400,caption= "Test Fit Line")
            st.image(img_inuron,caption= "Internship Completion Certificate",width =400)

    
    with rc:
        st.write("""
            The project demonstrates how Machine Learning can predict flight 
            fares based on historical data (a supervised machine learning problem). 
            To obtain the best model performance, I have implemented a number of algorithms. 
            If you look at the core of the problem, based on the data, it is a regression problem. 
            There are a number of algorithms developed to tackle such issues, but to the context 
            of this report and based on the model accuracy to be as high as possible, 
            I have used LinearRegression, KNeighborsRegressor, RandomForestRegressor, 
            XGBRegressor, DecisionTreeRegressor, etc.
            """)

        st.write("[Code Explanation >](https://drive.google.com/file/d/19wC7T-EyLfZOA7tcJ5BN-WTDBADqqV9i/view?usp=drive_link)")
        st.write("[Github > ](https://github.com/AmanSah17/Flight_fare_prediction)")

st.write("---")
with st.container():
    lcc,rcc = st.columns(2)
    with lcc:
        
        st.subheader("Deep Neural Network For Trash Tracking on Polluted Rivers")

    with rcc:
        st.subheader("[AIRSHED PLANNING PROFESSIONALS, KANPUR](https://www.airshed.in/)")



    lc_1, rc_1 = st.columns((2,1))
    with st.container():   
        with lc_1:
            st.image(dnn_trash,caption="Detection Results Obtained from YOLO-V5 with Centroid(s) co-ordinates ")



        with rc_1:
            st.write("""
                        A custom Yolo-V5 trained CNN Model used to track floating trash on water, and Post-processing using OpenCV-python.
                        Later this tracking code is Integrated with ROS Virtual Environment to Navigate your Autonomous Boat on the water.                 


                    """)
            st.write("[Github Link >](https://github.com/AmanSah17/Autonomous-Boat---Trash-detection-and-Tracking-)")
        

st.write("---")


with st.container():    
    pr_name,org = st.columns(2)

    with pr_name:
          st.subheader("Strategic Business Expansion in the Indian IT Landscape")
    with org:
     st.subheader("[FINLATICS BUSINESS ANALYTICS](http://finlatics.com/)")

    lc,rc = st.columns(2)

    with lc:
        lcl,lcr = st.columns(2)
        with lcl:
            st.image(fin_cert,width= 300, caption = "Certificate of completion")
            st.image(fin_lor,width=300,caption= "Letter of recommendation")
    with rc:
        st.write("""
                Conducted comprehensive Visual analysis of Indian market dynamics and growth potential,using matplotlib,folium,geopandas
                identifying key improvement areas and Provided strategic investment recommendations Using Tableau and PowerBI
                visualizations.""")
        st.write("""
                • targeted sectors, such as BFSI, healthcare, retail, and entertainment resulting in informed decision-making and targeted
                market entry.
                 """)
        st.write("[Report and Credentials > ](https://drive.google.com/drive/u/2/folders/1RB-q7Fx8JjAWc0RBUhZNbIUFGgAQ47yA)")