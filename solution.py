## Генерация sample_subbmission.csv

# Подготовка тестового набора данных для предсказания
X_test = test_df.drop(['id'], axis=1)
dtest = xgb.DMatrix(X_test)

# Предсказание с использованием уже обученной модели
test_predictions = bst.predict(dtest)

# Подготовка файла с решением
submission_df = pd.DataFrame({'id': test_df['id'], 'score': test_predictions})
submission_df.to_csv('submission.csv', index=False)

daf = pd.read_csv('/content/submission.csv')
daf
