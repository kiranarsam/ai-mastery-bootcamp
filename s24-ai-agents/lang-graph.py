from langgraph.graph import StateGraph, MessagesState

from langchain_core.tools import tool

from langgraph.prebuilt import ToolNode
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage

@tool
def search(quer: str):
  """ Simulate a web search """
  if "weather" in query.lower():
    return "It is sunny."
  return "No data available."

tools = [search]
tool_node = ToolNode(tools)

checkpointer = MemorySaver()

model = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0).bind_tools(tools)

def call_model(state: MessagesState):
  messages = state['messages']
  responses = model.invoke(messages)
  return {"messages": [responses]}

def should_continue(state: MessagesState):
  if state["messages"][-1].tool_calls:
    return "tools"
  return "END"

workflow = StateGraph(MessagesState)

workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_edge("START", "agent")
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("tools", "agent")

app = workflow.compile(checkpointer=checkpointer)

final_state = app.invoke(
  {
    "messages": [HumanMessage(content="What is the weather today")]
  },
  config={"configurable" : {"thread_id" : 1}}
)

print(final_state["messages"][-1].content)
