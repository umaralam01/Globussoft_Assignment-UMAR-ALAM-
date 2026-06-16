# Face Authentication Using FastAPI and InsightFace

This project was created as part of a technical assignment.

The application compares two face images and checks whether they belong to the same person. It uses the InsightFace pretrained model for face detection and feature extraction, and FastAPI for serving the API.

## How it Works

1. User uploads two face images.
2. Faces are detected from both images.
3. Facial embeddings are extracted.
4. Cosine similarity is calculated between the embeddings.
5. Based on the similarity score, the system returns:

   * Same Person
   * Different Person

Along with:

* Similarity Score
* Face Bounding Boxes

---

## Project Files

* `app.py` - FastAPI application
* `train.py` - Downloads and initializes the InsightFace model
* `predict.py` - Face verification logic
* `requirements.txt` - Required dependencies
* `sample_images/` - Images used for testing

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the model:

```bash
python train.py
```

Start the API:

```bash
python app.py
```

After the server starts, open:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /verify

Upload:

* image1
* image2

Example response:

```json
{
    "verification_result": "same person",
    "similarity_score": 0.82,
    "bbox1": [...],
    "bbox2": [...]
}
```

---

## Libraries Used

* FastAPI
* InsightFace
* OpenCV
* NumPy
* ONNX Runtime

---

## Notes

The project uses the pretrained `buffalo_l` model provided by InsightFace. The model is downloaded automatically during the first execution of `train.py`.
