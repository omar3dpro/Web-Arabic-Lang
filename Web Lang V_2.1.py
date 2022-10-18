"""   Web Lang   V_2.1   """

import os
from time import *

"""   Variables   """

html_w = open("الصفحة.html", "w", encoding = "utf-8")
html = open("الصفحة.html", "a", encoding = "utf-8")
file = open("مشروع.ويب", "r", encoding = "utf-8")
code = file.read()
cursor = 0
html_w.write("<!--   تم إنشاء هذه الصفحة بواسطة لغة ( ويب ) العربية   -->\n\n<!DOCTYPE html>\n")

"""   Code   """

try:
    if len(code) > 0:
        while cursor <= len(code):

#   Start Code :

#   Tags :

            if code[cursor:cursor + 1] == ">":
                html.write(">")
                cursor += 1

            elif code[cursor:cursor + 4] == "<!--":
                html.write("<!--")
                cursor += 4

            elif code[cursor:cursor + 3] == "-->":
                html.write("-->")
                cursor += 3

            elif code[cursor:cursor + 8] == "<لغة ويب":
                html.write("<html")
                cursor += 8

            elif code[cursor:cursor + 10] == "<\لغة ويب>":
                html.write("</html>")
                cursor += 10

            elif code[cursor:cursor + 4] == "<راس":
                cursor += 4
                if code[cursor:cursor + 5] == " جدول":
                    html.write("<th")
                    cursor += 5

                elif code[cursor:cursor + 7] == " تفاصيل":
                    html.write("<summary")
                    cursor += 7

                elif code[cursor:cursor + 4] == " حقل":
                    html.write("<legend")
                    cursor += 4

                else:
                    html.write("<head")

            elif code[cursor:cursor + 6] == "<\راس>":
                html.write("</head>")
                cursor += 6

            elif code[cursor:cursor + 4] == "<جسم":
                html.write("<body")
                cursor += 4

            elif code[cursor:cursor + 6] == "<\جسم>":
                html.write("</body>")
                cursor += 6

            elif code[cursor:cursor + 6] == "<عنوان":
                cursor += 6
                if code[cursor:cursor + 5] == " جدول":
                    html.write("<caption")
                    cursor += 5
                else:
                    html.write("<title")

            elif code[cursor:cursor + 8] == "<\عنوان>":
                html.write("</title>")
                cursor += 8

            elif code[cursor:cursor + 6] == "<تصميم":
                html.write("<style")
                cursor += 6

            elif code[cursor:cursor + 8] == "<\تصميم>":
                html.write("</style>")
                cursor += 8

            elif code[cursor:cursor + 4] == "<رمز":
                html.write("<script")
                cursor += 4

            elif code[cursor:cursor + 6] == "<\رمز>":
                html.write("</script>")
                cursor += 6

            elif code[cursor:cursor + 8] == "<بلا رمز":
                html.write("<noscript")
                cursor += 8

            elif code[cursor:cursor + 10] == "<\بلا رمز>":
                html.write("</noscript>")
                cursor += 10

            elif code[cursor:cursor + 9] == "<\نص ضخم>":
                html.write("</h1>")
                cursor += 9

            elif code[cursor:cursor + 14] == "<\نص كبير جدا>":
                html.write("</h2>")
                cursor += 14

            elif code[cursor:cursor + 10] == "<\نص كبير>":
                html.write("</h3>")
                cursor += 10

            elif code[cursor:cursor + 11] == "<\نص متوسط>":
                html.write("</h4>")
                cursor += 11

            elif code[cursor:cursor +10] == "<\نص صغير>":
                html.write("</h5>")
                cursor += 10

            elif code[cursor:cursor + 14] == "<\نص صغير جدا>":
                html.write("</h6>")
                cursor += 14

            elif code[cursor:cursor + 5] == "<قطاع":
                html.write("<div")
                cursor += 5

            elif code[cursor:cursor + 7] == "<\قطاع>":
                html.write("</div>")
                cursor += 7

            elif code[cursor:cursor + 7] == "<امتداد":
                html.write("<span")
                cursor += 7

            elif code[cursor:cursor + 9] == "<\امتداد>":
                html.write("</span>")
                cursor += 9

            elif code[cursor:cursor + 5] == "<مقال":
                cursor += 5
                if code[cursor:cursor + 5] == " كامل":
                    html.write("<pre")
                    cursor += 5
                else:
                    html.write("<p")

            elif code[cursor:cursor + 12] == "<\مقال كامل>":
                html.write("</pre>")
                cursor += 12

            elif code[cursor:cursor + 7] == "<\مقال>":
                html.write("</p>")
                cursor += 7

            elif code[cursor:cursor + 9] == "<سطر جديد":
                html.write("<br")
                cursor += 9

            elif code[cursor:cursor + 3] == "<خط":
                html.write("<hr")
                cursor += 3

            elif code[cursor:cursor + 5] == "<سميك":
                html.write("<strong")
                cursor += 5

            elif code[cursor:cursor + 7] == "<\سميك>":
                html.write("</strong>")
                cursor += 7

            elif code[cursor:cursor + 5] == "<مائل":
                html.write("<em")
                cursor += 5

            elif code[cursor:cursor + 7] == "<\مائل>":
                html.write("</em>")
                cursor += 7

            elif code[cursor:cursor + 6] == "<محذوف":
                html.write("<del")
                cursor += 6

            elif code[cursor:cursor + 8] == "<\محذوف>":
                html.write("</del>")
                cursor += 8

            elif code[cursor:cursor + 7] == "<اقتباس":
                html.write("<q")
                cursor += 7

            elif code[cursor:cursor + 9] == "<\اقتباس>":
                html.write("</q>")
                cursor += 9

            elif code[cursor:cursor + 7] == "<اختصار":
                html.write("<abbr")
                cursor += 7

            elif code[cursor:cursor + 9] == "<\اختصار>":
                html.write("</abbr>")
                cursor += 9

            elif code[cursor:cursor + 5] == "<خطاب":
                html.write("<address")
                cursor += 5

            elif code[cursor:cursor + 7] == "<\خطاب>":
                html.write("</address>")
                cursor += 7

            elif code[cursor:cursor + 8] == "<تحته خط":
                html.write("<ins")
                cursor += 8

            elif code[cursor:cursor + 10] == "<\تحته خط>":
                html.write("</ins>")
                cursor += 10

            elif code[cursor:cursor + 9] == "<صغير تحت":
                html.write("<sub")
                cursor += 9

            elif code[cursor:cursor + 11] == "<\صغير تحت>":
                html.write("</sub>")
                cursor += 11

            elif code[cursor:cursor + 9] == "<صغير فوق":
                html.write("<sup")
                cursor += 9

            elif code[cursor:cursor + 11] == "<\صغير فوق>":
                html.write("</sup>")
                cursor += 11

            elif code[cursor:cursor + 3] == "<نص":
                cursor += 3
                if code[cursor:cursor + 4] == " ضخم":
                    html.write("<h1")
                    cursor += 4

                elif code[cursor:cursor + 5] == " كبير":
                    if code[cursor:cursor + 9] == " كبير جدا":
                        html.write("<h2")
                        cursor += 9
                    else:
                        html.write("<h3")
                        cursor += 5

                elif code[cursor:cursor + 6] == " متوسط":
                    html.write("<h4")
                    cursor += 6

                elif code[cursor:cursor + 5] == " صغير":
                    if code[cursor:cursor + 9] == " صغير جدا":
                        html.write("<h6")
                        cursor += 9
                    else:
                        html.write("<h5")
                        cursor += 5

                else:
                    html.write("<bdo")

            elif code[cursor:cursor + 5] == "<\نص>":
                html.write("</bdo>")
                cursor += 5

            elif code[cursor:cursor + 3] == "<زر":
                html.write("<button")
                cursor += 3

            elif code[cursor:cursor + 5] == "<\زر>":
                html.write("</button>")
                cursor += 5

            elif code[cursor:cursor + 5] == "<جدول":
                html.write("<table")
                cursor += 5

            elif code[cursor:cursor + 7] == "<\جدول>":
                html.write("</table>")
                cursor += 7

            elif code[cursor:cursor + 13] == "<\عنوان جدول>":
                html.write("</caption>")
                cursor += 13

            elif code[cursor:cursor + 3] == "<صف":
                html.write("<tr")
                cursor += 3

            elif code[cursor:cursor + 5] == "<\صف>":
                html.write("</tr>")
                cursor += 5

            elif code[cursor:cursor + 6] == "<عامود":
                html.write("<td")
                cursor += 6

            elif code[cursor:cursor + 8] == "<\عامود>":
                html.write("</td>")
                cursor += 8

            elif code[cursor:cursor + 11] == "<\راس جدول>":
                html.write("</th>")
                cursor += 11

            elif code[cursor:cursor + 6] == "<قائمة":
                cursor += 6
                if code[cursor:cursor + 6] == " مرقمة":
                    cursor += 6
                    if code[cursor:cursor + 7] == " معكوسة":
                        html.write("<ol reversed")
                        cursor += 7
                    else:
                        html.write("<ol")
                else:
                    html.write("<ul")

            elif code[cursor:cursor + 14] == "<\قائمة مرقمة>":
                html.write("</ol>")
                cursor += 14

            elif code[cursor:cursor + 8] == "<\قائمة>":
                html.write("</ul>")
                cursor += 8

            elif code[cursor:cursor + 11] == "<عنصر قائمة":
                html.write("<li")
                cursor += 11

            elif code[cursor:cursor + 13] == "<\عنصر قائمة>":
                html.write("</li>")
                cursor += 13

            elif code[cursor:cursor + 7] == "<تفاصيل":
                html.write("<details")
                cursor += 7

            elif code[cursor:cursor + 9] == "<\تفاصيل>":
                html.write("</details>")
                cursor += 9

            elif code[cursor:cursor + 13] == "<\راس تفاصيل>":
                html.write("</summary>")
                cursor += 13

            elif code[cursor:cursor + 4] == "<حقل":
                html.write("<fieldset")
                cursor += 4

            elif code[cursor:cursor + 6] == "<\حقل>":
                html.write("</fieldset>")
                cursor += 6

            elif code[cursor:cursor + 10] == "<\راس حقل>":
                html.write("</legend>")
                cursor += 10

            elif code[cursor:cursor + 4] == "<اسم":
                html.write("<label")
                cursor += 4

            elif code[cursor:cursor + 6] == "<\اسم>":
                html.write("</label>")
                cursor += 6

            elif code[cursor:cursor + 6] == "<ادخال":
                html.write("<input")
                cursor += 6

            elif code[cursor:cursor + 6] == "<علامة":
                html.write("<mark")
                cursor += 6

            elif code[cursor:cursor + 8] == "<\علامة>":
                html.write("</mark>")
                cursor += 8

            elif code[cursor:cursor + 6] == "<تحديد":
                html.write("<select")
                cursor += 6

            elif code[cursor:cursor + 8] == "<\تحديد>":
                html.write("</select>")
                cursor += 8

            elif code[cursor:cursor + 7] == "<اختيار":
                html.write("<option")
                cursor += 7

            elif code[cursor:cursor + 9] == "<\اختيار>":
                html.write("</option>")
                cursor += 9

            elif code[cursor:cursor + 6] == "<تحميل":
                html.write("<progress")
                cursor += 6

            elif code[cursor:cursor + 8] == "<\تحميل>":
                html.write("</progress>")
                cursor += 8

            elif code[cursor:cursor + 5] == "<بسيط":
                html.write("<samp")
                cursor += 5

            elif code[cursor:cursor + 7] == "<\بسيط>":
                html.write("</samp>")
                cursor += 7

            elif code[cursor:cursor + 9] == "<منطقة نص":
                html.write("<textarea")
                cursor += 9

            elif code[cursor:cursor + 11] == "<\منطقة نص>":
                html.write("</textarea>")
                cursor += 11

            elif code[cursor:cursor + 5] == "<رابط":
                html.write("<a")
                cursor += 5

            elif code[cursor:cursor + 11] == "<رابط تحميل":
                html.write("<a download")
                cursor += 11

            elif code[cursor:cursor + 7] == "<\رابط>":
                html.write("</a>")
                cursor += 7

            elif code[cursor:cursor + 6] == "<منتصف":
                html.write("<center")
                cursor += 6

            elif code[cursor:cursor + 8] == "<\منتصف>":
                html.write("</center>")
                cursor += 8

            elif code[cursor:cursor + 5] == "<صورة":
                html.write("<img")
                cursor += 5

            elif code[cursor:cursor + 4] == "<صوت":
                html.write("<audio controls")
                cursor += 4

            elif code[cursor:cursor + 6] == "<فيديو":
                html.write("<video controls")
                cursor += 6

            elif code[cursor:cursor + 5] == "<قالب":
                html.write("<form")
                cursor += 5

            elif code[cursor:cursor + 7] == "<\قالب>":
                html.write("</form>")
                cursor += 7

            elif code[cursor:cursor + 4] == "<ربط":
                html.write("<link rel = \"stylesheet\"")
                cursor += 4

            elif code[cursor:cursor + 4] == "<وصف":
                html.write("<meta")
                cursor += 4

            elif code[cursor:cursor + 4] == "<متر":
                html.write("<meter")
                cursor += 4

            elif code[cursor:cursor + 6] == "<\متر>":
                html.write("</meter>")
                cursor += 6

            elif code[cursor:cursor + 14] == "<مجموعة اختيار":
                html.write("<optgroup")
                cursor += 14

            elif code[cursor:cursor + 16] == "<\مجموعة اختيار>":
                html.write("</optgroup>")
                cursor += 16

            elif code[cursor:cursor + 5] == "<اطار":
                html.write("<iframe")
                cursor += 5

            elif code[cursor:cursor + 7] == "<\اطار>":
                html.write("</iframe>")
                cursor += 7

