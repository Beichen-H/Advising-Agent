import streamlit as st
from bedrock_kb_client import BedrockKnowledgeBaseClient

st.set_page_config(
    page_title="LAS Academic Advising Assistant",
    page_icon="🎓",
    layout="wide"
)


@st.cache_resource
def init_client():
    return BedrockKnowledgeBaseClient()


def main():
    st.title("🎓 LAS Academic Advising Assistant")
    st.markdown("### Multi-Department Academic Information")
    st.markdown("---")

    client = init_client()

    if "kb_session_id" not in st.session_state:
        st.session_state["kb_session_id"] = None

    query = st.text_area(
        "Enter your question:",
        placeholder="e.g., What are the Sociology major requirements?",
        height=100
    )

    if st.button("Ask Assistant", type="primary"):
        if query:
            with st.spinner("Researching your question..."):
                result = client.answer_question(
                    query=query,
                    session_id=st.session_state["kb_session_id"]
                )

                answer_text = result.get("output", {}).get(
                    "text", "No response returned.")
                new_session_id = result.get("sessionId")

                if new_session_id:
                    st.session_state["kb_session_id"] = new_session_id

                st.markdown("### Response")
                st.markdown(answer_text)

                citations = result.get("citations", [])
                if citations:
                    st.markdown("### Sources")
                    for i, citation in enumerate(citations, start=1):
                        st.write(f"{i}. {citation}")
        else:
            st.warning("Please enter a question.")


if __name__ == "__main__":
    main()
