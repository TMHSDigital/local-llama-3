# Contributing to Local LLaMA 3

## How to Contribute

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Modifying the Model Locally

### Setup Environment

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Modify the Model

1. **Adjust Hyperparameters**: Modify `config.json` to change hyperparameters.
2. **Add New Layers**: Edit `model.py` to include additional neural network layers.
3. **Train with New Data**: Use `train.py` to train the model with new datasets:
    ```bash
    python train.py --data new_dataset.csv
    ```

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.
