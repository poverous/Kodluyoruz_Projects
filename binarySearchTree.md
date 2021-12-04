## ***[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.***

### **Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.**
    
1. Binary Search Tree'de bir düğüm her iki tarafa da referans verebiliyordu. Bu nedenle ilk önce root belirlenmeli. Dizinin ilk elemanı olan 7 sayısı root olsun.
        
        7    
        
2. Dizinin elemanları 7'ye bağlı olmak zorunda. 5 sayısı 7'den küçük olduğu için kök düğümünün sol tarafına yazıyoruz
        
            7
        5    

3. Dizinin 3. elemanı olan 1 sayısı 7'den küçük olduğu için kök düğümünün sol tarafında olmalı ancak sol tarafta 5 sayısı da olduğu için 5 ile karşılaştırılmalı. 1 sayısı 5'ten küçük olduğu için 5 sayısının soluna yazılır.
        
                7
            5    
        1

4. Dizinin 4. elemanı olan 8 sayısı 7'den büyük olduğu için kök düğümünün sağ tarafında olmalı.
        
                7
            5       8 
        1

4. Dizinin 5. elemanı olan 3 sayısı 7'den küçük olduğu için kök düğümünün sol tarafına yazılmalı. Fakat sol taraftaki 5 sayısı ile karşılaştırılmalıdır. 5 sayısı 3'den büyük olduğu için 3 sayısı 5'in soluna yazılmalıdır. Ancak burada da 1 sayısı olduğu için 1 sayısı ile 3 sayısı karşılaştırılır ve 3 sayısı 1'den büyük olduğu için 1'in sağına yazılır.
        
                7
            5       8 
        1
            3

5. Dizinin 6. elemanı olan 6 sayısı 7'den küçük olduğu için kök düğümünün sol tarafına yazılmalı. Fakat sol taraftaki 5 sayısı ile karşılaştırılmalıdır. 5 sayısı 6'den küçük olduğu için 6 sayısı 5'in sağına yazılmalıdır. 
        
                7

            5       8 

        1      6

            3

6. Dizinin 7. elemanı olan 0 sayısı 7'den küçük olduğu için kök düğümünün sol tarafına yazılmalı. Fakat sol taraftaki 5 sayısı ile karşılaştırılmalıdır. 5 sayısı 0'den büyük olduğu için 0 sayısı 5'in soluna yazılmalıdır. Buradaki 1 ile de karşılaştırılması gereken 0 sayısı, 1'den küçük olduğu için 1'in soluna yazılmalıdır.
        
                    7

                5       8 

            1       6

        0       3

7. Dizinin 8. elemanı olan 9 sayısı 7'den büyük olduğu için kök düğümünün sağ tarafına yazılmalı. Fakat sağ taraftaki 8 sayısı ile karşılaştırılmalıdır. 9 sayısı 8'den büyük olduğu için 9 sayısı 8'in sağına yazılmalıdır.
        
                    7

                5       8 

            1       6       9

        0       3

7. Dizinin 9. elemanı olan 4 sayısı 7'den küçük olduğu için kök düğümünün sol tarafına yazılmalı. Fakat sol taraftaki 5 sayısı ile karşılaştırılmalıdır. 4 sayısı 5'den küçük olduğu için 4 sayısı 5'in soluna yazılmalıdır. Burada 1 olduğu için bu sayı ile karşılaştırılmalıdır. 1'den büyük olduğu için 1'in sağına yazılmalıdır fakat oradaki 3 sayısı ile karşılatırılmaldır. 3 sayısı 4'den küçük olduğu için 4 sayısı 3'ün sağına yazılır. 
        
                    7

                5       8 

            1       6       9

        0       3

                    4

7. Dizinin 10. elemanı olan 2 sayısı 7'den küçük olduğu için kök düğümünün sol tarafına yazılmalı. Fakat sol taraftaki 5 sayısı ile karşılaştırılmalıdır. 2 sayısı 5'den küçük olduğu için 4 sayısı 2'in soluna yazılmalıdır. Burada 1 olduğu için bu sayı ile karşılaştırılmalıdır. 1'den büyük olduğu için 1'in sağına yazılmalıdır fakat oradaki 3 sayısı ile karşılatırılmaldır. 3 sayısı 2'den büyük olduğu için 2 sayısı 3'ün soluna yazılır. 
        
                    7

                5       8 

            1      6       9

         0     3

             2    4