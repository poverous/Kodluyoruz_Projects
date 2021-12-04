## ***[16, 21, 11, 8, 12, 22] -> Merge Sort***

1) ### **Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.**
    
    1.1. Diziyi tek eleman kalıncaya kadar her adımda yarıya bölüyoruz.
        
        [16, 21, 11] [8, 12, 22]
    
    1.2. Diziyi tek eleman kalıncaya kadar her adımda yarıya bölüyoruz.
         
        [16] [21, 11] [8, 12] [22]

    1.3. Diziyi tek eleman kalıncaya kadar her adımda yarıya bölüyoruz.
        
        [16] [21] [11] [8] [12] [22]

    1.4. Tek eleman kalıncaya kadar bölünen dizi, birleştirme aşamasına geçer. Birleştirirken sıralama yapılır ve böylece küçük sıralı diziler oluşur. 
        
        [16] [11, 21] [8, 12] [22]

    1.5. Küçük sıralı diziler tekrardan birleştirilirken sıralama yapılır ve büyük sıralı diziler elde edilir. Ancak küçük sıralı dizilerin ilk elemanları karşılaştırılır ve küçük olan büyük dizinin ilk elemanını olur. Böylece eleman bazlı sorgu yaptığımız için n tane sorugu olur.
        
        [11, 16, 21] [8, 12, 22]
    
    1.5. Büyük sıralı diziler tekrardan birleştirilirken sıralama yapılır istenen sıralı dizi elde edilir. Burada da bir önceki işlem gibi büyük sıralı dizilerin ilk elemanından küçük olan başa yazılır ve eleman sayısı kadar sorgu olur. Bir önceki adımla aynı.
        
        [8, 11, 12, 16, 21, 22]

2) ### **Big-O gösterimini yazınız.**

    Dizinin tek eleman kalıncaya kadar yarıya bölünmesi sonra da sırayıyla elemanlar karşılaştırılarak sıralanıyor ve birleştire birleştire sıralı dizi elde ediliyor. Dizinin birleştirme adımında eleman bazlı tek tek sorgu yapıldığı için time complexity n'dir. Ayrıca her seferinde diziyi yarıya bölüyoruz. Bu bölme işlemini logn kere yapıyoruz.

        2 ^ x = n

        logn = x

    Bütün bu işlemlerle beraber Big-O'su O(nlogn) olur. 
