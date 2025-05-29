
TELEGRAM_BOT_TOKEN = "7670723585:AAEacMjFIMHarGFjk3Vkfixzc8CbQCEPo1Y"
GEMINI_API_KEY = "AIzaSyD1hhhTheB1tv-Nbez9mYUJ9Dfhs-fxwRY"
# import logging
# import re
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
# )
# import google.generativeai as genai

# # === LOGGING ===
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# # === GEMINI SETUP ===
# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-pro")

# # === USER MEMORY ===
# user_sessions = {}

# # === TOPICS ===
# TOPICS = [
#     "Reading Comprehension-Based Legal Reasoning",
#     "Current Affairs",
#     "Quantitative Aptitude",
#     "Logical Reasoning",
#     "Legal Principle - Fact Application",
# ]

# # === PROMPT GENERATOR ===
# def build_prompt(topic):
#     return f"""
# Generate a CLAT-level question on the topic '{topic}'.
# Respond in the following format strictly:

# Question: <Your question here>

# A. <Option A>  
# B. <Option B>  
# C. <Option C>  

# Answer: <Correct Option Letter>  
# Explanation: <Brief explanation in 2 lines>
# """

# # === GEMINI RESPONSE PARSER ===
# def parse_gemini_response(text):
#     try:
#         q_match = re.search(r"Question:\s*(.*?)\n(?:A\.|A\s*\))", text, re.DOTALL)
#         options_match = re.findall(r"[ABC][.)]?\s*(.+)", text)
#         answer_match = re.search(r"Answer:\s*([ABC])", text)
#         explanation_match = re.search(r"Explanation:\s*(.*)", text, re.DOTALL)

#         question = q_match.group(1).strip() if q_match else "Question missing."
#         options = options_match if options_match else ["Option 1", "Option 2", "Option 3"]
#         answer = answer_match.group(1).strip() if answer_match else "A"
#         explanation = explanation_match.group(1).strip() if explanation_match else "Explanation not found."

#         formatted_question = f"🧠 *Question:*\n{question}\n\n" + "\n".join([
#             f"{letter}. {opt}" for letter, opt in zip(["A", "B", "C"], options)
#         ])
#         return formatted_question, answer, explanation
#     except Exception:
#         return "⚠️ Error parsing Gemini response.", "A", "Parsing failed."

# # === HANDLERS ===

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [[InlineKeyboardButton(t, callback_data=f"topic_{t}")] for t in TOPICS]
#     await update.message.reply_text("🧠 Choose a CLAT topic:", reply_markup=InlineKeyboardMarkup(keyboard))

# async def handle_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     topic = query.data.replace("topic_", "")
#     user_id = query.from_user.id

#     # Save topic
#     user_sessions[user_id] = {"topic": topic}
#     await generate_and_send_question(query, topic, user_id)

# async def generate_and_send_question(query, topic, user_id):
#     prompt = build_prompt(topic)
#     response = model.generate_content(prompt)
#     formatted_q, answer, explanation = parse_gemini_response(response.text)

#     user_sessions[user_id].update({
#         "latest_question": formatted_q,
#         "answer": answer,
#         "explanation": explanation
#     })

#     buttons = [
#         [InlineKeyboardButton("➡️ Next", callback_data="next")],
#         [InlineKeyboardButton("✅ Done", callback_data="done")],
#         [InlineKeyboardButton("❌ Stop", callback_data="stop")]
#     ]

#     await query.edit_message_text(
#         text=f"📘 *{topic}*\n\n{formatted_q}",
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(buttons)
#     )

# async def handle_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     user_id = query.from_user.id
#     action = query.data

#     session = user_sessions.get(user_id, {})
#     topic = session.get("topic", "")

#     if not session:
#         await query.edit_message_text("⚠️ Please restart with /start.")
#         return

#     if action == "next":
#         await generate_and_send_question(query, topic, user_id)
#     elif action == "done":
#         q_text = session.get("latest_question", "")
#         ans = session.get("answer", "A")
#         explanation = session.get("explanation", "No explanation.")
#         await query.edit_message_text(
#             text=f"{q_text}\n\n✅ *Answer:* {ans}\n🧾 *Explanation:* {explanation}",
#             parse_mode="Markdown"
#         )
#     elif action == "stop":
#         await query.edit_message_text("👋 Session ended. Type /start to begin again.")

