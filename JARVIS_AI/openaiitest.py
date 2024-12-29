# This code is for v1 of the openai package: pypi.org/project/openai
import openai
openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a letter to a boss for resignation",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)