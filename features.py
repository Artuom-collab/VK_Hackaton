## Генерация новых признаков (фичей)

# Я добавил такие признаки из сторонних датасетов или их сгенерировал в контексте задачи геоаналитики и предсказания успешности объекта ретейла:
#
# 1. Слияние по ближайшим координатам
#
# 2. Расстояние до центра определенной важной точки. Можно рассчитать евклидово расстояние от одного объекта ретейла до другого объекта.
#
# 3. Количество объектов в радиусе X километров. Подсчитай количество других объектов ретейла в определённом радиусе.

# Центральная точка
central_lat = 55.7522  # Пример: широта центра
central_lon = 37.6156  # Пример: долгота центра

# Расстояние до центра для каждого объекта ретейла
train_df['distance_to_center'] = np.sqrt((train_df['lat'] - central_lat)**2 + (train_df['lon'] - central_lon)**2)
test_df['distance_to_center'] = np.sqrt((test_df['lat'] - central_lat)**2 + (test_df['lon'] - central_lon)**2)

from geopy.distance import geodesic

# Радиус в километрах
radius_km = 200  # Пример: радиус в 200 км

def count_objects_in_radius(row, radius):
    # Функция для подсчёта объектов в радиусе для каждой строки датасета
    center_point = (row['lat'], row['lon'])
    within_radius = 0
    for _, other_row in features_df.iterrows():
        other_point = (other_row['lat'], other_row['lon'])
        if geodesic(center_point, other_point).kilometers <= radius:
            within_radius += 1
    return within_radius

# Подсчитываем количество объектов в радиусе для каждой строки в train_df и test_df
train_df['objects_in_radius'] = train_df.apply(count_objects_in_radius, axis=1, radius=radius_km)
test_df['objects_in_radius'] = test_df.apply(count_objects_in_radius, axis=1, radius=radius_km)

# Слияние по ближайшим координатам
train_df = pd.merge_asof(train_df.sort_values('lat'), features_df.sort_values('lat'), on='lat')
test_df = pd.merge_asof(test_df.sort_values('lat'), features_df.sort_values('lat'), on='lat')

train_df['new_feature'] = train_df['lat'] * 0.5 # этот признак я сгенерировал, исходя из признаков которе доступны в датасетет train
# Добавляем новый признак в тестовый датафрейм
test_df['new_feature'] = test_df['lat'] * 0.5

train_df

test_df
