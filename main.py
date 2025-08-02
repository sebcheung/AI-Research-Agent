from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()

def main():
    """Display LLM response and information"""
    workflow = Workflow()
    print("Developer Tools Research Agent")

    spacing = 60
    while True:
        query = input("\nDeveloper Tools Query: ").strip()
        # Exiting out of Research
        if query.lower() in {"quit", "exit"}:
            break
        if query:
            result = workflow.run(query)
            print(f"\nResults for: {query}")
            print("=" * spacing)

            # Info structure displayed to user for each company found with tools
            for i, company in enumerate(result.companies, 1):
                print(f"\n{i}. {company.name}")
                print(f"   🌐 Website: {company.website}")
                print(f"   💰 Pricing: {company.pricing_model}")
                print(f"   📖 Open Source: {company.is_open_source}")

                if company.tech_stack:
                    print(f"   🛠️  Tech Stack: {', '.join(company.tech_stack[:5])}")

                if company.language_support:
                    print(
                        f"   💻 Language Support: {', '.join(company.language_support[:5])}"
                    )

                if company.api_available is not None:
                    api_status = (
                        "✅ Available" if company.api_available else "❌ Not Available"
                    )
                    print(f"   🔌 API: {api_status}")

                if company.integration_capabilities:
                    print(
                        f"   🔗 Integrations: {', '.join(company.integration_capabilities[:4])}"
                    )

                if company.description and company.description != "Analysis failed":
                    print(f"   📝 Description: {company.description}\n")

            if result.analysis:
                print("Developer Recommendations: ")
                print("-" * spacing)
                print(result.analysis)

if __name__ == "__main__":
    main()