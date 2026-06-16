import cv2
import numpy as np
from insightface.app import FaceAnalysis

# Load model
face_app = FaceAnalysis(name="buffalo_l")
face_app.prepare(ctx_id=-1)

def verify_faces(img1_path, img2_path):

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    faces1 = face_app.get(img1)
    faces2 = face_app.get(img2)

    if len(faces1) == 0 or len(faces2) == 0:
        return {
            "error": "Face not detected"
        }

    emb1 = faces1[0].embedding
    emb2 = faces2[0].embedding

    similarity = np.dot(emb1, emb2) / (
        np.linalg.norm(emb1) * np.linalg.norm(emb2)
    )

    result = "same person"

    if similarity < 0.5:
        result = "different person"

    return {
        "verification_result": result,
        "similarity_score": float(similarity),
        "bbox1": faces1[0].bbox.tolist(),
        "bbox2": faces2[0].bbox.tolist()
    }


if __name__ == "__main__":

    output = verify_faces(
        "sample_images/Person1.jpg",
        "sample_images/Person2.jpg"
    )

    print(output)