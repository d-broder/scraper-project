import sys

from scraper.scraper import run  # Corrigido o caminho do import


def main():
    # Expect exactly one argument: the output CSV filename
    if len(sys.argv) != 2:
        print("Usage: python -m scraper <output_csv_file>")
        sys.exit(1)

    output_file = sys.argv[1]
    run(output_file)


if __name__ == "__main__":
    main()
