import streamlit as st
import pandas as pd
import numpy as np
#import joblib
import requests
from keras.models import load_model



st.set_page_config(page_title="Patient Survival prediction",page_icon="🚧", layout="centered")
features=['ventilated_apache', 'gcs_motor_apache', 'gcs_verbal_apache',
       'gcs_eyes_apache', 'apache_4a_hospital_death_prob', 'albumin_apache',
       'apache_4a_icu_death_prob', 'd1_albumin_avg', 'd1_bun_avg',
       'bun_apache', 'intubated_apache', 'd1_spo2_avg', 'h1_inr_avg',
       'd1_inr_avg', 'd1_sysbp_avg', 'd1_sysbp_noninvasive_avg',
       'd1_arterial_ph_avg', 'age', 'h1_resprate_avg', 'd1_mbp_avg',
       'ethnicity_African American',
       'hospital_admit_source_Emergency Department', 'ethnicity_Other/Unknown',
       'hospital_admit_source_Direct Admit', 'ethnicity_Hispanic',
       'icu_type_SICU', 'icu_type_CTICU', 'icu_type_CCU-CTICU',
       'icu_type_MICU', 'icu_type_Cardiac ICU', 'hospital_admit_source_Floor',
       'hospital_admit_source_Acute Care/Floor', 'ethnicity_Asian',
       'icu_type_Neuro ICU', 'icu_stay_type_transfer',
       'ethnicity_Native American', 'hospital_admit_source_Other Hospital',
       'hospital_admit_source_Recovery Room']
