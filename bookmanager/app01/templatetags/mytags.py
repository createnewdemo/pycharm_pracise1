#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 18:05
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : mytags.py
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# @register.simple_tag
# def pugination(num):
#     li_list = ['<li><a href="#">{}</a></li>'.format(i) for i in range(1,num+1)]
#
#     return mark_safe("""
#     <nav aria-label="Page navigation">
#                     <ul class="pagination">
#                         <li>
#                             <a href="#" aria-label="Previous">
#                                 <span aria-hidden="true">&laquo;</span>
#                             </a>
#                         </li>
#                         {}
#
#                         <li>
#                             <a href="#" aria-label="Next">
#                                 <span aria-hidden="true">&raquo;</span>
#                             </a>
#                         </li>
#                     </ul>
#                 </nav>
#
#     """.format(''.join(li_list)))
@register.inclusion_tag('page.html')
def inclusion(num):


    return {'num':range(1,num+1)}