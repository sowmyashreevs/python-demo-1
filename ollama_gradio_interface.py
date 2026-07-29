import os
from openai import OpenAI
import gradio as gr
import json

OLLAMA_HOST = "http://localhost:11434/v1"
MODEL_NAME = "llama3.2"

ollama = OpenAI(base_url=OLLAMA_HOST,api_key="ollama")

SYSTEM_PROMPT = """
You are an python expert AI assistant in resolving user queries related to python only using chain of thoughts.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done. Finally give an OUTPUT.
Other than python topic you just say, I dont have info on this! as OUTPUT
you are strictly prohibited on answering none other than python programming.

Rules:
- strictly followthe JSON output format and make sure to json result is correctly formatted
- Only run step at a time
- Answer only python programming related queries
- Dont return half answers complete the query fully
- The sequence of steps is START(where user give an input), PLAN(that can be multiple items) and finally OUTPUT(which is going to be displayed tothe user in json format)

OUTPUT Json format:
{"step": "START" | "PLAN" | "OUTPUT", "content":"<message>"}

Examples:
START: Hey, can you solve 2+3 * 5/10
PLAN{"step":"PLAN","content":"looks like user likes to solve a math problem"}
PLAN{"step":"PLAN","content":"Looks like it is a combination of airthematic problem which can be solved using BODMAS method"}
PLAN{"step":"PLAN","content":"yes , the BADMAS method is correct way of solving it"}
PLAN{"step":"PLAN","content":"first we divide by 5 by 10 which is 0.5"}
PLAN{"step":"PLAN","content":"next we multiply 0.5 by 3 which is 1.5"}
PLAN{"step":"PLAN","content":"then we add 1.5 to 2 which is 3.5"}
PLAN{"step":"PLAN","content":"great we finally have an answer which is 3.5"}
PLAN{"step":"OUTPUT","content":"The answer is 3.5"}

START: what is a+b whole square
PLAN{"step":"OUTPUT","content":"Sorry, I dont know the answer"}
"""
def pythonExpert(pythonQuery):
    message_history = [{"role":"system","content": SYSTEM_PROMPT}]
    message_history.append({"role":"user","content":pythonQuery})
    output = []
    while True:
        response = ollama.chat.completions.create(model=MODEL_NAME, messages=message_history, response_format={"type": "json_object"})
        raw_result = response.choices[0].message.content
        message_history.append({"role":"assistant","content":raw_result})

        parsed_result = json.loads(raw_result)
        if parsed_result.get("step") == "START":
            output.append(f"--> {parsed_result.get('content')}")
            continue
        elif parsed_result.get("step") == "PLAN":
            output.append(f"--> {parsed_result.get('content')}")
            continue
        elif parsed_result.get("step") == "OUTPUT":
            output.append(f"--> {parsed_result.get('content')}")
            break
    result = "\n".join(output)
    return result

gr.Interface(
    fn=pythonExpert,
    inputs=gr.Textbox(lines=20, max_lines=1000, label="Input Text"),
    outputs=gr.Textbox(lines=20, max_lines=1000, label="Output Text"),
    flagging_mode="never",
).launch()