options_ethinicity=['Caucasian','African American','Other/Unknown','Hispanic','Asian','Native American']  
options_hospital_admit_source=['Emergency Department','Operating Room','Floor','Direct Admit','Recovery Room','Acute Care/Floor','Other Hospital',	
'PACU','Step-Down Unit (SDU)','Other ICU','Chest Pain Center','ICU to SDU','ICU','Observation','Other']     
options_icu_type=['Med-Surg ICU','Neuro ICU','MICU','CCU-CTICU','SICU','CSICU','Cardiac ICU','CTICU']
st.markdown("<h1 style='text-align: center;'>Patient Survival prediction 🚧</h1>", unsafe_allow_html=True)
def main():
    with st.form('prediction_form'):

        st.subheader("Enter the input for following features:")

        ventilated_apache=st.number_input('Ventilated_apache')
        gcs_motor_apache=st.number_input('gcs_motor_apache')
        gcs_verbal_apache=st.number_input('gcs_verbal_apache')
        gcs_eyes_apache=st.number_input('gcs_eyes_apache')
        apache_4a_hospital_death_prob=st.number_input('apache_4a_hospital_death_prob')
        albumin_apache=st.number_input('albumin_apache')
        apache_4a_icu_death_prob=st.number_input('apache_4a_icu_death_prob')
        d1_albumin_avg=st.number_input('d1_albumin_avg')
        d1_bun_avg=st.number_input('d1_bun_avg')
        bun_apache=st.number_input('bun_apache')
        intubated_apache=st.number_input('intubated_apache')
        d1_spo2_avg=st.number_input('d1_spo2_avg')
        h1_inr_avg=st.number_input('h1_inr_avg')
        d1_inr_avg=st.number_input('d1_inr_avg')
        d1_sysbp_avg=st.number_input('d1_sysbp_avg')
        d1_sysbp_noninvasive_avg=st.number_input('d1_sysbp_noninvasive_avg')
        d1_arterial_ph_avg=st.number_input('d1_arterial_ph_avg')
        age=st.number_input('age')
        h1_resprate_avg=st.number_input('h1_resprate_avg')
        d1_mbp_avg=st.number_input('d1_mbp_avg')
        ethinicity=st.selectbox("Ethinicity",options=options_ethinicity)
        hospital_admit_source=st.selectbox("Hospital_admit_source",options=options_hospital_admit_source)
        icu_type=st.selectbox("ICU_Type",options=options_icu_type)

        submit = st.form_submit_button("Predict")

        if submit:
            #model=load_model(open(r'Model/keras_bestmodel.h5',"rb"))
            model=load_model(r'Model\keras_bestmodel.h5',"rb")
            st.write("hello")
            ethnicity_African_American,ethnicity_Other_Unknown,ethnicity_Asian,ethnicity_Native_American=0,0,0,0
            if ethinicity == 'African American':
                ethnicity_African_American =1
            elif ethinicity == 'ethnicity_Other/Unknown':    
                ethnicity_Other_Unknown =1
            elif ethinicity == 'ethnicity_Asian':
                ethnicity_Asian = 1
            else:
                ethnicity_Native_American=1

            hospital_admit_source_Emergency_Department=0
            hospital_admit_source_Direct_Admit=0
            hospital_admit_source_Floor=0
            hospital_admit_source_Acute_Care_Floor=0 
            hospital_admit_source_Other_Hospital=0
            hospital_admit_source_Recovery_Room =0

            if hospital_admit_source == 'hospital_admit_source_Emergency_Department':
               hospital_admit_source_Emergency_Department =1
            elif hospital_admit_source == 'hospital_admit_source_Direct_Admit':  
                hospital_admit_source_Direct_Admit =1 
            elif hospital_admit_source == 'hospital_admit_source_Floor':
                hospital_admit_source_Floor =1
            elif hospital_admit_source == 'hospital_admit_source_Acute_Care_Floor':
                hospital_admit_source_Acute_Care_Floor=1        
            elif  hospital_admit_source == 'hospital_admit_source_Other_Hospital':
                hospital_admit_source_Other_Hospital =1
            else :
                hospital_admit_source_Recovery_Room = 1
            
            icu_type_SICU=0
            icu_type_CTICU=0
            icu_type_CCU_CTICU=0
            icu_type_MICU=0
            icu_type_Cardiac_ICU=0
            icu_type_Neuro_ICU=0
            icu_stay_type_transfer=0

            if icu_type == 'icu_type_SICU':
                icu_type_SICU = 1
            elif icu_type == 'icu_type_CTICU':
                icu_type_CTICU =1
            elif icu_type == 'icu_type_CCU_CTICU':
                icu_type_CCU_CTICU=1
            elif  icu_type == 'icu_type_MICU':
                icu_type_MICU=1
            elif  icu_type == 'icu_type_Cardiac_ICU':
                icu_type_Cardiac_ICU=1
            elif icu_type == 'icu_type_Neuro_ICU':
                icu_type_Neuro_ICU=1
            else:
                icu_stay_type_transfer=1

            data=np.array(['ventilated_apache', 'gcs_motor_apache', 'gcs_verbal_apache','gcs_eyes_apache', 'apache_4a_hospital_death_prob', 'albumin_apache',
       'apache_4a_icu_death_prob', 'd1_albumin_avg', 'd1_bun_avg','bun_apache', 'intubated_apache', 'd1_spo2_avg', 'h1_inr_avg',
       'd1_inr_avg', 'd1_sysbp_avg', 'd1_sysbp_noninvasive_avg','d1_arterial_ph_avg', 'age', 'h1_resprate_avg', 'd1_mbp_avg','ethnicity_African_American',
       'hospital_admit_source_Emergency Department', 'ethnicity_Other_Unknown','hospital_admit_source_Direct_Admit', 'ethnicity_Hispanic',
       'icu_type_SICU', 'icu_type_CTICU', 'icu_type_CCU-CTICU','icu_type_MICU', 'icu_type_Cardiac_ICU', 'hospital_admit_source_Floor','hospital_admit_source_Acute_Care_Floor', 'ethnicity_Asian',
       'icu_type_Neuro_ICU', 'icu_stay_type_transfer','ethnicity_Native_American', 'hospital_admit_source_Other_Hospital','hospital_admit_source_Recovery_Room']).reshape(1,-1)
            
            
            st.write(data)
            pred=model.predict(data)
            if pred[0] == 0:
                result = 'Alive'
            else:
                result = 'Sorry,No hope'

            st.write(f"The predicted severity is: {result}")    

if __name__ == '__main__':
    main()
