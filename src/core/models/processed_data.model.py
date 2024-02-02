class LoadedData:
  def __init__(self, text: str, text_embedded, duplicates_to: int):
    self.text = text,
    self.text_embedded = text_embedded,
    self.duplicates_to = duplicates_to
    
  def __str__(self) -> str:
    return f"LoadedData(embedding_dim={len(self.text_embedded)})"