import streamlit as st
import time
from groq import Groq
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import JsonOutputParser




# ----------------- PAGE STYLE -----------------
st.markdown("""
<style>
.center-title {
    text-align: center;
    color: #4B88FF;
    font-family: 'Segoe UI', sans-serif;
}
</style>
<h1 class="center-title">AVA 🤖</h1>
""", unsafe_allow_html=True)

# ----------------- GROQ CLIENT -----------------
<<<<<<< HEAD

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
  # Your API key from .env
=======
client = Groq(api_key=st.secrets["GROQ_API_KEY"]) # Your API key from .env
>>>>>>> f7fce468e07e8700edb9ff97d0e4f2761d219455

# ----------------- RESPONSE SCHEMA -----------------
schema = [ResponseSchema(name="response", description="The model's helpful response")]
parser = StructuredOutputParser.from_response_schemas(schema)
json_parser = JsonOutputParser()

# ----------------- PROMPT TEMPLATE -----------------
template = PromptTemplate(
    input_variables=["input"],
    template="Based on the following request: {input}.\n{format_ins}",
    partial_variables={"format_ins": parser.get_format_instructions()},
)

# ----------------- MODEL CALL FUNCTION -----------------
def call_model(user_input: str):
    prompt_text = template.format(input=user_input)

    # --- BUILD MESSAGES LIST WITH MEMORY ---
    messages = [{"role": "system", "content": "You are AVA 🤖, a friendly assistant who always has the user's back."}]
    
    for msg in st.session_state.history:
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    messages.append({"role": "user", "content": prompt_text})

    # --- CALL THE MODEL ---
    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=messages,
        temperature=0.6,
        max_tokens=4096,
        top_p=0.95,
        stream=False,
    )

    content = response.choices[0].message.content.strip()

    # --- TRY PARSING STRUCTURED OUTPUT ---
    try:
        # Clean up code fences if present
        if content.startswith("```"):
            content = content.strip("```").replace("json", "").strip()

        ai_message = AIMessage(content=content)
        json_data = json_parser.invoke(ai_message)
        if isinstance(json_data, dict) and "response" in json_data:
            return json_data["response"]
        else:
            return json_data
    except Exception:
        parsed = parser.parse(content)
        return parsed["response"]

# ----------------- STREAMING EFFECT -----------------
def chat_stream(text):
    for char in text:
        yield char
        time.sleep(0.01)

# ----------------- FEEDBACK HANDLER -----------------
def save_feedback(index):
    st.session_state.history[index]["feedback"] = st.session_state[f"feedback_{index}"]

# ----------------- INIT CHAT MEMORY -----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ----------------- DISPLAY PREVIOUS CHAT -----------------
for i, message in enumerate(st.session_state.history):
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if message["role"] == "assistant":
            feedback = message.get("feedback", None)
            st.session_state[f"feedback_{i}"] = feedback
            st.feedback(
                "thumbs",
                key=f"feedback_{i}",
                disabled=feedback is not None,
                on_change=save_feedback,
                args=[i],
            )

# ----------------- USER INPUT -----------------
if prompt := st.chat_input("Say something to AVA 🤖..."):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("AVA 🤖 is thinking..."):
            try:
                response = call_model(prompt)
                st.write_stream(chat_stream(str(response)))
            except Exception as e:
                response = f"Error: {e}"
                st.error(response)

        st.feedback(
            "thumbs",
            key=f"feedback_{len(st.session_state.history)}",
            on_change=save_feedback,
            args=[len(st.session_state.history)],
        )

    st.session_state.history.append({"role": "assistant", "content": str(response)})
