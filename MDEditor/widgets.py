# -*- coding:utf-8 -*-
from __future__ import absolute_import

from django import forms
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.encoding import force_str
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

try:
    # Django >=1.7
    from django.forms.utils import flatatt
except ImportError:
    # Django <1.7
    from django.forms.util import flatatt

from .configs import MDConfig

class MDEditorWidget(forms.Textarea):
    def __init__(self, config_name='default', *args, **kwargs):
        super(MDEditorWidget, self).__init__(*args, **kwargs)
        # Setup config from defaults.
        self.config = MDConfig(config_name)

    def render(self, name, value, renderer=None, attrs=None):
        """
        name : 字段名
        value : 对应字段的值，但是显示出来换行直接生效了

        renderer: django2.1 新增加的参数，此处不做应用，赋值None做兼容处理
        """
        if value is None:
            value = ''
        # 换行问题，转义...只能想到这个解决办法了，想了我多久啊，起码一个星期...想想就难受，人菜瘾大...
        value = value.replace('\r\n', '\\r\\n')  
        # print(f'正常的值：{value}')
        # print(f'改后的值force_text：{(force_text(value))}')
        # print(f'改后的值force_str：{(force_str(value))}')
        # print(f'改后的值conditional_escape：{conditional_escape(force_text(value))}')
        '''tem
        正常的值：<123>[hello]\r\n\r\n<你好>\r\n\r\n<>？“{}\r\n\r\n{}
        改后的值force_text：<123>[hello]\r\n\r\n<你好>\r\n\r\n<>？“{}\r\n\r\n{}
        改后的值force_str：<123>[hello]\r\n\r\n<你好>\r\n\r\n<>？“{}\r\n\r\n{}
        改后的值conditional_escape：&lt;123&gt;[hello]\r\n\r\n&lt;你好&gt;\r\n\r\n&lt;&gt;？“{}\r\n\r\n{}
        '''
        final_attrs = self.build_attrs(self.attrs, attrs, name=name)

        return mark_safe(render_to_string('MDEditor/markdown.html', {
            'final_attrs': flatatt(final_attrs),
            # 'value': conditional_escape(force_text(value)),
            'value': value,
            'id': final_attrs['id'],
            'config': self.config,
            }))

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        """
        Helper function for building an attribute dictionary.
        This is combination of the same method from Django<=1.10 and Django1.11+
        """
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    def _get_media(self):
        return forms.Media(
            css={
                # "all": ("vditor/css/index.css",)
            },
            js=(
                # "vditor/js/index.min.js",
            ))
    media = property(_get_media)