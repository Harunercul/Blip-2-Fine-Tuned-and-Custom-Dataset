# Blip-2-Fine-Tuned-and-Custom-Dataset
Merhaba 

Bugün Blip-2 Modelini Custom Dataset ile fine tuned edicez ana hedefimiz image captioning yapmak. 

# Data Hazırlamak:
İlk önce datamızı hazırlıycaz datamızın başlıkları [image,text] olucak image'in altında fotoğraflarımız text olarak dediğimiz şey fotoğrafın açıklaması caption'ı. Verimizi İlk önce parquet veritabanı olarak hazırlıycaz bunun amacı verimizi huggingface yüklerken sıkıntın çekmemek. Paylaştığım data oluşturma kodunda excelden Caption altındaki veriyi texte koyuyor image altına da image pathlerinden yola çıkarak imagein altına byte olarak koyuyor ama bu dosyayı huggingface yükleyince byte = resime dönücek.  Ben fashion için 260bin fotoğraf datalı bir veri seti oluşturdum sizin için paylaşıyorum linkini.

# Huggingface Data Link: https://huggingface.co/datasets/shadowtime/dataset
Örnek datadan ekran görüntüsü:
![image](https://github.com/Harunercul/Blip-2-Fine-Tuned-and-Custom-Dataset/assets/105969081/20df070b-518b-4cc3-909b-ad22887ff60a)


# Eğitimi başlatmak
Eğitim yapmak için kodu paylaşıyorum sizin için kendinize göre batch size değerini datanızı ve epoch değerinizi ayarlayabilirsiniz.
# Eğitim Bittikten sonra
FinishTrain.py dosyasından eğittiniz yeni modeli huggingface yükleyip test edebilirsiniz

# English Version

Hello

Today we will fine tune the Blip-2 Model with Custom Dataset, our main goal is to do image captioning. 

# Prepare Data
First, we will prepare our data, the titles of our data will be [image, text], under the image will be our photos, what we call text is the description caption of the photo. We will first prepare our data as a parquet database, the purpose of this is not to have trouble loading our data huggingface. In the data creation code I shared, it puts the data under Caption from excel in text and puts it under the image as a byte under the image based on the image paths, but when huggingface loads this file, byte = image.  I created a dataset with 260 thousand photo data for fashion, I share the link for you.

# Huggingface Data Link: https://huggingface.co/datasets/shadowtime/dataset
Screenshot from sample data:
![image](https://github.com/Harunercul/Blip-2-Fine-Tuned-and-Custom-Dataset/assets/105969081/540c4093-a29d-4092-af7f-b91d9831b6aa)

# Start the training
I am sharing the code to make training for you, you can set the batch size value for yourself and your epoch value.
# After the training is over
You can test the new model you trained from FinishTrain.py by loading huggingface


# Eğitimi Multi-GPU kullanarak yapmak istiyorsanız diğer repomda paylaşıcam bunun nedeni kullandığımız model aşırı büyük bu yüzden cpu da yavaş çalışıyor eğer birden fazla datanız var ise Multi-GPU ile eğitimi başlatabilirsiniz diğer repomda paylaşacağım.

# If you want to do the training using Multi-GPU, I will share it in my other repo, the reason for this is that the model we use is extremely large, so the cpu is also running slowly, if you have more than one data, you can start the training with Multi-GPU.
