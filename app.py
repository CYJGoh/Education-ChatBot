import streamlit as st
from transformers import pipeline

st.title('COS30081 Education Chatbot')
st.info('This is a Education Chatbot prototype created by Clement Goh Yung Jing 101218668 for COS30081 FNLP D & HD Task')

# loading model
model_checkpoint = r"roberta-finetuned-squad-50k"
question_answerer = pipeline("question-answering", model=model_checkpoint)
st.success("The model is loaded")

question = ""
context = """
    COS30081 is an Artificial Intelligence major unit. The unit name is Fundamentals of Natural Language Processing (FNLP). Its unit code is COS30081. The unit has a total contact hours of 48 hours. It has two pre-requisite units which are COS20015 Fundamentals of Data Management and COS30019 Introduction to Artificial Intelligence. The unit is delivered in blended mode - physical and online. The unit is a portfolio unit which means the assesments are consist of lab tasks and assignments. 

    The aim of the unit is to introduce students to the essential natural language processing (NLP) tasks and techniques. Students will learn skills to carry out basic text data pre-processing, feature extraction, building and evaluating a text classifier, and visualising NLP results. This unit also exposes students to an advanced NLP technique. 

    The unit has 4 unit learning outcomes (ULO) which are explain the basics of computational linguistics, prepare textual data into suitable representation for text analytics, apply exploratory data analysis and visualisation techniques to textual data, and develop and evaluate text classifiers for general natural language processing tasks. 

    This unit may contribute to the development of 3 Swinburne Graduate Attributes which are communication skills, teamwork skills, and digital literacies. The unit's content are basic string analysis techniques, text wrangling, web scrapping and pre-processing, feature extraction, text classifiers information retreival evaluation, visualisation and advanced NLP technique, which may include only one of the following topics: topic modelling, text summarization, vector representation, deep learning, or sentiment analysis.

    There is one unit teaching staff who is Dr Joel Than Chia Ming who is also the lecturer and tutor of this unit . He can be contacted through his email which is jcmthan@swinburne.edu.my. The learning and teaching structure of the unit consist of two parts which are lectures and tutorials of 24 hours of total contact hours each with two hours each of contact per week.

    The week by week schedule of the unit for Semester 1, 2022 can be observed below:
    Week 1 starts at 28 February - Topic: Introduction to NLP & Linguistics - Task & Assessment: Tutorial 1: Getting Started with Python
    Week 2 starts at 7 March - Topic: Word Tokenization: Dot product, Token improvement, Vocabulary - Task & Assessment: Tutorial 2: Word Tokenization and Pass Task #1
    Week 3 starts at 14 March  - Topic: TF-IDF vectors: Bag of words, Vectorization, Topic modelling - Task & Assessment: Tutorial 3: TF-IDF and Pass Task #2
    Week 4 starts at 21 March  - Topic: Semantic Analysis: LSA - Task & Assessment: Tutorial 4: Semantic Analysis and Pass Task #3
    Week 5 starts at 28 March  - Topic: Introduction to Deep Learning for NLP: Neural network, Word Vectors - Task & Assessment: Tutorial 5: Deep Learning Introduction and Pass Task #4
    Week 6 starts at 4 April - Topic: CNN basics and usage for NLP - Task & Assessment: Tutorial 6: Neural Networks & CNN and Pass Task #5
    Week 7 starts at 18 April - Topic: RNN & LSTM basics - Task & Assessment: Tutorial 7: RNN & LSTM and Pass Task #6
    Week 8 starts at 25 April - Topic: Transformer basics 1 - Task & Assessment: Tutorial 8: Transformer 1 and Pass Task #7
    Week 9 starts at 2 May - Topic: Transformer basics 2 - Task & Assessment: Tutorial 9: Transformer 2 and Pass Task #8
    Week 10 starts at 9 May - Topic: Performance Evaluation & Scaling up - Task & Assessment: Tutorial 10: Submission of Tutorial 10 and Pass Task #9
    Week 11 starts at 16 May - Topic: Showcase of Real-World Problems - Task & Assessment: Tutorial 11: Discussion of Assignment 2 and Pass Task #10
    Week 12 starts at 23 May - Topic: Conclusion and Wrap Up - Task & Assessment: Tutorial 12: Discussion of Assignment 2

    The assessments for this unit are Portfolio (for Pass and Credit) which is an individual task with 100% Weighting and Portfolio and Interview (for Distinction and High Distinction) which is an individual task with 100% Weighting.

    There will be a total of 10 pass tasks. Each pass task is released at the start of each week and is due two weeks after its release. There will be one Credit task which will be made available on 8 April and due on 6 May. There will be one D & HD task for Distinction and High Distinction (D & HD) grade which will be made available on 9 May and due on 3 June. The minimum requirement to pass this unit is to submit a passable portfolio, which means all pass tasks must be submitted and marked as complete. To achieve credit (C) grade, all pass tasks and the credit task must be submitted and marked as complete. To achieve distinction (D), all pass tasks, credit task and the D & HD task must be submitted and obtain at least 70 marks for it. To achieve high distinction (HD), all pass tasks, credit task and the D & HD task must be submitted and obtain at least 80 marks for it.

    Unless an extension has been approved, late submissions will result in a penalty. You will be penalised 10% of your mark for each working day the task is late, up to a maximum of 5 days. After 5 working days, a zero result will be recorded. 

    There will be two tutorial sessions available each week with one hybrid session and one online session. The hybrid tutorial is on the Monday of the week at 9:00 am. whereas, the online session is on the Thursday of the week at 11:00 am. 

    There will be one lecture session on the Tuesday of the week at 9:00 am. All sessions or classes will be recorded. All the lecture and tutorial materials as well as the recordings for all sessions are available on Canvas.
"""

with st.expander("Start chatting with bot here!"):
    st.write("""
        CGBOT: Hi, I'm CGBOT. The COS30081 Education virtual assistant. How may I help you today?
     """)

    question = st.text_area('Ask a question about COS30081!')

    if question != "":
        st.write(f"You: {question}")

        predict = question_answerer(question=question, context=context)
        answer = predict['answer']

        st.write(f"CGBOT: {answer}")
