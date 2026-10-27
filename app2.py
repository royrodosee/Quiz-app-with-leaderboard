import json
import random
from pathlib import Path

import streamlit as st

# Keep leaderboard.json in the same folder as this app.py file.
SCORE_FILE = Path(__file__).with_name("leaderboard.json")

# Questions from the original command-line quiz.
QUESTIONS = [
    {
        "question": "What is the output of print(2 ** 3) in Python?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. fun", "C. def", "D. define"],
        "answer": "C",
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. list", "D. bool"],
        "answer": "D",
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B",
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. input()", "B. show()", "C. print()", "D. display()"],
        "answer": "C",
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D",
    },
    {
        "question": "What is the result of 10 // 3 in Python?",
        "options": ["A. 3", "B. 3.33", "C. 1", "D. 4"],
        "answer": "A",
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A. add()", "B. append()", "C. insert_end()", "D. push()"],
        "answer": "B",
    },
    {
        "question": "Which loop repeats while a condition is True?",
        "options": ["A. if", "B. def", "C. while", "D. class"],
        "answer": "C",
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["A. object", "B. class", "C. create", "D. struct"],
        "answer": "B",
    },
]


def load_leaderboard():
    """Load saved scores, returning an empty list if the file is missing/invalid."""
    if not SCORE_FILE.exists():
        return []
    try:
        with SCORE_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_leaderboard(scores):
    """Persist scores to the JSON file."""
    with SCORE_FILE.open("w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4)


def save_result(name, score, total):
    scores = load_leaderboard()
    scores.append({"name": name, "score": score, "total": total})
    # Highest score first; preserve earlier entries when scores are tied.
    scores.sort(key=lambda player: player.get("score", 0), reverse=True)
    save_leaderboard(scores)


def start_new_quiz():
    quiz_questions = QUESTIONS.copy()
    random.shuffle(quiz_questions)
    st.session_state.quiz_questions = quiz_questions
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.quiz_finished = False
    st.session_state.result_saved = False


st.set_page_config(page_title="Python Quiz Game", page_icon="🧠", layout="centered")

st.title("🧠 Python Quiz Game")
st.caption("Test your Python knowledge, track your score, and compete on the leaderboard.")

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Choose a page", ["Play Quiz", "Leaderboard"])
    st.divider()
    st.write("**Quiz rules**")
    st.write("• 10 multiple-choice questions")
    st.write("• 1 point for each correct answer")
    st.write("• Questions are shuffled for each attempt")

if "quiz_questions" not in st.session_state:
    start_new_quiz()

if page == "Play Quiz":
    if not st.session_state.quiz_finished:
        st.subheader("Let's play!")
        player_name = st.text_input(
            "Enter your name",
            value=st.session_state.get("player_name", ""),
            placeholder="Your name",
        )
        st.session_state.player_name = player_name.strip() or "Anonymous"

        quiz_questions = st.session_state.quiz_questions
        index = st.session_state.current_question
        total = len(quiz_questions)

        st.progress(index / total)
        st.write(f"Question **{index + 1}** of **{total}**")

        item = quiz_questions[index]
        st.markdown(f"### {item['question']}")

        # Use a separate form for each question so an answer is submitted once.
        with st.form(key=f"question_form_{index}"):
            choice = st.radio(
                "Choose one answer:",
                item["options"],
                index=None,
                key=f"answer_widget_{index}",
            )
            submitted = st.form_submit_button(
                "Submit answer" if index < total - 1 else "Submit final answer",
                type="primary",
                use_container_width=True,
            )

        if submitted:
            if choice is None:
                st.warning("Please select an answer before continuing.")
            else:
                selected_letter = choice[0]
                st.session_state.answers[index] = selected_letter
                if index + 1 < total:
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    st.session_state.quiz_finished = True
                    st.rerun()

    else:
        quiz_questions = st.session_state.quiz_questions
        answers = st.session_state.answers
        total = len(quiz_questions)
        score = sum(
            1
            for index, item in enumerate(quiz_questions)
            if answers.get(index) == item["answer"]
        )
        percentage = score / total * 100

        st.subheader("🏁 Quiz Results")
        st.success(f"You scored **{score}/{total}** ({percentage:.0f}%).")
        if percentage == 100:
            st.balloons()
            st.write("Perfect score! Excellent work.")
        elif percentage >= 70:
            st.write("Great job! Keep practising.")
        elif percentage >= 40:
            st.write("Good effort—review the answers and try again.")
        else:
            st.write("Keep learning. You can improve with another attempt!")

        if not st.session_state.result_saved:
            save_result(st.session_state.get("player_name", "Anonymous"), score, total)
            st.session_state.result_saved = True

        with st.expander("Review your answers"):
            for index, item in enumerate(quiz_questions, start=1):
                selected = answers.get(index - 1)
                correct = item["answer"]
                is_correct = selected == correct
                st.markdown(f"**Q{index}. {item['question']}**")
                st.write(f"Your answer: {selected or 'Not answered'}")
                st.write(f"Correct answer: {correct}")
                if is_correct:
                    st.success("Correct")
                else:
                    st.error("Incorrect")
                st.divider()

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Play again", type="primary", use_container_width=True):
                start_new_quiz()
                st.rerun()
        with col2:
            if st.button("View leaderboard", use_container_width=True):
                st.session_state.show_leaderboard_hint = True
                st.rerun()

        if st.session_state.get("show_leaderboard_hint"):
            st.info("Choose **Leaderboard** in the sidebar to view the rankings.")

elif page == "Leaderboard":
    st.subheader("🏆 Leaderboard")
    scores = load_leaderboard()
    if not scores:
        st.info("No scores available yet. Play the quiz first!")
    else:
        top_scores = scores[:10]
        rows = [
            {
                "Rank": rank,
                "Player": player.get("name", "Anonymous"),
                "Score": f"{player.get('score', 0)}/{player.get('total', 10)}",
            }
            for rank, player in enumerate(top_scores, start=1)
        ]
        st.dataframe(rows, hide_index=True, use_container_width=True)

    if st.button("Start a new quiz", type="primary"):
        start_new_quiz()
        st.session_state.show_leaderboard_hint = False
        st.rerun()
