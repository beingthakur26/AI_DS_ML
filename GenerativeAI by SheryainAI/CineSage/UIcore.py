import streamlit as st
from dotenv import load_dotenv
from typing import List, Optional

from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="🎬 CineSage",
    page_icon="🎥",
    layout="centered"
)

# -------------------------
# Load Environment
# -------------------------
load_dotenv()

# -------------------------
# Load Model
# -------------------------
model = ChatMistralAI(
    model="mistral-small-2506"
)

# -------------------------
# Pydantic Models
# -------------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str


class MovieCollection(BaseModel):
    movies: List[Movie]


# -------------------------
# UI
# -------------------------
st.title("🎬 CineSage")
st.caption("Extract structured movie information from any paragraph using AI.")

choice = st.radio(
    "Select Extraction Mode",
    ["Single Movie", "Multiple Movies"]
)

paragraph = st.text_area(
    "Enter Paragraph",
    height=220,
    placeholder="Paste a movie paragraph here..."
)

# -------------------------
# Button
# -------------------------
if st.button("Extract Movie Information", use_container_width=True):

    if not paragraph.strip():
        st.warning("Please enter a paragraph.")
        st.stop()

    # -------------------------
    # Single Movie Extraction
    # -------------------------
    if choice == "Single Movie":

        parser = PydanticOutputParser(
            pydantic_object=Movie
        )

        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
You are an expert movie information extractor.

Extract ONLY the primary movie discussed in the paragraph.

If multiple movies are mentioned, choose the most important/main movie.

Do not invent information.

{format_instructions}
"""
            ),
            ("human", "{paragraph}")
        ])

    # -------------------------
    # Multiple Movie Extraction
    # -------------------------
    else:

        parser = PydanticOutputParser(
            pydantic_object=MovieCollection
        )

        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
You are an expert movie information extractor.

Extract EVERY movie mentioned in the paragraph.

Do not invent information.

{format_instructions}
"""
            ),
            ("human", "{paragraph}")
        ])

    # -------------------------
    # Build Prompt
    # -------------------------
    final_prompt = prompt.invoke(
        {
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        }
    )

    # -------------------------
    # Model Response
    # -------------------------
    with st.spinner("Extracting..."):
        response = model.invoke(final_prompt)
        movie_data = parser.parse(response.content)

    # -------------------------
    # Output
    # -------------------------
    st.success("Extraction Complete!")

    st.subheader("Structured Output")
    st.json(movie_data.model_dump())

    with st.expander("Raw Pydantic Output"):
        st.write(movie_data)
        