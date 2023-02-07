import scrapy
import pandas as pd

# Create a Spider class to scrape host data from Airbnb
class HostSpider(scrapy.Spider):
  # Set the name of the spider
  name = 'host_spider'

  # Set the start URL for the spider
  start_urls = ['https://www.airbnb.com/s/Rhode-Island--United-States/homes?refinement_paths%5B%5D=%2Fhomes&query=Rhode%20Island%2C%20United%20States&place_id=ChIJYbX9Zl8E5IkR6QJx6xQ_2QM&source=structured_search_input_header&search_type=pagination']

  # Set the custom settings for the spider
  custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'DOWNLOAD_DELAY': 3
  }

  # Define the parse method to handle the response from the start URL
  def parse(self, response):
    # Find all the listing cards on the search results page
    listing_cards = response.css('div._1df8k1k8')

    # Loop through each listing card
    for listing_card in listing_cards:
      # Extract the host data
      host_name = listing_card.css('div._1ohxh37::text').get()
      contact_info = listing_card.css('div._1u5v60gu::text').get()
      email = ''
      phone_number = ''
      if contact_info:
        # Split the contact info text by newline character
        lines = contact_info.split('\n')
        # Loop through each line
        for line in lines:
          # If the line starts with "Email: " extract the email address
          if line.startswith('Email: '):
            email = line[7:]
          # If the line starts with "Phone: " extract the phone number
          elif line.startswith('Phone: '):
            phone_number = line[7:]

      # Yield the host data as an item
      yield {
        'name': host_name,
        'email': email,
        'phone_number': phone_number
      }

    # Find the next page link
    next_page_link = response.css('link[rel="next"]::attr(href)').get()
    if next_page_link:
      # Follow the next page link
      yield response.follow(next_page_link, callback=self.parse)

# Run the spider to scrape the host data
def run_spider():
  # Create a process to run the spider
  process = scrapy.crawler.CrawlerProcess()
  process.crawl(HostSpider)
  process.start()

# Main function
def main():
  # Run the spider
  run_spider