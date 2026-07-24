"""
AI Tutor
Main Application
"""

import streamlit as st

from automation.ui.workflow_designer.workflow_designer_page import WorkflowDesignerPage
from automation.ui.workflow_designer.workflow_history_page import WorkflowHistoryPage
from pages.ai_mentor import ai_mentor_page
from pages.interview_preparation import interview_preparation_page
from pages.rag.rag_page import RAGPage
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
from ui.header import Header

#from ui.header import Header
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
# Session State Initialization
# ---------------------------------------------------

DEFAULTS = {
    "provider": None,
    "model": None,
    "page": "📊 Dashboard"
}

for key, value in DEFAULTS.items():
    st.session_state.setdefault(key, value)


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

# Initialize app only once
if "initialized" not in st.session_state:
    st.session_state["initialized"] = True

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

    "⚙️ Workflow Designer",

   "📜 Workflow History",

    "⚙ Settings",

    "ℹ About"

]

page = st.sidebar.radio(
    "📚 Navigation",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = page

st.sidebar.markdown("---")
st.sidebar.caption("Enterprise AI Tutor")
st.sidebar.caption("Version: v1.1.0")


st.set_page_config(
    page_title="Enterprise AI Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


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


    "⚙️ Workflow Designer": lambda: WorkflowDesignerPage.render(),

    "📜 Workflow History": lambda: WorkflowHistoryPage.render(),


    "⚙ Settings": lambda: SettingsPage.render(),

    "ℹ About": lambda: AboutPage.render()

}

try:
    if page in PAGES:
        PAGES[page]()
    else:
        st.error("Page not found.")
except Exception as e:
    st.exception(e)

# ---------------------------------------------------
# Sidebar Statistics
# ---------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.info(
    f"**Provider:** {provider}\n\n"
    f"**Model:** {model}"
)


# ---------------------------------------------------
# Footer
# ---------------------------------------------------

Footer.render()