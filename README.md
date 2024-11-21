Onnxruntime vs Llama.cpp
========================


Run onnx with `make run-onnx`  (CPU)
Run llama.cpp with `make run-llama` (CPU)


Apple M1 onnx:

```
Prompt length: 247, New tokens: 96, Time to first: 0.83s, Prompt tokens per second: 295.87 tps, New tokens per second: 4.85 tps
```


Apple M1 llama:

```
llama_perf_sampler_print:    sampling time =      11,02 ms /   333 runs   (    0,03 ms per token, 30206,82 tokens per second)
llama_perf_context_print:        load time =     242,78 ms
llama_perf_context_print: prompt eval time =     294,28 ms /   233 tokens (    1,26 ms per token,   791,77 tokens per second)
llama_perf_context_print:        eval time =    1610,17 ms /    99 runs   (   16,26 ms per token,    61,48 tokens per second)
llama_perf_context_print:       total time =    1927,63 ms /   332 tokens
```



Windows 11 onnx

```
Prompt length: 247, New tokens: 97, Time to first: 0.38s, Prompt tokens per second: 643.80 tps, New tokens per second: 67.34 tps
```

Windows 11 non avx

```
llama_perf_sampler_print:    sampling time =      10.06 ms /   328 runs   (    0.03 ms per token, 32591.41 tokens per second)
llama_perf_context_print:        load time =     369.39 ms
llama_perf_context_print: prompt eval time =    2701.08 ms /   228 tokens (   11.85 ms per token,    84.41 tokens per second)
llama_perf_context_print:        eval time =    2653.97 ms /    99 runs   (   26.81 ms per token,    37.30 tokens per second)
llama_perf_context_print:       total time =    5385.98 ms /   327 tokens
```


Windows 11 avx 

```
llama_perf_sampler_print:    sampling time =      10.91 ms /   328 runs   (    0.03 ms per token, 30053.14 tokens per second)
llama_perf_context_print:        load time =     359.68 ms
llama_perf_context_print: prompt eval time =     692.37 ms /   228 tokens (    3.04 ms per token,   329.31 tokens per second)
llama_perf_context_print:        eval time =     883.43 ms /    99 runs   (    8.92 ms per token,   112.06 tokens per second)
llama_perf_context_print:       total time =    1606.08 ms /   327 tokens
```

