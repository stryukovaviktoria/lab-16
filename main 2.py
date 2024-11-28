import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords

# Якщо ви ще не завантажували NLTK пакети, потрібно виконати:
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

# 1. Збереження тексту у файлі
text = """Artificial intelligence (AI) refers to the simulation of human intelligence in machines
that are programmed to think like humans and mimic their actions. The term may also be applied
to any machine that exhibits traits associated with a human mind such as learning and problem-solving."""

# Зберігаємо текст у файл
with open('input_text.txt', 'w') as file:
    file.write(text)

# 2. Читання тексту з файлу
with open('input_text.txt', 'r') as file:
    text = file.read()

# 3. Токенізація по словам
tokens = word_tokenize(text)

# 4. Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# 5. Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# 6. Видалення пункуації
filtered_tokens = [token for token in filtered_tokens if token.isalpha()]
