
import lxml.etree as ET


dom = ET.parse('course.xml')
xslt = ET.parse('course_transform.xml')
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))