#   Attributes :

            elif code[cursor:cursor + 6] == "موقع =":
                html.write("href =")
                cursor += 6

            elif code[cursor:cursor + 5] == "موقع=":
                html.write("href =")
                cursor += 5

            elif code[cursor:cursor + 7] == "اتجاه =":
                html.write("dir =")
                cursor += 7

            elif code[cursor:cursor + 6] == "اتجاه=":
                html.write("dir =")
                cursor += 6

            elif code[cursor:cursor + 5] == "نوع =":
                html.write("type =")
                cursor += 5

            elif code[cursor:cursor + 4] == "نوع=":
                html.write("type =")
                cursor += 4

            elif code[cursor:cursor + 6] == "قيمة =":
                html.write("value =")
                cursor += 6

            elif code[cursor:cursor + 5] == "قيمة=":
                html.write("value =")
                cursor += 5

            elif code[cursor:cursor + 6] == "مصدر =":
                html.write("src =")
                cursor += 6

            elif code[cursor:cursor + 5] == "مصدر=":
                html.write("src =")
                cursor += 5

            elif code[cursor:cursor + 5] == "عرض =":
                html.write("width =")
                cursor += 5

            elif code[cursor:cursor + 4] == "عرض=":
                html.write("width =")
                cursor += 4

            elif code[cursor:cursor + 5] == "طول =":
                html.write("height =")
                cursor += 5

            elif code[cursor:cursor + 4] == "طول=":
                html.write("height =")
                cursor += 4

            elif code[cursor:cursor + 6] == "كنية =":
                html.write("alt =")
                cursor += 6

            elif code[cursor:cursor + 5] == "كنية=":
                html.write("alt =")
                cursor += 5

            elif code[cursor:cursor + 7] == "مسموح =":
                html.write("accept =")
                cursor += 7

            elif code[cursor:cursor + 6] == "مسموح=":
                html.write("accept =")
                cursor += 6

            elif code[cursor:cursor + 6] == "لاجل =":
                html.write("for =")
                cursor += 6

            elif code[cursor:cursor + 5] == "لاجل=":
                html.write("for =")
                cursor += 5

            elif code[cursor:cursor + 5] == "حدث =":
                html.write("action =")
                cursor += 5

            elif code[cursor:cursor + 4] == "حدث=":
                html.write("action =")
                cursor += 4

            elif code[cursor:cursor + 5] == "اسم =":
                html.write("name =")
                cursor += 5

            elif code[cursor:cursor + 4] == "اسم=":
                html.write("name =")
                cursor += 4
                
            elif code[cursor:cursor + 4] == "عنوان =":
                html.write("label =")
                cursor += 4

            elif code[cursor:cursor + 3] == "عنوان=":
                html.write("label =")
                cursor += 3

            elif code[cursor:cursor + 5] == "حرف =":
                html.write("charset =")
                cursor += 5

            elif code[cursor:cursor + 4] == "حرف=":
                html.write("charset =")
                cursor += 4

            elif code[cursor:cursor + 5] == "صنف =":
                html.write("class =")
                cursor += 5

            elif code[cursor:cursor + 4] == "صنف=":
                html.write("class =")
                cursor += 4

            elif code[cursor:cursor + 6] == "معرف =":
                html.write("id =")
                cursor += 6

            elif code[cursor:cursor + 5] == "معرف=":
                html.write("id =")
                cursor += 5

            elif code[cursor:cursor + 4] == "صف =":
                html.write("rows =")
                cursor += 4

            elif code[cursor:cursor + 3] == "صف=":
                html.write("rows =")
                cursor += 3

            elif code[cursor:cursor + 7] == "عامود =":
                html.write("cols =")
                cursor += 7

            elif code[cursor:cursor + 6] == "عامود=":
                html.write("cols =")
                cursor += 6

            elif code[cursor:cursor + 7] == "محتوى =":
                html.write("content =")
                cursor += 7

            elif code[cursor:cursor + 6] == "محتوى=":
                html.write("content =")
                cursor += 6

            elif code[cursor:cursor + 6] == "اعلى =":
                html.write("high =")
                cursor += 6

            elif code[cursor:cursor + 5] == "اعلى=":
                html.write("high =")
                cursor += 5

            elif code[cursor:cursor + 5] == "اقل =":
                html.write("low =")
                cursor += 5

            elif code[cursor:cursor + 4] == "اقل=":
                html.write("low =")
                cursor += 4

            elif code[cursor:cursor + 6] == "اقصى =":
                html.write("max =")
                cursor += 6

            elif code[cursor:cursor + 5] == "اقصى=":
                html.write("max =")
                cursor += 5

            elif code[cursor:cursor + 6] == "ادنى =":
                html.write("min =")
                cursor += 6

            elif code[cursor:cursor + 5] == "ادنى=":
                html.write("min =")
                cursor += 5

            elif code[cursor:cursor + 5] == "لغة =":
                html.write("lang =")
                cursor += 5

            elif code[cursor:cursor + 4] == "لغة=":
                html.write("lang =")
                cursor += 4

            elif code[cursor:cursor + 9] == "حدود-نص =":
                html.write("maxlength =")
                cursor += 9

            elif code[cursor:cursor + 8] == "حدود-نص=":
                html.write("maxlength =")
                cursor += 8

            elif code[cursor:cursor + 7] == "تلميح =":
                html.write("placeholder =")
                cursor += 7

            elif code[cursor:cursor + 6] == "تلميح=":
                html.write("placeholder =")
                cursor += 6

            elif code[cursor:cursor + 6] == "ملصق =":
                html.write("poster =")
                cursor += 6

            elif code[cursor:cursor + 5] == "ملصق=":
                html.write("poster =")
                cursor += 5

            elif code[cursor:cursor + 9] == "صف-ممتد =":
                html.write("rowspan =")
                cursor += 9

            elif code[cursor:cursor + 8] == "صف-ممتد=":
                html.write("rowspan =")
                cursor += 8

            elif code[cursor:cursor + 12] == "عامود-ممتد =":
                html.write("colspan =")
                cursor += 12

            elif code[cursor:cursor + 11] == "عامود-ممتد=":
                html.write("colspan =")
                cursor += 11

            elif code[cursor:cursor + 7] == "بداية =":
                html.write("start =")
                cursor += 7

            elif code[cursor:cursor + 6] == "بداية=":
                html.write("start =")
                cursor += 6

            elif code[cursor:cursor + 6] == "خطوة =":
                html.write("step =")
                cursor += 6

            elif code[cursor:cursor + 5] == "خطوة=":
                html.write("step =")
                cursor += 5

            elif code[cursor:cursor + 5] == "هدف =":
                html.write("target =")
                cursor += 5

            elif code[cursor:cursor + 4] == "هدف=":
                html.write("target =")
                cursor += 4

            elif code[cursor:cursor + 8] == "كاميرا =":
                html.write("capture =")
                cursor += 8

            elif code[cursor:cursor + 7] == "كاميرا=":
                html.write("capture =")
                cursor += 7

