from src.models.search_result import SearchResult

class ContextBuilder:
    def build(self,results:list[SearchResult])->str:
        if not results:
            return ""
        context = []
        for i,result in enumerate(results,start=1):
            context.append(
                f"""
Document {i}

Document ID: {result.document_id}
Source: {result.source}

{result.content}
"""
            )

        return "\n" + "=" * 80 + "\n".join(context)