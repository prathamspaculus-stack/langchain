# from langchain_community.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()

# results = search_tool.invoke('today cricket news')

# print(results)

from langchain_community.tools import ShellTool

shell_tool = ShellTool()

results = shell_tool.invoke('whoami')

print(results)