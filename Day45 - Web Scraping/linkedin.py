import requests
from bs4 import BeautifulSoup
import time
import csv
import random
import os
from dotenv import load_dotenv

# IMPORTANT: Please note that scraping LinkedIn is against their Terms of Service.
# This code is for educational purposes only to demonstrate web scraping techniques.
# Using this code to scrape LinkedIn may result in your account being banned or legal consequences.

class LinkedInScraper:
    def __init__(self):
        """Initialize the LinkedIn scraper with necessary configurations."""
        # Load environment variables for credentials
        load_dotenv()
        
        # User credentials - should be stored in .env file
        self.email = os.getenv("LINKEDIN_EMAIL")
        self.password = os.getenv("LINKEDIN_PASSWORD")
        
        # User agent to mimic a real browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Create a session to maintain cookies
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
        # Base LinkedIn URLs
        self.base_url = "https://www.linkedin.com"
        self.login_url = f"{self.base_url}/login"
        self.search_url = f"{self.base_url}/search/results/people/"
        
    def login(self):
        """Log in to LinkedIn using provided credentials."""
        if not self.email or not self.password:
            print("Error: LinkedIn credentials not found. Please set LINKEDIN_EMAIL and LINKEDIN_PASSWORD in .env file.")
            return False
            
        print("Attempting to log in to LinkedIn...")
        
        # First, get the login page to retrieve CSRF token
        try:
            response = self.session.get(self.login_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract CSRF token - this might change as LinkedIn updates their site
            csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')
            
            # Prepare login data
            login_data = {
                'session_key': self.email,
                'session_password': self.password,
                'loginCsrfParam': csrf
            }
            
            # Perform login
            login_response = self.session.post(self.login_url, data=login_data)
            
            # Check if login was successful
            if login_response.url == self.base_url or 'feed' in login_response.url:
                print("Successfully logged in to LinkedIn")
                return True
            else:
                print("Failed to log in to LinkedIn. Check your credentials.")
                return False
                
        except Exception as e:
            print(f"Error during login: {e}")
            return False
    
    def search_people(self, keywords, location=None, max_pages=1):
        """Search for people on LinkedIn based on keywords and location."""
        print(f"Searching for people with keywords: {keywords}")
        
        results = []
        
        # Build search query parameters
        params = {
            'keywords': keywords,
            'origin': 'GLOBAL_SEARCH_HEADER'
        }
        
        if location:
            params['location'] = location
        
        for page in range(max_pages):
            try:
                params['page'] = page + 1
                
                # Add random delay to avoid being detected as a bot
                sleep_time = random.uniform(3, 7)
                print(f"Waiting {sleep_time:.2f} seconds before next request...")
                time.sleep(sleep_time)
                
                # Make the search request
                search_response = self.session.get(self.search_url, params=params)
                
                if search_response.status_code != 200:
                    print(f"Error: Received status code {search_response.status_code}")
                    break
                
                # Parse the search results
                soup = BeautifulSoup(search_response.text, 'html.parser')
                
                # Extract people from search results
                # The actual selectors would need to be updated based on LinkedIn's current HTML structure
                people_elements = soup.select('li.reusable-search__result-container')
                
                if not people_elements:
                    print("No results found or selector may be outdated")
                    break
                
                for person in people_elements:
                    try:
                        name_element = person.select_one('.entity-result__title-text a')
                        profile_link = name_element.get('href') if name_element else None
                        name = name_element.get_text(strip=True) if name_element else "Name not found"
                        
                        headline_element = person.select_one('.entity-result__primary-subtitle')
                        headline = headline_element.get_text(strip=True) if headline_element else "No headline"
                        
                        location_element = person.select_one('.entity-result__secondary-subtitle')
                        location = location_element.get_text(strip=True) if location_element else "No location"
                        
                        results.append({
                            'name': name,
                            'headline': headline,
                            'location': location,
                            'profile_url': f"{self.base_url}{profile_link}" if profile_link else "No URL"
                        })
                    except Exception as e:
                        print(f"Error parsing person data: {e}")
                
                print(f"Processed page {page+1}, found {len(people_elements)} people")
                
            except Exception as e:
                print(f"Error during search: {e}")
                break
        
        return results
    
    def save_to_csv(self, results, filename="linkedin_results.csv"):
        """Save search results to a CSV file."""
        if not results:
            print("No results to save")
            return
            
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = results[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for result in results:
                    writer.writerow(result)
                    
            print(f"Successfully saved {len(results)} results to {filename}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")
    
    def get_profile_details(self, profile_url):
        """Get detailed information from a LinkedIn profile."""
        print(f"Fetching profile details from: {profile_url}")
        
        try:
            # Add random delay
            time.sleep(random.uniform(3, 7))
            
            profile_response = self.session.get(profile_url)
            
            if profile_response.status_code != 200:
                print(f"Error: Received status code {profile_response.status_code}")
                return None
            
            soup = BeautifulSoup(profile_response.text, 'html.parser')
            
            # Extract profile information
            # Note: These selectors would need to be updated based on LinkedIn's current HTML structure
            profile_data = {}
            
            # Basic information
            profile_data['name'] = self._get_text(soup, '.pv-top-card--list .text-heading-xlarge')
            profile_data['headline'] = self._get_text(soup, '.pv-top-card--list .text-body-medium')
            profile_data['location'] = self._get_text(soup, '.pv-top-card--list .text-body-small[aria-label="Location"]')
            
            # Experience
            profile_data['experiences'] = []
            experience_elements = soup.select('.experience-section .pv-entity__position-group')
            
            for experience in experience_elements:
                company = self._get_text(experience, '.pv-entity__secondary-title')
                role = self._get_text(experience, '.pv-entity__summary-info-container .t-16')
                duration = self._get_text(experience, '.pv-entity__date-range .pv-entity__date-range span:nth-child(2)')
                
                profile_data['experiences'].append({
                    'company': company,
                    'role': role,
                    'duration': duration
                })
            
            # Education
            profile_data['education'] = []
            education_elements = soup.select('.education-section .pv-entity__degree-info')
            
            for education in education_elements:
                institution = self._get_text(education, '.pv-entity__school-name')
                degree = self._get_text(education, '.pv-entity__degree-name .pv-entity__comma-item')
                field = self._get_text(education, '.pv-entity__fos .pv-entity__comma-item')
                
                profile_data['education'].append({
                    'institution': institution,
                    'degree': degree,
                    'field': field
                })
            
            return profile_data
            
        except Exception as e:
            print(f"Error fetching profile details: {e}")
            return None
    
    def _get_text(self, soup, selector):
        """Helper method to extract text from an element."""
        element = soup.select_one(selector)
        return element.get_text(strip=True) if element else "Not found"


def main():
    print("LinkedIn Scraper - Educational Purposes Only")
    print("=" * 50)
    print("WARNING: Scraping LinkedIn violates their Terms of Service.")
    print("This script should NOT be used to actually scrape LinkedIn.")
    print("It is provided solely for educational purposes to demonstrate web scraping techniques.")
    print("=" * 50)
    
    # Create a .env file with LinkedIn credentials before using
    scraper = LinkedInScraper()
    
    # Example usage:
    # if scraper.login():
    #     # Search for people
    #     results = scraper.search_people(keywords="data scientist", location="New York", max_pages=2)
    #     
    #     # Save results to CSV
    #     scraper.save_to_csv(results, "data_scientists_nyc.csv")
    #     
    #     # Get profile details (for educational purposes only)
    #     # if results and results[0]['profile_url'] != "No URL":
    #     #     profile_data = scraper.get_profile_details(results[0]['profile_url'])
    #     #     print(profile_data)


if __name__ == "__main__":
    main()
