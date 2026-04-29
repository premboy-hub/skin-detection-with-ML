import tensorflow as tf
# Removed unused import: from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras import layers, models  # type: ignore

# Image settings
IMG_SIZE = 128
BATCH_SIZE = 16

# Data loading
train_data = tf.keras.utils.image_dataset_from_directory(
    'dataset/',
    validation_split=0.2,
    subset='training',
    seed=123,
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE
)

val_data = tf.keras.utils.image_dataset_from_directory(
    'dataset/',
    validation_split=0.2,
    subset='validation',
    seed=123,
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE
)

# Normalization layer
normalization_layer = tf.keras.layers.Rescaling(1./255)

# Apply normalization
train_data = train_data.map(lambda x, y: (normalization_layer(x), y))
val_data = val_data.map(lambda x, y: (normalization_layer(x), y))

# Model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(7, activation='softmax')  # Assuming 7 classes from the dataset
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Fixed: Use sparse for integer labels
    metrics=['accuracy']
)

# Train model
model.fit(train_data, validation_data=val_data, epochs=5)

# Save model
model.save('model/skin_model.h5')

print("✅ Model Trained & Saved Successfully!")
loss, accuracy = model.evaluate(val_data)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")

loss, accuracy = model.evaluate(val_data)

with open("model/accuracy.txt", "w") as f:
    f.write(str(accuracy))