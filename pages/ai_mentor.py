"""
AI Mentor Page
"""

import streamlit as st

from services.ai_mentor_service import AIMentorService
from services.goal_service import GoalService
from services.progress_service import ProgressService
from services.recommendation_service import RecommendationService
from services.weakness_service import WeaknessService
from services.insight_service import InsightService

from models.mentor_models import MentorGoal
from models.mentor_models import MentorProgress


def ai_mentor_page():
    st.title("🎓 AI Mentor")

    tabs = st.tabs([
        "🏠 Dashboard",
        "🎯 Goals",
        "📈 Progress",
        "💡 Recommendations",
        "🔍 Weakness",
        "📊 Insights",
        "🤖 Mentor Chat",
    ])

    # ---------------------------------------------------
    # Dashboard
    # ---------------------------------------------------
    with tabs[0]:
        dashboard = AIMentorService.dashboard()

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("Goals", dashboard["goals"]["total"])

        with c2:
            st.metric("Completed", dashboard["goals"]["completed"])

        with c3:
            st.metric("Study Hours", round(dashboard["progress"]["total_hours"] or 0, 2))

        with c4:
            st.metric("Average Score", round(dashboard["progress"]["average_score"] or 0, 2))

        st.divider()

        st.subheader("Latest Insights")

        st.dataframe(dashboard["insights"], use_container_width=True)

    # ---------------------------------------------------
    # Goals
    # ---------------------------------------------------
    with tabs[1]:
        st.subheader("Create Goal")

        title = st.text_input("Goal Title")

        description = st.text_area("Description")

        category = st.text_input("Category")

        target = st.number_input("Target", 1, 10000, 100)

        priority = st.selectbox("Priority", ["Low", "Medium", "High"])

        due = st.date_input("Due Date")

        if st.button("Save Goal"):
            goal = MentorGoal(
                title=title,
                description=description,
                category=category,
                target_value=target,
                priority=priority,
                due_date=due,
            )

            GoalService.create(goal)

            st.success("Goal Created")

        st.divider()

        st.dataframe(GoalService.get_all(), use_container_width=True)

    # ---------------------------------------------------
    # Progress
    # ---------------------------------------------------
    with tabs[2]:
        st.subheader("Study Progress")

        hours = st.number_input("Study Hours", 0.0, 24.0, 1.0)

        quizzes = st.number_input("Quizzes", 0, 100, 0)

        flashcards = st.number_input("Flashcards", 0, 1000, 0)

        notes = st.number_input("Notes", 0, 1000, 0)

        coding = st.number_input("Coding Sessions", 0, 100, 0)

        rag = st.number_input("RAG Queries", 0, 1000, 0)

        score = st.slider("Score", 0, 100, 75)

        remarks = st.text_area("Remarks")

        if st.button("Save Progress"):
            progress = MentorProgress(
                study_date=st.session_state.get("today"),
                study_hours=hours,
                quizzes_completed=quizzes,
                flashcards_completed=flashcards,
                notes_created=notes,
                coding_sessions=coding,
                rag_queries=rag,
                score=score,
                remarks=remarks,
            )

            ProgressService.create(progress)

            st.success("Progress Saved")

        st.divider()

        st.dataframe(ProgressService.get_all(), use_container_width=True)

    # ---------------------------------------------------
    # Recommendations
    # ---------------------------------------------------
    with tabs[3]:
        if st.button("Generate Recommendations"):
            RecommendationService.save_generated()

        st.dataframe(RecommendationService.get_all(), use_container_width=True)

    # ---------------------------------------------------
    # Weakness
    # ---------------------------------------------------
    with tabs[4]:
        weakness = WeaknessService.summary()

        st.metric("Weak Areas", weakness["total"])

        st.dataframe(weakness["items"], use_container_width=True)

    # ---------------------------------------------------
    # Insights
    # ---------------------------------------------------
    with tabs[5]:
        if st.button("Generate Insights"):
            InsightService.save()

        st.dataframe(InsightService.get_all(), use_container_width=True)

    # ---------------------------------------------------
    # AI Mentor Chat
    # ---------------------------------------------------
    with tabs[6]:
        model = st.text_input("Model", "qwen2.5:1.5b")

        question = st.text_area("Ask AI Mentor")

        if st.button("Ask Mentor"):
            result = AIMentorService.mentor_chat(question, model)

            st.success(result["answer"])

            c1, c2 = st.columns(2)

            c1.metric("Response Time", f"{result['response_time']:.2f}s")

            c2.metric("Tokens", result["token_usage"])