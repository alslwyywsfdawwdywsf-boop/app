from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
import webbrowser

class YusufApp(App):
    def build(self):
        # إعدادات الشاشة
        Window.clearcolor = (0, 0, 0, 1)
        layout = BoxLayout(orientation='vertical', padding=[15, 20, 15, 20], spacing=15)
        
        # 1. عرض صورتك الشخصية (my_photo.jpg)
        user_img = Image(
            source='my_photo.jpg', 
            size_hint=(1, 3), 
            allow_stretch=True, 
            keep_ratio=True
        )
        layout.add_widget(user_img)
        
        # 2. النص التعريفي الذهبي في المنتصف
        layout.add_widget(Label(
            text='Designed by Programmer YUSUF', 
            font_size='22sp', 
            color=(1, 0.84, 0, 1), 
            bold=True,
            size_hint=(1, 0.4)
        ))
        
        # 3. زر إنستجرام (رابط حسابك الحقيقي)
        btn_insta = Button(
            text='Follow me on Instagram',
            background_color=(0.7, 0.5, 0, 1),
            size_hint=(1, 0.4),
            bold=True
        )
        btn_insta.bind(on_press=self.open_instagram)
        layout.add_widget(btn_insta)
        
        # 4. زر واتساب (رقمك الصحيح 736192558)
        btn_whatsapp = Button(
            text='Contact me on WhatsApp',
            background_color=(0.1, 0.4, 0.1, 1),
            size_hint=(1, 0.4),
            bold=True
        )
        btn_whatsapp.bind(on_press=self.open_whatsapp)
        layout.add_widget(btn_whatsapp)
        
        return layout

    # وظيفة فتح إنستجرام برابطك الخاص
    def open_instagram(self, instance):
        webbrowser.open("https://www.instagram.com/yusef_0n?igsh=MThhc3licWtzenJxZg==")

    # وظيفة فتح واتساب برقمك الصحيح
    def open_whatsapp(self, instance):
        # الرقم: 736192558 مع مفتاح اليمن 967
        phone_number = "967736192558" 
        webbrowser.open(f"https://wa.me/{phone_number}")

if __name__ == '__main__':
    YusufApp().run()
