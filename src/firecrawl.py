import os
from firecrawl import FirecrawlApp, ScrapeOptions
from dotenv import load_dotenv

load_dotenv()

class FirecrawlService:
    def __init__(self):
        """Retrieve and access the Firecrawl API to begin research tasks"""
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("Missing Firecrawl API Key environment variable")
        self.app = FirecrawlApp(api_key=api_key)

    def search_companies(self, query: str, num_results: int = 5):
        """Search for the companies related to query, return top 5 results"""
        try:
            result = self.app.search(
                query = f"{query} company pricing",
                limit = num_results,
                scrape_options = ScrapeOptions(
                    formats=["markdown"]
                )
            )

            return result
        except Exception as e:
            print(e)
            return []
        
    def scrape_company_pages(self, url: str):
        """After finding company pages, scrape the information on pages"""
        try:
            result = self.app.scrape_url(
                url,
                formats=["markdown"],
            )
            return result
        except Exception as e:
            print(e)
            return None
        
    
            