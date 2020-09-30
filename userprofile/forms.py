from django import forms
from django.contrib.auth.models import User
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    #forms.Form则需要手动配置每个字段，它适用于不与数据库进行直接交互的功能。
    # 用户登录不需要对数据库进行任何改动，因此直接继承forms.Form就可以了。
#注册用户表单
class UserRegisterForm(forms.ModelForm):  #覆写了password字段
    password = forms.CharField()
    password2  = forms.CharField()

    class Meta:
        model = User
        fields =('username','email')
#覆写某字段之后，内部类class Meta中的定义对这个字段就没有效果了，所以fields不用包含password
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")

#验证密码一致性方法不能写def clean_password()，因为如果你不定义def clean_password2()方法，会导致password2中的数据被Django
# 判定为无效数据从而清洗掉，从而password2属性不存在。最终导致两次密码输入始终会不一致，并且很难判断出错误原因。
#从POST中取值用的data.get('password')是一种稳妥的写法，即使用户没有输入密码也不会导致程序错误而跳出。前面章节提取POST数据
# 我们用了data['password']，这种取值方式如果data中不包含password，Django会报错。另一种防止用户不输入密码就提交的方式是在表单
# 中插入required属性，