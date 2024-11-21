VENV_DIR = .
HUGGINGFACE_CLI = bin/huggingface-cli
MODEL_DIR = .
QWEN_DIR = qwen

install: $(VENV_DIR) download_model

$(VENV_DIR):
	python3.12 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r requirements.txt

download_model: $(VENV_DIR)
	if [ ! -d "$(QWEN_DIR)" ]; then \
		echo "Downloading Qwen model..."; \
		${VENV_DIR}/bin/python3 -m onnxruntime_genai.models.builder -m "Qwen/Qwen2.5-0.5B-Instruct" -o $(QWEN_DIR) -p int4 -e cpu; \
	else \
		echo "Qwen directory exists. Skipping download."; \
	fi

# Clean up
clean:
	rm -rf $(VENV_DIR)
	rm -rf $(MODEL_DIR)/*
	rm -rf $(QWEN_DIR)

run-onnx: install
	${VENV_DIR}/bin/python3 run.py

run-llama: 
	./llama.sh

.PHONY: all download_model clean run-onnx runn-llama


