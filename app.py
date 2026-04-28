import streamlit as st
from bedrock_kb_client import BedrockKnowledgeBaseClient

st.set_page_config(
    page_title="LAS Academic Advising Assistant",
    page_icon="🎓",
    layout="centered"
)


@st.cache_resource
def init_client():
    return BedrockKnowledgeBaseClient()


def set_sample_question(question):
    st.session_state["query_input"] = question


def main():
    client = init_client()

    if "kb_session_id" not in st.session_state:
        st.session_state["kb_session_id"] = None

    if "query_input" not in st.session_state:
        st.session_state["query_input"] = ""

    with st.sidebar:
        st.title("LAS Assistant")
        st.info("Academic advising answers using official UIUC LAS documents.")

        st.subheader("Available Areas")
        st.write("Sociology")
        st.write("Statistics")
        st.write("LAS Academic Policies")

        st.success("Connected to AWS Bedrock")

        st.subheader("Useful Links")
        st.link_button("Course Explorer", "https://courses.illinois.edu")
        st.link_button("Academic Calendar",
                       "https://registrar.illinois.edu/academic-calendar")
        st.link_button("Student Self-Service",
                       "https://apps.uillinois.edu/selfservice")

    st.title("LAS Academic Advising Assistant")
    st.caption("AI-powered academic guidance for UIUC LAS students")

    st.divider()

    st.subheader("Ask a Question")

    query = st.text_area(
        "Enter your question:",
        value=st.session_state["query_input"],
        placeholder="What are the Sociology major requirements?",
        height=140,
        key="query_input_widget"
    )

    ask_clicked = st.button(
        "Ask Assistant", type="primary", use_container_width=True)

    st.divider()

    st.subheader("Sample Questions")

    tab1, tab2, tab3 = st.tabs(["Sociology", "Statistics", "LAS Policies"])

    with tab1:
        if st.button("Sociology major requirements", use_container_width=True):
            st.session_state["query_input"] = "What are all the requirements for the Sociology major at UIUC?"
            st.rerun()

        if st.button("Sociology minor requirements", use_container_width=True):
            st.session_state["query_input"] = "What courses do I need for a Sociology minor?"
            st.rerun()

        if st.button("CLS minor", use_container_width=True):
            st.session_state["query_input"] = "Tell me about the Criminology, Law & Society minor."
            st.rerun()

    with tab2:
        if st.button("Statistics major requirements", use_container_width=True):
            st.session_state["query_input"] = "What are the requirements for the Statistics major at UIUC?"
            st.rerun()

        if st.button("Stat & CS major requirements", use_container_width=True):
            st.session_state["query_input"] = "What are the requirements for the Statistics & Computer Science major?"
            st.rerun()

        if st.button("Statistics minor", use_container_width=True):
            st.session_state["query_input"] = "Tell me about the Statistics minor requirements."
            st.rerun()

        if st.button("Data Science minor", use_container_width=True):
            st.session_state["query_input"] = "What are the requirements for the Data Science minor?"
            st.rerun()

    with tab3:
        if st.button("Graduation requirements", use_container_width=True):
            st.session_state["query_input"] = "What should LAS students know about graduation requirements?"
            st.rerun()

        if st.button("Changing majors", use_container_width=True):
            st.session_state["query_input"] = "How does changing majors work in LAS?"
            st.rerun()

        if st.button("Academic standing", use_container_width=True):
            st.session_state["query_input"] = "Explain LAS academic standing policies."
            st.rerun()

    if ask_clicked:
        if query.strip():
            with st.spinner("Researching your question..."):
                result = client.answer_question(
                    query=query,
                    session_id=st.session_state["kb_session_id"]
                )

            answer_text = result.get("output", {}).get(
                "text",
                "No response returned."
            )

            new_session_id = result.get("sessionId")
            if new_session_id:
                st.session_state["kb_session_id"] = new_session_id

            st.session_state["last_response"] = answer_text
            st.session_state["last_citations"] = result.get("citations", [])

            st.divider()
            st.subheader("Response")
            st.write(answer_text)

            citations = st.session_state["last_citations"]
            if citations:
                st.subheader("Sources")
                for i, citation in enumerate(citations, start=1):
                    st.write(f"{i}. {citation}")
        else:
            st.warning("Please enter a question.")

    elif "last_response" in st.session_state:
        st.divider()
        st.subheader("Last Response")
        st.write(st.session_state["last_response"])

    st.divider()
    st.caption(
        "Information based on official UIUC academic documents. "
        "Course availability may change each semester."
    )


if __name__ == "__main__":
    main()
