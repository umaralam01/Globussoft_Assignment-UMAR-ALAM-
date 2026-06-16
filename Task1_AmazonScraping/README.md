# Amazon Product Scraper

## Project Overview

This project scrapes laptop product information from Amazon India (amazon.in) using Python, Requests, and BeautifulSoup. The scraper collects product details from multiple search result pages and exports the data into a timestamped CSV file for further analysis.

---

## Features

* Multi-page scraping using pagination
* Extracts product information:

  * Product Title
  * Price
  * Rating
  * Product Image URL
  * Ad / Organic Classification
* Removes duplicate products
* Generates timestamped CSV output
* Lightweight implementation without Selenium

---

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas


---

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

---

## Execution

Open the Jupyter Notebook or Jupyter Lab and run all cells:

```bash
jupyter lab
```

Run:

```text
Task1_Amazon_Scraping.ipynb
```

---

## Data Collected

The scraper extracts the following fields:

| Column Name | Description                                                |
| ----------- | ---------------------------------------------------------- |
| Image       | Product image URL                                          |
| Title       | Product title                                              |
| Rating      | Customer rating                                            |
| Price       | Product price                                              |
| Ad_Organic  | Indicates whether the product is Ad or Organic |

---

## Output

The scraped data is exported as:

```text
amazon_laptop_YYYY-MM-DD_HH-MM-SS.csv
```

Example:

```text
amazon_laptop_2026-06-16_08-07-19.csv
```

---

## Sample Result

* Multiple product pages scraped successfully
* Duplicate products removed
* Ad and Organic products classified separately

---

## Notes

* Amazon page structures may change over time.
* Some products may not contain ratings or prices; such values are stored as N/A.
* Image URLs are collected directly from Amazon search results.

