import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler

# Streamlit app setup
st.set_page_config(page_title="Text to Math Problem Solver", page_icon="🧮")
st.title("🧮 Text to Math Problem Solver Using Gemma 2")

# Sidebar for API key
groq_api_key = st.sidebar.text_input("🔑 Groq API Key", type="password")

if not groq_api_key:
    st.info("Please enter your Groq API key to continue.")
    st.stop()

# Load LLM
llm = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

# Wikipedia Tool
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="Use this tool to look up general information about a topic."
)

# Math Tool
math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="Use this tool to solve mathematical expressions."
)

# Reasoning Prompt
reasoning_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a math assistant. Solve the following question step-by-step, using logical reasoning. 
Provide a clear, point-wise answer.

Question: {question}

Answer:
"""
)

# Reasoning Tool
reasoning_chain = LLMChain(llm=llm, prompt=reasoning_prompt)
reasoning_tool = Tool(
    name="Reasoning",
    func=reasoning_chain.run,
    description="Use this tool for logical reasoning or word-based math problems."
)

# Initialize agent with tools
tools = [wikipedia_tool, calculator, reasoning_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Chat state initialization
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "👋 Hello! I'm your math assistant. Ask me any question!"}
    ]

# Display message history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
question = st.text_area("✍️ Enter your math question:", "I have 5 bananas. I give 2 to my friend. How many bananas do I have left?")

# Generate answer
if st.button("✅ Get Answer"):
    if question.strip():
        st.session_state.messages.append({"role": "user", "content": question})
        st.chat_message("user").write(question)

        with st.spinner("Thinking..."):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = agent.run(question, callbacks=[st_cb])

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
    else:
        st.warning("Please enter a valid question.")
