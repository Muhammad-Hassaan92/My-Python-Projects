import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.optimizers import Adam

# Load a large dataset (e.g., a corpus from NLTK or an external file)
import nltk
from nltk.corpus import reuters
nltk.download('reuters')
nltk.download('punkt')

# Prepare dataset
text_data = ' '.join([' '.join(sent) for fileid in reuters.fileids() for sent in reuters.sents(fileid)])

# Tokenize text
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text_data])
total_words = len(tokenizer.word_index) + 1

# Create input sequences
input_sequences = []
for line in text_data.split(".\n"):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        input_sequences.append(token_list[:i+1])

# Pad sequences
max_sequence_length = max(len(seq) for seq in input_sequences)
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')

# Split data into features and labels
X, y = input_sequences[:, :-1], input_sequences[:, -1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)

# Build the model
model = Sequential([
    Embedding(total_words, 256, input_length=max_sequence_length-1),
    LSTM(256, return_sequences=True),
    LSTM(128),
    Dense(256, activation='relu'),
    Dense(total_words, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=50, verbose=2, batch_size=128)

# Function to predict next words
def complete_sentence(seed_text, next_words=10):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# Example Usage
print(complete_sentence("The stock market"))