import streamlit as st

from utils.chat_helper import ask_question


def show_chat(extracted_text):
    """
    Displays the AI chat interface.
    """

    st.header("💬 Ask AI About Your Report")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_input(
        "Ask a medical question about your report",
        placeholder="Example: Why is my TSH high?"
    )

    if st.button("🤖 Ask AI"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Gemini is thinking..."):

                answer = ask_question(
                    extracted_text,
                    question
                )

            # Save chat history
            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer
                }
            )

    # Display chat history
    if st.session_state.chat_history:

        st.subheader("📝 Conversation")

        for chat in reversed(st.session_state.chat_history):

            with st.chat_message("user"):

                st.write(chat["question"])

            with st.chat_message("assistant"):

                st.write(chat["answer"])

    st.divider()