FROM python:3.8

WORKDIR /app

RUN pip install streamlit

COPY ./sample_quiz-app.py /app/

CMD ["streamlit", "run", "sample_quiz-app.py"]
