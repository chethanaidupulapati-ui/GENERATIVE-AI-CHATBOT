import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# =========================================================
# API SETUP
# =========================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY was not found in your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Generative AI Chatbot",
    page_icon="🌷",
    layout="centered"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Poppins:wght@300;400;500;600;700&display=swap'
);


/* =========================================================
   MAIN BACKGROUND
   ========================================================= */

.stApp {

    min-height: 100vh;

    background:

        /* soft pink/lavender glow */
        radial-gradient(
            circle at 15% 20%,
            rgba(255, 188, 224, 0.70),
            transparent 30%
        ),

        radial-gradient(
            circle at 85% 25%,
            rgba(194, 162, 239, 0.65),
            transparent 32%
        ),

        radial-gradient(
            circle at 50% 90%,
            rgba(241, 177, 219, 0.55),
            transparent 35%
        ),

        /* blurry floral photography */
        linear-gradient(
            rgba(239, 190, 224, 0.50),
            rgba(207, 185, 238, 0.52)
        ),

        url("https://images.unsplash.com/photo-1527061011665-3652c757a4d4?auto=format&fit=crop&w=2200&q=90");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;

    font-family: 'Poppins', sans-serif;

    animation:
        backgroundBreathing 14s ease-in-out infinite alternate;
}


/* =========================================================
   BACKGROUND ANIMATION
   ========================================================= */

@keyframes backgroundBreathing {

    0% {
        background-position:
            48% 48%;
    }

    50% {
        background-position:
            52% 52%;
    }

    100% {
        background-position:
            47% 50%;
    }
}


/* =========================================================
   MAIN CONTAINER
   ========================================================= */

.block-container {

    max-width: 850px;

    padding-top: 3rem;
    padding-bottom: 3rem;
}


/* =========================================================
   SOFT FLOATING LIGHT EFFECT
   ========================================================= */

.stApp::before {

    content: "";

    position: fixed;

    width: 320px;
    height: 320px;

    top: 8%;
    left: -100px;

    background:
        radial-gradient(
            circle,
            rgba(255, 196, 230, 0.38),
            transparent 68%
        );

    filter: blur(35px);

    pointer-events: none;

    animation:
        floatingGlow 9s ease-in-out infinite alternate;

    z-index: 0;
}


.stApp::after {

    content: "";

    position: fixed;

    width: 380px;
    height: 380px;

    bottom: -120px;
    right: -100px;

    background:
        radial-gradient(
            circle,
            rgba(190, 157, 237, 0.35),
            transparent 68%
        );

    filter: blur(45px);

    pointer-events: none;

    animation:
        floatingGlowTwo 11s ease-in-out infinite alternate;

    z-index: 0;
}


@keyframes floatingGlow {

    from {
        transform: translate(
            0px,
            0px
        );
    }

    to {
        transform: translate(
            100px,
            50px
        );
    }
}


@keyframes floatingGlowTwo {

    from {
        transform: translate(
            0px,
            0px
        );
    }

    to {
        transform: translate(
            -80px,
            -60px
        );
    }
}


/* =========================================================
   TITLE
   ========================================================= */

h1 {

    position: relative;
    z-index: 2;

    font-family:
        'DM Serif Display',
        serif !important;

    font-size:
        50px !important;

    font-weight:
        400 !important;

    text-align:
        center !important;

    letter-spacing:
        1.5px;

    line-height:
        1.15 !important;

    margin-top:
        10px !important;

    margin-bottom:
        8px !important;

    background:
        linear-gradient(
            90deg,
            #b9328c,
            #8750bd,
            #c14498,
            #8c50bd
        );

    background-size:
        250% auto;

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;

    animation:
        titleShimmer 6s ease-in-out infinite;

    filter:
        drop-shadow(
            0 4px 8px
            rgba(104, 53, 118, 0.18)
        );
}


@keyframes titleShimmer {

    0% {
        background-position:
            0% center;
    }

    50% {
        background-position:
            100% center;
    }

    100% {
        background-position:
            0% center;
    }
}


/* =========================================================
   FLOWERS UNDER TITLE
   ========================================================= */

.stMarkdown p {

    color:
        #603657;
}


/* Center flower decoration */

.stMarkdown:first-of-type {

    text-align:
        center !important;
}


/* =========================================================
   INTRO TEXT
   ========================================================= */

div[data-testid="stCaptionContainer"] p {

    color:
        #66345f !important;

    font-family:
        'Poppins',
        sans-serif !important;

    font-size:
        16px !important;

    font-weight:
        600 !important;

    text-align:
        center !important;

    letter-spacing:
        0.35px;

    line-height:
        1.7;

    text-shadow:
        0 1px 2px
        rgba(255,255,255,0.75);

    background:
        transparent !important;

    border:
        none !important;

    box-shadow:
        none !important;
}


/* =========================================================
   INPUT LABEL
   ========================================================= */

.stTextArea label {

    color:
        #5e3158 !important;

    font-family:
        'Poppins',
        sans-serif !important;

    font-size:
        15px !important;

    font-weight:
        600 !important;
}


/* =========================================================
   TEXT INPUT
   ========================================================= */

.stTextArea textarea {

    background:
        rgba(
            255,
            244,
            252,
            0.94
        ) !important;

    color:
        #482842 !important;

    border:
        2px solid
        rgba(
            182,
            81,
            164,
            0.32
        ) !important;

    border-radius:
        24px !important;

    font-family:
        'Poppins',
        sans-serif !important;

    font-size:
        15px !important;

    padding:
        18px !important;

    box-shadow:
        0 15px 40px
        rgba(
            106,
            55,
            122,
            0.14
        ) !important;

    transition:
        all 0.3s ease !important;
}


/* =========================================================
   INPUT PLACEHOLDER
   ========================================================= */

