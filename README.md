# 🧮 Text to Math Problem Solver Using Gemma 2

This is a **Streamlit** web application that uses **LangChain**, **Groq's Gemma 2 model**, and a set of intelligent tools to solve text-based math problems. It also leverages **Wikipedia search** for additional context or definitions and a **calculator agent** for handling math expressions.

---

## 🚀 Features

- 🔢 Solves arithmetic and logic-based math questions  
- 🧠 Uses reasoning to break down word problems step-by-step  
- 📚 Includes Wikipedia search for background info on math-related topics  
- ⚡ Powered by [Groq](https://groq.com/) and the **Gemma 2 9B Instruct** model  
- 💬 Chat interface to interact with the assistant easily

---

## 🧰 Technologies Used

- [Streamlit](https://streamlit.io/)  
- [LangChain](https://www.langchain.com/)  
- [Groq API (Gemma 2)](https://console.groq.com/)  
- [WikipediaAPIWrapper (LangChain)]  
- Python 3.10+

---

## 📦 Installation

1. **Clone this repo:**

```bash
git clone https://github.com/your-username/text-to-math-solver.git
cd text-to-math-solver
````

2. **Create virtual environment & install dependencies:**

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, install manually:

```bash
pip install streamlit langchain langchain-groq langchain-community python-dotenv
```

3. **Set your Groq API Key:**

Run the app and enter the key in the sidebar when prompted.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 Example Question

```text
A rectangular garden has a length that is twice its width. A path of uniform width is built around the garden, and the area of the path is 208 square meters.

If the width of the garden is x meters, and the width of the path is 2 meters,
what is the value of x, and what is the area of the entire garden including the path?
```

The app will return a step-by-step explanation with the correct math reasoning.

---

## 📸 Screenshot

*(Insert your app screenshot here)*

---

## 🛡 License

MIT License

---

## 🙋‍♂️ Author

Developed by **Your Name**
🔗 [GitHub](https://github.com/KartikNimhan)
📧 [kartiknimhan9929.com](mailto:kartiknimhan9929.com)

```

