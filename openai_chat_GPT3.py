from openai_core import *

model = 'gpt-3.5-turbo'
MAX_TOKENS = 4096
# from openAI website here: https://openai.com/pricing
usd_per_1k_tokens = 0.002

model_tuple = (model, MAX_TOKENS, usd_per_1k_tokens)
call_core(model_tuple, True)