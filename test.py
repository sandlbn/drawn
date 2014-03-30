from shop.cart import Cart
from drawn import Drawn
from random import choice

Drawn('http://www.wp.pl')
c = Cart()
c.add(Drawn('http://www.amazon.co.uk/Doctor-Who-50th-Anniversary-Special/dp/B00F37VHX4/ref=pd_cp_d_h__0'))
c.add(Drawn('http://www.amazon.co.uk/Star-Wars-Original-Trilogy-Episodes/dp/B00E0NHP6K/ref=br_lf_m_1000772753_1_2_img?ie=UTF8&s=dvd&pf_rd_p=453915507&pf_rd_s=center-2&pf_rd_t=1401&pf_rd_i=1000772753&pf_rd_m=A3P5ROKL5A1OLE&pf_rd_r=0S4X8JSW469NW7P9RQ7B'))
c.add(Drawn('http://www.amazon.com/Star-Trek-VIII-First-Contact/dp/B000IZ8SD8/ref=pd_sim_mov_aiv_7'))

#print c.elements[0].item.title

for element in c.elements:
    print element.item.title, element.item.price

print "Wybralem dla Ciebie"
el = choice(c.elements)
print el.item.title

