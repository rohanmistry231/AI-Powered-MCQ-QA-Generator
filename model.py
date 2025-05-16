import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from transformers.utils.hub import cached_file

model_name = "mistralai/Mistral-7B-Instruct-v0.1"
model_path = cached_file(model_name, "config.json")

print(f"Model is stored at: {model_path}")
