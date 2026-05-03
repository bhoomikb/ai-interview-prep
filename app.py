"""
AI Interview Prep Assistant
Powered by Anthropic's Claude API

Paste a job description and get:
  - Top 10 likely interview questions
  - Strong sample answers tailored to your background
  - Key skills to highlight

Usage:
    python app.py
"""

import anthropic
import textwrap


def get_interview_prep(job_description: str, candidate_background: str) -> None:
    """
    Calls Claude API to generate interview questions and answers
    based on the job description and candidate background.
    """
    client = anthropic.Anthropic()

    prompt = f"""
You are an expert career coach and interview preparation specialist.

A candidate is preparing for a job interview. Based on the job description and their background, 
generate a comprehensive interview prep guide.

JOB DESCRIPTION:
{job_description}

CANDIDATE BACKGROUND:
{candidate_background}

Please provide:

1. TOP 10 INTERVIEW QUESTIONS - The most likely questions for this specific role
2. STRONG SAMPLE ANSWERS - For each question, write a tailored answer using the candidate's background
3. KEY SKILLS TO HIGHLIGHT - Based on the job description, what should they emphasize?
4. ONE SMART QUESTION TO ASK THE INTERVIEWER - Something that shows curiosity and preparation

Format your response clearly with numbered sections.
"""

    print("\n🤖 Generating your personalized interview prep guide...\n")
    print("=" * 60)

    # Using streaming for a better user experience
    with client.messages.stream(
        model="claude-opus-4-5",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    print("\n" + "=" * 60)
    print("\n✅ Interview prep complete! Good luck! 🍀\n")


def main():
    print("=" * 60)
    print("   🎯 AI Interview Prep Assistant")
    print("   Powered by Claude (Anthropic)")
    print("=" * 60)

    print("\nPaste the JOB DESCRIPTION below.")
    print("(Type 'END' on a new line when done)\n")

    job_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        job_lines.append(line)
    job_description = "\n".join(job_lines)

    print("\nBriefly describe YOUR BACKGROUND (skills, experience, education).")
    print("(Type 'END' on a new line when done)\n")

    bg_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        bg_lines.append(line)
    candidate_background = "\n".join(bg_lines)

    if not job_description.strip() or not candidate_background.strip():
        print("❌ Please provide both a job description and your background.")
        return

    get_interview_prep(job_description, candidate_background)


if __name__ == "__main__":
    main()
