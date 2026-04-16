import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="OPENAI_API_Keys")

st.title("AI Healthcare Assistant")

# Input box
symptoms = st.text_input("Enter your symptoms:")

# Button
if st.button("Analyze"):
    
    # Simple severity logic
    def get_severity(symptoms):
        symptoms = symptoms.lower()
        if "chest pain" in symptoms or "breathing difficulty" in symptoms:
            return "High"
        elif "fever" in symptoms or "body pain" in symptoms:
            return "Medium"
        else:
            return "Low"

    severity = get_severity(symptoms)

    prompt = f"""
    You are an AI healthcare assistant.

    The system has already predicted severity as: {severity}

    Provide:
    - Possible Conditions
    - Severity Level
    - Recommended Actions
    - When to See a Doctor

    Symptoms: {symptoms}

    Add disclaimer: This is not medical advice.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    result = response.choices[0].message.content

    st.write(f"### Predicted Severity: {severity}")
    st.write(result)
