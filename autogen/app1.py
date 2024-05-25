import autogen
from memgpt.autogen.memgpt_agent import create_memgpt_autogen_agent_from_config

config_list = [
    {
        "model": "default",
        "api_base": "http://localhost:5001/v1",
        "openai_key": "YOUR_OPENAI_KEY",
        #"context_window": 8192,
        "preset": "memgpt_chat",  # NOTE: you can change the preset here
        # OpenAI specific
        "model_endpoint_type": "openai",
    }
]


llm_config = {"config_list": config_list, 
             # "seed": 42
              }

user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    #system_message="A human admin.",
    code_execution_config={
        #"last_n_messages": 2, 
        "work_dir": "coding"},
    #human_input_mode="TERMINATE",  # needed?
    # default_auto_reply="You are going to figure all out by your own. "
    # "Work by yourself, the user won't reply until you output `TERMINATE` to end the conversation.",
    default_auto_reply="...",  # Set a default auto-reply message here (non-empty auto-reply is required for LM Studio)
)

coder = create_memgpt_autogen_agent_from_config(
    "MemGPT_coder",
    llm_config=llm_config,
    system_message="You are a python developer.",
    #system_message=f"You are an AI coder. You are participating in a group chat with a user ({user_proxy.name}).",
    # system_message=f"I am a 10x engineer, trained in Python. I was the first engineer at Uber "
    # f"(which I make sure to tell everyone I work with).",
    #human_input_mode="TERMINATE",
)

user_proxy.initiate_chat(
    coder,
      #message="I want to design an app to make me one million dollars in one month. " "Tell me all the details, then try out every steps."
      message="create a python function to find the first 5 even numbers"
      )