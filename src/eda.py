import matplotlib.pyplot as plt
import seaborn as sns
from data_prep import load_data, clean_data

def run_eda(path='data/raw/train.csv'):
    df = clean_data(load_data(path))
    sample_n = min(500, len(df))
    sns.pairplot(df.sample(sample_n), y_vars='SalePrice', x_vars=['GrLivArea','BedroomAbvGr','FullBath'], height=4)
    plt.suptitle('Pairwise plots', y=1.02)
    plt.show()
    print("Correlation with SalePrice:")
    print(df.corr()['SalePrice'].sort_values(ascending=False))

if __name__ == '__main__':
    run_eda()
