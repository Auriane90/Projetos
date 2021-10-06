from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput
from .models import Horario, Advertencia, Frequencia, DadosPessoais, Conteudo, Notas, Resp, RespSuper


horarios_CHOICES = [
    ('português', 'Portugues'),
    ('biologia', 'Biologia'),
    ('educação física', 'Educação Física'),
    ('filosofia', 'Filosofia'),
    ('física', 'Física'),
    ('geografia', 'Geografia'),
    ('história', 'História'),
    ('espanhol', 'Espanhol'),
    ('inglês', 'Inglês'),
    ('matemática', 'Matemática'),
    ('química', 'Química'),
    ('sociologia', 'Sociologia')
]

turma_CHOICES = [
    ('1A', '1A'),
    ('2A', '2A'),
    ('3A', '3A'),
    ('1B', '1B'),
    ('2B', '2B'),
    ('3B', '3B'),
    ('1C', '1C'),
    ('2C', '2C'),
    ('3C', '3C'),
    ('1D', '1D'),
    ('2D', '2D'),
    ('3D', '3D'),

]

turma_CHOICES.sort()
horarios_CHOICES.sort()


class CdAluno(forms.ModelForm):
    first_name = forms.CharField(widget=forms.Select(choices=turma_CHOICES))

    class Meta:
        model = User
        field = ['username', 'password', 'first_name', 'last_name']
        exclude = ['last_login', 'is_superuser', 'is_staff', 'email', 'is_active', 'date_joined']
        widgets = {
            'username': forms.TextInput(attrs={
                'maxlength': 255,
                'placeholder': 'Digite seu nome'
            }),
            'password': forms.PasswordInput(attrs={
                'maxlength': 255,
                'placeholder': 'Digite sua senha'
            }),

            'last_name': forms.TextInput(attrs={
                'maxlength': 255,
                'placeholder': 'Digite seu nome'
            }),
        }

    def save(self, commit=True):
        user = super(CdAluno, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user


class CdResp(forms.ModelForm):
    turma = forms.CharField(label='Qual sua turma?', widget=forms.Select(choices=turma_CHOICES))

    class Meta:
        model = Resp
        field = ['nome', 'senha', 'nome_aluno', 'matricula_aluno', 'turma']
        exclude = []
        widgets = {
            'nome': forms.TextInput(attrs={
                'maxlength': 255,
                'placeholder': 'Digite seu nome'
            }),
            'senha': forms.PasswordInput(attrs={
                'maxlength': 255,
                'placeholder': 'Digite sua senha'
            }),
            'matricula_aluno': forms.TextInput(attrs={
                'maxlength': 255,
                'placeholder': 'Digite seu nome'
            }),

        }


class AuxResp(forms.ModelForm):
    id_aluno = forms.ModelChoiceField(queryset=User.objects.filter(last_name='aluno').order_by('id'), widget=forms.Select)

    class Meta:
        model = RespSuper
        field = ['id_resp', 'id_aluno']
        exclude = []


class UserHorario(forms.ModelForm):
    primeiraAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    segundaAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    terceiraAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quartaAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quintaAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    sextaAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    setimaAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    oitavaAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    nonaAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    decimaAulaS = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))

    primeiraAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    segundaAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    terceiraAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quartaAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quintaAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    sextaAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    setimaAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    oitavaAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    nonaAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    decimaAulaT = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))

    primeiraAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    segundaAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    terceiraAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quartaAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quintaAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    sextaAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    setimaAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    oitavaAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    nonaAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    decimaAulaQ = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))

    primeiraAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    segundaAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    terceiraAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quartaAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quintaAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    sextaAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    setimaAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    oitavaAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    nonaAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    decimaAulaQUI = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))

    primeiraAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    segundaAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    terceiraAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quartaAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    quintaAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    sextaAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    setimaAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    oitavaAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    nonaAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    decimaAulaSEX = forms.CharField(label='Qual a aula de hoje?', widget=forms.Select(choices=horarios_CHOICES))
    turma = forms.CharField(label='Qual sua turma?', widget=forms.Select(choices=turma_CHOICES))

    class Meta:
        model = Horario
        field = ['idAluno', 'primeiraAulaS', 'segundaAulaS', 'terceiraAulaS', 'quartaAulaS', 'quintaAulaS',
                 'sextaAulaS', 'setimaAulaS', 'oitavaAulaS', 'nonaAulaS', 'decimaAulaS',
                 'primeiraAulaT', 'segundaAulaT', 'terceiraAulaT', 'quartaAulaT', 'quintaAulaT',
                 'sextaAulaT', 'setimaAulaT', 'oitavaAulaT', 'nonaAulaT', 'decimaAulaT',
                 'primeiraAulaQ', 'segundaAulaQ', 'terceiraAulaQ', 'quartaAulaQ', 'quintaAulaQ',
                 'sextaAulaQ', 'setimaAulaQ', 'oitavaAulaQ', 'nonaAulaQ', 'decimaAulaQ',
                 'primeiraAulaQUI', 'segundaAulaQUI', 'terceiraAulaQUI', 'quartaAulaQUI', 'quintaAulaQUI',
                 'sextaAulaQUI', 'setimaAulaQUI', 'oitavaAulaQUI', 'nonaAulaQUI', 'decimaAulaQUI',
                 'primeiraAulaSEX', 'segundaAulaSEX', 'terceiraAulaSEX', 'quartaAulaSEX', 'quintaAulaSEX',
                 'sextaAulaSEX', 'setimaAulaSEX', 'oitavaAulaSEX', 'nonaAulaSEX', 'decimaAulaSEX', 'turma']
        exclude = []


