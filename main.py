import requests
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords

# Якщо ви ще не завантажували NLTK стоп-слова, потрібно виконати:
# nltk.download('stopwords')

# === 1. Завантаження тексту з Project Gutenberg ===
url = "https://www.gutenberg.org/files/1342/1342-0.txt"  # URL до книги "Pride and Prejudice"
response = requests.get(url)

# Перевірка статусу запиту
if response.status_code == 200:
    text = response.text
    print("Текст успішно завантажено!")
else:
    print("Помилка завантаження тексту!")

# === 2. Очищення тексту ===
# Видаляємо метадані Project Gutenberg
start_text = re.search(r'\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*', text)
end_text = re.search(r'\*\*\* END OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*', text)

if start_text and end_text:
    clean_text = text[start_text.end():end_text.start()]
else:
    clean_text = text

# Видаляємо небажані символи та робимо текст малими літерами
clean_text = clean_text.lower()
clean_text = re.sub(r'[^a-z\s]', '', clean_text)  # Видаляємо все окрім літер та пробілів

# === 3. Аналіз тексту ===
# Токенізація (розбиваємо текст на слова)
words = clean_text.split()

# Видаляємо стоп-слова (часті слова, які не несуть особливого смислу, наприклад: "the", "and")
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Підрахунок частоти слів
word_counts = Counter(filtered_words)

# Виведення 10 найчастіших слів
print("10 найчастіших слів:")
print(word_counts.most_common(10))

# === 4. Збереження результатів у файл ===
with open('word_frequencies.txt', 'w') as f:
    for word, count in word_counts.items():
        f.write(f"{word}: {count}\n")

print("Результати збережено у файл 'word_frequencies.txt'")
