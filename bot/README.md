# création d'un bot
- avec mémoire https://memgpt.readme.io/docs/quickstart


# venv
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

# configure with groq

# run client
python admin_client.py













# configure with local llm

- https://memgpt.readme.io/docs/local_llm
- running igora-reloaded https://github.com/scenaristeur/igora-reloaded?tab=readme-ov-file#lancer-le-backend
with dolphin Q6 https://huggingface.co/TheBloke/dolphin-2.2.1-mistral-7B-GGUF/tree/main


```
python3 -m llama_cpp.server --model ./models/dolphin-2.2.1-mistral-7b.Q6_K.gguf --port 5678 --host 0.0.0.0 --n_ctx 16192

```

memgpt configure

? Select LLM inference provider: local
? Select LLM backend (select 'openai' if you have an OpenAI compatible proxy): llamacpp
? Enter default endpoint: http://localhost:5678/v1
? Select default model wrapper (recommended: airoboros-l2-70b-2.1): airoboros-l2-70b-2.1-grammar
? Select your model's context window (for Mistral 7B models, this is probably 8k / 8192): custom
? Enter context window (e.g. 8192) 16192
? Select embedding provider: local
? Select default preset: memgpt_chat
? Select default persona: memgpt_starter
? Select default human: basic
? Select storage backend for archival data: local
Saving config to /home/smag/.memgpt/config
(.venv) smag@smag-IdeaPad:~/dev/quest/bot$ 



# to read
- https://community.aws/content/2eojjD2E7TBgPFJmB2FGAtrSSBh/the-rise-of-the-llm-os-from-aios-to-memgpt-and-beyond


# quickstart
```
memgpt run
```