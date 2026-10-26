
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, time
from io import BytesIO

st.set_page_config(
    page_title="Celebrate AI | Event Planner",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- PREMIUM DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background:
      radial-gradient(ellipse at 5% 0%, #302052 0%, transparent 36%),
      radial-gradient(ellipse at 95% 5%, #55233f 0%, transparent 30%),
      #0b0b16;
    color: #f7f4ff;
}
.block-container {
    max-width: 1200px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}
h1, h2, h3 { color: #fff !important; }
p, label, .stMarkdown { color: #e4def3; }
.hero {
    padding: 35px 30px;
    border-radius: 26px;
    background: linear-gradient(120deg, #6d35c8 0%, #c13d93 55%, #f28b55 100%);
    box-shadow: 0 15px 45px #0005;
    margin-bottom: 25px;
}
.hero h1 {
    font-size: clamp(32px, 5vw, 54px);
    line-height: 1.1;
    font-weight: 800;
    margin: 8px 0;
}
.hero p { font-size: 16px; color: #fff; }
.pill {
    display: inline-block;
    background: #ffffff25;
    border: 1px solid #ffffff55;
    padding: 6px 12px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
}
.section-title {
    font-size: 24px;
    font-weight: 800;
    margin: 22px 0 12px;
    color: #fff;
}
.panel {
    background: linear-gradient(145deg, #1c1a2b, #171421);
    border: 1px solid #ffffff18;
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 14px;
}
.feature {
    background: #ffffff09;
    border: 1px solid #ffffff17;
    border-radius: 16px;
    padding: 17px;
    min-height: 115px;
}
.feature .emoji { font-size: 25px; }
.feature strong { font-size: 15px; color: #fff; }
.feature small { color: #c7bedb; }
div.stButton > button {
    border: 0;
    border-radius: 12px;
    min-height: 46px;
    font-weight: 700;
    color: white;
    background: linear-gradient(100deg, #8b5cf6, #ec4899);
    transition: 0.2s ease;
}
div.stButton > button:hover {
    border: 1px solid #fff;
    color: white;
    transform: translateY(-2px);
}
div[data-testid="stMetric"] {
    background: #ffffff09;
    border: 1px solid #ffffff18;
    border-radius: 15px;
    padding: 15px;
}
div[data-testid="stMetricLabel"] { color: #c9bfdc; }
div[data-testid="stMetricValue"] { color: #fff; }
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background: #171421;
    border-color: #4c4260;
}
.stTextInput input, .stNumberInput input {
    color: #fff;
}
hr { border-color: #ffffff20; }
.footer {
    text-align: center;
    color: #b6a9cd;
    font-size: 12px;
    padding: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
  <span class="pill">✨ YOUR PERSONAL EVENT ASSISTANT</span>
  <h1>Make moments<br>feel magical.</h1>
  <p>Plan your celebration, manage your budget, and bring your ideas to life.</p>
  <span class="pill">🎉 Plan smarter</span>
  <span class="pill">💜 Celebrate better</span>
</div>
""", unsafe_allow_html=True)

# ---------- FEATURE CARDS ----------
f1, f2, f3 = st.columns(3)
with f1:
    st.markdown("""
    <div class="feature">
      <div class="emoji">🎨</div>
      <strong>Personalised ideas</strong><br>
      <small>Ideas based on your event and theme.</small>
    </div>""", unsafe_allow_html=True)
with f2:
    st.markdown("""
    <div class="feature">
      <div class="emoji">💰</div>
      <strong>Smart budget</strong><br>
      <small>See where your celebration budget goes.</small>
    </div>""", unsafe_allow_html=True)
with f3:
    st.markdown("""
    <div class="feature">
      <div class="emoji">✅</div>
      <strong>Easy planning</strong><br>
      <small>Keep track of your event checklist.</small>
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="section-title">🎈 Create your celebration</div>',
            unsafe_allow_html=True)

# ---------- EVENT FORM ----------
with st.container(border=True):
    left, right = st.columns(2)

    with left:
        event_type = st.selectbox(
            "What are we celebrating?",
            ["Birthday Party", "College Fest", "Farewell Party",
             "Anniversary", "Wedding", "Graduation Party",
             "Festival Celebration", "Other Celebration"]
        )
        event_date = st.date_input("Event date", value=date.today())
        guests = st.number_input(
            "Expected guests", min_value=1, max_value=10000, value=30
        )
        event_time = st.time_input("Start time", value=time(18, 0))

    with right:
        budget = st.number_input(
            "Total budget (₹)", min_value=500,
            max_value=10000000, value=10000, step=500
        )
        theme = st.selectbox(
            "Choose a theme",
            ["Surprise me", "Elegant", "Colourful",
             "Traditional", "Minimal", "Nature-inspired",
             "Retro", "Dreamy pastel"]
        )
        location = st.text_input(
            "City or venue (optional)", placeholder="e.g. Ahmedabad"
        )
        extra = st.text_input(
            "Any special request? (optional)",
            placeholder="e.g. music, games, photo booth"
        )

    generate = st.button(
        "✨ Generate My Celebration Plan",
        type="primary",
        use_container_width=True
    )

# ---------- BUDGET ----------
st.markdown('<div class="section-title">💰 Your budget at a glance</div>',
            unsafe_allow_html=True)

allocations = {
    "Venue": budget * 0.30,
    "Food & Drinks": budget * 0.35,
    "Decorations": budget * 0.20,
    "Other": budget * 0.15
}

m1, m2, m3, m4 = st.columns(4)
m1.metric("🏛️ Venue", f"₹{allocations['Venue']:,.0f}")
m2.metric("🍽️ Food", f"₹{allocations['Food & Drinks']:,.0f}")
m3.metric("🎨 Decor", f"₹{allocations['Decorations']:,.0f}")
m4.metric("✨ Other", f"₹{allocations['Other']:,.0f}")

chart_df = pd.DataFrame({
    "Category": list(allocations.keys()),
    "Estimated cost (₹)": list(allocations.values())
})
fig = px.pie(
    chart_df, names="Category", values="Estimated cost (₹)",
    hole=0.60, color_discrete_sequence=["#a78bfa", "#f472b6",
                                         "#fb923c", "#38bdf8"]
)
fig.update_traces(
    textposition="inside", textinfo="percent+label",
    textfont_color="white"
)
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#f5efff",
    showlegend=False,
    margin=dict(t=15, b=15, l=10, r=10),
    annotations=[dict(
        text=f"₹{budget:,.0f}", x=0.5, y=0.5,
        font_size=19, font_color="white", showarrow=False
    )]
)
st.plotly_chart(fig, use_container_width=True)
st.caption("Budget allocations are estimates. Actual costs may differ.")

# ---------- EVENT PLAN ----------
def get_demo_ideas(kind, chosen_theme, guests, special):
    ideas = {
        "Birthday Party": [
            "Create a photo backdrop and a memorable cake table.",
            "Plan music, party games, and a group photo moment.",
            "Send invitations and confirm the guest list."
        ],
        "College Fest": [
            "Prepare a stage schedule and assign volunteer roles.",
            "Plan student activities and a registration desk.",
            "Confirm sound, seating, and venue arrangements."
        ],
        "Farewell Party": [
            "Create a memory wall with photos and messages.",
            "Plan speeches, music, and a slideshow.",
            "Arrange refreshments and a group photograph."
        ],
        "Anniversary": [
            "Create a photo timeline of favourite memories.",
            "Plan a meal and decorations that match the theme.",
            "Prepare a short toast or memory-sharing activity."
        ],
        "Wedding": [
            "Prepare a venue, guest, and vendor checklist.",
            "Coordinate food, decorations, and event timings.",
            "Assign a point of contact for each major task."
        ],
        "Graduation Party": [
            "Create a graduation photo corner.",
            "Plan short speeches and a celebration playlist.",
            "Arrange snacks and a group photo."
        ],
        "Festival Celebration": [
            "Choose decorations suitable for the festival.",
            "Plan food, music, and inclusive group activities.",
            "Make a checklist for setup and cleanup."
        ],
        "Other Celebration": [
            "Choose a suitable venue and a clear event theme.",
            "Plan food, decorations, and engaging activities.",
            "Prepare invitations and an event-day schedule."
        ]
    }
    result = ideas.get(kind, ideas["Other Celebration"])
    result = result + [
        f"Plan for approximately {guests} guests and keep spending within budget."
    ]
    if special.strip():
        result.append(f"Special request to organise: {special.strip()}.")
    return result

if "plan" not in st.session_state:
    st.session_state.plan = None

if generate:
    prompt = f"""
You are a practical, creative event-planning assistant.
Create a useful event plan using the details below.
Event: {event_type}
Date: {event_date}
Time: {event_time.strftime('%I:%M %p')}
Guests: {guests}
Budget: INR {budget}
Theme preference: {theme}
City/venue: {location or 'Not specified'}
Special request: {extra or 'None'}
Budget allocation estimates: {allocations}

Return:
1. One short, exciting plan title.
2. A short description.
3. Exactly 5 practical event ideas.
4. A simple 5-step preparation timeline.
5. Three budget-saving tips.
Keep it realistic, beginner-friendly, and within the stated budget.
Do not claim that vendors or bookings are confirmed.
"""

    api_key = ""
    try:
        api_key = st.secrets.get("GEMINI_API_KEY", "")
    except Exception:
        api_key = ""

    ai_text = ""
    if api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )
            ai_text = response.text or ""
      
        
        except Exception as e:
               st.error(f"Gemini error type: {type(e).__name__}")
               st.error(f"Error details: {e}")
                

    if ai_text.strip():
        st.session_state.plan = {
            "ai": True,
            "text": ai_text,
            "ideas": [],
            "title": f"Your {event_type} Plan"
        }
    else:
        st.session_state.plan = {
            "ai": False,
            "text": "",
            "ideas": get_demo_ideas(event_type, theme, guests, extra),
            "title": f"Your {event_type} Plan"
        }

# ---------- DISPLAY PLAN ----------
if st.session_state.plan:
    plan = st.session_state.plan

    st.markdown('<div class="section-title">✨ Your celebration plan</div>',
                unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader(plan["title"])
    st.write(f"📅 **Date:** {event_date.strftime('%d %B %Y')}")
    st.write(f"🕒 **Time:** {event_time.strftime('%I:%M %p')}")
    st.write(f"👥 **Guests:** {guests}")
    st.write(f"💰 **Budget:** ₹{budget:,.0f}")
    st.write(f"🎨 **Theme:** {theme}")
    st.write(f"📍 **Location:** {location or 'Not specified'}")

    if plan["ai"]:
        st.success("🤖 Generated using Gemini AI")
        st.markdown(plan["text"])
    else:
        st.info(
            "Demo mode: these are built-in suggestions. "
            "Add your Gemini API key to enable real AI-generated plans."
        )
        st.markdown("### 🎯 Suggested ideas")
        for idea in plan["ideas"]:
            st.markdown(f"- {idea}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">✅ Event checklist</div>',
                unsafe_allow_html=True)

    tasks = [
        "Confirm venue and guest list",
        "Send invitations",
        "Arrange food and drinks",
        "Plan decorations",
        "Confirm music and activities",
        "Review the final budget"
    ]

    checked = []
    checklist_cols = st.columns(2)
    for i, task in enumerate(tasks):
        with checklist_cols[i % 2]:
            is_checked = st.checkbox(task, key=f"task_{i}")
            if is_checked:
                checked.append(task)

    st.progress(len(checked) / len(tasks))
    st.caption(f"{len(checked)} of {len(tasks)} tasks completed")

    plan_text = f"""CELEBRATE AI — EVENT PLAN

Event: {event_type}
Date: {event_date.strftime('%d %B %Y')}
Time: {event_time.strftime('%I:%M %p')}
Guests: {guests}
Budget: INR {budget:,.0f}
Theme: {theme}
Location: {location or 'Not specified'}
Special request: {extra or 'None'}

BUDGET ESTIMATES
""" + "\n".join(
        f"{name}: INR {amount:,.0f}"
        for name, amount in allocations.items()
    )

    if plan["ai"]:
        plan_text += "\n\nAI-GENERATED PLAN\n" + plan["text"]
    else:
        plan_text += "\n\nDEMO SUGGESTIONS\n" + "\n".join(
            "- " + idea for idea in plan["ideas"]
        )

    plan_text += "\n\nCHECKLIST\n" + "\n".join(
        ("[x] " if task in checked else "[ ] ") + task for task in tasks
    )

    st.download_button(
        "📥 Download My Event Plan",
        data=plan_text,
        file_name="my_celebration_plan.txt",
        mime="text/plain",
        use_container_width=True
    )

    st.markdown('<div class="section-title">🎊 Ready to celebrate?</div>',
                unsafe_allow_html=True)

    if st.button(
        "🎉 Confirm & Celebrate!",
        type="primary",
        use_container_width=True
    ):
        st.balloons()
        st.snow()
        st.success("Your celebration plan is confirmed! Let the fun begin! 🎉")
        st.toast("A new celebration is on the way!", icon="🎊")
        st.markdown("""
        <div class="hero" style="text-align:center">
          <h1>🎉 It's Celebration Time! 🎉</h1>
          <p>Your plan is ready. Make memories, share smiles, and enjoy your day!</p>
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="panel">
      <h3>💫 Your next memorable moment starts here</h3>
      <p>Fill in your event details above and click
      <b>Generate My Celebration Plan</b> to get started.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
  CELEBRATE AI · Student Project · Plan with creativity, celebrate with joy ✨
</div>
""", unsafe_allow_html=True)