# # === MAIN FUNCTION ===
# def main():
#     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CallbackQueryHandler(handle_topic, pattern="^topic_"))
#     app.add_handler(CallbackQueryHandler(handle_action, pattern="^(next|done|stop)$"))

#     app.run_polling()

# # === RUN ===
# if __name__ == "__main__":
#     main()


# import logging
# import re
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
# )
# import google.generativeai as genai

# # === LOGGING ===
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# # === GEMINI SETUP ===
# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-pro")

# # === USER MEMORY ===
# user_sessions = {}

# # === TOPICS ===
# TOPICS = [
#     "Reading Comprehension-Based Legal Reasoning",
#     "Current Affairs",
#     "Quantitative Aptitude",
#     "Logical Reasoning",
#     "Legal Principle - Fact Application",
# ]

# # === TOPIC PROMPTS ===
# TOPIC_PROMPTS = {
#     "Reading Comprehension-Based Legal Reasoning": """
# Generate a passage (~150–200 words) followed by 3 to 6 CLAT-level questions with 4 options each (A to D), based on legal reasoning or comprehension.

# Respond in this strict format:

# Passage:
# <Passage text>

# Question 1:
# <Question>

# A. <Option A>  
# B. <Option B>  
# C. <Option C>  
# D. <Option D>  

# Answer: <Correct Option Letter>  
# Explanation: <2-line explanation>

# Question 2:
# ... (same structure)

# (Continue till 3–6 questions)
# """,
#     "Current Affairs": """
# Generate 3 to 6 CLAT Current Affairs questions from the past 6 months with 4 options each.

# Format strictly:

# Question 1:
# <Question>

# A. <Option A>  
# B. <Option B>  
# C. <Option C>  
# D. <Option D>  

# Answer: <Correct Option Letter>  
# Explanation: <2-line context>

# (Repeat)
# """,
#     "Quantitative Aptitude": """
# Generate 3 to 6 CLAT Quantitative Aptitude questions (arithmetic, averages, ratios, etc.), each with 4 options (A–D).

# Use this format:

# Question 1:
# <Question>

# A. <Option A>  
# B. <Option B>  
# C. <Option C>  
# D. <Option D>  

# Answer: <Correct Option Letter>  
# Explanation: <Short working>

# (Repeat)
# """,
#     "Logical Reasoning": """
# Generate a short logical reasoning passage (~100–150 words), followed by 3 to 6 questions with 4 options each.

# Format:

# Passage:
# <Passage text>

# Question 1:
# ...

# A. ...
# B. ...
# C. ...
# D. ...

# Answer: ...
# Explanation: ...

# (Repeat)
# """,
#     "Legal Principle - Fact Application": """
# Generate a legal principle and related facts, followed by 3 to 6 questions applying the principle to different variations.

# Format:

# Principle:
# <Legal principle>

# Facts:
# <Set of facts>

# Question 1:
# ...

# A. ...
# B. ...
# C. ...
# D. ...

# Answer: ...
# Explanation: ...

# (Repeat)
# """
# }

# # === PARSE MULTIPLE QA ===
# def parse_multiple_qa(text):
#     try:
#         blocks = re.split(r"(?:Question\s*\d+:)", text)
#         passage_match = re.search(r"Passage:\s*(.*?)\n(?=Question|Question\s*\d+:)", text, re.DOTALL)
#         principle_match = re.search(r"Principle:\s*(.*?)\nFacts:", text, re.DOTALL)
#         facts_match = re.search(r"Facts:\s*(.*?)\nQuestion", text, re.DOTALL)

#         context_intro = ""
#         if passage_match:
#             context_intro = f"📜 *Passage:*\n{passage_match.group(1).strip()}\n\n"
#         elif principle_match and facts_match:
#             context_intro = f"📘 *Principle:*\n{principle_match.group(1).strip()}\n\n📖 *Facts:*\n{facts_match.group(1).strip()}\n\n"

