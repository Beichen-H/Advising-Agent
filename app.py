import streamlit as st
from llm_client_openai import OpenAIClient
from config import Config

# Page configuration
st.set_page_config(
    page_title="LAS Academic Advising Assistant",
    page_icon="🎓",
    layout="wide"
)

# Initialize OpenAI client
@st.cache_resource
def init_client():
    return OpenAIClient()

def main():
    st.title("🎓 LAS Academic Advising Assistant")
    st.markdown("### Multi-Department Academic Information")
    st.markdown("---")
    
    client = init_client()
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ About")
        st.markdown("""
        This assistant provides academic information for multiple departments at UIUC.
        
        **Currently Available:**
        - 📚 **Sociology** (Major, Minor, CLS, Courses)
        - 📊 **Statistics** (Major, Stat&CS, Minor, DS Minor, DS Certificate)
        
        **Coming Soon:**
        - 📈 Economics
        - 🧠 Psychology
        
        **Status:** 🟢 Connected to OpenAI
        """)
        
        st.markdown("---")
        
        st.header("🔗 Useful Links")
        st.markdown("""
        - [Course Explorer](https://courses.illinois.edu)
        - [Academic Calendar](https://registrar.illinois.edu/academic-calendar)
        - [Student Self-Service](https://apps.uillinois.edu/selfservice)
        """)
        
        st.markdown("---")
        st.caption("Department contact information will be provided by the AI when needed.")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💬 Ask your academic question")
        
        # Initialize session state for query
        if 'query_input' not in st.session_state:
            st.session_state['query_input'] = ""
        
        # Query input
        query = st.text_area(
            "Enter your question:",
            value=st.session_state['query_input'],
            placeholder="e.g., What are the Sociology major requirements?",
            height=100,
            key="query_input_widget"
        )
        
        if st.button("Ask Assistant", type="primary"):
            if query:
                with st.spinner("Researching your question..."):
                    messages = [
                        {"role": "system", "content": Config.SYSTEM_PROMPT},
                        {"role": "user", "content": query}
                    ]
                    response = client.generate_response(messages)
                
                st.markdown("### Response")
                st.markdown(response)
                
                # Store in session state
                st.session_state['last_response'] = response
                st.session_state['last_query'] = query
            else:
                st.warning("Please enter a question.")
        
        # Show last response if exists
        elif 'last_response' in st.session_state:
            st.markdown("### Last Response")
            st.markdown(st.session_state['last_response'])
    
    with col2:
        st.header("📝 Sample Questions")
        
        with st.expander("Sociology", expanded=True):
            if st.button("Sociology major requirements", use_container_width=True):
                st.session_state['query_input'] = "What are all the requirements for Sociology major at UIUC?"
                st.rerun()
            if st.button("Sociology minor requirements", use_container_width=True):
                st.session_state['query_input'] = "What courses do I need for a Sociology minor?"
                st.rerun()
            if st.button("CLS minor", use_container_width=True):
                st.session_state['query_input'] = "Tell me about the Criminology, Law & Society minor"
                st.rerun()
            if st.button("SOC 450 vs SOC 495", use_container_width=True):
                st.session_state['query_input'] = "What's the difference between SOC 450 and SOC 495?"
                st.rerun()
        
        with st.expander("Statistics", expanded=True):
            if st.button("Statistics major requirements", use_container_width=True):
                st.session_state['query_input'] = "What are the requirements for Statistics major at UIUC?"
                st.rerun()
            if st.button("Stat & CS major requirements", use_container_width=True):
                st.session_state['query_input'] = "What are the requirements for Statistics & Computer Science major?"
                st.rerun()
            if st.button("Statistics minor", use_container_width=True):
                st.session_state['query_input'] = "Tell me about the Statistics minor requirements"
                st.rerun()
            if st.button("Data Science minor", use_container_width=True):
                st.session_state['query_input'] = "What are the requirements for the Data Science minor?"
                st.rerun()
            if st.button("Data Science certificate", use_container_width=True):
                st.session_state['query_input'] = "How do I get the Certificate in Data Science?"
                st.rerun()
            if st.button("STAT vs SOC statistics", use_container_width=True):
                st.session_state['query_input'] = "Can I take STAT 100 instead of SOC 280? How does that work?"
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
        ⚠️ Information based on official UIUC department documents. 
        Course availability varies by semester - always check the Course Explorer.
        Department contact information will be provided by the AI when needed.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
