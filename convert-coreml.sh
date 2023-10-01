#!/bin/bash

python -m python_coreml_stable_diffusion.torch2coreml \
 --convert-unet \
 --convert-text-encoder \
 --convert-vae-decoder \
 --convert-vae-encoder \
 --convert-safety-checker \
 --bundle-resources-for-swift-cli \
 --latent-w 64 --latent-h 64 \
 --model-version blazingdrive-v05a \
 -o ./blazingdrive-v05a-coreml

