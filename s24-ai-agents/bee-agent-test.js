import {BeeAgent} from "bee-agent-framework/agents/bee/agent"
import { OllamaChatLLM } from "bee-agent-framework/adapters/ollama/chat"
import { TokenMemory} from "bee-agent-framework/memory/tokenMemory"
import { DuckDuckGoSearchTool } from "bee-agent-framework/tools/search/duckDuckGoSearch"
import { OpenMeteoTool } from "bee-agent-framework/tools/weather/openMeteo"

// to define a custome tool
import {tool} from "bee-agent-framework/tools"

const CustomTool = tool("CustomTool", {
  description: "Custom Tool to handle specific tasks",
  run : async (input) => {
    return `Handled task with input: ${input}`;
  },
});,

const llm = new OllamaChatLLM();
const memory = new TokenMemory({ llm });
const tools = [ new DuckDuckGoSearchTool(), new OpenMeteoTool() ];

const agent = new BeeAgent({ llm, memory, tools,});

// Adding custom tool to the agent
agent.addTool(new CustomTool());


agent.observe((emitter) => {
  emitter.on("update", async ({data}) => {
    console.log(`Update: `, data);
  });
});

const response = await agent
  .run({prompt: "Whats the current weather in Atlanta"})
  .observe((emitter) => {
    emitter.on("update", async ({data, update, meta}) => {
      console.log(`Agent (${update.key}) : `, update.value);
    });
  });

console.log(`Agent Response: `, response.result.text);