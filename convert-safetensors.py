import torch
from diffusers import AutoencoderKL
from diffusers.pipelines.stable_diffusion.convert_from_ckpt import (
    download_from_original_stable_diffusion_ckpt,
)
from safetensors.torch import save_file

OUTPUT_PATH = "./blazingdrive-v05a"
OUTPUT_VAE = "./blazingdrive-v05a/vae"

INPUT_SD = "./blazingDrive_V05a.safetensors"
INPUT_VAE = "./vae-ft-mse-840000-ema-pruned.ckpt"

# Save SD model
pipe = download_from_original_stable_diffusion_ckpt(INPUT_SD, from_safetensors=True)
pipe.to(torch_dtype=torch.float32)
pipe.save_pretrained(OUTPUT_PATH, safe_serialization=True)

# TODO: Convert safety_checker to torch.float32

# Save VAE model
vae = AutoencoderKL.from_single_file(INPUT_VAE).to(torch.float32)
vae.save_config(OUTPUT_VAE)
vae_dict = vae.state_dict()
save_file(vae_dict, f"{OUTPUT_VAE}/diffusion_pytorch_model.safetensors")

# TODO: support LoRA conversion
# INPUT_LORA = "./models/march7th.safetensors"
