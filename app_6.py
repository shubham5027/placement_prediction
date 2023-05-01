
import streamlit as st
import numpy as np
import pickle



#loading trained model
loaded_model = pickle.load(open('E:/SE/model_file_2','rb'))


def placement_prediction(x):
    

    prediction = loaded_model.predict(x)
    print(prediction)

    st.subheader("Placement Result")
    if (prediction == 1):
        st.write("Congratulations! You are likely to be placed.")
    else:
            st.write("Sorry, it seems unlikely that you will be placed.")	
       
  

def main():

    
    #getting title & input from user
    st.title("Engineering Student Placement Prediction")
    st.subheader("Please complete the form for a successful prediction")
    st.sidebar.header("")
    stream = st.selectbox("Select Stream", ["Computer Science","Electrical Engineerng","Information Technology","Electronics & Communication Engineering","Mechanical Engineering","Civil Engineering"])
    age = st.slider("Enter Age", min_value=0, max_value=30, step=1)
    gender = st.selectbox("Select Gender", ["Male", "Female"])
    internship = st.slider("Internship", min_value=0, max_value=10, step=1)
    backlogs = st.radio("Internship Experience", ["Yes", "No"])
    cgpa = st.slider("Enter CGPA", min_value=0, max_value=10, step=1)
    

    x[:, 1] = gender.transform(x[:, 1])
    x[:, 2] = stream.transform(x[:, 2])
    x[:, 5] = backlogs.transform(x[:, 5])
    x = x.astype(int)
    x = np.array([[ age,'gender', 'stream', internship, cgpa, 'backlogs']])
	

    #code for prediction
predict=''

    # Check if the button was clicked
if st.button("Test Result"):
        predict=placement_prediction(x)

st.success(predict)



if __name__=='__main__':
    main()
