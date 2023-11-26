from django import forms

class BookForm(forms.Form):
    book_name = forms.CharField(label = 'Book Name', max_length = 100)
    pages = forms.IntegerField(label = 'Number of Pages')
    publication_year = forms.CharField(label = "Publication Year", max_length=20)
    description = forms.CharField(label = 'Description', max_length=300,widget=forms.Textarea)
    image_url = forms.CharField(label = "Image URL", max_length=250)
    author_first_name = forms.CharField(label = "Author First Name", max_length=40)
    author_last_name = forms.CharField(label = "Author Last Name", max_length=40)