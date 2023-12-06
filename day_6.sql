--part 1
select 
    FLOOR((44+sqrt(power(44,2)-4*208))/2-0.0000001) - CEIL((44-sqrt(power(44,2)-4*208))/2+0.0000001) +1 ,
    FLOOR((80+sqrt(power(80,2)-4*1581))/2-0.0000001) - CEIL((80-sqrt(power(80,2)-4*1581))/2+0.0000001) +1 ,
    FLOOR((65+sqrt(power(65,2)-4*1050))/2-0.0000001) - CEIL((65-sqrt(power(65,2)-4*1050))/2+0.0000001) +1 ,
    FLOOR((72+sqrt(power(72,2)-4*1102))/2-0.0000001) - CEIL((72-sqrt(power(72,2)-4*1102))/2+0.0000001) +1 
from sys.dual;
--part2
select 
    FLOOR((44806572+sqrt(power(44806572,2)-4*208158110501102))/2-0.0000001) - CEIL((44806572-sqrt(power(44806572,2)-4*208158110501102))/2+0.0000001) +1
from sys.dual;

--validation
--select 
--    FLOOR((7+sqrt(power(7,2)-4*9))/2) - CEIL((7-sqrt(power(7,2)-4*9))/2) +1 ,
--    FLOOR((15+sqrt(power(15,2)-4*40))/2) - CEIL((15-sqrt(power(15,2)-4*40))/2) +1 ,
--    FLOOR(((30+sqrt(power(30,2)-4*200))/2)-0.000001) - CEIL((30-sqrt(power(30,2)-4*200))/2+0.0000001) +1 
--from sys.dual;
