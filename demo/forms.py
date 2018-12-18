from django import forms

from .models import Post, FastPow

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
        
class FastPowForm(forms.ModelForm):

	class Meta:
		model = FastPow
		#exclude = ['power']
		fields = ('x', 'n', 'mod', 'power', )
