#!/bin/bash

python -m python_coreml_stable_diffusion.pipeline --prompt "masterpiece, best quality, blonde hair, highres, 1girl, solo, green eyes, solo, low twintails, wariza, school uniform, depth of field, from side, looking at viewer" --negative-prompt "EasyNegative, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digi
t, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, lowres graffiti, low quality lowres simple background,
" -i ./blazingdrive-v05a-coreml -o output --compute-unit ALL --model-version blazingdrive-v05a --compute-unit CPU_AND_NE --seed 420
