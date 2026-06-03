import streamlit as st
import json
from chain import conversation_chain

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    opacity: 0.95;
}

.card {
    padding: 25px;
    border-radius: 18px;
    background-color: white;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
}

.metric-card {
    padding: 20px;
    border-radius: 16px;
    background-color: #ffffff;
    border-left: 6px solid #2563eb;
    box-shadow: 0 5px 18px rgba(0,0,0,0.06);
}

.label {
    font-size: 14px;
    color: #64748b;
    font-weight: 600;
    margin-bottom: 5px;
}

.value {
    font-size: 24px;
    color: #0f172a;
    font-weight: 800;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
    font-size: 14px;
}

.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 12px;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    font-weight: 700;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1d4ed8, #1e40af);
    color: white;
}

textarea {
    border-radius: 14px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown("""
<div class="hero">
    <h1>🌍 AI Language Translation & Tutor</h1>
    <p>
        Translate text into multiple languages with structured AI-generated JSON output.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LAYOUT
# ---------------------------------------------------

left_col, right_col = st.columns([1.1, 0.9])

# ---------------------------------------------------
# LEFT SIDE
# ---------------------------------------------------

with left_col:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📝 Translation Input")

    user_prompt = st.text_area(
        "Enter your translation request",
        placeholder='Example: Translate "Good Morning" into French.',
        height=120,
        label_visibility="collapsed"
    )

    translate_btn = st.button("Translate Text")

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------
    # SAMPLE INPUTS
    # -------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("💡 Sample Inputs")

    sample_1 = 'Translate "Good Morning" into French.'
    sample_2 = 'Translate "Apple" into Spanish.'
    sample_3 = 'Translate "Hello" into Japanese.'
    sample_4 = 'Translate "How are you?" into Hindi.'

    st.code(sample_1)
    st.code(sample_2)
    st.code(sample_3)
    st.code(sample_4)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# RIGHT SIDE
# ---------------------------------------------------

with right_col:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Translation Result")

    if translate_btn:

        if not user_prompt.strip():

            st.warning("Please enter a translation request.")

        else:

            with st.spinner("Translating text..."):

                try:

                    response = conversation_chain.invoke(
                        {"input": user_prompt},
                        config={
                            "configurable": {
                                "session_id": "translation_chat"
                            }
                        }
                    )

                    assistant_reply = response.content

                    try:
                        result = json.loads(assistant_reply)

                        st.success("Translation completed successfully!")

                        col1, col2 = st.columns(2)

                        with col1:
                            st.markdown(
                                f"""
                                <div class="metric-card">
                                    <div class="label">Input Language</div>
                                    <div class="value">{result.get("input_language", "")}</div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        with col2:
                            st.markdown(
                                f"""
                                <div class="metric-card">
                                    <div class="label">Output Language</div>
                                    <div class="value">{result.get("output_language", "")}</div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        st.markdown("---")

                        st.subheader("🌐 Translated Text")

                        st.info(result.get("translated_text", ""))

                        st.subheader("🧾 Structured JSON Output")

                        st.json(result)

                    except:
                        st.markdown(assistant_reply)

                except Exception as e:

                    st.error("Something went wrong during translation.")
                    st.exception(e)

    else:

        st.info(
            "Enter a translation request and click **Translate Text** to view AI-generated results."
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
    Built with Streamlit, LangChain, Gemini AI, and JSON Output Formatting.
</div>
""", unsafe_allow_html=True)