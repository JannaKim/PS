SELECT
   A.buyer_id
    , A.buy_date
    , B.book_name
    , B.price
FROM
   orderInfo A
LEFT JOIN library B ON A.book_id = B.book_id
WHERE
   B.book_name = 'Looking with Elice'
OR A.buy_date BETWEEN '2020-07-27' AND '2020-07-31'
ORDER BY A.buy_date ASC