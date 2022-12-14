import pickle
import streamlit as st

# membaca model
loan_model = pickle.load(open('loan.sav', 'rb'))
st.title("Loan approval")

col1, col2 = st.columns(2)
with col1:
    Income = st.text_input("Income")
    Age = st.number_input("Age")
    Experience = st.number_input("experience in years")
    Married_Single = st.selectbox("Status",['married','single'])

with col2:
    House_Ownership = st.selectbox("House ownership",['rented','owned'])
    Car_Ownership = st.selectbox("Have a car",['yes','no'])
    CURRENT_JOB_YRS = st.number_input("years experiance in current job")
    CURRENT_HOUSE_YRS = st.number_input("Years in current house")

LoanApproval = ''

Married_Single = 0 if Married_Single == "single" else 1
House_Ownership = 0 if Married_Single == "rented" else 1
Car_Ownership = 0 if Car_Ownership == "no" else 1

if st.button("Check approval !"):
    loan_predict = loan_model.predict([[
        Income,Age,Experience,Married_Single,House_Ownership,Car_Ownership,CURRENT_JOB_YRS,CURRENT_HOUSE_YRS
        ]])

    if(loan_predict[0] == 1):
        LoanApproval = "Congratulation, Your loan is approved !"
    else:
        LoanApproval = "We are sorry, Your approval was not approved !"

    st.success(LoanApproval)