class UserAdvertencia(forms.ModelForm):
    idAluno = forms.ModelChoiceField(queryset=User.objects.all().order_by('id'), widget=forms.Select)

    class Meta:
        model = Advertencia
        field = ['idAluno', 'Comum', 'Media', 'Grave']
        exclude = []
        widgets = {
            'Comum': forms.Textarea,
            'Media': forms.Textarea,
            'Grave': forms.Textarea,
        }


class UserFrequencia(forms.ModelForm):
    JaneiroPB = forms.IntegerField(required=False)
    FevereiroPB = forms.IntegerField(required=False)
    MarcoPB = forms.IntegerField(required=False)
    AbrilPB = forms.IntegerField(required=False)
    MaioPB = forms.IntegerField(required=False)
    JunhoPB = forms.IntegerField(required=False)
    JulhoPB = forms.IntegerField(required=False)
    AgostoPB = forms.IntegerField(required=False)
    SetembroPB = forms.IntegerField(required=False)
    OutubroPB = forms.IntegerField(required=False)
    NovembroPB = forms.IntegerField(required=False)
    DesembroPB = forms.IntegerField(required=False)

    JaneiroGR = forms.IntegerField(required=False)
    FevereiroGR = forms.IntegerField(required=False)
    MarcoGR = forms.IntegerField(required=False)
    AbrilGR = forms.IntegerField(required=False)
    MaioGR = forms.IntegerField(required=False)
    JunhoGR = forms.IntegerField(required=False)
    JulhoGR = forms.IntegerField(required=False)
    AgostoGR = forms.IntegerField(required=False)
    SetembroGR = forms.IntegerField(required=False)
    OutubroGR = forms.IntegerField(required=False)
    NovembroGR = forms.IntegerField(required=False)
    DesembroGR = forms.IntegerField(required=False)

    JaneiroRD = forms.IntegerField(required=False)
    FevereiroRD = forms.IntegerField(required=False)
    MarcoRD = forms.IntegerField(required=False)
    AbrilRD = forms.IntegerField(required=False)
    MaioRD = forms.IntegerField(required=False)
    JunhoRD = forms.IntegerField(required=False)
    JulhoRD = forms.IntegerField(required=False)
    AgostoRD = forms.IntegerField(required=False)
    SetembroRD = forms.IntegerField(required=False)
    OutubroRD = forms.IntegerField(required=False)
    NovembroRD = forms.IntegerField(required=False)
    DesembroRD = forms.IntegerField(required=False)

    JaneiroLT = forms.IntegerField(required=False)
    FevereiroLT = forms.IntegerField(required=False)
    MarcoLT = forms.IntegerField(required=False)
    AbrilLT = forms.IntegerField(required=False)
    MaioLT = forms.IntegerField(required=False)
    JunhoLT = forms.IntegerField(required=False)
    JulhoLT = forms.IntegerField(required=False)
    AgostoLT = forms.IntegerField(required=False)
    SetembroLT = forms.IntegerField(required=False)
    OutubroLT = forms.IntegerField(required=False)
    NovembroLT = forms.IntegerField(required=False)
    DesembroLT = forms.IntegerField(required=False)

    JaneiroBIO = forms.IntegerField(required=False)
    FevereiroBIO = forms.IntegerField(required=False)
    MarcoBIO = forms.IntegerField(required=False)
    AbrilBIO = forms.IntegerField(required=False)
    MaioBIO = forms.IntegerField(required=False)
    JunhoBIO = forms.IntegerField(required=False)
    JulhoBIO = forms.IntegerField(required=False)
    AgostoBIO = forms.IntegerField(required=False)
    SetembroBIO = forms.IntegerField(required=False)
    OutubroBIO = forms.IntegerField(required=False)
    NovembroBIO = forms.IntegerField(required=False)
    DesembroBIO = forms.IntegerField(required=False)

    JaneiroEDF = forms.IntegerField(required=False)
    FevereiroEDF = forms.IntegerField(required=False)
    MarcoEDF = forms.IntegerField(required=False)
    AbrilEDF = forms.IntegerField(required=False)
    MaioEDF = forms.IntegerField(required=False)
    JunhoEDF = forms.IntegerField(required=False)
    JulhoEDF = forms.IntegerField(required=False)
    AgostoEDF = forms.IntegerField(required=False)
    SetembroEDF = forms.IntegerField(required=False)
    OutubroEDF = forms.IntegerField(required=False)
    NovembroEDF = forms.IntegerField(required=False)
    DesembroEDF = forms.IntegerField(required=False)

    JaneiroFIL = forms.IntegerField(required=False)
    FevereiroFIL = forms.IntegerField(required=False)
    MarcoFIL = forms.IntegerField(required=False)
    AbrilFIL = forms.IntegerField(required=False)
    MaioFIL = forms.IntegerField(required=False)
    JunhoFIL = forms.IntegerField(required=False)
    JulhoFIL = forms.IntegerField(required=False)
    AgostoFIL = forms.IntegerField(required=False)
    SetembroFIL = forms.IntegerField(required=False)
    OutubroFIL = forms.IntegerField(required=False)
    NovembroFIL = forms.IntegerField(required=False)
    DesembroFIL = forms.IntegerField(required=False)

    JaneiroFSK = forms.IntegerField(required=False)
    FevereiroFSK = forms.IntegerField(required=False)
    MarcoFSK = forms.IntegerField(required=False)
    AbrilFSK = forms.IntegerField(required=False)
    MaioFSK = forms.IntegerField(required=False)
    JunhoFSK = forms.IntegerField(required=False)
    JulhoFSK = forms.IntegerField(required=False)
    AgostoFSK = forms.IntegerField(required=False)
    SetembroFSK = forms.IntegerField(required=False)
    OutubroFSK = forms.IntegerField(required=False)
    NovembroFSK = forms.IntegerField(required=False)
    DesembroFSK = forms.IntegerField(required=False)

    JaneiroGEO = forms.IntegerField(required=False)
    FevereiroGEO = forms.IntegerField(required=False)
    MarcoGEO = forms.IntegerField(required=False)
    AbrilGEO = forms.IntegerField(required=False)
    MaioGEO = forms.IntegerField(required=False)
    JunhoGEO = forms.IntegerField(required=False)
    JulhoGEO = forms.IntegerField(required=False)
    AgostoGEO = forms.IntegerField(required=False)
    SetembroGEO = forms.IntegerField(required=False)
    OutubroGEO = forms.IntegerField(required=False)
    NovembroGEO = forms.IntegerField(required=False)
    DesembroGEO = forms.IntegerField(required=False)

    JaneiroHIS = forms.IntegerField(required=False)
    FevereiroHIS = forms.IntegerField(required=False)
    MarcoHIS = forms.IntegerField(required=False)
    AbrilHIS = forms.IntegerField(required=False)
    MaioHIS = forms.IntegerField(required=False)
    JunhoHIS = forms.IntegerField(required=False)
    JulhoHIS = forms.IntegerField(required=False)
    AgostoHIS = forms.IntegerField(required=False)
    SetembroHIS = forms.IntegerField(required=False)
    OutubroHIS = forms.IntegerField(required=False)
    NovembroHIS = forms.IntegerField(required=False)
    DesembroHIS = forms.IntegerField(required=False)

    JaneiroING = forms.IntegerField(required=False)
    FevereiroING = forms.IntegerField(required=False)
    MarcoING = forms.IntegerField(required=False)
    AbrilING = forms.IntegerField(required=False)
    MaioING = forms.IntegerField(required=False)
    JunhoING = forms.IntegerField(required=False)
    JulhoING = forms.IntegerField(required=False)
    AgostoING = forms.IntegerField(required=False)
    SetembroING = forms.IntegerField(required=False)
    OutubroING = forms.IntegerField(required=False)
    NovembroING = forms.IntegerField(required=False)
    DesembroING = forms.IntegerField(required=False)

    JaneiroESP = forms.IntegerField(required=False)
    FevereiroESP = forms.IntegerField(required=False)
    MarcoESP = forms.IntegerField(required=False)
    AbrilESP = forms.IntegerField(required=False)
    MaioESP = forms.IntegerField(required=False)
    JunhoESP = forms.IntegerField(required=False)
    JulhoESP = forms.IntegerField(required=False)
    AgostoESP = forms.IntegerField(required=False)
    SetembroESP = forms.IntegerField(required=False)
    OutubroESP = forms.IntegerField(required=False)
    NovembroESP = forms.IntegerField(required=False)
    DesembroESP = forms.IntegerField(required=False)

    JaneiroMAT = forms.IntegerField(required=False)
    FevereiroMAT = forms.IntegerField(required=False)
    MarcoMAT = forms.IntegerField(required=False)
    AbrilMAT = forms.IntegerField(required=False)
    MaioMAT = forms.IntegerField(required=False)
    JunhoMAT = forms.IntegerField(required=False)
    JulhoMAT = forms.IntegerField(required=False)
    AgostoMAT = forms.IntegerField(required=False)
    SetembroMAT = forms.IntegerField(required=False)
    OutubroMAT = forms.IntegerField(required=False)
    NovembroMAT = forms.IntegerField(required=False)
    DesembroMAT = forms.IntegerField(required=False)

    JaneiroGEM = forms.IntegerField(required=False)
    FevereiroGEM = forms.IntegerField(required=False)
    MarcoGEM = forms.IntegerField(required=False)
    AbrilGEM = forms.IntegerField(required=False)
    MaioGEM = forms.IntegerField(required=False)
    JunhoGEM = forms.IntegerField(required=False)
    JulhoGEM = forms.IntegerField(required=False)
    AgostoGEM = forms.IntegerField(required=False)
    SetembroGEM = forms.IntegerField(required=False)
    OutubroGEM = forms.IntegerField(required=False)
    NovembroGEM = forms.IntegerField(required=False)
    DesembroGEM = forms.IntegerField(required=False)

    JaneiroALG = forms.IntegerField(required=False)
    FevereiroALG = forms.IntegerField(required=False)
    MarcoALG = forms.IntegerField(required=False)
    AbrilALG = forms.IntegerField(required=False)
    MaioALG = forms.IntegerField(required=False)
    JunhoALG = forms.IntegerField(required=False)
    JulhoALG = forms.IntegerField(required=False)
    AgostoALG = forms.IntegerField(required=False)
    SetembroALG = forms.IntegerField(required=False)
    OutubroALG = forms.IntegerField(required=False)
    NovembroALG = forms.IntegerField(required=False)
    DesembroALG = forms.IntegerField(required=False)

    JaneiroQUI = forms.IntegerField(required=False)
    FevereiroQUI = forms.IntegerField(required=False)
    MarcoQUI = forms.IntegerField(required=False)
    AbrilQUI = forms.IntegerField(required=False)
    MaioQUI = forms.IntegerField(required=False)
    JunhoQUI = forms.IntegerField(required=False)
    JulhoQUI = forms.IntegerField(required=False)
    AgostoQUI = forms.IntegerField(required=False)
    SetembroQUI = forms.IntegerField(required=False)
    OutubroQUI = forms.IntegerField(required=False)
    NovembroQUI = forms.IntegerField(required=False)
    DesembroQUI = forms.IntegerField(required=False)

    JaneiroSOC = forms.IntegerField(required=False)
    FevereiroSOC = forms.IntegerField(required=False)
    MarcoSOC = forms.IntegerField(required=False)
    AbrilSOC = forms.IntegerField(required=False)
    MaioSOC = forms.IntegerField(required=False)
    JunhoSOC = forms.IntegerField(required=False)
    JulhoSOC = forms.IntegerField(required=False)
    AgostoSOC = forms.IntegerField(required=False)
    SetembroSOC = forms.IntegerField(required=False)
    OutubroSOC = forms.IntegerField(required=False)
    NovembroSOC = forms.IntegerField(required=False)
    DesembroSOC = forms.IntegerField(required=False)

    class Meta:
        model = Frequencia
        field = ['idAluno', 'turma', 'JaneiroPB', 'FevereiroPB', 'MarcoPB', 'AbrilPB', 'MaioPB', 'JunhoPB', 'JulhoPB', 'AgostoPB', 'SetembroPB', 'OutubroPB', 'NovembroPB', 'DesembroPB',
                 'JaneiroGR', 'FevereiroGR', 'MarcoGR', 'AbrilGR', 'MaioGR', 'JunhoGR', 'JulhoGR', 'AgostoGR', 'SetembroGR', 'OutubroGR', 'NovembroGR', 'DesembroGR',
                 'JaneiroRD', 'FevereiroRD', 'MarcoRD', 'AbrilRD', 'MaioRD', 'JunhoRD', 'JulhoRD', 'AgostoRD', 'SetembroRD', 'OutubroRD', 'NovembroRD', 'DesembroRD',
                 'JaneiroLT', 'FevereiroLT', 'MarcoLT', 'AbrilLT', 'MaioLT', 'JunhoLT', 'JulhoLT', 'AgostoLT','SetembroLT', 'OutubroLT', 'NovembroLT', 'DesembroLT',
                 'JaneiroBIO', 'FevereiroBIO', 'MarcoBIO', 'AbrilBIO', 'MaioBIO', 'JunhoBIO', 'JulhoBIO', 'AgostoBIO','SetembroBIO', 'OutubroBIO', 'NovembroBIO', 'DesembroBIO',
                 'JaneiroEDF', 'FevereiroEDF', 'MarcoEDF', 'AbrilEDF', 'MaioEDF', 'JunhoEDF', 'JulhoEDF', 'AgostoEDF', 'SetembroEDF', 'OutubroEDF', 'NovembroEDF', 'DesembroEDF',
                 'JaneiroFIL', 'FevereiroFIL', 'MarcoFIL', 'AbrilFIL', 'MaioFIL', 'JunhoFIL', 'JulhoFIL', 'AgostoFIL','SetembroFIL', 'OutubroFIL', 'NovembroFIL', 'DesembroFIL',
                 'JaneiroFSK', 'FevereiroFSK', 'MarcoFSK', 'AbrilFSK', 'MaioFSK', 'JunhoFSK', 'JulhoFSK', 'AgostoFSK','SetembroFSK', 'OutubroFSK', 'NovembroFSK', 'DesembroFSK',
                 'JaneiroGEO', 'FevereiroGEO', 'MarcoGEO', 'AbrilGEO', 'MaioGEO', 'JunhoGEO', 'JulhoGEO', 'AgostoGEO','SetembroGEO', 'OutubroGEO', 'NovembroGEO', 'DesembroGEO',
                 'JaneiroHIS', 'FevereiroHIS', 'MarcoHIS', 'AbrilHIS', 'MaioHIS', 'JunhoHIS', 'JulhoHIS', 'AgostoHIS','SetembroHIS', 'OutubroHIS', 'NovembroHIS', 'DesembroHIS',
                 'JaneiroING', 'FevereiroING', 'MarcoING', 'AbrilING', 'MaioING', 'JunhoING', 'JulhoING', 'AgostoING','SetembroING', 'OutubroING', 'NovembroING', 'DesembroING',
                 'JaneiroESP', 'FevereiroESP', 'MarcoESP', 'AbrilESP', 'MaioESP', 'JunhoESP', 'JulhoESP', 'AgostoESP','SetembroESP', 'OutubroESP', 'NovembroESP', 'DesembroESP',
                 'JaneiroMAT', 'FevereiroMAT', 'MarcoMAT', 'AbrilMAT', 'MaioMAT', 'JunhoMAT', 'JulhoMAT', 'AgostoMAT','SetembroMAT', 'OutubroMAT', 'NovembroMAT', 'DesembroMAT',
                 'JaneiroGEM', 'FevereiroGEM', 'MarcoGEM', 'AbrilGEM', 'MaioGEM', 'JunhoGEM', 'JulhoGEM', 'AgostoGEM','SetembroGEM', 'OutubroGEM', 'NovembroGEM', 'DesembroGEM',
                 'JaneiroALG', 'FevereiroALG', 'MarcoALG', 'AbrilALG', 'MaioALG', 'JunhoALG', 'JulhoALG', 'AgostoALG','SetembroALG', 'OutubroALG', 'NovembroALG', 'DesembroALG',
                 'JaneiroQUI', 'FevereiroQUI', 'MarcoQUI', 'AbrilQUI', 'MaioQUI', 'JunhoQUI', 'JulhoQUI', 'AgostoQUI','SetembroQUI', 'OutubroQUI', 'NovembroQUI', 'DesembroQUI',
                 'JaneiroSOC', 'FevereiroSOC', 'MarcoSOC', 'AbrilSOC', 'MaioSOC', 'JunhoSOC', 'JulhoSOC', 'AgostoSOC','SetembroSOC', 'OutubroSOC', 'NovembroSOC', 'DesembroSOC'

                 ]
        exclude = []