#         qa_blocks = re.findall(
#             r"Question\s*\d+:\s*(.*?)\nA\. (.*?)\nB\. (.*?)\nC\. (.*?)\nD\. (.*?)\nAnswer:\s*([ABCD])\nExplanation:\s*(.*?)(?=\nQuestion\s*\d+:|\Z)",
#             text, re.DOTALL
#         )

#         formatted_questions = []
#         for i, (question, A, B, C, D, answer, explanation) in enumerate(qa_blocks, 1):
#             q = f"🔹 *Q{i}.* {question.strip()}\n\nA. {A.strip()}\nB. {B.strip()}\nC. {C.strip()}\nD. {D.strip()}"
#             formatted_questions.append({
#                 "question": q,
#                 "answer": answer.strip(),
#                 "explanation": explanation.strip()
#             })

#         return context_intro, formatted_questions
#     except Exception as e:
#         return "", [{"question": "⚠️ Error parsing Gemini response.", "answer": "A", "explanation": str(e)}]

# # === HANDLERS ===

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [[InlineKeyboardButton(t, callback_data=f"topic_{t}")] for t in TOPICS]
#     await update.message.reply_text("🧠 Choose a CLAT topic:", reply_markup=InlineKeyboardMarkup(keyboard))

# async def handle_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     topic = query.data.replace("topic_", "")
#     user_id = query.from_user.id

#     user_sessions[user_id] = {"topic": topic}
#     await generate_and_send_questions(query, topic, user_id)

# async def generate_and_send_questions(query, topic, user_id):
#     prompt = TOPIC_PROMPTS.get(topic, f"Generate a CLAT question on the topic: {topic}")
#     response = model.generate_content(prompt)

#     intro, questions = parse_multiple_qa(response.text)
#     user_sessions[user_id].update({
#         "questions": questions,
#         "intro": intro
#     })

#     text = intro + "\n\n\n".join(q["question"] for q in questions)
#     buttons = [
#         [InlineKeyboardButton("✅ Done (show answers)", callback_data="done")],
#         [InlineKeyboardButton("➡️ Next Set", callback_data="next")],
#         [InlineKeyboardButton("❌ Stop", callback_data="stop")]
#     ]

#     await query.edit_message_text(
#         text=text,
#         parse_mode="Markdown",
#         reply_markup=InlineKeyboardMarkup(buttons)
#     )


#     query = update.callback_query
#     await query.answer()
#     user_id = query.from_user.id
#     action = query.data

#     session = user_sessions.get(user_id, {})
#     topic = session.get("topic", "")

#     if not session:
#         await query.edit_message_text("⚠️ Please restart with /start.")
#         return

#     if action == "next":
#         await generate_and_send_questions(query, topic, user_id)
#     elif action == "done":
#         intro = session.get("intro", "")
#         questions = session.get("questions", [])
#         result = intro + "\n\n\n".join(
#             f"{q['question']}\n\n✅ *Answer:* {q['answer']}\n🧾 *Explanation:* {q['explanation']}"
#             for q in questions
#         )
#         await query.edit_message_text(text=result, parse_mode="Markdown")
#     elif action == "stop":
#         await query.edit_message_text("👋 Session ended. Type /start to begin again.")

# async def handle_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     user_id = query.from_user.id
#     action = query.data

#     session = user_sessions.get(user_id, {})
#     topic = session.get("topic", "")

#     if not session:
#         await query.edit_message_text("⚠️ Please restart with /start.")
#         return

#     if action == "next":
#         await generate_and_send_questions(query, topic, user_id)
#     elif action == "done":
#         intro = session.get("intro", "")
#         questions = session.get("questions", [])
#         result = intro + "\n\n\n".join(
#             f"{q['question']}\n\n✅ *Answer:* {q['answer']}\n🧾 *Explanation:* {q['explanation']}"
#             for q in questions
#         )

