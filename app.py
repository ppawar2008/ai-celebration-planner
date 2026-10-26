
import streamlit as st
from datetime import date, time

st.set_page_config(
    page_title="AI Celebration Planner",
    page_icon="🎉",
    layout="wide"
)

st.title("🎉 AI Celebration Planner")
st.write("Plan your celebration with a budget, checklist and creative ideas!")

st.divider()

st.header("🎈 Tell us about your event")

col1, col2 = st.columns(2)

with col1:
    event_type = st.selectbox(
        "Choose your event",
        [
            "Birthday Party",
            "College Fest",
            "Anniversary",
            "Wedding",
            "Farewell Party",
            "Other Celebration"
        ]
    )

    event_date = st.date_input(
        "Event date",
        value=date.today()
    )

    guests = st.number_input(
        "Expected number of guests",
        min_value=1,
        max_value=10000,
        value=30
    )

with col2:
    budget = st.number_input(
        "Total budget (₹)",
        min_value=500,
        max_value=10000000,
        value=10000,
        step=500
    )

    theme = st.selectbox(
        "Preferred theme",
        [
            "Surprise me",
            "Elegant",
            "Traditional",
            "Colourful",
            "Minimal",
            "Nature-inspired"
        ]
    )

    event_time = st.time_input(
        "Event starting time",
        value=time(18, 0)
    )

st.divider()

st.header("💰 Budget Planner")

venue = budget * 0.30
food = budget * 0.35
decoration = budget * 0.20
other = budget * 0.15

c1, c2, c3, c4 = st.columns(4)

c1.metric("🏛️ Venue", f"₹{venue:,.0f}")
c2.metric("🍕 Food", f"₹{food:,.0f}")
c3.metric("🎨 Decoration", f"₹{decoration:,.0f}")
c4.metric("✨ Other", f"₹{other:,.0f}")

st.caption(
    "These are estimated budget allocations. "
    "Adjust them according to your actual needs."
)

st.divider()

st.header("🤖 Celebration Ideas")

if st.button("✨ Generate My Event Plan", type="primary"):
    st.subheader(f"Your {event_type} Plan")

    st.write(f"📅 **Date:** {event_date.strftime('%d %B %Y')}")
    st.write(f"🕒 **Starting time:** {event_time.strftime('%I:%M %p')}")
    st.write(f"👥 **Guests:** {guests}")
    st.write(f"💰 **Budget:** ₹{budget:,.0f}")
    st.write(f"🎨 **Theme preference:** {theme}")

    if theme == "Surprise me":
        suggested_theme = "Colourful and joyful"
    else:
        suggested_theme = theme

    st.success(f"Suggested theme: {suggested_theme}")

    if event_type == "Birthday Party":
        ideas = [
            "Choose a birthday cake and photo backdrop.",
            "Arrange music and fun party games.",
            "Prepare invitations and a guest list."
        ]
    elif event_type == "College Fest":
        ideas = [
            "Plan a stage, sound system and event schedule.",
            "Arrange student activities and volunteers.",
            "Prepare registration and safety arrangements."
        ]
    elif event_type == "Anniversary":
        ideas = [
            "Choose a memorable photo display.",
            "Plan a special meal and decorations.",
            "Prepare a short celebration programme."
        ]
    elif event_type == "Wedding":
        ideas = [
            "Plan the venue and guest arrangements.",
            "Coordinate food, decorations and timings.",
            "Prepare a checklist for important ceremonies."
        ]
    elif event_type == "Farewell Party":
        ideas = [
            "Prepare a memory wall and photo slideshow.",
            "Plan speeches, music and group activities.",
            "Organise invitations and refreshments."
        ]
    else:
        ideas = [
            "Choose a suitable venue and event theme.",
            "Plan food, decorations and activities.",
            "Create a guest list and event schedule."
        ]

    st.subheader("🎯 Suggested Ideas")
    for idea in ideas:
        st.write(f"✅ {idea}")

    st.subheader("📝 Event Checklist")

    tasks = [
        "Confirm venue",
        "Prepare guest list",
        "Arrange food and drinks",
        "Organise decorations",
        "Confirm activities and music",
        "Check the final budget"
    ]

    for task in tasks:
        st.checkbox(task, key=f"{event_type}_{task}")

    plan_text = f"""
AI Celebration Planner - Event Plan

Event: {event_type}
Date: {event_date}
Time: {event_time.strftime('%I:%M %p')}
Guests: {guests}
Budget: Rs. {budget}
Theme: {suggested_theme}

Estimated budget:
Venue: Rs. {venue:.0f}
Food: Rs. {food:.0f}
Decoration: Rs. {decoration:.0f}
Other: Rs. {other:.0f}

Suggestions:
""" + "\n".join(f"- {idea}" for idea in ideas)

    st.download_button(
        "📥 Download Event Plan",
        data=plan_text,
        file_name="celebration_plan.txt",
        mime="text/plain"
    )

st.divider()
st.caption(
    "AI Celebration Planner | A student project for smarter event planning"
)
