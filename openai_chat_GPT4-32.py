from openai_core import *

model = 'gpt-4-32k'
MAX_TOKENS = 32768
usd_per_1k_tokens = 0.06

model_tuple = (model, MAX_TOKENS, usd_per_1k_tokens)
call_core(model_tuple, True)