from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()
model1 = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.7)
model2 = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.5)
parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model1 | parser
config = {
    'tags' : ['llm_app', 'report_generation', 'summarization'],
    'metadata': {'model1': 'gpt-4o-mini', 'model1-temp':0.7, 'parser': 'stroutputparser'}
}

result = chain.invoke({'topic': 'Unemployment in India'})

print(result)
