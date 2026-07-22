"""
Enterprise Voice AI Tutor Page
"""

import streamlit as st

from services.voice_chat_service import VoiceChatService
from services.voice_history_service import VoiceHistoryService
from services.voice_analytics_service import VoiceAnalyticsService
from services.voice_session_service import VoiceSessionService

from providers.provider_manager import ProviderManager
from providers.model_manager import ModelManager

from pages.rag.models import (
    SearchType,
    TOP_K_VALUES
)


class VoicePage:

    @staticmethod
    def render():

        st.title("🎙 Enterprise Voice AI Tutor")

        # ==========================================================
        # Session State
        # ==========================================================

        if "voice_session_id" not in st.session_state:
            st.session_state.voice_session_id = None

        # ==========================================================
        # Tabs
        # ==========================================================

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🎙 Voice Chat",
                "📜 History",
                "📊 Analytics",
                "🗂 Sessions"
            ]
        )

        # ==========================================================
        # TAB 1
        # ==========================================================

        with tab1:

            st.header("Voice Conversation")

            provider = ProviderManager.get_provider()

            models = ModelManager.get_models()

            if not models:

                st.error("No AI models available.")

                return

            model = st.selectbox(
                "Model",
                models
            )

            search_type = st.selectbox(
                "Search Type",
                [
                    SearchType.SEMANTIC.value,
                    SearchType.KEYWORD.value,
                    SearchType.HYBRID.value,
                    SearchType.REWRITE.value,
                    SearchType.MULTI_QUERY.value,
                    SearchType.HYDE.value,
                    SearchType.PARENT_CHILD.value
                ]
            )

            top_k = st.selectbox(
                "Top K",
                TOP_K_VALUES,
                index=2
            )

            language = st.selectbox(
                "Language",
                [
                    "en",
                    "hi",
                    "te"
                ]
            )

            st.divider()

            st.subheader("Session")

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                        "🆕 New Session",
                        use_container_width=True
                ):

                    session_id = VoiceSessionService.create_session(

                        provider=provider,

                        model=model,

                        language=language

                    )

                    st.session_state.voice_session_id = session_id

                    st.success("New Session Created")

            with col2:

                if st.button(
                        "🛑 End Session",
                        use_container_width=True
                ):

                    if st.session_state.voice_session_id:

                        VoiceChatService.end_session(

                            st.session_state.voice_session_id

                        )

                        st.success("Session Completed")

                        st.session_state.voice_session_id = None

                    else:

                        st.warning("No Active Session")

            st.divider()

            if st.session_state.voice_session_id:

                st.info(
                    f"Active Session : {st.session_state.voice_session_id}"
                )

            else:

                st.warning(
                    "No Active Session"
                )

            st.divider()

            audio_file = st.file_uploader(

                "Upload Voice",

                type=[
                    "wav",
                    "mp3",
                    "m4a",
                    "ogg"
                ]

            )

            speak = st.checkbox(

                "Speak AI Response",

                value=True

            )

            if st.button(

                    "Start Conversation",

                    use_container_width=True

            ):

                if audio_file is None:

                    st.warning(
                        "Please upload an audio file."
                    )

                else:

                    with st.spinner(
                            "Processing Voice..."
                    ):

                        result = VoiceChatService.chat(

                            audio_file=audio_file,

                            provider=provider,

                            model=model,

                            search_type=search_type,

                            top_k=top_k,

                            language=language,

                            speak_response=speak

                        )

                    if result["success"]:

                        st.session_state.voice_session_id = result[
                            "session_id"
                        ]

                        st.success("Conversation Completed")

                        st.subheader("🎤 Transcript")

                        st.write(
                            result["question"]
                        )

                        st.subheader("🤖 AI Response")

                        st.write(
                            result["answer"]
                        )

                        if result["audio_file"]:

                            st.audio(
                                result["audio_file"]
                            )

                        st.subheader("📂 Sources")

                        for source in result["sources"]:

                            with st.expander(
                                    source["document"]
                            ):

                                st.write(
                                    source["text"]
                                )

                        st.subheader("📖 Citations")

                        for citation in result["citations"]:

                            st.write(

                                f"[{citation['id']}] "

                                f"{citation['document']} "

                                f"(Chunk {citation['chunk']})"

                            )

                        st.subheader("Performance")

                        c1, c2 = st.columns(2)

                        c1.metric(

                            "Response Time",

                            f"{result['response_time']} ms"

                        )

                        c2.metric(

                            "Tokens",

                            result["token_usage"]["tokens"]

                        )

                    else:

                        st.error(
                            result["message"]
                        )
        # ===================================================
        # TAB 2 - HISTORY
        # ===================================================

        with tab2:

            st.header("📜 Voice Conversation History")

            history = VoiceHistoryService.get_all()

            if history:

                st.caption(
                    f"Total Conversations : {len(history)}"
                )

                for item in history:

                    title = (
                        f"{item['created_at']} | "
                        f"{item['provider']} | "
                        f"{item['model']}"
                    )

                    with st.expander(title):

                        st.markdown("### 🎤 Transcript")

                        st.write(
                            item["transcript"]
                        )

                        st.markdown("### 🤖 AI Response")

                        st.write(
                            item["ai_response"]
                        )

                        c1, c2 = st.columns(2)

                        c1.write(
                            f"**Provider:** {item['provider']}"
                        )

                        c2.write(
                            f"**Model:** {item['model']}"
                        )

                        st.write(
                            f"**Language:** {item['language']}"
                        )

            else:

                st.info(
                    "No voice history available."
                )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                keyword = st.text_input(
                    "Search Conversation"
                )

            with col2:

                st.write("")

                st.write("")

                if st.button(
                        "Search",
                        use_container_width=True
                ):

                    if keyword.strip():

                        results = VoiceHistoryService.search(
                            keyword
                        )

                        if results:

                            st.success(
                                f"{len(results)} result(s) found."
                            )

                            for item in results:

                                with st.expander(
                                        item["created_at"]
                                ):

                                    st.write(
                                        item["transcript"]
                                    )

                                    st.divider()

                                    st.write(
                                        item["ai_response"]
                                    )

                        else:

                            st.warning(
                                "No matching conversations."
                            )

            st.divider()

            if st.button(
                    "🗑 Clear Voice History",
                    use_container_width=True
            ):

                VoiceHistoryService.clear()

                st.success(
                    "Voice history cleared."
                )

                st.rerun()

        # ===================================================
        # TAB 3 - ANALYTICS
        # ===================================================

        with tab3:

            st.header("📊 Voice Analytics")

            stats = VoiceAnalyticsService.overall_statistics()

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(

                "Sessions",

                stats["total_sessions"]

            )

            c2.metric(

                "Messages",

                stats["total_messages"]

            )

            c3.metric(

                "Average Duration",

                round(
                    stats["average_duration"] or 0,
                    2
                )

            )

            c4.metric(

                "Average Response",

                round(
                    stats["average_response_time"] or 0,
                    2
                )

            )

            st.divider()

            st.subheader("Provider Statistics")

            provider_stats = VoiceAnalyticsService.provider_statistics()

            if provider_stats:

                st.dataframe(

                    provider_stats,

                    use_container_width=True,

                    hide_index=True

                )

            else:

                st.info(
                    "No analytics available."
                )

            st.divider()

            st.subheader("Longest Sessions")

            sessions = VoiceAnalyticsService.top_sessions()

            if sessions:

                st.dataframe(

                    sessions,

                    use_container_width=True,

                    hide_index=True

                )

            else:

                st.info(
                    "No session statistics available."
                )

        # ===================================================
        # TAB 4 - SESSIONS
        # ===================================================

        with tab4:

            st.header("🗂 Voice Sessions")

            sessions = VoiceSessionService.get_sessions()

            if sessions:

                st.dataframe(

                    sessions,

                    use_container_width=True,

                    hide_index=True

                )

                st.divider()

                st.subheader("Session Statistics")

                statistics = VoiceSessionService.get_statistics()

                c1, c2 = st.columns(2)

                c3, c4 = st.columns(2)

                c1.metric(

                    "Total Sessions",

                    statistics["total_sessions"] or 0

                )

                c2.metric(

                    "Messages",

                    statistics["total_messages"] or 0

                )

                c3.metric(

                    "Average Duration",

                    round(
                        statistics["average_duration"] or 0,
                        2
                    )

                )

                c4.metric(

                    "Longest Session",

                    round(
                        statistics["longest_session"] or 0,
                        2
                    )

                )

                st.divider()

                st.subheader("Manage Sessions")

                selected = st.selectbox(

                    "Select Session",

                    [
                        session["session_id"]
                        for session in sessions
                    ]

                )

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(
                            "Complete Session",
                            use_container_width=True
                    ):

                        VoiceSessionService.complete_session(
                            selected
                        )

                        st.success(
                            "Session completed."
                        )

                        st.rerun()

                with col2:

                    if st.button(
                            "Delete Session",
                            use_container_width=True
                    ):

                        VoiceHistoryService.delete(
                            selected
                        )

                        VoiceAnalyticsService.delete(
                            selected
                        )

                        VoiceSessionService.delete_session(
                            selected
                        )

                        st.success(
                            "Session deleted."
                        )

                        st.rerun()

            else:

                st.info(
                    "No voice sessions available."
                )