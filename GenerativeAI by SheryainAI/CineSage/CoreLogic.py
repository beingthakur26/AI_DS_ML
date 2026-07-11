from dotenv import load_dotenv
from typing import List, Optional

from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

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
# User Choice
# -------------------------
print("\nSelect Extraction Mode")
print("1. Single Movie")
print("2. Multiple Movies")

choice = input("\nEnter your choice (1/2): ").strip()

paragraph = input("\nGive your paragraph:\n\n")

# -------------------------
# Single Movie Extraction
# -------------------------
if choice == "1":

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
response = model.invoke(final_prompt)

# -------------------------
# Parse Output
# -------------------------
movie_data = parser.parse(response.content)

# -------------------------
# Print Result
# -------------------------
print("\n========== Extracted Data ==========\n")
print(movie_data)