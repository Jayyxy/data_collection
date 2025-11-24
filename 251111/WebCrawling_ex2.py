'''
[크롤링 미션2]
특정 장르에 해당하는 책 구매 목록 페이지의 모든 페이지의 데이터를 크롤링하세요.
[필요한 정보]
책 사진 URL
별점 개수
제목
상세 페이지 URL
가격

[데이터 예시]
{
  "genre" : "장르",
  "items" : [
    {
      "page" : 1,
      "data" : [
        {
          "title" : "제목",
          "price" : "가격",
          "stars" : "별점 개수",
          "img_url" : "사진 URL",
          "detail_url" : "상세 페이지 URL"
        },
        {
         }
      ]
    },
    {
      "page" : 2,
      "data" : [
        {
          "title" : "제목",
          "price" : "가격",
          "stars" : "별점 개수",
          "img_url" : "사진 URL",
          "detail_url" : "상세 페이지 URL"
         },
          {
          }
        ]
     },
  ]
}

위 형태처럼 최상단에 장르 정보, 그리고 각 페이지마다 페이지 번호, 페이지에 있는 데이터를 구분하는 구조로 만드세요

https://books.toscrape.com/index.html 


'''