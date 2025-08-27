# ai.py
from __future__ import annotations
from typing import List, Dict
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema.runnable import Runnable
from llm import get_llm  # ← uses the hard-coded key in llm.py

llm = get_llm(model="gpt-4o-mini", temperature=0.6)
csv_parser = CommaSeparatedListOutputParser()

name_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a branding expert. Return ONLY a comma-separated list. Generate distinct, brandable restaurant names (no quotes)."),
    ("human",
     "Cuisine: {cuisine}\nVibe/Tone: {tone}\nCount: {count}\n"
     "Constraints: short (1–3 words), easy to pronounce, avoid cliches.\n"
     "Return exactly {count} names, comma-separated.")
])

menu_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a chef and menu architect. Return ONLY a comma-separated list of signature menu items (no headings, no numbering)."),
    ("human",
     "Restaurant: {res_name}\nCuisine: {cuisine}\nCount: {count}\n"
     "Constraints: diverse courses, clear, concise. Return exactly {count} items.")
])

name_chain: Runnable = name_prompt | llm | csv_parser
menu_chain: Runnable = menu_prompt | llm | csv_parser

def suggest_restaurant_names(cuisine: str, tone: str = "Modern", count: int = 10) -> List[str]:
    return name_chain.invoke({"cuisine": cuisine, "tone": tone, "count": count})

def suggest_menu_for_name(res_name: str, cuisine: str, count: int = 12) -> List[str]:
    return menu_chain.invoke({"res_name": res_name, "cuisine": cuisine, "count": count})

def suggest_names_and_menus(
    cuisine: str,
    tone: str = "Modern",
    n_names: int = 8,
    n_menu_items: int = 12
) -> List[Dict[str, List[str]]]:
    names = suggest_restaurant_names(cuisine=cuisine, tone=tone, count=n_names)
    menus: List[List[str]] = menu_chain.batch(
        [{"res_name": n, "cuisine": cuisine, "count": n_menu_items} for n in names]
    )
    return [{"name": n, "menu": m} for n, m in zip(names, menus)]
