import functions
	
file = open('tests/test_html.txt', 'r', encoding="utf8")
text = file.read()
file.close()

functions.get_data_from_text(text,"test_output.csv",0,"dummy url")