#         buttons = [
#             [InlineKeyboardButton("➡️ Next Set", callback_data="next")],
#             [InlineKeyboardButton("❌ Stop", callback_data="stop")]
#         ]

#         await query.edit_message_text(
#             text=result,
#             parse_mode="Markdown",
#             reply_markup=InlineKeyboardMarkup(buttons)
#         )
#     elif action == "stop":
#         await query.edit_message_text("👋 Session ended. Type /start to begin again.")

# # === MAIN ===
# def main():
#     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CallbackQueryHandler(handle_topic, pattern="^topic_"))
#     app.add_handler(CallbackQueryHandler(handle_action, pattern="^(next|done|stop)$"))

#     app.run_polling()

# if __name__ == "__main__":
#     main()
# import logging
# import re
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
# )
# import google.generativeai as genai

# # === CONFIG ===


# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-pro")

# # === LOGGING ===
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# # === STATE ===
# user_sessions = {}

# # === TOPICS ===
# TOPICS = [
#     "Reading Comprehension-Based Legal Reasoning",
#     "Current Affairs",
#     "Quantitative Aptitude",
#     "Logical Reasoning",
#     "Legal Principle - Fact Application",
# ]

# # === PROMPT ===
# def build_prompt(topic):
#     return f"""
# Generate one CLAT-level passage with 3 to 6 MCQ questions on the topic '{topic}'.
# Respond in the following format:

# Passage: <Passage text here>

# Q1: <Question 1>
# A. <Option A>
# B. <Option B>
# C. <Option C>
# D. <Option D>
# Answer: <Correct Option Letter>
# Explanation: <Explanation in 1-2 lines>

# Q2: ... (and so on)
# """

# # === PARSER ===
# def parse_passage_and_questions(text):
#     passage_match = re.search(r"Passage:(.*?)\nQ\d+:", text, re.DOTALL)
#     questions = re.findall(r"Q\d+:\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\nAnswer:\s*([A-Da-d])\nExplanation:\s*(.*?)(?=\nQ\d+:|$)", text, re.DOTALL)

#     passage = passage_match.group(1).strip() if passage_match else "Passage not found."
#     parsed_questions = []
#     for q_text, a, b, c, d, answer, explanation in questions:
#         parsed_questions.append({
#             "question": q_text.strip(),
#             "options": [a.strip(), b.strip(), c.strip(), d.strip()],
#             "answer": answer.strip().upper(),
#             "explanation": explanation.strip()
#         })
#     return passage, parsed_questions

# # === HANDLERS ===
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [[InlineKeyboardButton(t, callback_data=f"topic_{t}")] for t in TOPICS]
#     await update.message.reply_text("🧠 Choose a CLAT topic:", reply_markup=InlineKeyboardMarkup(keyboard))

# async def handle_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     topic = query.data.replace("topic_", "")
#     user_id = query.from_user.id

#     prompt = build_prompt(topic)
#     response = model.generate_content(prompt)
#     passage, questions = parse_passage_and_questions(response.text)

#     user_sessions[user_id] = {
#         "topic": topic,
#         "passage": passage,
#         "questions": questions,
#         "current_q": 0,
#         "correct": 0,
#         "incorrect": 0,
#         "total": 0,
#     }

#     await ask_next_question(update, context, user_id)

# async def ask_next_question(update, context, user_id):
#     session = user_sessions[user_id]
#     current_index = session["current_q"]
#     questions = session["questions"]

#     if current_index == 0:
#         await context.bot.send_message(
#         chat_id=user_id,
#         text=f"📘 *Passage:*\n{session['passage']}",
#         parse_mode="Markdown"
# )


#     if current_index < len(questions):
#         q = questions[current_index]
#         options_text = "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(q["options"])])
#         await context.bot.send_message(chat_id=user_id, text=f"❓ *Q{current_index+1}:* {q['question']}\n\n{options_text}\n\n_Reply with A, B, C or D._", parse_mode="Markdown")
#     else:
#         await context.bot.send_message(chat_id=user_id, text=f"✅ Session Complete!\nCorrect: {session['correct']}\nIncorrect: {session['incorrect']}\nTotal: {session['total']}\n\nType /start to begin again.")
#         user_sessions.pop(user_id)

