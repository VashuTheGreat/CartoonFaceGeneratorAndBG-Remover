import torch
import os
S3_CLIENT="s3"
BUCKET_NAME=os.getenv("S3_BUCKET_NAME","photoshopml")

DEVICE="cuda" if torch.cuda.is_available() else "cpu"


SAVED_MODELS_FOLDER_PATH="models"
EMOJI_GENERATOR_MODEL_NAME="EmojiFaceGenerator.pth"
BG_REMOVER_MODEL_NAME="BgRemover.pth"
