from smolagents import CodeAgent, InferenceClientModel
import os

mon_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]

# Initialize a model (using Hugging Face Inference API)
model = InferenceClientModel(token=mon_token,
                             model_id="mistralai/Mistral-7B-Instruct-v0.3")

# Create an agent with no tools
agent = CodeAgent(tools=[], model=model)

# Run the agent with a task
result = agent.run("Calculate the sum of numbers from 1 to 10")
result2 = agent.run("Choose a name for a baby girl")
print(result)
print(result2)


# Adding Tools

from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool

model = InferenceClientModel(token=mon_token,
                             model_id="mistralai/Mistral-7B-Instruct-v0.3")
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
)

# Now the agent can search the web!
result3 = agent.run("Resume moi comment est fabriqué l'indice des prix à la consommation français. Pour cela fais une recherche sur insee.fr.")
print(result3)