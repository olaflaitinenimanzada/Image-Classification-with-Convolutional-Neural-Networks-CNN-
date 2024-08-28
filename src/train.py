from tensorflow.keras.optimizers import Adam
from model import create_model

def train_model():
    model = create_model()
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    # Eğitim verilerini yükleme ve modeli eğitme kodu
    pass

if __name__ == "__main__":
    train_model()
