"""
Enterprise AI Tutor
Interview Preparation Page
"""

import pandas as pd
import streamlit as st

from models.interview_models import InterviewQuestion
from services.interview_question_service import InterviewQuestionService
from services.interview_service import InterviewService
from services.interview_evaluation_service import InterviewEvaluationService
from services.interview_report_service import InterviewReportService
from services.interview_history_service import InterviewHistoryService

DEFAULT_SESSION = {
    "interview_started": False,
    "interview_completed": False,
    "current_question": 0,
    "answers": {},
    "session_id": None,
    "questions": [],
    "evaluation": None,
    "report": None,
}


def interview_preparation_page():
    st.title("🎤 AI Interview Preparation")

    for k, v in DEFAULT_SESSION.items():
        st.session_state.setdefault(k, v)

    tabs = st.tabs([
        "Dashboard",
        "Question Bank",
        "Start Interview",
        "Live Interview",
        "Evaluation",
        "Reports",
        "History",
        "Analytics",
    ])

    # ---------------------------------------------------
    # Dashboard
    # ---------------------------------------------------
    with tabs[0]:
        st.header("Dashboard")
        stats = InterviewHistoryService.statistics() or {}
        st.write(stats)

    # ---------------------------------------------------
    # Question Bank
    # ---------------------------------------------------
    with tabs[1]:
        st.header("Question Bank")

        with st.form("add"):
            category = st.selectbox("Category", ["Technical", "Coding", "HR"])
            difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
            question = st.text_area("Question")
            answer = st.text_area("Expected Answer")
            tags = st.text_input("Tags")

            if st.form_submit_button("Add"):
                InterviewQuestionService.create(
                    InterviewQuestion(
                        category=category,
                        difficulty=difficulty,
                        question=question,
                        answer=answer,
                        tags=tags,
                    )
                )
                st.success("Added")

        data = InterviewQuestionService.get_all()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    # ---------------------------------------------------
    # Start Interview
    # ---------------------------------------------------
    with tabs[2]:
        st.header("🎤 Start Interview")
        st.write("Configure and start an AI interview session.")
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            interview_type = st.selectbox(
                "Interview Type",
                ["Technical", "Coding", "HR"],
                key="start_type",
            )

        with col2:
            start_difficulty = st.selectbox(
                "Difficulty",
                ["Easy", "Medium", "Hard"],
                key="start_difficulty",
            )

        total_questions = st.slider(
            "Number of Questions",
            min_value=5,
            max_value=20,
            value=10,
            step=1,
            key="start_total",
        )

        provider = st.session_state.get("provider", "Ollama")
        model = st.session_state.get("model", "qwen2.5:1.5b")

        st.info(f"Provider : {provider}\n\nModel : {model}")

        st.divider()

        if st.button("🚀 Start Interview", use_container_width=True):
            try:
                session = InterviewService.start_session(
                    interview_type=interview_type,
                    provider=provider,
                    model=model,
                    difficulty=start_difficulty,
                    total_questions=total_questions,
                )
                st.session_state.interview_started = True
                st.session_state.interview_completed = False
                st.session_state.session_id = session["session_id"]
                st.session_state.questions = session["questions"]
                st.session_state.answers = {}
                st.session_state.current_question = 0
                st.success("Interview Started Successfully")
            except Exception as e:
                st.error(str(e))

        if st.session_state.interview_started:
            st.success("Current Session")
            st.write("Session ID :", st.session_state.session_id)
            st.write("Interview Type :", interview_type)
            st.write("Difficulty :", start_difficulty)
            st.write("Questions :", len(st.session_state.questions))

            progress = 0
            if len(st.session_state.questions) > 0:
                progress = st.session_state.current_question / len(st.session_state.questions)

            st.progress(progress)

            st.write(
                f"Current Question : "
                f"{st.session_state.current_question + 1}/"
                f"{len(st.session_state.questions)}"
            )

    # ---------------------------------------------------
    # Live Interview
    # ---------------------------------------------------
    with tabs[3]:
        st.header("💬 Live Interview")

        if not st.session_state.interview_started:
            st.info("Start an interview first.")
        else:
            questions = st.session_state.questions
            total = len(questions)
            current = st.session_state.current_question

            if total == 0:
                st.warning("No questions found.")
            else:
                question = questions[current]

                st.progress((current + 1) / total)
                st.write(f"Question {current + 1} of {total}")
                st.divider()
                st.subheader(question["question"])

                previous_answer = st.session_state.answers.get(current, "")
                answer = st.text_area(
                    "Your Answer",
                    value=previous_answer,
                    height=220,
                    key=f"answer_{current}",
                )
                st.session_state.answers[current] = answer

                st.divider()

                c1, c2, c3, c4 = st.columns(4)

                with c1:
                    if st.button("⬅ Previous", disabled=current == 0, use_container_width=True):
                        st.session_state.current_question -= 1
                        st.rerun()

                with c2:
                    if st.button("💾 Save", use_container_width=True):
                        st.session_state.answers[current] = answer
                        st.success("Answer Saved")

                with c3:
                    if st.button("Next ➡", disabled=current == total - 1, use_container_width=True):
                        st.session_state.answers[current] = answer
                        st.session_state.current_question += 1
                        st.rerun()

                with c4:
                    if st.button("Skip", use_container_width=True):
                        st.session_state.answers[current] = ""
                        if current < total - 1:
                            st.session_state.current_question += 1
                        st.rerun()

                st.divider()

                # Evaluate current answer
                if st.button("🤖 Evaluate Current Answer", use_container_width=True):
                    if answer.strip() == "":
                        st.warning("Please answer the question.")
                    else:
                        result = InterviewService.evaluate_answer(
                            session_id=st.session_state.session_id,
                            question=question["question"],
                            expected_answer=question["answer"],
                            user_answer=answer,
                            provider=st.session_state.get("provider", "Ollama"),
                            model=st.session_state.get("model", "qwen2.5:1.5b"),
                        )
                        st.success(f"Score : {result['score']}/10")
                        st.write(result["feedback"])
                        st.caption(f"Response Time : {result['response_time']} sec")
                        st.caption(f"Tokens : {result['token_usage']}")

                st.divider()

                # Finish interview
                if st.button("🏁 Finish Interview", use_container_width=True):
                    InterviewService.finish_session(st.session_state.session_id)
                    st.session_state.interview_completed = True
                    st.session_state.interview_started = False
                    st.success("Interview Completed")
                    st.info("Go to the Evaluation tab to view your results.")

    # ---------------------------------------------------
    # Evaluation
    # ---------------------------------------------------
    with tabs[4]:
        st.header("📊 Interview Evaluation")

        if not st.session_state.interview_completed:
            st.info("Complete an interview to view evaluation.")
        else:
            session_id = st.session_state.session_id
            summary = InterviewEvaluationService.summary(session_id)

            st.subheader("Overall Performance")

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric("Overall Score", f"{summary['overall_score']}/10")

            with c2:
                st.metric("Performance", summary["performance"])

            with c3:
                st.metric("Highest", summary["highest_score"])

            with c4:
                st.metric("Lowest", summary["lowest_score"])

            st.divider()

            # Strengths
            st.subheader("💪 Strengths")
            strengths = summary["strengths"]

            if strengths:
                for item in strengths:
                    with st.expander(f"⭐ Score : {item['score']}/10"):
                        st.write(item["question"])
            else:
                st.info("No strengths identified.")

            st.divider()

            # Weaknesses
            st.subheader("⚠ Weaknesses")
            weaknesses = summary["weaknesses"]

            if weaknesses:
                for item in weaknesses:
                    with st.expander(f"Score : {item['score']}/10"):
                        st.write(item["question"])
            else:
                st.success("No major weaknesses.")

            st.divider()

            # Question-wise evaluation
            st.subheader("Question-wise Evaluation")
            answers = InterviewEvaluationService.get_answers(session_id)

            if answers:
                df = pd.DataFrame(answers)
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.warning("No evaluation records.")

            st.divider()

            # AI suggestions
            st.subheader("AI Suggestions")
            score = summary["overall_score"]

            if score >= 9:
                st.success("Excellent interview performance.")
                st.write("- Continue practicing advanced problems.")
                st.write("- Prepare for system design.")
                st.write("- Focus on communication.")
            elif score >= 8:
                st.info("Very good performance.")
                st.write("- Improve confidence.")
                st.write("- Practice mock interviews.")
                st.write("- Solve additional coding questions.")
            elif score >= 6:
                st.warning("Average performance.")
                st.write("- Strengthen fundamentals.")
                st.write("- Review incorrect answers.")
                st.write("- Practice daily.")
            else:
                st.error("Needs significant improvement.")
                st.write("- Revise core concepts.")
                st.write("- Take beginner mock interviews.")
                st.write("- Build confidence with practice.")

            st.divider()

            # Generate report
            if st.button("📄 Generate Interview Report", use_container_width=True):
                report = InterviewReportService.save(session_id)
                st.session_state.report = report
                st.success("Interview Report Generated.")
                st.json(report)

    # ---------------------------------------------------
    # Reports
    # ---------------------------------------------------
    with tabs[5]:
        st.header("📄 Interview Reports")

        reports = InterviewReportService.get_all()

        if not reports:
            st.info("No interview reports available.")
        else:
            df = pd.DataFrame(reports)
            st.dataframe(df, use_container_width=True, hide_index=True)

            st.divider()

            # View report
            report_ids = [report["id"] for report in reports]
            selected_report = st.selectbox("Select Report", report_ids, key="report_view")

            report = next((r for r in reports if r["id"] == selected_report), None)

            if report:
                st.subheader("Interview Report")

                c1, c2 = st.columns(2)

                with c1:
                    st.metric("Overall Score", report["overall_score"])

                with c2:
                    st.metric("Session", report["session_id"])

                st.divider()

                st.subheader("Strengths")
                st.text(report["strengths"])

                st.divider()

                st.subheader("Weaknesses")
                st.text(report["weaknesses"])

                st.divider()

                st.subheader("Recommendations")
                st.text(report["recommendations"])

            st.divider()

            # Download report
            if report:
                markdown = f"""
# Interview Report

## Session

{report['session_id']}

## Overall Score

{report['overall_score']}

## Strengths

{report['strengths']}

## Weaknesses

{report['weaknesses']}

## Recommendations

{report['recommendations']}
"""
                st.download_button(
                    "⬇ Download Markdown",
                    markdown,
                    file_name=f"report_{selected_report}.md",
                    mime="text/markdown",
                )

            st.divider()

            # Delete report
            if st.button("🗑 Delete Report", use_container_width=True):
                InterviewReportService.delete(selected_report)
                st.success("Report Deleted")
                st.rerun()

            # Report statistics
            st.divider()
            stats = InterviewReportService.statistics()
            st.subheader("Report Statistics")

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric("Reports", stats["total_reports"])

            with c2:
                st.metric("Average Score", round(stats["average_score"] or 0, 2))

            with c3:
                st.metric("Highest", stats["highest_score"])

            with c4:
                st.metric("Lowest", stats["lowest_score"])

    # ---------------------------------------------------
    # History
    # ---------------------------------------------------
    with tabs[6]:
        st.header("🕒 Interview History")

        history = InterviewHistoryService.get_all()

        if not history:
            st.info("No interview history available.")
        else:
            # Search & filters
            col1, col2 = st.columns(2)

            with col1:
                search_session = st.text_input("Search Session ID")

            with col2:
                history_interview_type = st.selectbox(
                    "Interview Type",
                    ["All", "Technical", "Coding", "HR"],
                )

            filtered = history

            if search_session.strip():
                filtered = [
                    item for item in filtered
                    if search_session.lower() in item["session_id"].lower()
                ]

            if history_interview_type != "All":
                filtered = [
                    item for item in filtered
                    if item["interview_type"] == history_interview_type
                ]

            st.dataframe(pd.DataFrame(filtered), use_container_width=True, hide_index=True)

            st.divider()

            # Recent interviews
            st.subheader("Recent Interviews")
            recent = InterviewHistoryService.recent()

            if recent:
                st.dataframe(pd.DataFrame(recent), use_container_width=True, hide_index=True)

            st.divider()

            # Top scores
            st.subheader("Top Scores")
            top = InterviewHistoryService.top_scores()

            if top:
                st.dataframe(pd.DataFrame(top), use_container_width=True, hide_index=True)

            st.divider()

            # View session
            session_ids = [item["session_id"] for item in history]
            selected = st.selectbox("View Session", session_ids)

            session = InterviewHistoryService.get(selected)

            if session:
                st.json(session)

            st.divider()

            # Delete history
            history_ids = [item["id"] for item in history]
            delete_id = st.selectbox("Delete History", history_ids, key="delete_history")

            if st.button("🗑 Delete Selected History", use_container_width=True):
                InterviewHistoryService.delete(delete_id)
                st.success("History Deleted")
                st.rerun()

            st.divider()

            # Clear history
            if st.button("❌ Clear Entire History", use_container_width=True):
                InterviewHistoryService.clear()
                st.success("History Cleared")
                st.rerun()

            # Statistics
            st.divider()
            st.subheader("History Statistics")
            stats = InterviewHistoryService.statistics()

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Total Interviews", stats["total_interviews"])

            with c2:
                st.metric("Average Score", round(stats["average_score"] or 0, 2))

            with c3:
                st.metric("Average Duration", round(stats["average_duration"] or 0, 2))

    # ---------------------------------------------------
    # Analytics
    # ---------------------------------------------------
    with tabs[7]:
        st.header("📈 Interview Analytics")

        stats = InterviewHistoryService.statistics()

        if not stats:
            st.info("No analytics available.")
        else:
            # KPI cards
            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric("Total Interviews", stats["total_interviews"])

            with c2:
                st.metric("Average Score", round(stats["average_score"] or 0, 2))

            with c3:
                st.metric("Highest Score", stats["highest_score"])

            with c4:
                st.metric("Lowest Score", stats["lowest_score"])

            st.divider()

            # Provider analytics
            st.subheader("Provider Analytics")
            providers = InterviewHistoryService.provider_statistics()

            if providers:
                provider_df = pd.DataFrame(providers)
                st.dataframe(provider_df, use_container_width=True, hide_index=True)

                if "provider" in provider_df.columns:
                    chart = provider_df.set_index("provider")
                    if "interviews" in chart.columns:
                        st.bar_chart(chart["interviews"])

            st.divider()

            # Model analytics
            st.subheader("Model Analytics")
            models = InterviewHistoryService.model_statistics()

            if models:
                model_df = pd.DataFrame(models)
                st.dataframe(model_df, use_container_width=True, hide_index=True)

                if "model" in model_df.columns:
                    chart = model_df.set_index("model")
                    if "average_score" in chart.columns:
                        st.bar_chart(chart["average_score"])

            st.divider()

            # Performance distribution
            st.subheader("Performance Distribution")
            performance = InterviewHistoryService.score_distribution()

            if performance:
                perf_df = pd.DataFrame(performance)
                st.dataframe(perf_df, use_container_width=True, hide_index=True)

                if "performance" in perf_df.columns:
                    chart = perf_df.set_index("performance")
                    if "total" in chart.columns:
                        st.bar_chart(chart["total"])

            st.divider()

            # Interview type distribution
            st.subheader("Interview Types")
            history = InterviewHistoryService.get_all()

            if history:
                history_df = pd.DataFrame(history)
                if "interview_type" in history_df.columns:
                    counts = history_df.groupby("interview_type").size()
                    st.bar_chart(counts)

            st.divider()

            # Difficulty distribution
            st.subheader("Difficulty Distribution")

            if history:
                history_df = pd.DataFrame(history)
                if "difficulty" in history_df.columns:
                    counts = history_df.groupby("difficulty").size()
                    st.bar_chart(counts)

            st.divider()

            # Recent performance trend
            st.subheader("Recent Performance")

            if history:
                trend = pd.DataFrame(history)
                if "created_at" in trend.columns:
                    trend = trend.sort_values("created_at")
                if "score" in trend.columns:
                    st.line_chart(trend["score"])

            st.divider()

            # Export analytics
            st.subheader("Export")

            if history:
                csv = pd.DataFrame(history).to_csv(index=False)
                st.download_button(
                    "⬇ Export Analytics CSV",
                    csv,
                    file_name="interview_analytics.csv",
                    mime="text/csv",
                )

            st.divider()

            # Summary
            st.success("Interview Analytics Dashboard Loaded Successfully.")
            st.write("""
### Summary

- Total Interviews
- Average Performance
- Highest / Lowest Scores
- Provider Usage
- Model Usage
- Performance Distribution
- Interview Type Distribution
- Difficulty Distribution
- Performance Trend
- CSV Export
""")