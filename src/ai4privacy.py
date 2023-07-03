
# TODO: onnx, not pickle
with open(model_path, "rb") as model_f:
    model = pickle.load(model_f)

# Config: allow deciding which model to use
# Default: light model

def model_tf(raw_text):
    masked_text= model_f(raw_text)
    # Build template_index: map templates to real values

def unmask(template_text, template_index):
    "Interpolate the text with the index"
    # NOTE: pay attention to start with the longest texts first
    pass

# decorator
def mask(openai_func):
    def inner(*args):
        if "prompt" in args:
            input_arg= "prompt"
        ...
        args[input_arg], template_index = model_tf(args[input_arg])
        template_out= openai_func(*args)
        return unmask(template_out, template_index)
