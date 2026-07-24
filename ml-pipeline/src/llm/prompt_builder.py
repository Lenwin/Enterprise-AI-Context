from src.retrieval.query import RetrievalQuery

class PromptBuilder:

    def build(self,query:RetrievalQuery,context:str)->str:
        prompt = f"""You are an Enterprise AI Assistant.

Answer ONLY using the information provided in the context.

If the answer cannot be found in the context, say:
"I couldn't find that information in the provided documents."

Always be concise and accurate.

==========================
CONTEXT
==========================

{context}

==========================
QUESTION
==========================

{query.query}

==========================
ANSWER
==========================
"""

        return prompt.strip()