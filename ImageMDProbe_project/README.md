ImageMDProbe\*\* is a Flask-based web application for detecting and classifying skin diseases from uploaded images.  

It leverages a pre-trained deep learning model (`skin\_disease\_model.h5`) to provide quick, user-friendly predictions in the browser.



---



&nbsp;**📂 Project Structure**







ImageMDProbe\\\_project/

│

├── app.py                   # Flask backend application

├── requirements.txt         # Python dependencies

├── README.md                # Project documentation

│

├── model/

│   └── skin\\\_disease\\\_model.h5   # Trained deep learning model (to be added)

│

├── templets/

│   └── index.html           # Main web page template

│

└── static/

├── script.js            # Frontend JavaScript

└── styles.css           # Styling for the web page



```





**🚀 Features**



\- Upload skin images directly from your browser

\- Instant prediction of possible skin disease

\- Simple and responsive web interface

\- Runs locally without an internet connection after setup

\- Modular design for model replacement or upgrades







 **🛠 Requirements**



\- \*\*Python\*\*: 3.8+

\- \*\*pip\*\*: Latest version

\- Trained TensorFlow/Keras model file: `skin\_disease\_model.h5`



Dependencies are listed in `requirements.txt`:

```



pip install -r requirements.txt





**⚙️ Installation \& Setup**



1\. \*\*Clone or Download\*\* this repository:

&nbsp;  ```bash

&nbsp;  git clone <your\_repo\_link>

&nbsp;  cd ImageMDProbe\_project





2\. Create \& activate a virtual environment:



&nbsp;  ```bash

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate       # On Windows

&nbsp;  source venv/bin/activate    # On macOS/Linux

&nbsp;  ```



3\. \*\*Install dependencies\*\*:



&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt

&nbsp;  



4\. Place the trained model:



&nbsp;  \* Copy `skin\_disease\_model.h5` into the `model/` folder.



5\. Run the app:



&nbsp;  ```bash

&nbsp;  python app.py

&nbsp;  ```



6\. Open in browser:



&nbsp;  \* Go to: \[http://127.0.0.1:5000](http://127.0.0.1:5000)







 **🧠 Model Information**



\* The model should be a `.h5` file trained with TensorFlow/Keras.

\* You can retrain or replace the model as long as it follows the same input/output specifications.

\* Place your trained model in `model/skin\_disease\_model.h5`.







&nbsp;**📸 Usage**



1\. Open the web app in your browser.

2\. Click \*\*"Upload Image"\*\* and select a skin image.

3\. Wait for the prediction to appear below the upload section.







&nbsp;**📌 Notes**



\* Ensure the model file path is correct. This app uses:



&nbsp; ```python

&nbsp; tf.keras.models.load\_model(os.path.join(app.root\_path, 'model', 'skin\_disease\_model.h5'))

&nbsp; ```

\* The default folder name is `templets` (as per original code). Flask standard is `templates`, but the app works as-is.



---



&nbsp;**📄 License**



This project is for educational and research purposes.

If you use or modify it, please provide attribution to the original author(s).





