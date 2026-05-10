import argparse
import numpy as np
from sklearn.model_selection import train_test_split
from src.core import ModelExplainer

def main():
    parser = argparse.ArgumentParser(description='ModelExplainer')
    parser.add_argument('--help', action='help', help='show this help message and exit')
    args = parser.parse_args()
    # Run the explainer
    explainer = ModelExplainer()
    explainer.run()
if __name__ == '__main__':
    main()