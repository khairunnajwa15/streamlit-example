import streamlit as st
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="My Online Resume",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

# Session State remembers information while the user interacts
# with the Streamlit application.

if "profile_views" not in st.session_state:
    st.session_state.profile_views = 0

if "show_contact" not in st.session_state:
    st.session_state.show_contact = False


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    .main-title {
        font-size: 45px;
        font-weight: bold;
        color: #1f3a56;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 20px;
        color: #666666;
        margin-top: 0px;
    }

    .section-title {
        background-color: #1f3a56;
        color: white;
        padding: 8px;
        text-align: center;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .profile-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #dddddd;
        background-color: #f8f9fa;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📋 Resume Menu")

st.sidebar.write("Use the controls below to interact with my resume.")

# USER EVENT 1 - Checkbox
show_skills = st.sidebar.checkbox(
    "Show my skills",
    value=True
)

# USER EVENT 2 - Selectbox
language = st.sidebar.selectbox(
    "Choose language",
    ["English", "Malay"]
)

# USER EVENT 3 - Slider
skill_level = st.sidebar.slider(
    "Programming Skill Level",
    min_value=0,
    max_value=100,
    value=75
)

st.sidebar.divider()

st.sidebar.write("### Resume Statistics")

st.sidebar.write(
    f"Profile views: {st.session_state.profile_views}"
)

st.sidebar.write(
    f"Selected skill level: {skill_level}%"
)


# ============================================================
# HEADER
# ============================================================

header_col1, header_col2 = st.columns([1, 3])

with header_col1:

    try:
        st.image(
            "profile.jpg",
            width=200
        )
    except:
        st.info("Put your profile photo in the project folder as profile.jpg")


with header_col2:

    st.markdown(
        '<div class="main-title">KHAIRUN NAJWA BINTI ROZAIDI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Computer Science Student</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Welcome to my online resume. "
        "This website demonstrates my education, skills, "
        "experience and projects."
    )


st.divider()


# ============================================================
# METRIC SECTION
# ============================================================

st.subheader("📊 Resume Overview")

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric(
        label="Projects",
        value="1"
    )

with metric2:
    st.metric(
        label="Programming Languages",
        value="3"
    )

with metric3:
    st.metric(
        label="Certificates",
        value="4"
    )

with metric4:
    st.metric(
        label="CGPA",
        value="3.35"
    )


st.divider()


# ============================================================
# MAIN RESUME - TWO COLUMNS
# ============================================================

left_column, right_column = st.columns([1, 2])


# ============================================================
# LEFT COLUMN
# ============================================================

with left_column:

    st.markdown(
        '<div class="section-title">ABOUT ME</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        I am a motivated Computer Science student who is interested
        in networking, cybersecurity, programming and information
        technology. I enjoy learning new technologies and developing
        practical projects.
        """
    )


    # --------------------------------------------------------
    # CONTACT
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">CONTACT</div>',
        unsafe_allow_html=True
    )

    st.write("📧 Email: khairunnajwa1576@gmail.com")
    st.write("📱 Phone: 019-7849789")
    st.write("📍 Location: Politeknik Mersing, Johor")


    # --------------------------------------------------------
    # POPOVER
    # --------------------------------------------------------

    with st.popover("📞 More Contact Information"):

        st.write("### Contact Me")

        st.write("Email: khairunnajwa1576@gmail.com")
        st.write("Phone: 019-7849789")
        st.write("LinkedIn: linkedin.com/in/student")


    # --------------------------------------------------------
    # LANGUAGES
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">LANGUAGES</div>',
        unsafe_allow_html=True
    )

    st.write("• English")
    st.write("• Malay")
    st.write("• Basic Korean")
    st.write("• Basic Arabic")


    # --------------------------------------------------------
    # SKILLS
    # --------------------------------------------------------

    if show_skills:

        st.markdown(
            '<div class="section-title">SKILLS</div>',
            unsafe_allow_html=True
        )

        st.write("• Python")
        st.write("• Computer Networking")
        st.write("• Cybersecurity")
        st.write("• HTML / CSS")
        st.write("• Database")
        st.write("• Problem Solving")


# ============================================================
# RIGHT COLUMN
# ============================================================

with right_column:

    # --------------------------------------------------------
    # TABS
    # --------------------------------------------------------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "💼 Experience",
            "🎓 Education",
            "💻 Projects",
            "📊 Data"
        ]
    )


    # ========================================================
    # TAB 1 - EXPERIENCE
    # ========================================================

    with tab1:

        st.markdown(
            '<div class="section-title">EXPERIENCE</div>',
            unsafe_allow_html=True
        )

        st.subheader("IT / Computer Science Student")

        st.write("2024 - Present")

        st.write(
            """
            Developed practical knowledge in computer networking,
            programming, cybersecurity and database management.
            Participated in academic projects and laboratory exercises.
            """
        )

        st.divider()

        st.subheader("Academic Projects")

        st.write("2025 - 2026")

        st.write(
            """
            Worked with classmates on several academic projects
            involving programming, networking and information systems.
            """
        )


    # ========================================================
    # TAB 2 - EDUCATION
    # ========================================================

    with tab2:

        st.markdown(
            '<div class="section-title">EDUCATION</div>',
            unsafe_allow_html=True
        )

        st.subheader("Bachelor of Computer Science")

        st.write("POLITEKNIK MERSING JOHOR")
        st.write("2024 - Present")

        st.write(
            """
            Relevant subjects include Computer Networks,
            Computer Security, Programming, Database Systems
            and Cloud Computing.
            """
        )

        st.divider()

        st.subheader("Previous Education")

        st.write("Your College / School")
        st.write("2021 - 2024")


    # ========================================================
    # TAB 3 - PROJECTS
    # ========================================================

    with tab3:

        st.markdown(
            '<div class="section-title">PROJECTS</div>',
            unsafe_allow_html=True
        )

        project_col1, project_col2 = st.columns(2)

        with project_col1:

            st.subheader("🌐 Network Project")

            st.write(
                """
                Designed and configured a computer network
                using Cisco Packet Tracer.
                """
            )

        with project_col2:

            st.subheader("🔐 Security Project")

            st.write(
                """
                Studied computer network security concepts
                and implemented basic security configurations.
                """
            )

        st.divider()

        st.subheader("🐍 Python Project")

        st.write(
            """
            Developed Python applications to demonstrate
            programming concepts and data processing.
            """)


    # ========================================================
    # TAB 4 - DATA
    # ========================================================

    with tab4:

        st.markdown(
            '<div class="section-title">PANDAS DATAFRAME</div>',
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # PANDAS DATA
        # ----------------------------------------------------

        education_data = pd.DataFrame(
            {
                "Institution": [
                    "Your University"
                    
                ],
                "Qualification": [
                    "Bachelor of Computer Science"
                    
                ],
                "Year": [
                    "2024 - Present"
                    
                ]
            }
        )


        # ----------------------------------------------------
        # STATIC DATAFRAME
        # ----------------------------------------------------

        st.subheader("Education Data")

        st.dataframe(
            education_data,
            use_container_width=True
        )


        # ----------------------------------------------------
        # DATA EDITOR
        # ----------------------------------------------------

        st.subheader("Editable Education Data")

        st.write(
            "You can edit the information in the table below."
        )

        edited_data = st.data_editor(
            education_data,
            num_rows="dynamic",
            use_container_width=True
        )

        st.write("Updated data:")

        st.dataframe(
            edited_data,
            use_container_width=True
        )


# ============================================================
# USER INTERACTION SECTION
# ============================================================

st.divider()

st.header("🖱️ Interactive Resume")


# ============================================================
# USER EVENT 4 - RADIO BUTTON
# ============================================================

st.subheader("1. Select a resume section")

selected_section = st.radio(
    "Which section would you like to see?",
    [
        "About Me",
        "Education",
        "Experience",
        "Projects"
    ],
    horizontal=True
)

st.write(
    f"You selected: **{selected_section}**"
)


# ============================================================
# USER EVENT 5 - BUTTON
# ============================================================

st.subheader("2. View Profile")

if st.button("👤 View My Profile"):

    st.session_state.profile_views += 1

    st.success(
        "Profile viewed successfully!"
    )

    st.write(
        f"This profile has been viewed "
        f"{st.session_state.profile_views} time(s)."
    )


# ============================================================
# USER EVENT 6 - TEXT INPUT
# ============================================================

st.subheader("3. Visitor Information")

visitor_name = st.text_input(
    "Enter your name"
)

if visitor_name:

    st.write(
        f"Hello **{visitor_name}**! "
        "Thank you for visiting my resume."
    )


# ============================================================
# USER EVENT 7 - TEXT AREA
# ============================================================

st.subheader("4. Leave a Message")

visitor_message = st.text_area(
    "Write a message for me"
)

if visitor_message:

    st.info(
        f"Your message: {visitor_message}"
    )


# ============================================================
# SKILL LEVEL RESULT
# ============================================================

st.subheader("💻 My Programming Skill")

st.progress(
    skill_level
)

st.write(
    f"Current selected skill level: {skill_level}%"
)


# ============================================================
# LANGUAGE RESPONSE
# ============================================================

st.subheader("🌐 Language Selection")

if language == "English":

    st.write(
        "Welcome to my online resume!"
    )

else:

    st.write(
        "Selamat datang ke resume dalam talian saya!"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "© 2026 Your Name | Online Resume created using Python and Streamlit"
)
