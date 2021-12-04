## ***[22, 27 ,16, 2, 18, 6]  -> Insertion Sort***

1) ### **Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.**
    
    1.1. Dizinin 6 elamanından en küçük elemanı bulunur ve en baştaki eleman ile yer değiştirilir. En küçük eleman 2'dir
        
        [2, 27, 16, 22, 18, 6]
    
    1.2. Dizinin geri kalan 5 elemanından en küçük olanı baştaki elemanla yer değiştirir. Geri kalan elemanlardan en küçüğü 6'dır.

        [2, 6, 16, 22, 18, 27]

    1.3. Dizinin geri kalan 4 elemanından en küçük olanı baştaki iki elemanlanın yanına yerleştirilir. Ancak en küçük eleman zaten doğru yerdedir.
        
        [2, 6, 16, 22, 18, 27]

    1.4. Dizinin geri kalan 3 elemanından en küçük olanı baştaki elemanlanın yanına yerleştirilir. Geri kalan elemanlardan en küçüğü 18'dir. Bundan dolayı 22 ile yer değiştirir.
        
        [2, 6, 16, 18, 22, 27]

    1.5. Dizinin geri kalan 2 elemanın karşılaştırılır. Küçük olan daha önce yazıldığı için herhangi bir işleme gerek kalmaz ve sıralama işlemi biter.
        
        [2, 6, 16, 18, 22, 27]

2) ### **Big-O gösterimini yazınız.**

    İlk önce dizinin bütün elemaları arasından en küçüğü aranıyor. Yani dizinin eleman sayısı kadar yani "n" kadar işlem yapılıyor. Sonraki adımda ilk eleman sırasında olduğu için geri kalan elemanlar arasında en küçüğünü arama işlemi yapılıyor. Yani dizinin yeni eleman sayısı n-1 kadar işlem yapılıyor. Bu işlem bütün dizi sıralıncaya kadar tekrar eder.
    
        = [ n * (n-1) ] / 2

        = [ n ^ 2 - n ] /2

        = n ^ 2 

        = O(n ^ 2) 

    Big-O'su O(n ^ 2)'dir

3) ### **Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.**

        [2, 6, 16, 18, 22, 27]
    
    18 sayısı dizinin ortasında bulunduğu için **Avarage Case** kapsamındadır. Arama algoritmalarının time complexitiy'lerine göre **Linear Search** algoritması **O(n)** zamanda, **Binary Search** algoritması **O(logn)** zamanda bulur.

---
<br>

## ***[7, 3, 5, 8, 2, 9, 4, 15, 6] dizisinin Insertion sort'a göre ilk 4 adımını yazınız.***

1. Dizi içerisindeki en küçük sayı bulunur ve ilk baştaki değer ile yer değiştirilir.

        [2, 3, 5, 8, 7, 9, 4, 15, 6]

2. Dizi içerisinde geriye kalan sayılar arasındaki en küçük sayı baştaki sayı ile yer değiştirir. Ancak geriye kalan sayılar arasındaki en küçük sayı zaten başta olduğu için diğer sayılar arasında karşılaştırma yapılır.

3. Geriye kalan sayılar arasındaki en küçük sayı baştaki sayı ile yer değiştirir. yazılır.
        
        [2, 3, 4, 8, 7, 9, 5, 15, 6]

4. Tekrardan geriye kalan sayılar arasındaki en küçük sayı baştaki sayı ile yer değiştirir. Bu sayı 5'tir ve 8 ile yeri değiştirilir. Diğer adımlar da bir önceki adımlar gibi birbirini tekrar ederek devam eder.
        
        [2, 3, 4, 5, 7, 9, 8, 15, 6]