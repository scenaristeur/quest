import autogen
from memgpt.autogen.memgpt_agent import create_memgpt_autogen_agent_from_config
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# create a config for the MemGPT AutoGen agent
# config_list_memgpt = [
#     {
#         "model": "mistralai_mistral-7b-instruct-v0.2",
#         "api_base": "http://localhost:5001/v1",
#         "context_window": 8192,
#         "preset": "memgpt_chat",  # NOTE: you can change the preset here
#         # OpenAI specific
#         "model_endpoint_type": "openai",
#         "openai_key": "YOUR_OPENAI_KEY",
#     },
# ]

config_list_memgpt = config_list_from_json(env_or_file="OAI_CONFIG_LIST", filter_dict={
    "model": {
        "mistralai_mistral-7b-instruct-v0.2"
        #"codellama-7b-instruct-gguf",
        #"ggml-gpt4all-j"
        # "gpt-4",
        # "gpt-3.5-turbo"
    },
})

llm_config_memgpt = {"config_list": config_list_memgpt, "seed": 42}

# there are some additional options to do with how you want the interface to look (more info below)
interface_kwargs = {
    "debug": True,
    "show_inner_thoughts": True,
    "show_function_outputs": True,
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

# then pass the config to the constructor
# memgpt_autogen_agent = create_memgpt_autogen_agent_from_config(
#     "MemGPT_agent",
#     llm_config=llm_config_memgpt,
#     system_message=f"Your desired MemGPT persona",
#     interface_kwargs=interface_kwargs,
#     default_auto_reply="...",
#     skip_verify=False,  # NOTE: you should set this to True if you expect your MemGPT AutoGen agent to call a function other than send_message on the first turn
#     auto_save=False,  # NOTE: set this to True if you want the MemGPT AutoGen agent to save its internal state after each reply - you can also save manually with .save()
# )

coder = create_memgpt_autogen_agent_from_config(
    "MemGPT_coder",
    llm_config=llm_config_memgpt,
    system_message="You are a python developer.",
    interface_kwargs=interface_kwargs,
    default_auto_reply="...",
    skip_verify=False,  # NOTE: you should set this to True if you expect your MemGPT AutoGen agent to call a function other than send_message on the first turn
    auto_save=False,  # NOTE: set this to True if you want the MemGPT AutoGen agent to save its internal state after each reply - you can also save manually with .save()

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