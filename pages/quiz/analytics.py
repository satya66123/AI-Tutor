"""
Quiz Analytics
"""

import streamlit as st


class QuizAnalytics:

    @staticmethod
    def render(result):

        st.divider()

        st.subheader("📊 Quiz Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Correct",
            result["correct"]
        )

        c2.metric(
            "Wrong",
            result["wrong"]
        )

        c3.metric(
            "Score",
            f'{result["percentage"]}%'
        )

        if result["status"] == "PASS":

            st.success("✅ PASS")

        else:

            st.error("❌ FAIL")