We have the `ai4privacy-model: raw-input -> private-input`. Private input can be safely passed to OpenAI.

OpenAI functions to protect:
- openai.Completion.create(prompt)
- openai.ChatCompletion.create(messages)
- openai.Edit.create(input)
- openai.Embedding.create(input)

chrome extension:
- content.js: mask/unmaskVariables
- adapt the service worker to python (chatgpt) -> it is the model functions
- load the weights from a standard format (onnx)
