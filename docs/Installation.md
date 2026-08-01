# Installation Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/SubhamKumarg/Colog.git
   cd Colog
   ```

2. **Set up Virtual Environment** (Python 3.12 required)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with any required paths
   ```

5. **Install Local Models**
   - Install [Ollama](https://ollama.ai/)
   - Pull the required model: `ollama run qwen` (or `gemma`)

6. **Run the Application**
   ```bash
   streamlit run frontend/app.py
   ```
