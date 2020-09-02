import camelot

# PDF file to extract tables from
file = "foo.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# export individually
tables[0].to_csv("foo.csv")

# or export all in a zip
tables.export("foo.csv", f="csv", compress=True)

# export to HTML
tables.export("foo.html", f="html")