## Requirements

- Xcode
- https://github.com/apple/ml-stable-diffusion

## Preparation

```
micromamba create -n stable-diffusion -c conda-forge python="3.8.*"
micromamba activate stable-diffusion
cd ml-stable-diffusion
pip install -e .
```

## Conversion

Download the model from HuggingFace or Civit.ai and set the paths in `convert-coreml.sh` and `convert-safetensors.py`.

```
python convert-safetensors.py
./convert-coreml.sh
 ```

 ## Inference Example

```
python -m python_coreml_stable_diffusion.pipeline --prompt "masterpiece, best quality, highres, 1girl, solo, green eyes, solo, low twintails, pom pom (clothes), wariza, poo
l side, tight navy blue school swimsuit, depth of field, from side, looking at viewer" --negative-prompt "EasyNegative, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digi
t, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, lowres graffiti, low quality lowres simple background,
" -i ./blazingdrive-v05a-coreml -o output --compute-unit ALL --model-version blazingdrive-v05a --compute-unit CPU_AND_NE
```