#   Vocabs :

            elif code[cursor:cursor + 6] == "\"يمين\"":
                html.write("\"rtl\"")
                cursor += 6

            elif code[cursor:cursor + 6] == "\"يسار\"":
                html.write("\"ltr\"")
                cursor += 6

            elif code[cursor:cursor + 4] == "\"زر\"":
                html.write("\"button\"")
                cursor += 4

            elif code[cursor:cursor + 4] == "\"نص\"":
                html.write("\"text\"")
                cursor += 4

            elif code[cursor:cursor + 5] == "\"رقم\"":
                html.write("\"number\"")
                cursor += 5

            elif code[cursor:cursor + 5] == "\"سرى\"":
                html.write("\"password\"")
                cursor += 5

            elif code[cursor:cursor + 6] == "\"بريد\"":
                html.write("\"email\"")
                cursor += 6

            elif code[cursor:cursor + 7] == "\"صندوق\"":
                html.write("\"checkbox\"")
                cursor += 7

            elif code[cursor:cursor + 7] == "\"دائرة\"":
                html.write("\"radio\"")
                cursor += 7

            elif code[cursor:cursor + 5] == "\"لون\"":
                html.write("\"color\"")
                cursor += 5

            elif code[cursor:cursor + 6] == "\"نطاق\"":
                html.write("\"range\"")
                cursor += 6

            elif code[cursor:cursor + 5] == "\"ملف\"":
                html.write("\"file\"")
                cursor += 5

            elif code[cursor:cursor + 7] == "\"تاريخ\"":
                html.write("\"date\"")
                cursor += 7

            elif code[cursor:cursor + 5] == "\"وقت\"":
                html.write("\"time\"")
                cursor += 5

            elif code[cursor:cursor + 6] == "\"رابط\"":
                html.write("\"url\"")
                cursor += 6

            elif code[cursor:cursor + 6] == "\"هاتف\"":
                html.write("\"tel\"")
                cursor += 6

            elif code[cursor:cursor + 5] == "\"بحث\"":
                html.write("\"search\"")
                cursor += 5

            elif code[cursor:cursor + 5] == "\"شهر\"":
                html.write("\"month\"")
                cursor += 5

            elif code[cursor:cursor + 7] == "\"اسبوع\"":
                html.write("\"week\"")
                cursor += 7

            elif code[cursor:cursor + 6] == "\"مخفى\"":
                html.write("\"hidden\"")
                cursor += 6

            elif code[cursor:cursor + 12] == "\"وقت وتاريخ\"" or code[cursor:cursor + 12] == "\"تاريخ ووقت\"":
                html.write("\"datetime-local\"")
                cursor += 12

            elif code[cursor:cursor + 6] == "\"صورة\"":
                html.write("\"image/*\"")
                cursor += 6

            elif code[cursor:cursor + 7] == "\"فيديو\"":
                html.write("\"video/*\"")
                cursor += 7

            elif code[cursor:cursor + 5] == "\"صوت\"":
                html.write("\"audio/*\"")
                cursor += 5

            elif code[cursor:cursor + 7] == "\"تاكيد\"":
                html.write("\"submit\"")
                cursor += 7

            elif code[cursor:cursor + 7] == "\"اعادة\"" or code[cursor:cursor + 7] == "\"ارجاع\"":
                html.write("\"reset\"")
                cursor += 7

            elif code[cursor:cursor + 12] == "\"صفحة جديدة\"":
                html.write("\"_blank\"")
                cursor += 12

            elif code[cursor:cursor + 5] == "\"وصف\"":
                html.write("\"description\"")
                cursor += 5

            elif code[cursor:cursor + 14] == "\"كلمة مفتاحية\"":
                html.write("\"keywords\"")
                cursor += 14

            elif code[cursor:cursor + 6] == "\"مظهر\"":
                html.write("\"theme-color\"")
                cursor += 6

            elif code[cursor:cursor + 14] == "\"صفحة متجاوبة\"":
                html.write("\"viewport\" content = \"width = device-width, initial-scale = 1.0\"")
                cursor += 14

            elif code[cursor:cursor + 7] == "\"خلفية\"":
                html.write("\"environment\"")
                cursor += 7

            elif code[cursor:cursor + 8] == "\"امامية\"":
                html.write("\"user\"")
                cursor += 8

            elif code[cursor:cursor + 6] == "\"عربى\"":
                html.write("\"ar\"")
                cursor += 6

#   Write UnKnown Chars :

            else:
                html.write(code[cursor:cursor + 1])
                cursor += 1

#   End Code ;

#   Complete Msg :

        os.system("title Web Lang")
        os.system("color 02")
        print("""
╔═══════════════════╗    
║                   ║
║   <!-- Done -->   ║
║                   ║
╚═══════════════════╝
        
V { 2.1 }
        """)
        sleep(1)

#   Empty Msg :

    else:
        os.system("title Web Lang")
        os.system("color 06")
        print("""
╔════════════════════╗    
║                    ║
║   <!-- Empty -->   ║
║                    ║
╚════════════════════╝
        
V { 2.1 }
        """)
        sleep(1)

#   Error Msg :

except:
    os.system("title Web Lang")
    os.system("color 04")
    print("""
╔════════════════════╗    
║                    ║
║   <!-- Error -->   ║
║                    ║
╚════════════════════╝
    
V { 2.1 }
    """)
    sleep(1)