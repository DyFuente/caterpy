#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Defines css and html tags."""


def return_tags(tags="all"):
    HTML_TAGS = ("!DOCTYPE a abbr acronym address applet article aside audio "
                 "b base basefont bdi bdo big blockquote area button canvas "
                 "caption center cite code col colgroup datalist dd details "
                 "dfn dialog dir div dl dt embed fieldset figcaption figure "
                 "font footer form frame frameset head header hr html i iframe"
                 " input ins kbd label legend li link main map mark menu body"
                 "meta meter nav noframes noscript object ol optgroup option "
                 "output p param picture pre progress q rp rt ruby s samp "
                 "section select small source span strike strong style summary"
                 " sup svg table tbody td template textarea tfoot thead time "
                 "title tr track tt u ul var video wbr br figure img th sub "
                 "menuitem script body br em del")

    TOKEN_IDS = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD',
                 'VBG', 'VBN', 'VBP', 'VBG']

    RESERVED_WORDS = ("abstract arguments await boolean break byte case catcr"
                      " class const continue debugger default delete double "
                      "else enum eval export extends false final finally float"
                      " function goto if implements import in instanceof int "
                      "interface let long native new null package private for "
                      "protected public return short static super switch do "
                      "synchronized this throw throws transient true typeof "
                      "void volatile while with yield abstract boolean byte "
                      "char double final float goto int long native short try "
                      "synchronized throws transient volatile array date eval "
                      "function hasownproperty infinity isfinite isnan var "
                      "isprototypeof length math name number object prototype "
                      "string tostring undefined valueof getclass javaarray "
                      "javaclass javaobject javapackage alert anchor anchors "
                      "area assign button checkbox clearinterval cleartimeout"
                      " clientinformation close closed confirm constructor "
                      "decodeuri decodeuricomponent defaultstatus document"
                      " elements embed embeds encodeuri encodeuricomponent "
                      "event fileupload focus form forms frame innerheight "
                      "innerwidth layer layers all location mimetypes navigate"
                      " navigator frames framerate hidden history image images"
                      " offscreenbuffering open opener option outerheight nan "
                      "outerwidth width packages pagexoffset pageyoffset "
                      "parsefloat parseint password pkcs11 plugin prompt java "
                      "propertyisenum radio reset screenx screeny scroll link "
                      "select self setinterval settimeout status submit taint "
                      "text textarea unescape untaint window onblur onclick "
                      "secure onfocus onkeydown onkeypress onkeyup onmouseover"
                      " onload onmouseup onmousedown popsettings onsubmit "
                      "blur ecape crypto browser element top onerror parent")

    if tags == "all":
        return HTML_TAGS, TOKEN_IDS, RESERVED_WORDS
    else:
        return eval(tags.upper())
