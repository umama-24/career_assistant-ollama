import sys
import ollama

SYSTEM_PROMPT = """
You are an expert, encouraging, and actionable Career Advisor AI.
Your goals:
- Help users with resume tips, interview preparation, career transitions, and skill guidance.
- Keep responses practical, well-structured, and concise.
- Tailor suggestions directly to the user's situation.
- Maintain a professional and encouraging tone.
"""

def chat_with_assistant():
    print("==================================================")
    print("      AI Career Advisor (Powered by Ollama)       ")
    print("==================================================")
    print("Type your career questions below. Type 'exit' or 'quit' to stop.\n")

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            # Added a clean newline prompt to prevent stacked 'You: You:'
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nCareer Advisor: Session ended. Goodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("\nCareer Advisor: Best of luck on your career journey! Goodbye.")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            print("\nCareer Advisor: ", end="", flush=True)

            # Enable streaming (stream=True) for real-time word output
            response_stream = ollama.chat(
                model="llama3.2",
                messages=messages,
                stream=True
            )

            full_reply = ""
            for chunk in response_stream:
                content = chunk["message"]["content"]
                print(content, end="", flush=True)
                full_reply += content

            print("\n" + "-" * 50)
            messages.append({"role": "assistant", "content": full_reply})

        except Exception as e:
            print(f"\nError interacting with Ollama: {e}")
            print("Make sure the Ollama application is running in the background.\n")

if __name__ == "__main__":
    chat_with_assistant()