# async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.strip().upper()

#     if user_id not in user_sessions:
#         return

#     session = user_sessions[user_id]
#     if session["current_q"] >= len(session["questions"]):
#         return

#     if text not in ["A", "B", "C", "D"]:
#         await update.message.reply_text("⚠️ Please answer with A, B, C or D.")
#         return

#     current_q = session["questions"][session["current_q"]]
#     correct_ans = current_q["answer"]
#     explanation = current_q["explanation"]

#     if text == correct_ans:
#         session["correct"] += 1
#         await update.message.reply_text("✅ Correct!")
#     else:
#         session["incorrect"] += 1
#         await update.message.reply_text(f"❌ Incorrect. Correct Answer: {correct_ans}\nExplanation: {explanation}")

#     session["total"] += 1
#     session["current_q"] += 1
#     await ask_next_question(update, context, user_id)

# # === MAIN ===
# def main():
#     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CallbackQueryHandler(handle_topic, pattern="^topic_"))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))

#     app.run_polling()

# if __name__ == "__main__":
#     main()


# import logging
# import re
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
# )
# import google.generativeai as genai


# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-pro")

# # === LOGGING ===
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# # === STATE ===
# user_sessions = {}

# # === TOPICS ===
# TOPICS = [
#     "Reading Comprehension-Based Legal Reasoning",
#     "Current Affairs",
#     "Quantitative Aptitude",
#     "Logical Reasoning",
#     "Legal Principle - Fact Application",
# ]

# # === PROMPT ===
# def build_prompt(topic):
#     return f"""
# Generate one CLAT-level passage with 3 to 6 MCQ questions on the topic '{topic}'.
# Respond in the following format:

# Passage: <Passage text here>

# Q1: <Question 1>
# A. <Option A>
# B. <Option B>
# C. <Option C>
# D. <Option D>
# Answer: <Correct Option Letter>
# Explanation: <Explanation in 1-2 lines>

# Q2: ... (and so on)
# """

# # === PARSER ===
# def parse_passage_and_questions(text):
#     passage_match = re.search(r"Passage:(.*?)\nQ\d+:", text, re.DOTALL)
#     questions = re.findall(r"Q\d+:\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\nAnswer:\s*([A-Da-d])\nExplanation:\s*(.*?)(?=\nQ\d+:|$)", text, re.DOTALL)

#     passage = passage_match.group(1).strip() if passage_match else "Passage not found."
#     parsed_questions = []
#     for q_text, a, b, c, d, answer, explanation in questions:
#         parsed_questions.append({
#             "question": q_text.strip(),
#             "options": [a.strip(), b.strip(), c.strip(), d.strip()],
#             "answer": answer.strip().upper(),
#             "explanation": explanation.strip()
#         })
#     return passage, parsed_questions

# # === HANDLERS ===
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [[InlineKeyboardButton(t, callback_data=f"topic_{t}")] for t in TOPICS]
#     await update.message.reply_text("🧠 Choose a CLAT topic:", reply_markup=InlineKeyboardMarkup(keyboard))

# async def handle_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     topic = query.data.replace("topic_", "")
#     user_id = query.from_user.id

#     await generate_new_passage(context, user_id, topic)
#     await ask_next_question(update, context, user_id)

# async def generate_new_passage(context, user_id, topic):
#     prompt = build_prompt(topic)
#     response = model.generate_content(prompt)
#     passage, questions = parse_passage_and_questions(response.text)

#     user_sessions[user_id] = {
#         "topic": topic,
#         "passage": passage,
#         "questions": questions,
#         "current_q": 0,
#         "correct": 0,
#         "incorrect": 0,
#         "total": 0,
#     }

# async def ask_next_question(update, context, user_id):
#     session = user_sessions[user_id]
#     current_index = session["current_q"]
#     questions = session["questions"]

#     if current_index == 0:
#         await context.bot.send_message(
#             chat_id=user_id,
#             text=f"📘 *Passage:*\n{session['passage']}",
#             parse_mode="Markdown"
#         )

