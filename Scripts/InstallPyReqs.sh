# pip install langchain==0.3.17       # Langchain for the LLM
# # pip install python-dotenv==1.0.*  #ToDo: Use env to store API keys after implementing keys in the LLM endpoint
# pip install fastapi==0.115.6        # FastAPI for the API server
# pip install uvicorn==0.32.1         # Uvicorn for the API server
# pip install faiss-cpu==1.9.0.post1  # For FAISS
# pip install httpx==0.24.1
# pip install langserve==0.3.0        # For serving Langchain as an API
# pip install pydantic==2.10.4
# pip install langchain-nvidia-ai-endpoints==0.3.7
# pip install gradio==5.9.1
# pip install langchain-community==0.3.16 
# pip install sse_starlette==2.2.1
# pip install arxiv==2.1.3
# pip install pymupdf==1.25.2
# pip install pydantic_factories==1.17.*
# pip install https://github.com/Lexa-B/RExtract/archive/refs/tags/v0.0.1.zip
# pip install matplotlib==3.10.0
# pip install scikit-learn==1.6.1
# pip install keras==3.8.*
# pip install tensorflow==2.12.0
# pip install torch==2.5.1+cu124 --extra-index-url https://download.pytorch.org/whl/cu124


pip install langchain==0.3.17 # For the LLM
pip install langchain-nvidia-ai-endpoints==0.3.9 # For the NVIDIA AI endpoints
pip install langchain_community==0.3.16 # For the community LLM models
pip install rich # For pretty printing
pip install faiss-gpu-cu12==1.10.* # For FAISS on the GPU (CUDA 12)
pip install fast-langdetect==0.2.5 # For language detection
pip install hjson==3.1.0 # Even though this is for hjson, we use it for JSONC files, such as the model config
pip install langchain-openai==0.3.4 # For the OpenAI LLM
#pip install gradio==5.15.0 # For the Gradio UI
pip install langserve==0.3.1 # For the LangServe API server
pip install sse_starlette==2.2.1 # For the LangServe API server
pip install git+https://github.com/Lexa-B/DramaticLogger.git@v0.0.2-pre4
pip install lxml==5.3.1 # For the XML parser
pip install base32-crockford==0.3.0 # For the base32 encoder/decoder