"""
AI Tutor
Main Application
"""

import streamlit as st

from pages.about.about_page import AboutPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.home import HomePage
from pages.planner.planner_page import PlannerPage
from pages.quiz.quiz_page import QuizPage
from pages.settings.settings_page import SettingsPage
from pages.tutor.tutor_page import TutorPage
from pages.tutor.stats import ChatStats
from pages.flashcards.flashcards_page import render as flashcards_page

from ui.header import Header
from ui.sidebar import Sidebar
from ui.footer import Footer


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------
# Header
# ---------------------------------------------------

Header.render()


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

provider, model = Sidebar.render()

st.session_state["provider"] = provider
st.session_state["model"] = model

if "page" not in st.session_state:
    st.session_state.page = "📊 Dashboard"


# ---------------------------------------------------
# Navigation
# ---------------------------------------------------

pages = [

    "📊 Dashboard",

    "🏠 Home",

    "🎓 AI Tutor",

    "📚 Study Planner",

    "📝 Quiz Generator",

    "📚 Flashcards",


    "⚙ Settings",

    "ℹ About"
]

page = st.sidebar.radio(
    "📚 Navigation",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = page




# ---------------------------------------------------
# Pages
# ---------------------------------------------------


if page == "📊 Dashboard":

    DashboardPage.render()

elif page == "🏠 Home":

    HomePage.render()

elif page == "🎓 AI Tutor":

    TutorPage.render(model)

elif page == "📚 Study Planner":

    PlannerPage.render(model)

elif page == "⚙ Settings":

    SettingsPage.render()

elif page == "ℹ About":

    AboutPage.render()

elif page == "📝 Quiz Generator":

    QuizPage.render()

elif page == "📚 Flashcards":
    flashcards_page()

# ---------------------------------------------------
# Sidebar Statistics
# ---------------------------------------------------

ChatStats.render()


# ---------------------------------------------------
# Footer
# ---------------------------------------------------

Footer.render()