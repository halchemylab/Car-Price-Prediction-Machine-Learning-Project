# Car Price Estimator App

This is a Streamlit-based app that provides a simple user interface for estimating car prices based on user input.

## Dataset

The dataset used for training the model is a car purchasing dataset, which can be found [here](https://www.kaggle.com/datasets/mohdshahnawazaadil/sales-prediction-dataset?resource=download&select=car_purchasing.csv).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/halchemylab/car-price-estimator-app.git
```

2. Navigate to the project directory:

```bash
cd car-price-prediction-machine-learning-project
```

3. Install the required dependencies:

* Streamlit
* joblib
* numpy
* scikit-learn

## Usage

1. Run the app:

```bash
streamlit run app.py
```

2. Open a web browser and navigate to `http://localhost:8501` to access the app.

3. Enter your age, annual salary, and net worth in the input fields.
4. Click the "Predict Price" button to get an estimated car price.

## Model Training

The model is trained using a linear regression algorithm and is saved to a file named `model.pkl`. The training process can be found in the `analysis.ipynb` notebook.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or issues, please contact the project maintainer at hyp243@nyu.edu.

I hope this helps! Let me know if you have any other questions.