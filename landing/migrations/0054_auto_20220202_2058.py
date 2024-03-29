# Generated by Django 3.1.6 on 2022-02-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0053_auto_20220202_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='district',
            field=models.CharField(blank=True, choices=[('Taplejung', 'Taplejung'), ('Panchthar', 'Panchthar'), ('Ilam', 'Ilam'), ('Jhapa', 'Jhapa'), ('Sankhuwasabha', 'Sankhuwasabha'), ('Bhojpur', 'Bhojpur'), ('Terhathum', 'Terhathum'), ('Dhankuta', 'Dhankuta'), ('Morang', 'Morang'), ('Sunsari', 'Sunsari'), ('Solukhumbu', 'Solukhumbu'), ('Okhaldhunga', 'Okhaldhunga'), ('Khotang', 'Khotang'), ('Udayapur', 'Udayapur'), ('Siraha', 'Siraha'), ('Saptari', 'Saptari'), ('Dolakha', 'Dolakha'), ('Ramechhap', 'Ramechhap'), ('Sindhuli', 'Sindhuli'), ('Sarlahi', 'Sarlahi'), ('Mahottari', 'Mahottari'), ('Dhanusha', 'Dhanusha'), ('Sindhupalchowk', 'Sindhupalchowk'), ('Rasuwa', 'Rasuwa'), ('Kavrepalanchowk', 'Kavrepalanchowk'), ('Dhading', 'Dhading'), ('Kathmandu', 'Kathmandu'), ('Lalitpur', 'Lalitpur'), ('Bhaktapur', 'Bhaktapur'), ('Nuwakot', 'Nuwakot'), ('Parsa', 'Parsa'), ('Bara', 'Bara'), ('Makwanpur', 'Makwanpur'), ('Chitwan', 'Chitwan'), ('Rautahat', 'Rautahat'), ('Gorkha', 'Gorkha'), ('Lamjung', 'Lamjung'), ('Tanahun', 'Tanahun'), ('Kaski', 'Kaski'), ('Syangja', 'Syangja'), ('Manang', 'Manang'), ('Nawalpur', 'Nawalpur'), ('Gulmi', 'Gulmi'), ('Kapilbastu', 'Kapilbastu'), ('Palpa', 'Palpa'), ('Rupandehi', 'Rupandehi'), ('Arghakhachi', 'Arghakhachi'), ('Mustang', 'Mustang'), ('Parbat', 'Parbat'), ('Myagdi', 'Myagdi'), ('Baglung', 'Baglung'), ('Eastern Rukum', 'Eastern Rukum'), ('Salyan', 'Salyan'), ('Rolpa', 'Rolpa'), ('Pyuthan', 'Pyuthan'), ('Dang', 'Dang'), ('Dolpa', 'Dolpa'), ('Humla', 'Humla'), ('Mugu', 'Mugu'), ('Jumla', 'Jumla'), ('Kalikot', 'Kalikot'), ('Jajarkot', 'Jajarkot'), ('Banke', 'Banke'), ('Dhailekh', 'Dhailekh'), ('Surkhet', 'Surkhet'), ('Bardiya', 'Bardiya'), ('Achham', 'Achham'), ('Bajhang', 'Bajhang'), ('Kailali', 'Kailali'), ('Doti', 'Doti'), ('Bajura', 'Bajura'), ('Kanchanpur', 'Kanchanpur'), ('Baitadi', 'Baitadi'), ('Dadeldhura', 'Dadeldhura'), ('Darchula', 'Darchula'), ('Western Rukum', 'Western Rukum'), ('Parasi', 'Parasi')], max_length=70, null=True),
        ),
    ]
