## Обучение модели

from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_absolute_error

# Подготовка данных для модели
X = train_df.drop(['id', 'score'], axis=1)
y = train_df['score']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=42)

# Создание объекта DMatrix - специализированной структуры данных для XGBoost, оптимизированной для эффективности и производительности.
dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_val, label=y_val)

# Настройка параметров XGBoost
params = {
    'max_depth': 8,  # максимальная глубина деревьев
    'eta': 0.3,  # скорость обучения
    'silent': 1,  # вывод логов обучения (1 - выключить логи)
    'objective': 'reg:squarederror',  # задача на минимизацию квадратичной ошибки
    'eval_metric': 'mae',  # метрика для оценки модели - средняя абсолютная ошибка
    'learning_rate': 0.15  # темп обучения
}
num_rounds = 50  # количество итераций бустинга

# Обучение модели
bst = xgb.train(params, dtrain, num_rounds, evals=[(dval, 'Validation')], early_stopping_rounds=10)

# Оценка модели
predictions = bst.predict(dval)
mae = mean_absolute_error(y_val, predictions)
print(f'Средняя абсолютная ошибка: {mae}')
