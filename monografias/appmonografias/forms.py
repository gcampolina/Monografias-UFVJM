from django import forms
from .models import Monografia, Aluno, Professor, Banca
from allauth.account.forms import SignupForm


class BancaForm(forms.ModelForm):
    class Meta:
        model = Banca
        fields = ['monografia', 'professores_avaliadores', 'data', 'horario', 'local']
        widgets = {
            'monografia': forms.Select(attrs={
                'class': 'form-select',  
            }),
            'professores_avaliadores': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': 5  
            }),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'horario': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o local da defesa'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['monografia'].empty_label = "Selecione uma monografia"


class MonografiaForm(forms.ModelForm):
    class Meta:
        model = Monografia
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título da monografia'}),
            'autor': forms.Select(),
            'orientador': forms.Select(),
            'coorientador': forms.Select(),
            'resumo': forms.Textarea(attrs={'placeholder': 'Digite o resumo'}),
            'abstract': forms.Textarea(attrs={'placeholder': 'Digite o abstract'}),
            'palavras_chave': forms.TextInput(attrs={'placeholder': 'Digite as palavras-chave'}),
            'arquivo': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].empty_label = 'Selecione o autor (aluno)'
        self.fields['orientador'].empty_label = 'Selecione o orientador'
        self.fields['coorientador'].empty_label = 'Selecione o coorientador'






class CustomSignupForm(SignupForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail (opcional)'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
    )


class AlunoForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Usuário'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nome'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail (opcional)'})
    )

    class Meta:
        model = Aluno
        fields = ['matricula']
        widgets = {
            'matricula': forms.TextInput(attrs={'placeholder': 'Digite a matrícula do aluno'})
        }


class ProfessorForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Usuário'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nome'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail (opcional)'})
    )

    class Meta:
        model = Professor
        fields = ['titulação', 'area_pesquisa']
        widgets = {
            'area_pesquisa': forms.TextInput(attrs={'placeholder': 'Digite a área de pesquisa'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulação'].choices = [('', 'Selecione a titulação')] + list(self.fields['titulação'].choices)[1:]


