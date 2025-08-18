# 🍋 MangoGen – Mango Species Identifier
MangoGen is a simple **deep learning + Streamlit** web application that identifies mango species from an uploaded image. It uses a pre-trained **TensorFlow/Keras model (`trained_model.h5`)** to classify mango images into their respective species.

---

## 🚀 Features
- 📂 Upload mango images through a **Streamlit interface**  
- 🧠 Uses a trained **TensorFlow CNN model** for predictions  
- 🔖 Reads labels from `labels.txt` for species names  
- 🎨 Displays uploaded image and predicted result in a clean UI  

---

## 📂 Project Structure
MangoGen/  
│-- trained_model.h5        # Pre-trained TensorFlow model  
│-- labels.txt              # Labels for mango species  
│-- app.py                  # Streamlit app (main script)  
│-- requirements.txt        # Python dependencies  
│-- README.md               # Project documentation  

---

## 🛠️ Installation & Setup
1. **Clone the repository**  
`git clone git@github.com:bassam165/mangogen.git`  
`cd mangogen`  

2. **Create virtual environment (optional but recommended)**  
`python3 -m venv venv`  
`source venv/bin/activate   # On Linux/Mac`  
`venv\Scripts\activate      # On Windows`  

3. **Install dependencies**  
`pip install -r requirements.txt`  

4. **Run the Streamlit app**  
`streamlit run app.py`  

---

## 🖼️ Usage
1. Open the local Streamlit app in your browser (`http://localhost:8501`)  
2. Upload a mango image (`.jpg`, `.png`)  
3. Click **Predict**  
4. The model will classify and display the mango species  

---

## 📊 Example Prediction Flow
1. Upload an image:  
![Upload](https://via.placeholder.com/300x200.png?text=Upload+Mango+Image)  
2. Click **Predict**  
3. Output:  
✅ *This is Amrapali Mango*  

---

## 📌 Requirements
- Python 3.8+  
- TensorFlow  
- Streamlit  
- NumPy  

Install with:  
`pip install tensorflow streamlit numpy`  

---

## 🤝 Contributing
Pull requests are welcome! If you’d like to improve the model or add features, please open an issue first.

---

## 📜 License
MIT License © 2025 [Bassam165](https://github.com/bassam165)
