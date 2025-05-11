import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Load Gemini API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Load Gemini model via LangChain
@st.cache_resource
def load_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-04-17",
        temperature=0.7 
    )

# Function to call Gemini Pro and get text response
def get_gemini_pro_text_response(model, prompt, temperature):
    model.temperature = temperature
    response = model.invoke(prompt)
    return response.content

# Streamlit app
st.header("Story Generator", divider="rainbow")
st.subheader("with Gemini API and LangChain")
st.write("(Developer Jahanzeb)")
text_model_pro = load_model()

st.subheader("Generate a story")

# Collect user inputs without defaults
character_name = st.text_input("Enter character name:", placeholder="e.g., Mittens")
character_type = st.text_input("What type of character is it?", placeholder="e.g., Cat")
character_persona = st.text_input("What personality does the character have?", placeholder="e.g., Very friendly and curious.")
character_location = st.text_input("Where does the character live?", placeholder="e.g., Andromeda Galaxy")

length_of_story = st.radio("Select the length of the story:", ["Short", "Long"], horizontal=True)
story_premise = st.multiselect(
    "What is the story premise? (you must select at least one)", 
    ["Love", "Adventure", "Mystery", "Horror", "Comedy", "Sci-Fi", "Fantasy", "Thriller"]
)
creative_control = st.radio("Select the creativity level:", ["Low", "High"], horizontal=True)

temperature = 0.30 if creative_control == "Low" else 0.95

# Story generation logic
if st.button("Generate my story"):
    try:
        # Validate inputs
        if not character_name.strip():
            raise ValueError("Character name is required.")
        if not character_type.strip():
            raise ValueError("Character type is required.")
        if not character_persona.strip():
            raise ValueError("Character personality is required.")
        if not character_location.strip():
            raise ValueError("Character location is required.")
        if not story_premise:
            raise ValueError("Please select at least one story premise.")

        # Create prompt
        prompt = f"""Write a {length_of_story} story based on the following premise:\n
        character_name: {character_name}\n
        character_type: {character_type}\n
        character_persona: {character_persona}\n
        character_location: {character_location}\n
        story_premise: {', '.join(story_premise)}\n
        If the story is \"short\", then make sure to have 5 chapters or else if it is \"long\" then 10 chapters.
        Important point is that each chapter should be generated based on the premise given above.
        First start by giving the book introduction, chapter introductions and then each chapter. It should also have a proper ending.
        The book should have a prologue and an epilogue."""

        with st.spinner("Generating your story..."):
            story_response = get_gemini_pro_text_response(text_model_pro, prompt, temperature)
            st.subheader("Your Story")
            st.write(story_response)

            st.download_button(
                label="Download Story as TXT File",
                data=story_response,
                file_name=f"{character_name}_story.txt",
                mime="text/plain"
            )

    except ValueError as ve:
        st.error(str(ve))
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
