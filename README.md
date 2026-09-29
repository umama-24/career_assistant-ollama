# AI Career Advisor (Powered by Ollama)

An interactive, command-line AI Career Assistant built using Python and Ollama. This project demonstrates basic interaction between a Python client and a locally hosted LLM using strict system prompting and streaming responses.

---

## Features

- **Custom System Prompt:** Guides the AI to act as an encouraging, expert career advisor.
- **Local Model Execution:** Runs entirely on your machine via Ollama (`llama3.2`).
- **Real-Time Streaming:** Streams response tokens live to the console for instant feedback.
- **Graceful Shutdown:** Handles keyboard interrupts (`Ctrl + C`) cleanly.

---

## Requirements

- **Python:** 3.8 or higher
- **Ollama:** Installed and running locally
- **Model:** `llama3.2` (or any local model pulled via Ollama)

---

## Setup & Running

1. **Install Python dependencies:**
   ```bash
   pip install ollama
