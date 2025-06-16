import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Dosyaları yükleyin
file_path_egitim = "C:/Users/sms/Desktop/orb_tahmin_data/ALG_data_model_train.csv"
file_path_tahmin = "C:/Users/sms/Desktop/orb_tahmin_data/GT_data_model_train.csv"

df_egitim = pd.read_csv(file_path_egitim)
df_tahmin = pd.read_csv(file_path_tahmin)

# Veri çerçevelerini oluşturun
positioning = pd.DataFrame({
    'onceki_x': df_tahmin['x'],
    'onceki_y': df_tahmin['y'],
    'translation_x': df_egitim['x'],
    'translation_y': df_egitim['y']
})

# Veriyi CSV olarak kaydedin
positioning.to_csv("egitim_orjinal.csv", index=False)

# Normalizasyon
scaler_x = StandardScaler()
scaler_y = StandardScaler()

# Verilerin hazırlanması
X = positioning[['onceki_x', 'onceki_y']]
y_x = positioning['translation_x']
y_y = positioning['translation_y']

# Veriyi normalize etme
X_scaled = scaler_x.fit_transform(X)
y_x_scaled = scaler_y.fit_transform(y_x.values.reshape(-1, 1)).flatten()
y_y_scaled = scaler_y.fit_transform(y_y.values.reshape(-1, 1)).flatten()

# Modelleri oluşturun
model_x = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=0)
model_y = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=0)

model_x.fit(X_scaled, y_x_scaled)
model_y.fit(X_scaled, y_y_scaled)

# Modelleri kaydedin
joblib.dump(model_x, "gradient_boosting_model_x.pkl")
joblib.dump(model_y, "gradient_boosting_model_y.pkl")

# Tahminler
y_x_pred_scaled = model_x.predict(X_scaled)
y_y_pred_scaled = model_y.predict(X_scaled)

# Tahminleri ters ölçekleme
y_x_pred = scaler_y.inverse_transform(y_x_pred_scaled.reshape(-1, 1)).flatten()
y_y_pred = scaler_y.inverse_transform(y_y_pred_scaled.reshape(-1, 1)).flatten()

# Gerçek ve tahmin edilen değerleri karşılaştırma
comparison_df = pd.DataFrame({
    'onceki_x': positioning['onceki_x'],
    'onceki_y': positioning['onceki_y'],
    'gercek_translation_x': positioning['translation_x'],
    'tahmin_translation_x': y_x_pred,
    'gercek_translation_y': positioning['translation_y'],
    'tahmin_translation_y': y_y_pred
})

# Sonuçları CSV olarak kaydedin
comparison_df.to_csv("results_comparison_with_predictions.csv", index=False)

# MAE hesapla
mae_x = mean_absolute_error(positioning['translation_x'], comparison_df['tahmin_translation_x'])
mae_y = mean_absolute_error(positioning['translation_y'], comparison_df['tahmin_translation_y'])

# NumPy print ayarlarını yapılandır
np.set_printoptions(precision=8, suppress=True)

# Yazdırma
print(f"MAE for translation_x: {mae_x:.8f}")
print(f"MAE for translation_y: {mae_y:.8f}")

print("\nComparison DataFrame:")
print(comparison_df.head())
