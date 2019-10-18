
### **Amaç**: 
Görüntü işleme örneklerini barındıran repodur. Doküman ve kullanılan medya dosylarını içermektedir. Sürekli güncellenecektir.

OpenCV konusunda belli bir fikre sahip olmak ve openCV'nin çeşitli kısımlarını öğrenmek. 

#### Bunun için kullanılan kod ve ders kaynağı:
* Sentdex - OpenCV with Python for Image and Video Analysis
* Ve yine aynı kişinin blog'u:  https://pythonprogramming.net


! Kullanılanlar arasında sadece yorumlar kendime ait.

* Gereklilikler:
 * OpenCV
 * Numpy
 * Matplotlib(Tercihi)
 

   
#### Gerekenleri indirme & kurma:
> pip install numpy
> pip install matplotlib
> * OpenCV, pip ile veya kendi sitesinden indirilebilir.

# İçindekiler
## 1_Loading Images
Daha önce kayıtlı bir resmin nasıl okunup openCV ve matplotlib'de gösterilebileceği ve üzerinde işlem yapılan resimlerin nasıl kaydedilebileceği gösterilmiştir.
 
## 2_Loading Video Source
Webcam' den video alma, videoyu dışarıya kaydetme ve video kareleri üzerinde işlem yapma gösterilmiştir.

## 3_Drawing and Writing on Image
Okunan resim üzerine nasıl çizgi, dikdörtgen, çember veya çokgen çizilebileceği ve nasıl yazı yazılabileceği gösterilmiştir.

## 4_Image Operations
Resim üzerinde pixellere nasıl ulaşılabileceği, ROI(Region of Interest) nasıl seçilebileceği ve bunlarla yapılabilecek değişikler gösterilmiştir.

## 5_Image Arithmetics and Logic
Resimleri birbirleriyle birleştirmek için kullanılabilecek üç toplama şeklini ve openCV bitsel mantık işlemleri de kullanılarak bir resmin arka planından ön planını ayırıp başka bir resmi arka plan olarak kullanacak şekilde nasıl bir ekleme yapabiliriz gösterilmiştir.

## 6_Thresholding
Resme eşik değeri uygulama ve değişik eşikleme yöntemlerinin uygulanması gösterilmiştir.

  * Gauss Adaptive Threshold, Otsu Threshold

## 7_Color Filtering
Seçilen bir renk, burada kırmızı, için istenen ton aralığı(range) belirlenip, HSV renk uzayına çevrilmiş video karelerinde bu aralıkta olan tonlara uyan nesnelerin seçilmesi diğerlerinin ise arka plan olarak siyaha dönüştürülmesi gösterilmiştir.

## 8_Blurring and Smoothing
Resimdeki gürültüyü azaltmak için kullanılan blurring ve smoothing yöntemlerinden bazıları gösterilmiştir.

  * Ortalama alma, Gaussian Blur, Median Blur ve Bilateral Filter

## 9_Morphological Transformations
Filtreleme sonucu oluşan siyah-beyaz sonuç görüntünün sahip olabileceği birçok kusuru azaltmak veya düzeltmek amacıyla kullanılan morphological transformasyonlardan bazıları gösterilmiştir.

  * Erosion, Dilation, Opening ve Closing

## 10_Edge Detection and Gradients
Çeşitli kenar ve gradyan bulma yöntemleri gösterilmiştir.

* Laplacian Transform, Sobel Operation, Canny Edge Detection

## 11_Template Matching
İstediğimiz bir şeyi alınan resimde bulabilmek için bir template seçilmesi ve alınan resimde matchTemplate() fonksiyonu kullanılarak arananın bulunması ve bulunan yerlerde dikdörtgen çizilerek nerelerde olduğunun belirtilmesi gösterilmiştir.

## 12_GrabCut Foreground Extraction
GrabCut algoritması kullanılarak arka planın silinmesinin ve ön planın arka plandan ayrılmasının nasıl olacağı gösterilmiştir.

## 13_Corner Detection
goodFeaturesToTrack() fonksiyonunu kullanılarak köşelerin nasıl bulunabileceği ve sonra da bulunan köşelerin dairelerle işaretlenmesi gösterilmiştir.

## 14_Feature Matching and Homography
FAST Keypoint Detector ve BRIEF Descriptor algoritmalarının performans arttırıcı şekilde birleştiren ORB algoritmasını ve sonrada uyuşmaları çizmek için drawMatches() fonksiyonunu kullanarak iki resim arasındaki eşleşmelerin nasıl bulunabileceği gösterilmiştir.

## 15_MOG Background Reduction
Alınan videoda createBackgroundSubtractorMOG2() fonksiyonu ile video kareleri arası değişimlerin algılanıp ön plan olarak nasıl belirtilebileceği gösterilmiştir.

## 16_Haar Cascade Object Detection
Kaynakları kodda belirtilen cascadeler kullanılarak, Haar Cascade yöntemiyle nasıl nesne, burada yüz ve göz, tanınabileceği gösterilmiştir.