class UserNotas(forms.ModelForm):
    idAluno = forms.ModelChoiceField(queryset=User.objects.all().order_by('id'), widget=forms.Select)
    PBFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBHistoria = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBHistoria = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBHistoria = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBHistoria = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecHistoria = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MHistoria = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBBiologia = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBBiologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBBiologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBBiologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecBiologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MBiologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBFilosofia = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBFilosofia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBFilosofia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBFilosofia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecFilosofia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MFilosofia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBGeografia = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBGeografia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBGeografia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBGeografia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecGeografia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MGeografia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBPortuques = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBPortuques = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBPortuques = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBPortuques = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecPortuques = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MPortuques = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBMatematica = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBMatematica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBMatematica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBMatematica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecMatematica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MMatematica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBEdFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBEdFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBEdFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBEdFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecEdFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MEdFisica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBEspanhol = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBEspanhol = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBEspanhol = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBEspanhol = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecEspanhol = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MEspanhol = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBIngles = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBIngles = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBIngles = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBIngles = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecIngles = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MIngles = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBQuimica = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBQuimica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBQuimica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBQuimica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecQuimica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MQuimica = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    PBSociologia = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    SBSociologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    TBSociologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    QBSociologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    RecSociologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)
    MSociologia = forms.DecimalField(max_digits=4, decimal_places=2, required=False)

    class Meta:
        model = Notas
        field = ['idAluno', 'PBFisica', 'SBFisica', 'TBFisica', 'QBFisica', 'RecFisica', 'MFisica',
                 'PBHistoria', 'SBHistoria', 'TBHistoria', 'QBHistoria', 'RecHistoria', 'MHistoria',
                 'PBBiologia', 'SBBiologia', 'TBBiologia', 'QBBiologia', 'RecBiologia', 'MBiologia',
                 'PBFilosofia', 'SBFilosofia', 'TBFilosofia', 'QBFilosofia', 'RecFilosofia', 'MFilosofia',
                 'PBGeografia', 'SBGeografia', 'TBGeografia', 'QBGeografia', 'RecGeografia', 'MGeografia',
                 'PBPortuques', 'SBPortuques', 'TBPortuques', 'QBPortuques', 'RecPortuques', 'MPortuques',
                 'PBMatematica', 'SBMatematica', 'TBMatematica', 'QBMatematica', 'RecMatematica', 'MMatematica',
                 'PBEdFisica', 'SBEdFisica', 'TBEdFisica', 'QBEdFisica', 'RecEdFisica', 'EdFisica',
                 'PBEspanhol', 'SBEspanhol', 'TBEspanhol', 'QBEspanhol', 'RecEspanhol', 'MEspanhol',
                 'PBIngles', 'SBIngles', 'TBIngles', 'QBIngles', 'RecIngles', 'MIngles',
                 'PBQuimica', 'SBQuimica', 'TBQuimica', 'QBQuimica', 'RecQuimica', 'MQuimica',
                 'PBSociologia', 'SBSociologia', 'TBSociologia', 'QBSociologia', 'RecSociologia', 'MSociologia'
                 ]
        exclude = []


