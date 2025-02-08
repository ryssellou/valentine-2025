import streamlit as st
import time

def main():
    st.set_page_config(page_title="A Love Quest", page_icon="💖")
    add_custom_css()
    
    if "page" not in st.session_state:
        st.session_state.page = "welcome"
    
    if st.session_state.page == "welcome":
        show_welcome_page()
    elif st.session_state.page == "quiz":
        show_quiz()
    elif st.session_state.page == "final":
        show_final_message()

def add_custom_css():
    st.markdown(
        """
        <style>
            body {
                background-color: #ffe4e1;
                color: #d63384;
                font-family: 'Comic Sans MS', cursive, sans-serif;
            }
            .stButton>button {
                background-color: #ff69b4;
                color: white;
                border-radius: 12px;
                font-size: 18px;
                font-weight: bold;
            }
            .stButton>button:hover {
                background-color: #ff1493;
            }
            .stRadio label {
                color: #d63384;
                font-weight: bold;
            }
            .valentine-text {
                font-size: 32px;
                font-weight: bold;
                color: #d63384;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_welcome_page():
    st.title("💌 A Love Quest 💌")
    st.subheader("Hi my wabii, I have a little adventure for you… Will you play along?")
    
    if st.button("Ofcourse!💘"):
        st.session_state.page = "quiz"
        st.rerun()  # Replaced experimental_rerun() with st.rerun()

def show_quiz():
    st.title("💞 The Love Quiz 💞")
    
    with st.form("quiz_form"):
        q1 = st.radio("Where did we first cross paths in this legendary love story?", 
              ["Angela's Debut (where fate intervened)", "Cafe Agapita (love at first sip?)", 
               "Silang (because all roads lead to us)", "All of the Above (destiny, obviously)"])

        q2 = st.radio("What’s my absolute favorite thing about you?", 
                    ["Your dazzling smile (it lights up my world)", 
                    "Your kindness (you're basically an angel)", 
                    "Your laugh (music to my ears)", 
                    "Everything (why choose just one?)"])

        q3 = st.radio("What am I absolutely TERRIFIED of?", 
                    ["Gutom na Jamie (a national emergency)",  
                    "It's the time of the month Jamie (RUN.)",
                    "Miss na miss ako na Jamie (dangerous levels of clinginess)",
                    "All of the Above (send help)"])

        q4 = st.radio("What’s our ultimate meryenda bonding snack?", 
                    ["Ice Cream (sweet, just like us)", 
                    "Fries (crispy, and irresistible—like you)", 
                    "Any Cravings (because cravings must be obeyed)", 
                    "All of the Above (food = love)"])

        q5 = st.radio("What’s one thing I **always** say to you?", 
                    ["I love you (duh, obviously)", 
                    "You’re my everything (and more)", 
                    "I miss you (even when you just left)", 
                    "All of the Above (because I mean it every time)"])

        q6 = st.radio("If I were a superhero, what would be my ultimate power?", 
                    ["Flying to see you faster (because long-distance is the villain (Parehas taga Dasma))",  
                    "Teleportation to be with you instantly (no more waiting!)", 
                    "Mind reading to always know what you want for meryenda (the ultimate life hack)",
                    "All of the above (hehe)"])

        submit = st.form_submit_button("Submit Answers")
                
        if submit:
            st.session_state.page = "final"
            st.rerun()  # Replaced experimental_rerun() with st.rerun()

def show_final_message():
    st.title("🎉 You’ve Completed the Quest! 🎉")
    
    st.markdown("<h3 class='valentine-text'>You’ve unlocked the greatest treasure… My heart. ❤️</h3>", unsafe_allow_html=True)
    
    st.markdown("<h5 class='valentine-text'>I know you've asked me to be your valentine, and my answer has always been yes, but I have been planning on making something like this. So, here I am, continuing with it. Ms. Ardiente, Will you be my Valentine?</h5>", unsafe_allow_html=True)

    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! 💖"):
            st.balloons()
            st.success("Yay! Can't wait for our date! 🥰")
    with col2:
        if st.button("Absolutely YES! 💞"):
            st.balloons()
            st.success("I knew it! I love you! 😘")

if __name__ == "__main__":
    main()