#     if current_index < len(questions):
#         q = questions[current_index]
#         options_text = "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(q["options"])])
#         await context.bot.send_message(
#             chat_id=user_id,
#             text=f"❓ *Q{current_index+1}:* {q['question']}\n\n{options_text}\n\n_Reply with A, B, C or D._",
#             parse_mode="Markdown"
#         )
#     else:
#         keyboard = [[InlineKeyboardButton("➡️ Next Passage", callback_data="next")],
#                    [InlineKeyboardButton("❌ Stop", callback_data="stop")]]
#         await context.bot.send_message(
#             chat_id=user_id,
#             text=f"✅ Passage Complete!\nCorrect: {session['correct']}\nIncorrect: {session['incorrect']}\nTotal: {session['total']}\nChoose what to do next:",
#             reply_markup=InlineKeyboardMarkup(keyboard)
#         )

# async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.strip().upper()

#     if user_id not in user_sessions:
#         return

#     session = user_sessions[user_id]
#     if session["current_q"] >= len(session["questions"]):
#         return

#     if text not in ["A", "B", "C", "D"]:
#         await update.message.reply_text("⚠️ Please answer with A, B, C or D.")
#         return

#     current_q = session["questions"][session["current_q"]]
#     correct_ans = current_q["answer"]
#     explanation = current_q["explanation"]

#     if text == correct_ans:
#         session["correct"] += 1
#         await update.message.reply_text("✅ Correct!")
#     else:
#         session["incorrect"] += 1
#         await update.message.reply_text(f"❌ Incorrect. Correct Answer: {correct_ans}\nExplanation: {explanation}")

#     session["total"] += 1
#     session["current_q"] += 1
#     await ask_next_question(update, context, user_id)

# async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     user_id = query.from_user.id

#     if query.data == "next":
#         topic = user_sessions[user_id]["topic"]
#         await generate_new_passage(context, user_id, topic)
#         await ask_next_question(update, context, user_id)
#     elif query.data == "stop":
#         user_sessions.pop(user_id, None)
#         await query.edit_message_text("👋 Session ended. Type /start to begin again.")

# # === MAIN ===
# def main():
#     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CallbackQueryHandler(handle_topic, pattern="^topic_"))
#     app.add_handler(CallbackQueryHandler(handle_callback, pattern="^(next|stop)$"))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))

#     app.run_polling()

# if __name__ == "__main__":
#     main()
import logging
import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
)
import google.generativeai as genai


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# === LOGGING ===
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# === STATE ===
user_sessions = {}
user_stats = {}

# === TOPICS ===
TOPICS = [
    "Reading Comprehension-Based Legal Reasoning",
    "Current Affairs",
    "Quantitative Aptitude",
    "Logical Reasoning",
    "Legal Principle - Fact Application",
]

# === PROMPT ===
def build_prompt(topic):
    return f"""
Generate one CLAT-level passage with 3 to 6 MCQ questions on the topic '{topic}'.
Respond in the following format:

Passage: <Passage text here>

Q1: <Question 1>
A. <Option A>
B. <Option B>
C. <Option C>
D. <Option D>
Answer: <Correct Option Letter>
Explanation: <Explanation in 1-2 lines>

Q2: ... (and so on)
"""

# === PARSER ===
def parse_passage_and_questions(text):
    passage_match = re.search(r"Passage:(.*?)\nQ\d+:", text, re.DOTALL)
    questions = re.findall(r"Q\d+:\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\nAnswer:\s*([A-Da-d])\nExplanation:\s*(.*?)(?=\nQ\d+:|$)", text, re.DOTALL)

    passage = passage_match.group(1).strip() if passage_match else "Passage not found."
    parsed_questions = []
    for q_text, a, b, c, d, answer, explanation in questions:
        parsed_questions.append({
            "question": q_text.strip(),
            "options": [a.strip(), b.strip(), c.strip(), d.strip()],
            "answer": answer.strip().upper(),
            "explanation": explanation.strip()
        })
    return passage, parsed_questions

