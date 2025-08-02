import os
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory, SQLiteChatMessageHistory
from langchain.agents import initialize_agent
from composio_langchain import ComposioToolSet
from .mixtral_handler import MixtralHandler  # Import handler

class ExcaliburCore:
    def __init__(self):
        self.llm = Ollama(model="mixtral:8x22b", base_url="http://localhost:11434")
        self.memory = ConversationBufferMemory(chat_memory=SQLiteChatMessageHistory("chat_history.db"))
        toolset = ComposioToolSet()
        composio_tools = toolset.get_tools(["git", "file_operations"])
        tools = composio_tools + [
            {"name": "Shell", "func": lambda x: os.popen(x).read(), "description": "Run shell commands"}
        ]
        self.agent = initialize_agent(tools, self.llm, memory=self.memory, agent_type="zero-shot-react-description")
        self.mixtral_handler = MixtralHandler()  # For fine-tuning stubs

    def process_query(self, prompt):
        config = open(os.path.expanduser("~/.llm_config")).read() if os.path.exists(os.path.expanduser("~/.llm_config")) else "Default preferences"
        full_prompt = f"Preferences: {config}\nHistory: {self.memory.load_memory_variables({})['history']}\n{prompt}"
        response = self.agent.run(full_prompt)
        self.memory.save_context({"input": prompt}, {"output": response})
        return response
