echo $(date) , $(pdfinfo thesis.pdf | grep Pages | awk '{print $2}') >> PageNumbers.md
python scripts/plot_page_numbers.py
