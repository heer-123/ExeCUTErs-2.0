import sqlite3
import openai
import os

# ✅ Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# ✅ Initialize the notes database
def init_db():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 content TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# ✅ Add a note
def add_note():
    content = input("Enter your note: ")
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()
    print("Note added.")

# ✅ View all notes
def view_notes():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM notes")
    notes = c.fetchall()
    conn.close()
    print("\n📓 Your Notes:")
    for note in notes:
        print(f"[{note[0]}] {note[1]}")
    print()

# ✅ Delete a note
def delete_note():
    note_id = input("Enter the note ID to delete: ")
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    print("Note deleted.")

# ✅ Chat with GPT
def chat_with_bot():
    user_input = input("You: ")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" if you prefer
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        reply = response.choices[0].message['content']
        print("Bot:", reply)
    except Exception as e:
        print("Error with chatbot:", str(e))

# ✅ Main CLI Menu
def main():
    init_db()
    while True:
        print("\n📘 Digital Notes & Chatbot")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Chat with Bot")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            chat_with_bot()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
