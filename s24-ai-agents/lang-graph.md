# LangGraph
Lang graph is a specialized framework within the lang chain ecosystem that focuses on building and managing stateful, multi-agent applications using large language models (Llms).

Its key purpose is to orchestrate complex workflows where multiple agents can collaborate or work independently to achieve specific tasks.

Unlike simpler agent frameworks, Lang Graph allows for more control and flexibility, making it suitable for applications where agents need to manage complex decision making processes, incorporate human feedback, or handle various domain specific tasks.


```bash
$ python -m venv langgraph
$ source langgraph/bin/activate

# install specific modules
$ pip install langgraph langchain openai

$ export OPENAI_API_KEY="MYAPIKEY"

```