# === HANDLERS ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(t, callback_data=f"topic_{t}")] for t in TOPICS]
    await update.message.reply_text("🧠 Choose a CLAT topic:", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except Exception as e:
        logging.warning(f"Callback query error (topic): {e}")

    topic = query.data.replace("topic_", "")
    user_id = query.from_user.id

    if user_id not in user_stats:
        user_stats[user_id] = {"correct": 0, "incorrect": 0, "total": 0}

    await generate_new_passage(context, user_id, topic)
    await ask_next_question(update, context, user_id)

async def generate_new_passage(context, user_id, topic):
    prompt = build_prompt(topic)
    response = model.generate_content(prompt)
    passage, questions = parse_passage_and_questions(response.text)

    user_sessions[user_id] = {
        "topic": topic,
        "passage": passage,
        "questions": questions,
        "current_q": 0
    }

async def ask_next_question(update, context, user_id):
    session = user_sessions[user_id]
    current_index = session["current_q"]
    questions = session["questions"]

    if current_index == 0:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"📘 *Passage:*\n{session['passage']}",
            parse_mode="Markdown"
        )

    if current_index < len(questions):
        q = questions[current_index]
        options_text = "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(q["options"])])
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ *Q{current_index+1}:* {q['question']}\n\n{options_text}\n\n_Reply with A, B, C or D._",
            parse_mode="Markdown"
        )
    else:
        stats = user_stats[user_id]
        passage_total = session['current_q']
        passage_correct = stats['correct'] - (stats['total'] - passage_total)
        passage_incorrect = stats['incorrect'] - (stats['total'] - passage_total)

        keyboard = [[InlineKeyboardButton("➡️ Next Passage", callback_data="next")],
                   [InlineKeyboardButton("❌ Stop", callback_data="stop")],
                   [InlineKeyboardButton("🔄 Switch Topic", callback_data="switch_topic")]]
        await context.bot.send_message(
            chat_id=user_id,
            text=(f"✅ Passage Complete!\n\nCorrect this passage: {passage_correct}\n"
                  f"Incorrect this passage: {passage_incorrect}\n"
                  f"Total this passage: {passage_total}\n\n"
                  f"📊 Session Total:\nCorrect: {stats['correct']}\nIncorrect: {stats['incorrect']}\nTotal: {stats['total']}\n\nChoose what to do next:"),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.strip().upper()

    if user_id not in user_sessions:
        return

    session = user_sessions[user_id]
    if session["current_q"] >= len(session["questions"]):
        return

    if text not in ["A", "B", "C", "D"]:
        await update.message.reply_text("⚠️ Please answer with A, B, C or D.")
        return

    current_q = session["questions"][session["current_q"]]
    correct_ans = current_q["answer"]
    explanation = current_q["explanation"]

    stats = user_stats[user_id]
    if text == correct_ans:
        stats["correct"] += 1
        await update.message.reply_text("✅ Correct!")
    else:
        stats["incorrect"] += 1
        await update.message.reply_text(f"❌ Incorrect. Correct Answer: {correct_ans}\nExplanation: {explanation}")

    stats["total"] += 1
    session["current_q"] += 1
    await ask_next_question(update, context, user_id)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except Exception as e:
        logging.warning(f"Callback query error: {e}")

    user_id = query.from_user.id

    if query.data == "next":
        topic = user_sessions[user_id]["topic"]
        await generate_new_passage(context, user_id, topic)
        await ask_next_question(update, context, user_id)
    elif query.data == "stop":
        user_sessions.pop(user_id, None)
        await query.edit_message_text("👋 Session ended. Type /start to begin again.")
    elif query.data == "switch_topic":
        keyboard = [[InlineKeyboardButton(t, callback_data=f"topic_{t}")] for t in TOPICS]
        await query.edit_message_text("🔄 Choose a new topic:", reply_markup=InlineKeyboardMarkup(keyboard))

# === MAIN ===
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_topic, pattern="^topic_"))
    app.add_handler(CallbackQueryHandler(handle_callback, pattern="^(next|stop|switch_topic)$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))

    app.run_polling()

if __name__ == "__main__":
    main()
