from src.llm.client import BaseLLMClient
from src.llm.prompt_builder import PromptBuilder
from src.llm.response import LLMResponse
from src.retrieval.context_builder import ContextBuilder
from src.retrieval.hybrid import HybridRetriever
from src.retrieval.query import RetrievalQuery
from src.retrieval.reranker import CrossEncoderReranker
from src.llm.rag_response import RAGResponse

class EnterpriseRAGPipeline:

    def __init__(self,retriever:HybridRetriever,reranker:CrossEncoderReranker,llm:BaseLLMClient):
        self.retriever = retriever
        self.reranker = reranker
        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()
        self.llm = llm
    def ask(self,question:str,top_k:int=5)->LLMResponse:
        query = RetrievalQuery(query=question,top_k=top_k)
        results = self.retriever.retrieve(query)

        results = self.reranker.rerank(query=question,results=results,top_k=top_k)
        context = self.context_builder.build(results)

        prompt = self.prompt_builder.build(query=query,context=context)

        llm_response =  self.llm.generate(prompt)

        return RAGResponse(
            answer = llm_response.answer,
            sources = results
        )