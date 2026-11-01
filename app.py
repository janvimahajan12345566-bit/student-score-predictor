

import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("student_score_model.pkl")

model = load_model()

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef2ff, #fdf2f8, #eff6ff);
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #3730a3;
    text-align: center;
    padding: 12px;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 17px;
    margin-bottom: 25px;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.07);
}

div.stButton > button {
    background: linear-gradient(90deg, #4f46e5, #9333ea);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.02);
    color: white;
}

.result-card {
    background: linear-gradient(120deg, #4f46e5, #9333ea);
    color: white;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    animation: revealScore 1s ease-out;
}

@keyframes revealScore {
    from {
        opacity: 0;
        transform: translateY(30px) scale(0.9);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.small-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    min-height: 120px;
}

.section-heading {
    color: #3730a3;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🎓 Student Score Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart predictions powered by Machine Learning</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- NAVIGATION TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Dashboard",
    "🔮 Predict Score",
    "📊 Data Analytics",
    "⚡ Model Performance",
    "ℹ️ About Project"
])

# ==================================================
# TAB 1: DASHBOARD
# ==================================================
with tab1:
    st.markdown("## 👋 Welcome to Your Dashboard")

    st.write(
        "Explore how academic habits and lifestyle factors "
        "relate to student examination performance."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="small-card">
            <h2>📚 20,000</h2>
            <p>Student Records</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="small-card">
            <h2>🎯 11</h2>
            <p>Input Features</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="small-card">
            <h2>🤖 73.30%</h2>
            <p>Model R² Score</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown("### ✨ What can you do here?")

    left, right = st.columns(2)

    with left:
        st.info(
            "🔮 **Predict Score**\n\n"
            "Enter student details and get a predicted exam score."
        )

        st.info(
            "📊 **Explore Analytics**\n\n"
            "Understand the relationship between study habits and scores."
        )

    with right:
        st.info(
            "⚡ **Check Model Performance**\n\n"
            "Explore how well the machine learning model performs."
        )

        st.info(
            "💡 **Learn About the Project**\n\n"
            "Discover the technology and methods behind this application."
        )

    st.success("Your learning journey starts here! 🚀")


# ==================================================
# TAB 2: PREDICT SCORE
# ==================================================
with tab2:
    st.markdown("## 🔮 Predict Your Exam Score")

    st.write(
        "Enter the following details to generate your estimated score."
    )

    with st.form("prediction_form"):

        st.markdown("### 👤 Student Information")

        col1, col2 = st.columns(2)

        with col1:
            age = st.slider("Age", 17, 24, 20)

            gender = st.selectbox(
                "Gender", ["male", "female", "other"]
            )

            course = st.selectbox(
                "Course",
                ["b.tech", "bca", "b.sc", "bba",
                 "ba", "b.com", "diploma"]
            )

        with col2:
            study_hours = st.slider(
                "Daily Study Hours", 0.08, 7.91, 4.0
            )

            attendance = st.slider(
                "Class Attendance (%)", 40.6, 99.4, 70.0
            )

            internet = st.selectbox(
                "Internet Access", ["yes", "no"]
            )

        st.divider()

        st.markdown("### 🌙 Lifestyle Details")

        col3, col4 = st.columns(2)

        with col3:
            sleep_hours = st.slider(
                "Daily Sleep Hours", 4.1, 9.9, 7.0
            )

            sleep_quality = st.selectbox(
                "Sleep Quality", ["poor", "average", "good"]
            )

            study_method = st.selectbox(
                "Study Method",
                ["coaching", "online videos", "mixed",
                 "self-study", "group study"]
            )

        with col4:
            facility_rating = st.selectbox(
                "Study Facility Rating", ["low", "medium", "high"]
            )

            exam_difficulty = st.selectbox(
                "Exam Difficulty", ["hard", "moderate", "easy"]
            )

        submitted = st.form_submit_button(
            "🚀 Predict My Exam Score",
            use_container_width=True
        )

    if submitted:

        input_data = pd.DataFrame([{
            "age": age,
            "gender": gender,
            "course": course,
            "study_hours": study_hours,
            "class_attendance": attendance,
            "internet_access": internet,
            "sleep_hours": sleep_hours,
            "sleep_quality": sleep_quality,
            "study_method": study_method,
            "facility_rating": facility_rating,
            "exam_difficulty": exam_difficulty
        }])

        prediction = model.predict(input_data)[0]
        prediction = max(0, min(100, prediction))

        st.balloons()
        st.toast("Your prediction is ready! 🎉")

        st.markdown(
            f"""
            <div class="result-card">
                <h2>🎉 Your Predicted Exam Score</h2>
                <h1 style="font-size:55px;">{prediction:.2f}</h1>
                <h3>Out of 100</h3>
                <p>Your machine learning prediction is ready!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(int(prediction))

        if prediction >= 80:
            st.success("🌟 Excellent predicted performance!")
        elif prediction >= 60:
            st.info("👏 Keep learning and building your skills!")
        else:
            st.info(
                "💪 Use this estimate to reflect on your study habits "
                "and identify areas for improvement."
            )

        st.caption(
            "Note: This is a model-generated estimate, not a guaranteed "
            "exam result."
        )


# ==================================================
# TAB 3: DATA ANALYTICS
# ==================================================
with tab3:
    st.markdown("## 📊 Student Data Analytics")

    st.write(
        "Explore selected relationships found during "
        "the analysis of the dataset."
    )

    st.metric("Average Exam Score", "62.51 / 100")

    correlation_data = pd.DataFrame({
        "Feature": [
            "Study Hours",
            "Class Attendance",
            "Sleep Hours",
            "Age"
        ],
        "Correlation": [0.72, 0.31, 0.13, 0.01]
    })

    st.markdown("### 📈 Feature Correlation with Exam Score")

    chart_data = correlation_data.set_index("Feature")
    st.bar_chart(chart_data)

    st.markdown("### 🔍 Key Insights")

    st.success(
        "📚 Study hours showed the strongest positive correlation "
        "with exam scores in this dataset (0.72)."
    )

    st.info(
        "🏫 Class attendance showed a positive correlation of 0.31."
    )

    st.info(
        "🌙 Sleep hours showed a smaller positive correlation of 0.13."
    )

    st.caption(
        "Correlation describes an association, not proof that one "
        "factor causes a change in exam scores."
    )


# ==================================================
# TAB 4: MODEL PERFORMANCE
# ==================================================
with tab4:
    st.markdown("## ⚡ Machine Learning Model Performance")

    st.write(
        "The Linear Regression model was selected after comparing "
        "it with Random Forest."
    )

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("R² Score", "73.30%")

    with m2:
        st.metric("MAE", "7.86")

    with m3:
        st.metric("RMSE", "9.77")

    st.divider()

    st.markdown("### 🤖 Model Comparison")

    comparison = pd.DataFrame({
        "Model": ["Linear Regression", "Random Forest"],
        "MAE": [7.86, 8.30],
        "RMSE": [9.77, 10.29],
        "R² Score": [0.733, 0.704]
    })

    st.dataframe(comparison, use_container_width=True)

    st.success(
        "🏆 Linear Regression performed better on the test metrics "
        "and was selected as the final model."
    )

    st.markdown("### 📖 What do these metrics mean?")

    st.write(
        "- **R² Score:** The model explains approximately 73.3% "
        "of the variation in test scores.\n"
        "- **MAE:** The average absolute prediction error was "
        "approximately 7.86 marks.\n"
        "- **RMSE:** The root mean squared prediction error was "
        "approximately 9.77 marks."
    )


# ==================================================
# TAB 5: ABOUT PROJECT
# ==================================================
with tab5:
    st.markdown("## ℹ️ About This Project")

    st.write(
        "The Student Exam Score Predictor is a machine learning "
        "application designed to estimate student examination scores "
        "using academic and lifestyle information."
    )

    st.markdown("### 🛠️ Technologies Used")

    technologies = [
        "🐍 Python",
        "📊 Pandas",
        "🤖 Scikit-learn",
        "🎨 Streamlit",
        "📦 Joblib",
        "📈 Machine Learning"
    ]

    for technology in technologies:
        st.write("• " + technology)

    st.markdown("### 📚 Project Details")

    st.write("**Dataset:** 20,000 student records")
    st.write("**Input Features:** 11")
    st.write("**Selected Model:** Linear Regression")
    st.write("**Target Variable:** Exam Score")

    st.divider()

    st.markdown("### 💡 Project Objective")

    st.write(
        "To demonstrate how machine learning can use student-related "
        "data to estimate examination performance and explore "
        "patterns in academic habits."
    )

    st.success("Thank you for exploring my project! 🎓")


# ---------------- FOOTER ----------------
st.divider()

st.markdown(
    "<center>🎓 Student Score Predictor | "
    "Machine Learning Project</center>",
    unsafe_allow_html=True
)
