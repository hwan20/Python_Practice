# -*- coding: utf-8 -*-

import urllib.request as req 
from bs4 import BeautifulSoup

# 오픈 API 아이디, 비번 (최초 설정 후 건드리지 말 것)
#client_id = "ySy22EO2tWjPZZiqDtKz"
#client_secret = "MR27Hc6GT8"

#쿠팡
#url = "https://www.coupang.com/np/search?component=&q=%EC%8B%A0%EB%9D%BC%EB%A9%B4&channel=user"
#urllib.error.HTTPError: HTTP Error 403: Forbidden

#ssg
#url = "https://www.ssg.com/search.ssg?target=all&query=%EC%8B%A0%EB%9D%BC%EB%A9%B4"
#urllib.error.HTTPError: HTTP Error 401: Unauthorized

#롯데마트
#url = "https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EC%8B%A0%EB%9D%BC%EB%A9%B4&mallId=4"

#홈플러스
url = "https://front.homeplus.co.kr/search?entry=direct&keyword=%EC%8B%A0%EB%9D%BC%EB%A9%B4"

#11번가
#url = "https://search.11st.co.kr/Search.tmall?kwd=%25EC%258B%25A0%25EB%259D%25BC%25EB%25A9%25B4"
wiki = req.urlopen(url) 
#print(wiki.read())
soup = BeautifulSoup(wiki,"lxml")

#print(soup)

#mw-content-text > div.mw-parser-output > p:nth-child(5)
#ss = soup.select("div.mw-parser-output > p > b") #p태그 안에 있는 b태그만 출력
#ss = soup.select("div.mw-parser-output > p") #p태그 안에 있는 p태그만 출력 비어있는 것은 if문을 통해 공백으로 처리 가능


#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(3) > ul > li:nth-child(1) > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2 > a > strong
#ss = soup.select("div.box__item-title > span.text__item-title text__item-title--ellipsis > a.link__item > span.text__item")
#print(ss)
#<strong>농심)신라면(봉지/30봉입/1BOX)</strong>
#for s in ss:
#    if s.string != None:
#        print(s.string)

#div.box__item-title > span.text__item-title text__item-title--ellipsis > a.link__item > span.text__item
#<a class="link__item" href="http://item.gmarket.co.kr/Item?goodscode=1811926534" target="_blank" data-montelena-acode="200003323" data-montelena-utsevent="click" data-montelena-utsimpression="true" data-montelena-utstype="item" data-montelena-goodscode="1811926534" data-montelena-asn="1" data-montelena-page="1" data-montelena-keyword="신라면" data-montelena-tab="a" data-montelena-tier="1" data-montelena-request_id="30be49c35a2d4508bd3125eeef0f5b13" data-montelena-tracking_id="e5033p5009r5032m9239d5s1022i3" data-montelena-device_type="100" data-montelena-page_type="200" data-montelena-view_type="l" data-montelena-tier_asn="1" data-montelena-atsclickurl="https://ats.gmarket.co.kr/cpc/clk?r=6FE28C86F61EC9A47E901239034FF41AF9E5F9FF6EC4BFB62F8CD0F3AEAB8E99929DADB8FA5A5E754B12B69890B914A0E34870B9118B41BB7C8364E8CFC4593E42EFA8FDD5BDDEC063A08D15B42225E257781ED5D8DC2F61AB3BAF4B21C4E7CBC814C88D176C34291D9D66C38C632D911867A19C9631E98ED87F18581BC0D20BB93EAD77D9B5A12D77AA298A265759DBDD7D4414384BBA2103B73C3C8668E918D44A9A061D4473E96724BB6668F7033364A4A00F8DB48FEAB129CE16E7B82A3F7DF4B395AE856588C0919BCE14C39742AC5B43C1D71041C2E97C94FE5E62B8EF57F2A5F4A88EB65F5E4024467779BBFC744D60157A28449B6D1374E6D12B504D65099F33B6CD382B92EE7659C56F764171D8EB6DC7362AA871E61B09C5B153C6551DF7C1FFAE9B7BD103B91A01EE99BF82EA66C37E3BF3E7A0515F88754E3635AC0A67128CD8DF17BB9CF5BE2EDA2200328F1B153F111476D68F6726E13FD686163F1B76C8F3EAFEFCB71A57DEE6F485EDE3522C9F50DA2C71EF412EE8E764CC720844459B7234ED8D6413D1F588FA4915E69FC17FA41AA9288483F3DAE5C423015498CA46E8A8A9C0CD3354AFA906282A532B091263BF5BCB8F080D0A8EC69574CF564509D52F04D60CC96508508FDD3C8D62BCD7065CFA164FE9E1E57CBA593797B36DE9DA80E2FC3DA503F37132A5EF6730A74F9576153C8A4F646A87CD20B08EF0221F4EB1D9B41F406A1E34666D1EFD10E143F224F236E670AA3F2BD50AE5ADE024AA100DD45596C1C0B156FF91&amp;ref=https%3a%2f%2fwww.gmarket.co.kr%2f"><span class="box__brand"><span class="text__brand">농심 신라면</span></span><span class="for-a11y">상품명 </span><span class="text__item" title="농심 신라면 큰사발 x 16개"> <!-- -->농심 신라면 큰사발 x 16개<!-- --> </span></a>


#root > div > div.css-1di1x1r-container > div.css-oiwa5q-defaultStyle-gridRow-IntegratedSearch > div.mainWrap > div > div > div.itemDisplayList > div:nth-child(1) > div.detailInfo > a > p
ss = soup.select("div.detailInfo > a.productTitle css-y9z3ts-defaultStyle-Linked > p.css-12cdo53-defaultStyle-Typography-ellips")
print(ss)
#<p class="css-12cdo53-defaultStyle-Typography-ellips">농심 신라면 120G*5입</p>
#<a class="productTitle css-y9z3ts-defaultStyle-Linked" target="_blank" href="/item?itemNo=120074651&amp;storeType=HYPER"><p class="css-12cdo53-defaultStyle-Typography-ellips">농심 신라면 120G*5입</p></a>
#<div class="detailInfo"><a class="productTitle css-y9z3ts-defaultStyle-Linked" target="_blank" href="/item?itemNo=120074651&amp;storeType=HYPER"><p class="css-12cdo53-defaultStyle-Typography-ellips">농심 신라면 120G*5입</p></a><div class="priceWrap"><div class="price"><strong class="priceValue">3,680</strong> 원 </div><span class="priceQty css-kd8ca0-defaultStyle-PriceUnit">(1개 당<span> 736</span>원)</span></div><div class="prodScoreWrap"><i class="css-12fua4g-defaultStyle-icon_093-Icon"><b class="css-1ypm30w-ir">평점</b></i><span>4.9(50,304건)</span><span>월 66,578개 구매</span></div><div class="detailInfoBtm"><button type="button" class="btnProdMore css-k6rw8e-defaultStyle-Button"><span>행사상품 보기</span></button></div></div>