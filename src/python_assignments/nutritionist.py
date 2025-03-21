import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key Securely
load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# Ensure API key is set
if not GOOGLE_API_KEY:
    st.error("API Key is missing! Set GOOGLE_API_KEY in environment variables or .env file.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# Streamlit UI with Sidebar
st.sidebar.title("⚙️ User Settings")

# User Inputs in Sidebar
st.sidebar.header("🔢 Enter Your Details")
height = st.sidebar.slider("Height (cm)", 100, 250, 175)
weight = st.sidebar.slider("Weight (kg)", 40, 200, 70)
age = st.sidebar.number_input("Age", min_value=5, max_value=100, value=25)
gender = st.sidebar.radio("Gender", ["Male", "Female", "Other"])
goal = st.sidebar.selectbox("🎯 Select Your Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
diet_type = st.sidebar.selectbox("🍽️ Choose Your Diet Type", ["Vegan", "Keto", "Balanced", "High Protein"])

# BMI Calculation
bmi = weight / ((height / 100) ** 2)
st.sidebar.write(f"### Your BMI: **{bmi:.2f}**")

# Initialize session state for history and responses
if "history" not in st.session_state:
    st.session_state.history = []
if "diet_plan" not in st.session_state:
    st.session_state.diet_plan = ""
if "workout_plan" not in st.session_state:
    st.session_state.workout_plan = ""
if "recipes" not in st.session_state:
    st.session_state.recipes = ""
if "full_plan" not in st.session_state:
    st.session_state.full_plan = ""

# Function to Get AI Responses
def get_ai_response(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")  
    response = model.generate_content([prompt])  # Use list format
    return response.text

# Function to Get AI Diet Plan
def get_diet_plan():
    prompt = f"""
    I am a {age}-year-old {gender} with a height of {height} cm and weight of {weight} kg.
    My BMI is {bmi:.2f} and my goal is {goal}.
    Suggest a detailed diet plan for me including breakfast, lunch, dinner, and snacks.
    """
    return get_ai_response(prompt)

# Function to Get AI Workout Plan
def get_workout_plan():
    prompt = f"I have a BMI of {bmi:.2f} and my goal is {goal}. Suggest a 7-day workout plan."
    return get_ai_response(prompt)

# Function to Get AI Recipes
def get_recipes():
    prompt = f"Suggest 3 healthy {diet_type} recipes with ingredients and preparation steps."
    return get_ai_response(prompt)

# Main UI Section
st.title("🔥 NutriPal 🥦💬 – Your AI Nutritionist Friend")
st.write("Welcome to NutriPal 🥦💬 – your AI health buddy! Ask me about diet plans, workouts, or healthy recipes. Let’s get fit together! 🚀")

# Tabs for Different Features
tab1, tab2, tab3 = st.tabs(["🏥 Health Plans", "💬 AI Chatbot", "📊 BMI Info"])

# 🏥 Health Plans Tab
with tab1:
    st.header("📌 Personalized Health Plans")

    # Create Columns for Buttons (4 columns for side-by-side layout)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🥗 Diet Plan"):
            st.session_state.diet_plan = get_diet_plan()
            st.session_state.history.insert(0,("Diet Plan", st.session_state.diet_plan))

    with col2:
        if st.button("🏋️ Workout Plan"):
            st.session_state.workout_plan = get_workout_plan()
            st.session_state.history.insert(0,("Workout Plan", st.session_state.workout_plan))

    with col3:
        if st.button("🍲 Recipes"):
            st.session_state.recipes = get_recipes()
            st.session_state.history.insert(0,("Recipes", st.session_state.recipes))

    with col4:
        if st.button("🚀 Full Plan"):
            diet = get_diet_plan()
            workout = get_workout_plan()
            st.session_state.full_plan = f"### 🥗 Personalized Diet Plan\n{diet}\n\n### 🏋️ Customized Workout Plan\n{workout}"
            st.session_state.history.insert(0,("Complete Health Plan", st.session_state.full_plan))

    # **Now Display Responses Below the Buttons in Full Width**
    if st.session_state.diet_plan:
        st.write("## 🥗 AI-Powered Diet Plan")
        st.write(st.session_state.diet_plan)

    if st.session_state.workout_plan:
        st.write("## 🏃‍♂️ AI-Powered Workout Plan")
        st.write(st.session_state.workout_plan)

    if st.session_state.recipes:
        st.write("## 🍛 AI-Generated Healthy Recipes")
        st.write(st.session_state.recipes)

    if st.session_state.full_plan:
        st.write("## 🔥 Your AI-Powered Health Plan")
        st.write(st.session_state.full_plan)


# 💬 AI Chatbot Tab (Strictly Health & Nutrition Only)
with tab2:
    st.header("💬 NutriPal - AI Health Coach (Health & Nutrition Only)")

    # Keep input field always on top
    user_input = st.chat_input("Ask your AI Health Coach about diet, fitness, or nutrition...")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if user_input:
        # Add user message to history at the top
        st.session_state.messages.insert(0, {"role": "user", "content": user_input})

        # AI Prompt (Strict Instructions)
        ai_prompt = f"""
        You are NutriPal 🥦💬, an AI Health & Nutrition Coach.

        🚨 **IMPORTANT RULES** 🚨  
        - ONLY answer questions related to **health, nutrition, fitness, or diet**.  
        - If the user's question is about **politics, technology, coding, sports, entertainment, history**, or anything **not related to health**, then **DO NOT ANSWER**.  
        - Instead, reply with: **"I'm here to help with health, diet, and nutrition only. Please ask me something related to these topics. 😊"**  

        User's Question: "{user_input}"
        """

        # Get AI response
        ai_response = get_ai_response(ai_prompt)

        # Add response to history
        st.session_state.messages.insert(1, {"role": "assistant", "content": ai_response})

    # Display chat history (Newest messages first)
    for i in range(0, len(st.session_state.messages), 2):
        if i < len(st.session_state.messages):
            with st.chat_message(st.session_state.messages[i]["role"]):
                st.markdown(st.session_state.messages[i]["content"])

        if i + 1 < len(st.session_state.messages):
            with st.chat_message(st.session_state.messages[i + 1]["role"]):
                st.markdown(st.session_state.messages[i + 1]["content"])



# 📊 BMI Info Tab
with tab3:
    st.header("📊 BMI Categories")
    st.write("- **Underweight** : BMI less than 18.5")
    st.write("- **Normal weight** : BMI between 18.5 and 24.9")
    st.write("- **Overweight** : BMI between 25 and 29.9")
    st.write("- **Obesity** : BMI 30 or greater")

