import streamlit as st
import requests

st.title("AI Gym Trainer")
st.write("Generate your custom hypertrophy and nutrition plan!")

# 1. User Inputs
age = st.text_input("Age", "22")
weight = st.text_input("Weight", "75kg")
goal = st.text_input("Goal", "Maximize chest and back hypertrophy")
equipment = st.text_input("Equipment", "Dumbbells, cables, leg press machine")

if st.button("Generate Plan"):
    with st.spinner("Consulting the AI and FAISS database..."):
        
        # 2. Setup the connection to your Kaggle API
        URL = "https://outing-kindness-iodine.ngrok-free.dev/generate"
        headers = {"Authorization": "Bearer secret123"}
        payload = {
            "age": age,
            "weight": weight,
            "goal": goal,
            "equipment": equipment
        }
        
        try:
            # 3. Send the POST request (Adapted from NGROK_Send_Prompt_Local.ipynb)
            res = requests.post(URL, headers=headers, json=payload)
            
            if res.status_code == 200:
                # The backend returns the parsed JSON dictionary
                answer = res.json()["response"]
                
                if answer:
                    st.success("Plan Generated Successfully!")
                    
                    # 4. Render the JSON cleanly on the dashboard
                    st.subheader("🎯 Target Muscles")
                    st.write(answer.get("target_muscle_groups", ""))
                    
                    st.subheader("📅 Weekly Split")
                    st.write(answer.get("weekly_split", ""))
                    
                    st.subheader("🏋️ Exercises")
                    st.text(answer.get("exercises", ""))
                    
                    st.subheader("🧘 Form Cues")
                    st.text(answer.get("form_cues", ""))
                    
                    st.subheader("🍎 Nutrition")
                    st.text(answer.get("nutrition", ""))
                else:
                    st.error("Failed to parse the JSON on the backend.")
            else:
                st.error(f"Authentication or Server Error: {res.status_code}")
                
        except Exception as e:
            st.error(f"Connection Failed. Is your Kaggle notebook still running? Error: {e}")