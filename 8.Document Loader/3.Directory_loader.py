from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path="Cinacalcet",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

for d in docs:
    print(d.metadata)
