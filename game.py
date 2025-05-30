import streamlit as st
import time
import random

# Setup page
st.set_page_config(
    page_title="🔮 Mind Reader Magic",
    page_icon="🔮",
    layout="centered"
)

# Custom styling with animations and magical effects
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #e2e8f0;
    }
    
    .main-header {
        text-align: center;
        background: linear-gradient(45deg, #ffd700, #ff6b6b, #4ecdc4, #45b7d1);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Cinzel', serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        animation: gradientShift 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .sub-header {
        text-align: center;
        color: #94a3b8;
        font-size: 1.3rem;
        margin-bottom: 2rem;
        font-style: italic;
        opacity: 0.9;
    }
    
    .magic-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(51, 65, 85, 0.6));
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(148, 163, 184, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        margin: 1.5rem 0;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .magic-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .magic-card:hover::before {
        left: 100%;
    }
    
    .magic-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
    }
    
    .step-header {
        color: #ffd700;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .step-number {
        background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
        color: white;
        width: 35px;
        height: 35px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .result-card {
        background: linear-gradient(135deg, #16a34a, #22c55e, #15803d);
        background-size: 200% 200%;
        animation: resultGlow 2s ease-in-out infinite;
        padding: 2.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        margin: 2rem 0;
        box-shadow: 0 0 30px rgba(34, 197, 94, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    @keyframes resultGlow {
        0%, 100% { 
            background-position: 0% 50%;
            box-shadow: 0 0 30px rgba(34, 197, 94, 0.4);
        }
        50% { 
            background-position: 100% 50%;
            box-shadow: 0 0 40px rgba(34, 197, 94, 0.6);
        }
    }
    
    .magic-button {
        background: linear-gradient(135deg, #6366f1, #7c3aed, #8b5cf6);
        background-size: 200% 200%;
        color: white;
        padding: 0.8rem 2rem;
        font-weight: 600;
        border-radius: 30px;
        border: none;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
        animation: buttonPulse 2s ease-in-out infinite;
    }
    
    @keyframes buttonPulse {
        0%, 100% { 
            background-position: 0% 50%;
            transform: scale(1);
        }
        50% { 
            background-position: 100% 50%;
            transform: scale(1.05);
        }
    }
    
    .magic-button:hover {
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.4);
        animation: none;
        background-position: 100% 50%;
    }
    
    .calculation-box {
        background: rgba(15, 23, 42, 0.8);
        border: 2px solid #4ade80;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
        font-size: 1.2rem;
        text-align: center;
        color: #4ade80;
        box-shadow: 0 0 20px rgba(74, 222, 128, 0.2);
    }
    
    .digit-display {
        background: linear-gradient(135deg, #1e293b, #334155);
        border: 2px solid #64748b;
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem;
        display: inline-block;
        font-size: 1.5rem;
        font-weight: bold;
        color: #ffd700;
        min-width: 60px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    
    .digit-display:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 215, 0, 0.3);
    }
    
    .progress-bar {
        background: rgba(30, 41, 59, 0.8);
        height: 8px;
        border-radius: 4px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1);
        height: 100%;
        border-radius: 4px;
        transition: width 0.5s ease;
        box-shadow: 0 0 10px rgba(70, 183, 209, 0.5);
    }
    
    .sparkle {
        position: absolute;
        color: #ffd700;
        font-size: 1.5rem;
        animation: sparkle 2s ease-in-out infinite;
        pointer-events: none;
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0); }
        50% { opacity: 1; transform: scale(1); }
    }
    
    .stNumberInput > div > div > input {
        background: rgba(30, 41, 59, 0.8);
        border: 2px solid #64748b;
        border-radius: 12px;
        color: #e2e8f0;
        font-size: 1.2rem;
        padding: 0.8rem;
        text-align: center;
        font-weight: bold;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #4ade80;
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "game_state" not in st.session_state:
    st.session_state.game_state = "start"
if "current_step" not in st.session_state:
    st.session_state.current_step = 1
if "chosen_digits" not in st.session_state:
    st.session_state.chosen_digits = []
if "digits_sum" not in st.session_state:
    st.session_state.digits_sum = 0
if "combined_number" not in st.session_state:
    st.session_state.combined_number = 0
if "subtraction_result" not in st.session_state:
    st.session_state.subtraction_result = 0
if "hidden_digit" not in st.session_state:
    st.session_state.hidden_digit = None
if "remaining_digits" not in st.session_state:
    st.session_state.remaining_digits = []
if "sum_confirmed" not in st.session_state:
    st.session_state.sum_confirmed = False
if "number_confirmed" not in st.session_state:
    st.session_state.number_confirmed = False
if "subtraction_confirmed" not in st.session_state:
    st.session_state.subtraction_confirmed = False

# Main header with sparkles
st.markdown('''
<div style="position: relative;">
    <h1 class="main-header">🔮 Mind Reader Magic ✨</h1>
    <div class="sparkle" style="top: 10%; left: 20%; animation-delay: 0s;">✨</div>
    <div class="sparkle" style="top: 20%; right: 15%; animation-delay: 0.5s;">⭐</div>
    <div class="sparkle" style="bottom: 30%; left: 10%; animation-delay: 1s;">💫</div>
    <div class="sparkle" style="bottom: 10%; right: 25%; animation-delay: 1.5s;">✨</div>
</div>
''', unsafe_allow_html=True)

st.markdown('<p class="sub-header">Experience the ancient art of mind reading through mathematical magic</p>', unsafe_allow_html=True)

# Progress bar
def show_progress(step, total=6):
    progress = (step - 1) / (total - 1) * 100
    st.markdown(f'''
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress}%"></div>
    </div>
    <p style="text-align: center; color: #94a3b8; font-size: 0.9rem;">Step {step} of {total}</p>
    ''', unsafe_allow_html=True)

# Functions for each step
def step1_welcome():
    show_progress(1)
    st.markdown('<div class="magic-card">', unsafe_allow_html=True)
    st.markdown('<div class="step-header"><div class="step-number">1</div>Welcome, Seeker of Magic!</div>', unsafe_allow_html=True)
    st.write("""
    **Prepare to witness an ancient mathematical enchantment!**
    
    I will read your mind by revealing a digit you choose to hide from me. This mystical art has been passed down through generations of mathematicians and mystics.
    
    Are you ready to begin this magical journey? 🌟
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Begin the Magic", key="start_magic", help="Click to start your magical journey"):
            st.session_state.current_step = 2
            st.session_state.game_state = "step2"
            st.rerun()

def step2_choose_digits():
    show_progress(2)
    st.markdown('<div class="magic-card">', unsafe_allow_html=True)
    st.markdown('<div class="step-header"><div class="step-number">2</div>Choose Your Mystical Digits</div>', unsafe_allow_html=True)
    
    st.write("**Think of at least 2 different digits (0-9). Choose wisely, for they hold the key to the magic!**")
    
    if st.session_state.chosen_digits:
        st.write("**Your chosen digits:**")
        digits_html = "".join([f'<span class="digit-display">{digit}</span>' for digit in st.session_state.chosen_digits])
        st.markdown(f'<div style="text-align: center;">{digits_html}</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        digit = st.number_input("Add a mystical digit (0-9):", min_value=0, max_value=9, step=1, key="digit_input")
    
    with col2:
        st.write("") # Space
        st.write("") # Space
        if st.button("✨ Add Digit", key="add_digit"):
            if digit not in st.session_state.chosen_digits:
                st.session_state.chosen_digits.append(digit)
                st.rerun()
            else:
                st.warning("🔮 This digit already exists in your collection!")
    
    if len(st.session_state.chosen_digits) >= 2:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔮 Continue the Ritual", key="continue_step2"):
                st.session_state.current_step = 3
                st.session_state.game_state = "step3"
                st.session_state.digits_sum = sum(st.session_state.chosen_digits)  # Calculate sum for later use
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def step3_calculate_sum():
    show_progress(3)
    st.markdown('<div class="magic-card">', unsafe_allow_html=True)
    st.markdown('<div class="step-header"><div class="step-number">3</div>The Sacred Sum Calculation</div>', unsafe_allow_html=True)
    
    st.write("**Now, add all your chosen digits together in your mind. Focus your mental energy on this calculation...**")
    
    digits_html = " + ".join([f'<span style="color: #ffd700; font-weight: bold;">{digit}</span>' for digit in st.session_state.chosen_digits])
    st.markdown(f'<div class="calculation-box">{digits_html} = ?</div>', unsafe_allow_html=True)
    
    st.write("*Close your eyes, breathe deeply, and let the numbers flow through your consciousness...*")
    
    if not st.session_state.sum_confirmed:
        with st.spinner("✨ Sensing your mental calculations..."):
            time.sleep(1.5)
        
        st.write("**Have you completed the sacred addition in your mind?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Yes, I have the sum!", key="sum_ready"):
                st.session_state.sum_confirmed = True
                st.rerun()
        
        with col2:
            if st.button("🤔 Let me recalculate", key="recalculate"):
                st.info("Take your time... The magic requires precision. Focus your mind and try again.")
    else:
        st.success("🌟 Excellent! The cosmic energies confirm your mental calculation!")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔮 Continue the Mystical Journey", key="continue_step3"):
                st.session_state.current_step = 4
                st.session_state.game_state = "step4"
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def step4_combine_digits():
    show_progress(4)
    st.markdown('<div class="magic-card">', unsafe_allow_html=True)
    st.markdown('<div class="step-header"><div class="step-number">4</div>The Great Combination</div>', unsafe_allow_html=True)
    
    st.write("**Now combine your digits to form a single mystical number. Arrange them in any order your spirit desires!**")
    st.write("*For example: digits 2, 5, 7 could become 257, 275, 527, 572, 725, or 752*")
    
    digits_display = "".join([f'<span class="digit-display">{digit}</span>' for digit in st.session_state.chosen_digits])
    st.markdown(f'<div style="text-align: center;">Your mystical digits: {digits_display}</div>', unsafe_allow_html=True)
    
    st.write("*Let your intuition guide you... Feel the cosmic alignment as you arrange these sacred numbers...*")
    
    if not st.session_state.number_confirmed:
        with st.spinner("🔮 Sensing your mental combination..."):
            time.sleep(1.5)
        
        st.write("**Have you formed your mystical number in your mind?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✨ Yes, I have my number!", key="number_ready"):
                st.session_state.number_confirmed = True
                st.session_state.combined_number = 100  # Placeholder
                st.rerun()
        
        with col2:
            if st.button("🤔 Let me rearrange", key="rearrange"):
                st.info("Take your time to feel the perfect arrangement... The universe will guide you.")
    else:
        st.success("🎊 Magnificent! Your mystical number pulses with cosmic energy!")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🌟 Proceed to the Next Ritual", key="continue_step4"):
                st.session_state.current_step = 5
                st.session_state.game_state = "step5"
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def step5_subtraction():
    show_progress(5)
    st.markdown('<div class="magic-card">', unsafe_allow_html=True)
    st.markdown('<div class="step-header"><div class="step-number">5</div>The Mystical Subtraction</div>', unsafe_allow_html=True)
    
    st.write("**Now for the crucial enchantment! In your mind, subtract the sum of your original digits from your combined number.**")
    
    st.markdown(f'<div class="calculation-box">YOUR COMBINED NUMBER - {st.session_state.digits_sum} = ?</div>', unsafe_allow_html=True)
    
    st.write("*This is where the ancient magic begins to weave its spell... Feel the cosmic forces aligning as you perform this sacred calculation...*")
    
    if not st.session_state.subtraction_confirmed:
        with st.spinner("🔮 The mystical energies are building..."):
            time.sleep(2)
        
        st.write("**Have you completed the mystical subtraction in your mind?**")
        st.write("*Remember this result - it holds the key to the magic!*")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚡ Yes, I have the result!", key="subtraction_ready"):
                st.session_state.subtraction_confirmed = True
                st.session_state.subtraction_result = 0  # Placeholder
                st.rerun()
        
        with col2:
            if st.button("🧮 Let me recalculate", key="recalculate_sub"):
                st.info("Take your time with this crucial step... The accuracy of this calculation is essential for the magic to work!")
    else:
        st.success("🌟 Excellent! The cosmic calculation is complete!")
        st.write("**The magical transformation has occurred... Your number now carries mystical properties!**")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎭 Prepare for the Final Ritual", key="continue_step5"):
                st.session_state.current_step = 6
                st.session_state.game_state = "step6"
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def step6_hide_digit():
    show_progress(6)
    st.markdown('<div class="magic-card">', unsafe_allow_html=True)
    st.markdown('<div class="step-header"><div class="step-number">6</div>The Final Concealment</div>', unsafe_allow_html=True)
    
    st.write("**Now comes the moment of truth! From your subtraction result, hide ONE digit in your mind and tell me the remaining digits.**")
    st.write("*This is where the ancient art of mind reading reveals itself...*")
    
    st.write("**Look at your subtraction result. Choose one digit to conceal from me - guard it in your thoughts!**")
    st.write("*The digit you hide will be the one I divine through mystical calculation...*")
    
    with st.spinner("🔮 Preparing the mind-reading ritual..."):
        time.sleep(1.5)
    
    if st.session_state.remaining_digits:
        st.write("**The digits you've revealed to me:**")
        entered_html = "".join([f'<span class="digit-display">{digit}</span>' for digit in st.session_state.remaining_digits])
        st.markdown(f'<div style="text-align: center;">{entered_html}</div>', unsafe_allow_html=True)
    
    st.write("**Enter the digits you're willing to reveal (all except the one you're hiding):**")
    
    col1, col2 = st.columns(2)
    with col1:
        digit = st.number_input("Reveal a digit:", min_value=0, max_value=9, step=1, key="remaining_digit_input")
    
    with col2:
        st.write("")
        st.write("")
        if st.button("✨ Reveal This Digit", key="add_remaining"):
            st.session_state.remaining_digits.append(digit)
            st.rerun()
    
    if len(st.session_state.remaining_digits) >= 1:
        st.write("*I can sense the hidden digit calling to me through the mystical realm...*")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔮 DIVINE MY HIDDEN DIGIT!", key="reveal_magic", help="Click to witness the mind reading magic!"):
                st.session_state.game_state = "result"
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def calculate_hidden_digit(visible_digits):
    total = sum(visible_digits)
    remainder = total % 9
    return (9 - remainder) % 9

def show_result():
    st.markdown('<div style="text-align: center; margin: 2rem 0;">', unsafe_allow_html=True)
    
    with st.spinner("🔮 Peering into the mystical realm..."):
        time.sleep(2)
    
    st.balloons()
    
    hidden = calculate_hidden_digit(st.session_state.remaining_digits)
    
    st.markdown(f'''
    <div class="result-card">
        🎭 THE HIDDEN DIGIT IS: {hidden} 🎭
    </div>
    ''', unsafe_allow_html=True)
    
    # Magical explanation
    with st.expander("🧙‍♂️ Reveal the Ancient Secret"):
        st.markdown('''
        **The Mathematical Magic Behind the Trick:**
        
        This enchantment relies on the mystical properties of the number 9!
        
        ✨ When you subtract the sum of digits from any number, the result is always divisible by 9.
        
        🔮 The sum of digits in any multiple of 9 is also a multiple of 9.
        
        ⚡ So when you hide one digit, I simply calculate: `9 - (sum of visible digits % 9)`
        
        This ancient mathematical principle has been fascinating minds for centuries!
        ''')
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🌟 Experience the Magic Again", key="play_again"):
            # Reset all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# Main app flow
if st.session_state.game_state == "start":
    step1_welcome()
elif st.session_state.game_state == "step2":
    step2_choose_digits()
elif st.session_state.game_state == "step3":
    step3_calculate_sum()
elif st.session_state.game_state == "step4":
    step4_combine_digits()
elif st.session_state.game_state == "step5":
    step5_subtraction()
elif st.session_state.game_state == "step6":
    step6_hide_digit()
elif st.session_state.game_state == "result":
    show_result()