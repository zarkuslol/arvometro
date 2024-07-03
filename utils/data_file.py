import pandas as pd

# Lembrete: a função aceita APENAS arquivos csv como entrada

class DataFile:
    def __init__(self, path: str) -> None:
        self.path = path
        self.file: pd.DataFrame = pd.read_csv(path)

    def save_data(self, data: list, index: list) -> None:
        data_series: pd.Series = pd.Series(data, index)
        new_row: pd.DataFrame = data_series.to_frame().T
        self.file = pd.concat([self.file, new_row], ignore_index=True)
        self.file.to_csv(self.path, index=False)

    def load_data(self) -> pd.DataFrame:
        return self.file
