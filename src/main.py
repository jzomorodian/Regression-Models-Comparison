from src.data.DataLoader import DataLoader
from src.argparser import pars_input_args

if __name__ == '__main__':
    args = pars_input_args()
    dl = DataLoader(args.file_path)
    dl.remove_nans()
    print(dl.get_np())
