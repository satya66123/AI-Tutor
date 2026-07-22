"""
AI Tutor
Main Application
"""

import streamlit as st

from pages.ai_mentor import ai_mentor_page
from pages.interview_preparation import interview_preparation_page
from pages.voice.voice_page import VoicePage

from pages.about.about_page import AboutPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.home import HomePage
from pages.planner.planner_page import PlannerPage
from pages.quiz.quiz_page import QuizPage
from pages.settings.settings_page import SettingsPage
from pages.tutor.tutor_page import TutorPage
from pages.flashcards.flashcards_page import render as flashcards_page
from pages.pdf_tutor.pdf_page import PDFPage
from pages.coding_tutor.coding_page import CodingPage
from pages.revision_planner.reviuson_planner_page import RevisionPlannerPage
from pages.analytics.analytics_page import AnalyticsPage
from pages.learning_history.history_page import HistoryPage
from pages.rag.rag_page import RAGPage

from ui.header import Header
from ui.sidebar import Sidebar
from ui.footer import Footer
from pages.notes.notes_page import render as notes_page


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

    "📚 Enterprise RAG",

    "🎙 Voice AI Tutor",

    "📚 Study Planner",

    "📝 Quiz Generator",

    "🃏 Flashcards",

    "📝 Notes Generator",

    "📄 PDF Tutor",

    "💻 Coding Tutor",

    "📅 Revision Planner",

    "📈 Learning Analytics",

    "📚 Learning History",

    "🎓 AI Mentor",                  # NEW

    "🎤 Interview Preparation",      # NEW

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


PAGES = {

    "📊 Dashboard": lambda: DashboardPage.render(),

    "🏠 Home": lambda: HomePage.render(),

    "🎓 AI Tutor": lambda: TutorPage.render(model),

    "📚 Enterprise RAG": lambda: RAGPage.render(),

    "🎙 Voice AI Tutor": lambda: VoicePage.render(),

    "📚 Study Planner": lambda: PlannerPage.render(model),

    "📝 Quiz Generator": lambda: QuizPage.render(),

    "🃏 Flashcards": flashcards_page,

    "📝 Notes Generator": notes_page,

    "📄 PDF Tutor": lambda: PDFPage.render(),

    "💻 Coding Tutor": lambda: CodingPage.render(),

    "📅 Revision Planner": lambda: RevisionPlannerPage.render(),

    "📈 Learning Analytics": lambda: AnalyticsPage.render(),

    "📚 Learning History": lambda: HistoryPage.render(),

    # -------------------------------
    # Batch 15
    # -------------------------------

    "🎓 AI Mentor": ai_mentor_page,

    # -------------------------------
    # Batch 16
    # -------------------------------

    "🎤 Interview Preparation": interview_preparation_page,

    "⚙ Settings": lambda: SettingsPage.render(),

    "ℹ About": lambda: AboutPage.render()

}

PAGES[page]()

# ---------------------------------------------------
# Sidebar Statistics
# ---------------------------------------------------



# ---------------------------------------------------
# Footer
# ---------------------------------------------------

Footer.render()