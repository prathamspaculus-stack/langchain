from langchain_community.document_loaders import PyPDFLoader

loaders = PyPDFLoader('2022-09 - Lodine 600 mg SR Tablets (Almirall) -pil.pdf')

docs= loaders.load()

print( len(docs))


for page in docs:
    print(page.page_content)