.stTextArea textarea::placeholder {

    color:
        #9c6794 !important;

    opacity:
        1 !important;
}


/* =========================================================
   INPUT FOCUS
   ========================================================= */

.stTextArea textarea:focus {

    border-color:
        #bd4da7 !important;

    box-shadow:
        0 0 0 4px
        rgba(
            191,
            78,
            170,
            0.12
        ),
        0 18px 40px
        rgba(
            106,
            55,
            122,
            0.18
        ) !important;
}


/* =========================================================
   GENERATE BUTTON
   ========================================================= */

.stButton {

    margin-top:
        8px;
}


.stButton > button {

    width:
        100%;

    min-height:
        56px;

    border:
        none !important;

    border-radius:
        22px !important;

    background:
        linear-gradient(
            135deg,
            #d957ac,
            #a35bd0,
            #8d55c2
        ) !important;

    background-size:
        200% 200%;

    color:
        white !important;

    font-family:
        'Poppins',
        sans-serif !important;

    font-size:
        16px !important;

    font-weight:
        600 !important;

    letter-spacing:
        0.4px;

    box-shadow:
        0 12px 30px
        rgba(
            143,
            66,
            153,
            0.30
        ) !important;

    transition:
        all 0.35s ease !important;

    animation:
        buttonGlow 5s ease infinite;
}


@keyframes buttonGlow {

    0% {
        background-position:
            0% 50%;
    }

    50% {
        background-position:
            100% 50%;
    }

    100% {
        background-position:
            0% 50%;
    }
}


.stButton > button:hover {

    transform:
        translateY(-4px)
        scale(1.01);

    box-shadow:
        0 18px 38px
        rgba(
            143,
            66,
            153,
            0.40
        ) !important;
}


/* =========================================================
   RESPONSE HEADING
   ========================================================= */

h3 {

    color:
        #823e7c !important;

    font-family:
        'DM Serif Display',
        serif !important;

    font-size:
        29px !important;

    font-weight:
        400 !important;

    text-align:
        left;

    margin-top:
        28px !important;

    margin-bottom:
        12px !important;

    background:
        transparent !important;

    border:
        none !important;

    box-shadow:
        none !important;
}


/* =========================================================
   RESPONSE TEXT
   ========================================================= */

div[data-testid="stMarkdownContainer"] p {

    color:
        #4b2d47 !important;

    font-family:
        'Poppins',
        sans-serif !important;

    font-size:
        15px;

    line-height:
        1.8;
}


/* =========================================================
   RESPONSE LISTS
   ========================================================= */

div[data-testid="stMarkdownContainer"] li {

    color:
        #4b2d47 !important;

    line-height:
        1.8;
}


/* =========================================================
   WARNING
   ========================================================= */

div[data-testid="stAlert"] {

    border-radius:
        18px !important;

    background:
        rgba(
            255,
            238,
            249,
            0.88
        ) !important;

    color:
        #713c70 !important;

    border:
        1px solid
        rgba(
            195,
            91,
            170,
            0.25
        ) !important;
}


/* =========================================================
   SPINNER
   ========================================================= */

.stSpinner > div {

    border-top-color:
        #c451a8 !important;
}


/* =========================================================
   FOOTER
   ========================================================= */

div[data-testid="stCaptionContainer"]:last-of-type p {

    color:
        #75466e !important;

    font-size:
        13px !important;

    font-weight:
        500 !important;

    text-align:
        center !important;

    margin-top:
        35px !important;

    background:
        transparent !important;

    border:
        none !important;

    box-shadow:
        none !important;
}


/* =========================================================
   SOFT FLOATING PETALS
   ========================================================= */

@keyframes petalFloat {

    0% {
        transform:
            translateY(0px)
            rotate(0deg);
        opacity:
            0.20;
    }

    50% {
        transform:
            translateY(-25px)
            rotate(12deg);
        opacity:
            0.40;
    }

    100% {
        transform:
            translateY(0px)
            rotate(0deg);
        opacity:
            0.20;
    }
}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 600px) {

    h1 {

        font-size:
            35px !important;
    }

    .block-container {

        padding-left:
            1.1rem;

        padding-right:
            1.1rem;
    }

    div[data-testid="stCaptionContainer"] p {

        font-size:
            14px !important;
    }

    .stTextArea textarea {

        border-radius:
            20px !important;
    }

}


/* =========================================================
   REDUCE ANIMATION FOR ACCESSIBILITY
   ========================================================= */

@media (prefers-reduced-motion: reduce) {

    .stApp,
    h1,
    .stButton > button,
    .stApp::before,
    .stApp::after {

        animation:
            none !important;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.write("🌷  ✿  🌸  ❀  🌺  ❀  🌸  ✿  🌷")

st.title("GENERATIVE AI CHATBOT")

st.caption(
    "✨ Your dreamy little AI companion ✨"
)

st.caption(
    "Ask anything, explore ideas & let AI help you 💕"
)

st.write("")


# =========================================================
# CHAT INPUT
# =========================================================

prompt = st.text_area(
    "💌 What would you like to ask?",
    placeholder="✨ Ask me anything...",
    height=160
)


# =========================================================
# GENERATE
# =========================================================

generate = st.button(
    "🌸  Generate Response  ✨"
)


# =========================================================
# GEMINI RESPONSE
# =========================================================

if generate:

    if prompt.strip():

        with st.spinner("🌷 AI is thinking..."):

            try:

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

                st.subheader(
                    "💜 AI Response"
                )

                st.write(
                    response.text
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )

    else:

        st.warning(
            "🌸 Please enter a prompt first!"
        )


# =========================================================
# FOOTER
# =========================================================

st.caption(
    "Made with 💕 and a little AI magic ✨"
)