import torch
import os
import json
from torch.nn import functional as F

# torch device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Model name
MODEL_NAME = "lstm.pt"
# Model paths
PYTORCH_LSTM_MODEL_PATH = os.path.join(os.getcwd(), f"api/models/static/{MODEL_NAME}")

# STATIC FILE NAMES
RESPONSES = "response.json"
LABELS = "labels_dict.json"
VOCAB = "vocab.json"
# STATIC FILE PATHS

RESPONSES_PATH = os.path.join(os.getcwd(), f"api/models/static/{RESPONSES}")
LABELS_PATH = os.path.join(os.getcwd(), f"api/models/static/{LABELS}")
VOCAB_PATH = os.path.join(os.getcwd(), f"api/models/static/{VOCAB}")

# loading static files
with open(RESPONSES_PATH, "r", encoding="utf8") as reader:
    responses = json.loads(reader.read())

with open(LABELS_PATH, "r") as reader:
    labels_dict = json.load(reader)

with open(VOCAB_PATH, "r") as reader:
    stoi = json.load(reader)

# SPECIAL TOKENS
PAD_TOKEN = "[pad]"
SOS_TOKEN = "[sos]"
UNK_TOKEN = "[unk]"
EOS_TOKEN = "[eos]"


def text_pipeline(x: str):
    values = list()
    tokens = x.lower().split(" ")  # convert to lower case.
    for token in tokens:
        try:
            v = stoi[token]
        except KeyError:
            v = stoi[UNK_TOKEN]
        values.append(v)
    return values


def inference_preprocess_text(text, max_len=50, padding="pre"):
    assert padding == "pre" or padding == "post", (
        "the padding can be either pre or post"
    )
    text_holder = torch.zeros(
        max_len, dtype=torch.int32
    )  # fixed size tensor of max_len with  = 0
    processed_text = torch.tensor(text_pipeline(text), dtype=torch.int32)
    pos = min(max_len, len(processed_text))
    if padding == "pre":
        text_holder[:pos] = processed_text[:pos]
    else:
        text_holder[-pos:] = processed_text[-pos:]
    text_list = text_holder.unsqueeze(dim=0)
    return text_list


classes = list(labels_dict.keys())


def predict_intent(model, sentence, device):
    model.eval()
    with torch.no_grad():
        tensor = inference_preprocess_text(sentence).to(device)
        length = torch.tensor([len(t) for t in tensor])
        probs = F.softmax(model(tensor, length).squeeze(0))
        top = {
            "label": int(probs.argmax().item()),
            "probability": float(probs.max().item()),
            "class": classes[probs.argmax().item()],
        }
        predictions = [
            {"label": i, "probability": float(prob), "class": classes[i]}
            for i, prob in enumerate(probs)
        ]
        return {"top": top, "predictions": predictions}
