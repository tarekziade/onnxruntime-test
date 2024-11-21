Onnxruntime vs Llama.cpp
========================

Models: 

- Qwen2.5-0.5B-Instruct int4 for onnxruntime
- Qwen2.5-0.5B-Instruct GGUF q4_0 for llama.cpp

Hardware Specs:

- Apple M1 Pro 32GB
- Windows 11 AMD Ryzen Threadripper PRO 1- Cores 128G RAM


Software:

- onnxruntime-genai 0.5.1 (non CUDA for the CPU test)
- llama.cpp (running on CPU only for the CPU test, using gl=0)



CPU
---

For macOS onnxruntime does not seem to leverage CoreML or any other hardware acceleration on MacOS
as opposed as llama.cpp, making it 13x faster.

For Windows, onnxruntime is 2 times faster than the non avx build of llama.cpp
and is 1.6x slower than the avx build of llama.cpp  

Apple M1 onnx 4.85 tokens/s:

```
Prompt length: 247, New tokens: 96, Time to first: 0.83s, Prompt tokens per second: 295.87 tps, New tokens per second: 4.85 tps
```


Apple M1 llama 62 tokens/s:

```
llama_perf_sampler_print:    sampling time =      11,02 ms /   333 runs   (    0,03 ms per token, 30206,82 tokens per second)
llama_perf_context_print:        load time =     242,78 ms
llama_perf_context_print: prompt eval time =     294,28 ms /   233 tokens (    1,26 ms per token,   791,77 tokens per second)
llama_perf_context_print:        eval time =    1610,17 ms /    99 runs   (   16,26 ms per token,    61,48 tokens per second)
llama_perf_context_print:       total time =    1927,63 ms /   332 tokens
```



Windows 11 onnx 67 tokens/s:

```
Prompt length: 247, New tokens: 97, Time to first: 0.38s, Prompt tokens per second: 643.80 tps, New tokens per second: 67.34 tps
```

Windows 11 llama non avx 37 tokens/s:

```
llama_perf_sampler_print:    sampling time =      10.06 ms /   328 runs   (    0.03 ms per token, 32591.41 tokens per second)
llama_perf_context_print:        load time =     369.39 ms
llama_perf_context_print: prompt eval time =    2701.08 ms /   228 tokens (   11.85 ms per token,    84.41 tokens per second)
llama_perf_context_print:        eval time =    2653.97 ms /    99 runs   (   26.81 ms per token,    37.30 tokens per second)
llama_perf_context_print:       total time =    5385.98 ms /   327 tokens
```


Windows 11 avx 112 tokens/s:

```
llama_perf_sampler_print:    sampling time =      10.91 ms /   328 runs   (    0.03 ms per token, 30053.14 tokens per second)
llama_perf_context_print:        load time =     359.68 ms
llama_perf_context_print: prompt eval time =     692.37 ms /   228 tokens (    3.04 ms per token,   329.31 tokens per second)
llama_perf_context_print:        eval time =     883.43 ms /    99 runs   (    8.92 ms per token,   112.06 tokens per second)
llama_perf_context_print:       total time =    1606.08 ms /   327 tokens
```


GPU 
---

TBD
