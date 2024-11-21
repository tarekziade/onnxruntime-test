Onnxruntime vs Llama.cpp
========================


Run onnx with `make run-onnx`  (CPU)
Run llama.cpp with `make run-llama` (CPU)


On Apple M1:

```
➜  onnxruntime-test git:(main) ✗ make run-onnx
Qwen directory exists. Skipping download.
./bin/python3 run.py
Loading model...
Model loaded

Generator created
Running generation loop ...
The Eiffel Tower stands at 324 meters (1,063 feet), the tallest structure in Paris and the world's tallest man-made structure. It has been the highest structure in the world since 1930 and holds the record for being the tallest free-standing structure in France. Due to the addition of a broadcasting aerial in 1957, the Eiffel Tower now exceeds the Chrysler Building by 5.2 meters.
Prompt length: 247, New tokens: 96, Time to first: 0.83s, Prompt tokens per second: 295.87 tps, New tokens per second: 4.85 tps
```


```
➜  onnxruntime-test git:(main) ✗ make run-llama
The Eiffel Tower, located in Paris, France, stands at 324 meters tall, surpassing the Washington Monument to become the tallest man-made structure in the world, standing at 410 feet. It was the tallest structure in Paris for 41 years, until the Chrysler Building was finished in 1930. The Eiffel Tower was also the first structure to reach a height of 300 meters and was added a broadcasting aerial in 1

llama_perf_sampler_print:    sampling time =      11,02 ms /   333 runs   (    0,03 ms per token, 30206,82 tokens per second)
llama_perf_context_print:        load time =     242,78 ms
llama_perf_context_print: prompt eval time =     294,28 ms /   233 tokens (    1,26 ms per token,   791,77 tokens per second)
llama_perf_context_print:        eval time =    1610,17 ms /    99 runs   (   16,26 ms per token,    61,48 tokens per second)
llama_perf_context_print:       total time =    1927,63 ms /   332 tokens
ggml_metal_free: deallocating
```


