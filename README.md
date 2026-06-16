# Globussoft Assignment

This repository contains solutions for both tasks provided in the assignment.

## Task 1 - Amazon Product Scraper

A Python-based web scraper developed for Amazon India laptop search results.

### Features

* Scrapes laptop product information
* Extracts:

  * Product Title
  * Price
  * Rating
  * Image URL
  * Ad / Organic Classification
* Saves output in CSV format
* Generates timestamped output files

Location:

```text
Task1_AmazonScraping/
```

---

## Task 2 - Face Authentication API

A FastAPI-based face verification system built using InsightFace.

### Features

* Accepts two face images
* Detects faces
* Extracts facial embeddings
* Computes similarity score
* Returns:

  * Verification Result
  * Similarity Score
  * Bounding Boxes

Location:

```text
Task2_FaceAuthentication/
```

---

## Installation

Install all required dependencies:

```bash
pip install -r requirements.txt
```

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* FastAPI
* InsightFace
* OpenCV
* NumPy
* ONNX Runtime
