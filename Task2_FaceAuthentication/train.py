from insightface.app import FaceAnalysis


face_app = FaceAnalysis(name="buffalo_l")

face_app.prepare(ctx_id=-1)

print("Model downloaded and ready to use.")