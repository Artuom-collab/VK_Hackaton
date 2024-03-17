# Создание датасетов

import pandas as pd
import numpy as np

# Создаем базовый train.csv
train_df = pd.DataFrame({
    'id': range(1, 101),  # Пример: 100 объектов
    'lat': np.random.uniform(-90, 90, 100),
    'lon': np.random.uniform(-180, 180, 100),
    'score': np.random.randint(1, 100, 100)  # Простое случайное заполнение
})

# Создаем базовый test.csv
test_df = pd.DataFrame({
    'id': range(101, 151),  # Пример: 50 объектов
    'lat': np.random.uniform(-90, 90, 50),
    'lon': np.random.uniform(-180, 180, 50)
})

# Создаем базовый features.csv
features_df = pd.DataFrame({
    'lat': np.random.uniform(-90, 90, 150),
    'lon': np.random.uniform(-180, 180, 150),
    **{str(i): np.random.rand(150) for i in range(363)}  # 362 признака
})

# Сохраняем в CSV (этот шаг можно пропустить, если работаем только в памяти)
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)
features_df.to_csv('features.csv', index=False)

train_df

test_df

features_df

## Анализ данных

import pandas as pd
# Загрузка данных
train_df = pd.read_csv('/content/train.csv')
test_df = pd.read_csv('/content/test.csv')
features_df = pd.read_csv('/content/features.csv')

# Предварительный анализ
print(train_df.head())
print(test_df.head())
print(features_df.head())
