class TrainData:
  def __init__(self, text_left_embedded, text_right_embedded, label: int):
    self.text_left_embedded = text_left_embedded,
    self.text_right_embedded = text_right_embedded,
    self.label = label
    
  def __str__(self) -> str:
    return f"TrainData(embedding_dim={len(self.text_left_embedded)}, label={self.label})"