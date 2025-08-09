
ImageMDProbe is an AI-powered web application built with **Flask** and **TensorFlow/Keras** to detect skin diseases from uploaded images.  
It uses a pre-trained deep learning model to analyze an image and provide instant predictions through a simple, responsive browser interface.

---

## 📖 Description

The project combines **computer vision** and **web technologies** to make disease detection accessible and interactive.  
Users can upload a skin image, and the backend deep learning model processes it to identify potential skin conditions.  
The app runs locally, meaning no internet connection is needed after setup, and the model can be swapped for other datasets.

**Key Highlights**
- AI-powered classification of skin diseases.
- Simple, responsive UI for easy use.
- Runs entirely on your local machine.
- Easily replaceable AI model for different datasets.




<h1 align="center">🩺 ImageMDProbe</h1>
<p align="center">
  <b>Deep Learning–Powered Skin Disease Detection Web Application</b><br>
  Built with <a href="https://flask.palletsprojects.com/">Flask</a> & <a href="https://www.tensorflow.org/">TensorFlow/Keras</a>
</p>

<p align="center">
  <a href="https://github.com/Dibyacodecraft/ImageMDProbe/stargazers">
    <img src="https://img.shields.io/github/stars/Dibyacodecraft/ImageMDProbe?style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/Dibyacodecraft/ImageMDProbe/fork">
    <img src="https://img.shields.io/github/forks/Dibyacodecraft/ImageMDProbe?style=for-the-badge" alt="Forks">
  </a>
  <a href="https://github.com/Dibyacodecraft/ImageMDProbe/issues">
    <img src="https://img.shields.io/github/issues/Dibyacodecraft/ImageMDProbe?style=for-the-badge" alt="Issues">
  </a>
  <a href="https://github.com/Dibyacodecraft/ImageMDProbe/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Dibyacodecraft/ImageMDProbe?style=for-the-badge" alt="License">
  </a>
</p>

---

## 📖 Overview

**ImageMDProbe** is an AI-powered skin disease detection web app that allows users to upload skin images and get instant predictions using a pre-trained deep learning model.  
It runs locally via Flask, requires no internet connection after setup, and can easily be customized with your own model.

---

## ✨ Features

- 🧠 **AI-Powered**: Uses TensorFlow/Keras deep learning models.
- ⚡ **Fast Predictions**: Instant analysis after image upload.
- 📱 **Responsive UI**: Works on desktop and mobile browsers.
- 🔌 **Offline-Ready**: Runs locally without an internet connection.
- 🔄 **Customizable**: Replace the model to detect other conditions.

---

## 📂 Project Structure

```plaintext
ImageMDProbe/
├── app.py                   # Flask backend
├── requirements.txt         # Dependencies
├── README.md                # Documentation
│
├── model/
│   └── skin_disease_model.h5   # Trained model (add manually)
│
├── templets/
│   └── index.html           # Webpage template
│
└── static/
    ├── script.js            # JavaScript logic
    └── styles.css           # Styling


## 📂 Project Structure

```

ImageMDProbe/
│
├── app.py                   # Flask backend
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
│
├── model/
│   └── skin\_disease\_model.h5   # Trained model (add manually)
│
├── templets/
│   └── index.html           # Main HTML page
│
└── static/
├── script.js            # Frontend JavaScript
└── styles.css           # Stylesheet

````

---

## 🛠 Requirements

- **Python** 3.8 or higher  
- **pip** (latest)  
- Trained `.h5` deep learning model compatible with TensorFlow/Keras  

Install dependencies:
```bash
pip install -r requirements.txt
````

---

## ⚙️ Installation & Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/Dibyacodecraft/ImageMDProbe.git
   cd ImageMDProbe
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your trained model**

   * Place `skin_disease_model.h5` inside the `model/` folder.

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Open in your browser**

   * Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Usage

1. Open the app in your browser.
2. Click **"Upload Image"** and select a skin image.
3. View the predicted disease result instantly.

---

## 🧠 Model Details

* Format: `.h5` TensorFlow/Keras model
* Input: RGB skin image
* Output: Predicted disease label
* You can retrain or replace the model as long as it matches the app's expected input/output shapes.

---

## 🚀 Customization

* Swap `skin_disease_model.h5` with a new model for other diseases.
* Edit `templets/index.html`, `static/styles.css`, and `static/script.js` to modify the UI.
* Update preprocessing and class labels in `app.py` for new datasets.

---

## 📌 Notes

* The project uses a folder named `templets` instead of the Flask default `templates`.
  You may rename it and adjust the code if desired.
* Ensure your model file path matches:

  ```python
  tf.keras.models.load_model(os.path.join(app.root_path, 'model', 'skin_disease_model.h5'))
  ```

---

## 📄 License

This project is for **educational and research purposes only**.
It is **not** intended for actual medical diagnosis without professional evaluation.

---

**🔗 GitHub Repository:** [https://github.com/Dibyacodecraft/ImageMDProbe](https://github.com/Dibyacodecraft/ImageMDProbe)