class UserConteudo(forms.ModelForm):
    turma = forms.CharField(widget=forms.Select(choices=turma_CHOICES))
    PortuquesBasico = forms.FileField(widget=ClearableFileInput)
    Gramatica = forms.FileField(widget=ClearableFileInput)
    Redacao = forms.FileField(widget=ClearableFileInput)
    Leitura = forms.FileField(widget=ClearableFileInput)
    Biologia = forms.FileField(widget=ClearableFileInput)
    EducacaoFisica = forms.FileField(widget=ClearableFileInput)
    Filosofia = forms.FileField(widget=ClearableFileInput)
    Fisica = forms.FileField(widget=ClearableFileInput)
    Geografia = forms.FileField(widget=ClearableFileInput)
    Historia = forms.FileField(widget=ClearableFileInput)
    Ingles = forms.FileField(widget=ClearableFileInput)
    Espanhol = forms.FileField(widget=ClearableFileInput)
    MatematicaBasica = forms.FileField(widget=ClearableFileInput)
    Geometria = forms.FileField(widget=ClearableFileInput)
    Algebra = forms.FileField(widget=ClearableFileInput)
    Quimica = forms.FileField(widget=ClearableFileInput)
    Sociologia = forms.FileField(widget=ClearableFileInput)

    class Meta:
        model = Conteudo
        field = ['PortuquesBasico', 'Gramatica', 'Redacao', 'Leitura', 'Biologia', 'Quimica',
                 'EducacaoFisica', 'Filosofia', 'Fisica', 'Geografia', 'Historia', 'Sociologia',
                 'Ingles', 'Espanhol', 'MatematicaBasica', 'Geometria', 'Algebra', 'turma']
        exclude = []


