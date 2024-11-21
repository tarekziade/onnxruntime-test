import onnxruntime_genai as og
import time


prompt = """
<|im_start|>system
You are an expert in summarizing text
<|im_end|>  

<|im_start|>user 
Summarize the following text in 30 words maximum, capturing the essential parts:

The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. 
Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the 
Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler 
Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. 
Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler 
Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest 
free-standing structure in France after the Millau Viaduct.  

Summary:
<|im_end|>
<|im_start|>assistant
"""


def summarize_text(model_path):
    print("Loading model...")
    started_timestamp = 0
    first_token_timestamp = 0

    model = og.Model(model_path)
    print("Model loaded")
    tokenizer = og.Tokenizer(model)
    tokenizer_stream = tokenizer.create_stream()
    print()

    # 10 to 40 tokens
    search_options = {"max_length": len(prompt) + 40}

    started_timestamp = time.time()

    input_tokens = tokenizer.encode(prompt)

    params = og.GeneratorParams(model)
    params.set_search_options(**search_options)
    params.input_ids = input_tokens
    generator = og.Generator(model, params)

    print("Generator created")
    print("Running generation loop ...")

    first = True
    new_tokens = []

    first = True
    try:
        while not generator.is_done():
            generator.compute_logits()
            generator.generate_next_token()
            if first:
                first_token_timestamp = time.time()
                first = False

            new_token = generator.get_next_tokens()[0]
            print(tokenizer_stream.decode(new_token), end="", flush=True)
            new_tokens.append(new_token)
    except KeyboardInterrupt:
        print("  --control+c pressed, aborting generation--")
    finally:
        print()

    prompt_time = first_token_timestamp - started_timestamp
    run_time = time.time() - first_token_timestamp
    print(
        f"Prompt length: {len(input_tokens)}, New tokens: {len(new_tokens)}, "
        f"Time to first: {(prompt_time):.2f}s, Prompt tokens per second: {len(input_tokens)/prompt_time:.2f} tps, "
        f"New tokens per second: {len(new_tokens)/run_time:.2f} tps"
    )


if __name__ == "__main__":
    summarize_text("qwen")
