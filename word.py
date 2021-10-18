
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

from time import strftime, localtime
timestr=strftime('%Y-%m-%d %H:%M:%S',localtime())

doc1 = Document()  #生成一个空的docx对象
head=doc1.add_heading('安全测试题', level=1) # 添加标题
head.alignment = WD_ALIGN_PARAGRAPH.CENTER  # 居中
p1=doc1.add_paragraph('edit by:HuaBro \t update time: {}'.format(timestr))   # 添加段落
p1.alignment = WD_ALIGN_PARAGRAPH.CENTER  # 居中


for i,j in zip(queslst,optlst):
    doc1.add_paragraph(i)
    doc1.add_paragraph(j)
doc1.styles['Normal'].font.name = '宋体'
doc1.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体') # 字体
doc1.styles['Normal'].font.name = 'Times New Roman' # 数字字体
doc1.save('output1.docx')