import kagglehub 
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(__file__).parent.parent / "data"

def main():
    DATA_DIR.mkdir(exist_ok=True)

    kagglehub.competition_download(
        "titanic",
        output_dir=DATA_DIR
    )

if __name__=="__main__":
    main()