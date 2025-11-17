"""CSV stats helper.

Provides a function to read a CSV and compute mean, min, max for a column.

Contract:
- Inputs: file_path (str), column (None|int|str), delimiter (str), has_header (bool)
- Output: dict with keys: 'mean', 'min', 'max', 'count'
- Errors: raises ValueError if file empty or no numeric data found

"""
from typing import Optional, Union, Dict

def read_csv_stats(file_path: str, column: Optional[Union[int, str]] = None, delimiter: str = ',', has_header: bool = True) -> Dict[str, float]:
	"""Read a CSV and compute statistics for a single column.

	If `column` is None, the function will use the first column (index 0).
	If `column` is an int, it is interpreted as a 0-based column index.
	If `column` is a str, it is interpreted as a header name (requires has_header=True).

	Non-numeric values and empty cells are skipped. NaNs are ignored.

	Returns a dict: {'mean': float, 'min': float, 'max': float, 'count': int}

	Raises ValueError if the file is empty or no numeric values are found.
	"""
	import csv
	import math
	import statistics

	col_index: Optional[int]
	col_index = None

	values = []

	with open(file_path, newline='', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=delimiter)
		try:
			if has_header:
				header = next(reader)
			else:
				header = None
		except StopIteration:
			raise ValueError("CSV is empty")

		# Determine column index
		if column is None:
			col_index = 0
		elif isinstance(column, int):
			col_index = column
		elif isinstance(column, str):
			if not has_header:
				raise ValueError("column name provided but has_header is False")
			try:
				col_index = header.index(column)
			except ValueError:
				raise ValueError(f"Column name '{column}' not found in header")
		else:
			raise TypeError("column must be None, int, or str")

		for row in reader:
			# skip rows that are too short
			if col_index is None or col_index >= len(row):
				continue
			raw = row[col_index].strip()
			if raw == '':
				continue
			try:
				num = float(raw)
			except ValueError:
				# skip non-numeric
				continue
			if math.isnan(num):
				continue
			values.append(num)

	if not values:
		raise ValueError("No numeric data found in the selected column")

	return {
		'mean': statistics.mean(values),
		'min': min(values),
		'max': max(values),
		'count': len(values),
	}


if __name__ == '__main__':
	# Quick self-test: create a temporary CSV, run the function, print results
	import tempfile
	import os

	sample_rows = [
		['id', 'value', 'note'],
		['1', '10', 'ok'],
		['2', '20.5', 'ok'],
		['3', '', 'missing'],
		['4', 'abc', 'non-numeric'],
		['5', '30', 'ok'],
	]

	tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='w', newline='', encoding='utf-8')
	try:
		import csv as _csv
		writer = _csv.writer(tmp)
		writer.writerows(sample_rows)
		tmp.close()

		print(f"Wrote sample CSV to: {tmp.name}")
		stats = read_csv_stats(tmp.name, column='value', has_header=True)
		print("Stats for column 'value':")
		print(stats)
	finally:
		try:
			os.unlink(tmp.name)
		except Exception:
			pass
