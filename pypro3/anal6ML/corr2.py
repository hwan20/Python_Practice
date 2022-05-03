#공공 데이터(외국인 관광객 서울 관광지 관련)로 상관관계 분석
import json
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='malgun gothic') #그래프의 한글화 처리

#산점도 그래프 작성 함수
def setScatterGraph(tour_table, all_table, tourPoint):
    #print(tourPoint) #창덕궁, 운현궁, 경복궁, 창경궁, 종묘
    #계산할 관광지명에 해당하는 데이터만 뽑아 tour 변수에 저장하고 외국인 자료와 병합
    tour = tour_table[tour_table['resNm'] == tourPoint]
    #print(tour)
    merge_table = pd.merge(tour, all_table, left_index = True, right_index = True)
    #print(merge_table)
    
    #시각화
    fig = plt.figure()
    fig.suptitle(tourPoint + ' 상관관계분석')
    
    plt.subplot(1,3,1)
    plt.xlabel('중국인 입국자 수')
    plt.ylabel('외국인 입장객 수')
    lam1 = lambda p:merge_table['china'].corr(merge_table['ForNum']) #중국인 입국자 수와 관광지 입장객 수의 상관 관계를 알아냄
    r1 = lam1(merge_table)
    print('r1 : ', r1)
    plt.title('r={:.3f}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], s=6, c='red', alpha=0.8)
    
    plt.subplot(1,3,2)
    plt.xlabel('일본인 입국자 수')
    plt.ylabel('외국인 입장객 수')
    lam2 = lambda p:merge_table['japan'].corr(merge_table['ForNum']) #일본인 입국자 수와 관광지 입장객 수의 상관 관계를 알아냄
    r2 = lam2(merge_table)
    print('r2 : ', r2)
    plt.title('r={:.3f}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], s=6, c='green', alpha=0.8)
 
    plt.subplot(1,3,3)
    plt.xlabel('미국인 입국자 수')
    plt.ylabel('외국인 입장객 수')
    lam3 = lambda p:merge_table.usa.corr(merge_table.ForNum) #일본인 입국자 수와 관광지 입장객 수의 상관 관계를 알아냄
    r3 = lam3(merge_table)
    print('r3 : ', r3)
    plt.title('r={:.3f}'.format(r3))
    plt.scatter(merge_table['usa'], merge_table['ForNum'], s=6, c='blue', alpha=0.8)   
    
    plt.tight_layout()
    plt.show()

    return [tourPoint, r1, r2, r3] 

def chulbal():
    #서울시 관광지 정보 파일 읽기
    fname = "../testdata/서울시_관광지.json"
    jsonTP = json.loads(open(fname, 'r', encoding='UTF-8').read()) #str로 읽은 것을 dict로 바꿈 json decoding
    print(jsonTP, type(jsonTP)) #딕트 타입의 데이터를 리스트로 감싼 형태
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'resNm', 'ForNum')) #년월, 관광지명, 입장객수
    tour_table = tour_table.set_index('yyyymm')
    #print(tour_table[:2])
    
    resNm = tour_table.resNm.unique()
    #print('관광지명 : ', resNm[:5]) #관광지명 :  ['창덕궁' '운현궁' '경복궁' '창경궁' '종묘']
    
    #중국인 정보
    cdf = '../testdata/중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding='UTF-8').read())
    #print(jdata)
    china_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns = {'visit_cnt' : 'china'})
    china_table = china_table.set_index('yyyymm')
    #print(china_table[:2])
    
    #일본인 정보
    jdf = '../testdata/일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding='UTF-8').read())
    #print(jdata)
    japan_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns = {'visit_cnt' : 'japan'})
    japan_table = japan_table.set_index('yyyymm')
    #print(japan_table[:2])
    
    #미국인 정보
    udf = '../testdata/미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding='UTF-8').read())
    #print(jdata)
    usa_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns = {'visit_cnt' : 'usa'})
    usa_table = usa_table.set_index('yyyymm')
    #print(usa_table[:2])
    
    all_table = pd.merge(china_table, japan_table, left_index = True, right_index = True)
    all_table = pd.merge(all_table, usa_table, left_index = True, right_index = True)
    #print(all_table[:3])
    
    
    r_list = []
    #관광지 5군데에 대한 산점도
    for tourPoint in resNm[:5]:
        r_list.append(setScatterGraph(tour_table, all_table, tourPoint))
        
    #print(r_list) #[['창덕궁', -0.05879110406006314, 0.2774443570141011, 0.4028160633050156],  .....
    #
    #DataFrame형태로
    r_df = pd.DataFrame(r_list, columns=('관광지 명', '중국', '일본', '미국'))
    print(r_df)
    r_df = r_df.set_index('관광지 명') #인덱스 번호 대신에 관광지 명을 인덱스로 지정
    print(r_df)
    """
                     중국        일본        미국
    관광지 명                              
    창덕궁   -0.058791  0.277444  0.402816
    운현궁    0.445945  0.302615  0.281258
    경복궁    0.525673 -0.435228  0.425137
    창경궁    0.451233 -0.164586  0.624540
    종묘    -0.583422  0.529870 -0.121127
        
          관광지 명        중국        일본        미국
    0   창덕궁 -0.058791  0.277444  0.402816
    1   운현궁  0.445945  0.302615  0.281258
    2   경복궁  0.525673 -0.435228  0.425137
    3   창경궁  0.451233 -0.164586  0.624540
    4    종묘 -0.583422  0.529870 -0.121127
    """
    
    #시각화
    r_df.plot(kind='bar', rot=60) #rot=60은 x라벨 글자를 기울여줌
    plt.show()
    
if __name__ == "__main__":
    chulbal()









