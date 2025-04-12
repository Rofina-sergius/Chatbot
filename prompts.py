def greeting_prompt():
    return "👋 Hello! I'm TalentScout, your virtual hiring assistant. I’ll guide you through a quick screening process. Let's begin!"

def info_gathering_prompt():
    return (
        "📋 Please provide the following details:\n"
        "- Full Name:\n"
        "- Email:\n"
        "- Phone Number:\n"
        "- Years of Experience:\n"
        "- Desired Position(s):\n"
        "- Current Location:\n"
        "- Tech Stack (Languages, Frameworks, Tools):"
    )

def tech_questions_prompt(tech_stack):
    return (
        f"🧠 Generate 3-5 intermediate to advanced-level technical questions for each of the following technologies:\n"
        f"{tech_stack}\n"
        "Respond in this format:\n"
        "Technology: <Tech>\n"
        "Questions:\n"
        "1.\n2.\n3.\n"
    )
