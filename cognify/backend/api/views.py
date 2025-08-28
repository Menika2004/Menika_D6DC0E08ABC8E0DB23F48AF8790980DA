from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class HealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"})


class ReasonView(APIView):
    """Accepts a query and context, returns structured, explainable reasoning output."""

    def post(self, request):
        payload = request.data or {}
        query = payload.get("query", "").strip()
        domain = payload.get("domain", "general")
        context = payload.get("context", {})

        if not query:
            return Response({"error": "Missing 'query'"}, status=status.HTTP_400_BAD_REQUEST)

        # Simple placeholder reasoning: outline steps and produce an answer
        reasoning_steps = [
            "Parse intent and entities from the query",
            f"Identify domain-specific needs for '{domain}'",
            "Construct multi-step plan balancing clarity and utility",
            "Generate actionable recommendations",
        ]

        actions = [
            {"title": "Key actions", "items": [
                "Clarify objective and constraints",
                "Apply domain heuristics and best practices",
                "Provide top-3 prioritized recommendations",
            ]}
        ]

        result_summary = (
            "This is a placeholder response. The engine parsed the query, applied domain-aware"
            " reasoning, and produced prioritized, actionable recommendations with an explainable chain of thought."
        )

        return Response({
            "query": query,
            "domain": domain,
            "steps": reasoning_steps,
            "actions": actions,
            "summary": result_summary,
        })

# Create your views here.
