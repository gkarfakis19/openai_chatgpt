from openai_core import *

model = 'gpt-4'
MAX_TOKENS = 8192
usd_per_1k_tokens = 0.03

model_tuple = (model, MAX_TOKENS, usd_per_1k_tokens)
call_core(model_tuple, True)