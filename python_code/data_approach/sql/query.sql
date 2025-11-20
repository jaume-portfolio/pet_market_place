with 
temp as (
    select
        count(*) as rating_amount,
        avg(rating) as rating_score,
        (min(len_sitter_name)*1.0/26)*5 as profile_score,
        sitter,
        sitter_phone_number,
        sitter_email
    from df
    group by sitter,sitter_phone_number,sitter_email
    order by sitter,sitter_phone_number,sitter_email
),
final as (
select
    sitter_email as email,
    sitter as name,
    profile_score as profile_score,
    rating_score as rating_score,
    case 
        when rating_amount >= 10 then rating_score*1.0
        when rating_amount >=1 then (rating_amount*1.0/10)*rating_score+((10-rating_amount)*1.0/10)*profile_score
        else profile_score*1.0
    end as search_score
from temp
)
select 
    email,
    name,
    printf('%.2f', profile_score) AS profile_score,
    printf('%.2f', rating_score) AS ratings_score,
    printf('%.2f', search_score) AS search_score

from final

