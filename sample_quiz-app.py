import streamlit as st

# アプリのタイトル
st.title("QuizApp")

# サブタイトルや説明文
st.subheader("Sample")
st.write("This is the sample app.")

# クイズのデータ
questions_data = {
    "Question1": {
        "question": "Who was the second US President?",
        "options": ["John Adams", "George Washington", "Abraham Lincoln", "Thomas Jefferson"],
        "answer": "John Adams"
    },
    "Question2": {
        "question": "Which event triggered World War One?",
        "options": ["The assassination of Archduke Francis Ferdinand", "Germany's invasion of Poland", "The sinking of Lusitania", "The tsar's refusal of an offer to visit Germany"],
        "answer": "The assassination of Archduke Francis Ferdinand"
    }
}

# クイズの選択
selected_answer = st.selectbox("Select the question number:", list(questions_data.keys()))

# 選択されたクイズの問題を取得
question = questions_data[selected_answer]
st.write(question["question"])

# 選択肢を表示
options = question["options"]
selected_option = st.radio("Select your answer:", options)

if st.button("Answer"):
    if selected_option == question["answer"]:
        st.success("That is the correct answer!!")
    else:
        st.error(f"Unfortunately, that is the wrong answer!! The correct answer is {question['answer']}.")