class UserDados(forms.ModelForm):
    idAluno = forms.ModelChoiceField(queryset=User.objects.filter(first_name='3C').order_by('id'), widget=forms.Select)
    Foto = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = DadosPessoais
        field = ['idAluno', 'Telefone', 'Nome', 'Idade', 'CPF', 'RG', 'NomeResponsavel',
                 'TelefoneResponsavel', 'CPF_Responsavel', 'RG_Responsavel', 'Foto']
        exclude = []
        widgets = {
            'Telefone': forms.TextInput(attrs={
                'maxlength': 255,
            }),
            'Nome': forms.TextInput(attrs={
                'maxlength': 255,
            }),
            'Idade': forms.TextInput(attrs={
                'maxlength': 255,
            }),
            'CPF': forms.TextInput(attrs={
                'maxlength': 255,
            }),
            'RG': forms.TextInput(attrs={
                'maxlength': 255,
            }),
            'NomeResponsavel': forms.TextInput(attrs={
                'maxlength': 255,
            }),
            'TelefoneResponsavel': forms.TextInput(attrs={
                'maxlength': 255,
            }),
            'CPF_Responsavel': forms.TextInput(attrs={
                'maxlength': 255,
            }),
            'RG_Responsavel': forms.TextInput(attrs={
                'maxlength': 255,
            }),

        }




