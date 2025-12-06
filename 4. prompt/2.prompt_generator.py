from langchain_core.prompts import PromptTemplate

templet = PromptTemplate(
    template = """
please summarize the research paper titled = "{paper_input}" with the following specifications:
Explaination stle: {style_input}
Explaination length: {length_input}
1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathemsatical concept using simple, intutivre code snippets where applicable.
2. Analogies:
    - Use relatible analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficiet informarion available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provide style and length.
""",
input_variables = ['paper_input', 'style_input', 'length_input'],
validate_template=True
)

templet.save('templet.json')
