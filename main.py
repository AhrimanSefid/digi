from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.uix.recycleview import RecycleView
from kivy.utils import rgba
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter


import os
from kivymd.app import MDApp
import arabic_reshaper 
from bidi.algorithm import get_display 
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
import pandas as pd #openpyxl
from kivymd.uix.swiper import MDSwiperItem
from kivymd.uix.button import MDRoundFlatIconButton
import random
#from openpyxl import load_workbook
import webbrowser

dataframe_products = pd.read_excel (r'products.xls')
dataframe_products = dataframe_products.astype({"price_off": int})
dataframe_products = dataframe_products[dataframe_products['stock'] != 0]

items_in_order_screen = []
 
#Window.size = (350, 610)

Builder.load_file('main.kv')
Builder.load_file('main_searchbar.kv')
Builder.load_file('main_searchbar_screen.kv')
Builder.load_file('main_scroll.kv')
Builder.load_file('main_scroll_scroll1.kv')
Builder.load_file('main_scroll_gridLayout1.kv')
Builder.load_file('main_scroll_carousel1.kv')
Builder.load_file('main_scroll_gridLayout2.kv')
Builder.load_file('main_scroll_scroll2.kv')
Builder.load_file('main_scroll_gridLayout3.kv')
Builder.load_file('main_bottom_navigation.kv')
Builder.load_file('screen_product.kv')
Builder.load_file('screen_product_scroll3.kv')
Builder.load_file('screen_product_scroll3_scroll5.kv')
Builder.load_file('screen_off.kv')
Builder.load_file('screen_order.kv')
Builder.load_file('screen_grouping.kv')
Builder.load_file('screen_account.kv')

class ScrollMain(ScrollView):
    mgr1 = ObjectProperty()
    def on_scroll_stop(self, touch, check_children=True):
        super().on_scroll_stop(touch, check_children=False)

class ScrollView1(ScrollView):
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False 

class ScrollView2(ScrollView):
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False 
 
class ScrollView3(ScrollView):
    material = ObjectProperty()
    made_in = ObjectProperty()
    type = ObjectProperty()
    detail_1 = ObjectProperty()
    detail_2 = ObjectProperty()
    color = ObjectProperty()
    price = ObjectProperty()
    price_off = ObjectProperty()
    off = ObjectProperty()
    sizee = ObjectProperty()

    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False 

class ScrollView4(ScrollView):
    # screen_product_scroll3.kv
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False 

class ScrollView5(ScrollView):
    # screen_product_scroll3.kv
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False 

class cat1(ScrollView):
    # screen_product_scroll3.kv
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False 

class cat2(ScrollView):
    # screen_product_scroll3.kv
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False 

class cat3(ScrollView):
    # screen_product_scroll3.kv
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False 

class RV(RecycleView):
    dkp = ObjectProperty()
    title = ObjectProperty()
    price_off = ObjectProperty()
    icon_color = ObjectProperty()
    color_fa = ObjectProperty()
    total = ObjectProperty()
    

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        #self.data = [{'text': str(x)} for x in range(100)]
        self.data = [item for item in items_in_order_screen]

    def add_to_order(self):
        items_in_order_screen.append(
            {"DKP": '%s'%(self.dkp), 'image': 'img/Products/%s/%s-0.jpg'%(self.dkp, self.dkp), 'title': self.title, 'price_off': str(self.price_off), 'color_en': self.icon_color, 'color_fa': get_display(arabic_reshaper.reshape(self.color_fa))}
        )
        self.total = 0
        for i in range(len(items_in_order_screen)):
            self.total += int(items_in_order_screen[i]['price_off'].replace(",",""))
        total = self.total
        self.total = f'{total:,}'
        self.data = [item for item in items_in_order_screen]
        
    def remove_from_order(self, instance, DKP, color_en):
        for i in items_in_order_screen: 
            if i['DKP'] == DKP and i['color_en'] == color_en:
                items_in_order_screen.remove(i)
                self.data = [item for item in items_in_order_screen]

        self.total = 0
        for i in range(len(items_in_order_screen)):
            self.total += int(items_in_order_screen[i]['price_off'].replace(",",""))
        total = self.total
        self.total = f'{total:,}'
        self.mgr3.remove_widget(instance.parent.parent)

class MySwiper(MDSwiperItem):
    source = ObjectProperty()

class color_buttom(MDRoundFlatIconButton):
    title= ObjectProperty()
    ic_color= ObjectProperty()

class Product(Screen):
    dkp = ObjectProperty()
    title = ObjectProperty()
    price = ObjectProperty()
    price_off = ObjectProperty()
    off = ObjectProperty()
    icon = ObjectProperty()

class Button_scroll5(Button):
    image_source = ObjectProperty()

class scatter(Scatter):
    source = ObjectProperty()

class Off(Screen):
    title = ObjectProperty() 

class MainScreen(ScreenManager):
    mgr5 = ObjectProperty()

    # Deine back bottom in android
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)
    def on_key(self, window, key, *args):
        if key == 27:  # the esc key
            if self.current_screen.name == "product" or self.current_screen.name == "off" or self.current_screen.name == "order" or self.current_screen.name == "grouping":
                self.current = "main"
                return True  # exit the app from this page
            elif self.current_screen.name == "main":
                return True
            
    def open_product_screen(self, DKP):  
        try:
            DKP.split('/')
            DKP = int(DKP.split('/')[3].split('-')[0])
        except:
            pass
        self.mgr5.mgr1.mgr2.scroll_x = 1
        self.mgr5.mgr1.scroll_y = 1
        self.mgr5.mgr1.mgr3.scroll_x = 1
        self.mgr5.dkp = DKP
        self.mgr7.mgr2.dkp = DKP
        self.mgr5.mgr1.sizee = dataframe_products[(dataframe_products['DKP'] == DKP) ]['size'].values[0]
        self.mgr5.icon = "cards-heart-outline"
        # Delete all Swiper's children
        self.mgr5.mgr2.children[0].clear_widgets()
        # Add title
        self.mgr5.title = dataframe_products[(dataframe_products['DKP'] == DKP) ]['title'].values[0]
        self.mgr7.mgr2.title = self.mgr5.title
        # Calculate the number of photos
        directory_path = 'img/Products/%s'%(DKP)
        No_of_files = len(os.listdir(directory_path))
        self.mgr5.mgr2.set_current(0)
        # Add photos to Swiper
        for i in range(No_of_files):
            self.mgr5.mgr2.add_widget(Factory.MySwiper(source= 'img/Products/%s/%s-%s.jpg'%(DKP, DKP, i)))
        # Creating a list of colors in Farsi and English
        list_colors = dataframe_products[(dataframe_products['DKP'] == DKP) & (dataframe_products['stock'] != 0) ]['color'].tolist()
        list_colors_fa = dataframe_products[(dataframe_products['DKP'] == DKP) & (dataframe_products['stock'] != 0) ]['color-fa'].tolist()
        # Calculate the number of colors in stock
        self.mgr5.mgr1.mgr1.cols= len(list_colors)
        # Delete all color_scrollview's children
        try:
            self.mgr5.mgr1.mgr1.clear_widgets()
        except: 
            pass
        # Add colors button to scrollview3
        for i in range(len(list_colors)):
            self.mgr5.mgr1.mgr1.add_widget(Factory.color_buttom(title= str(list_colors_fa[i]), ic_color= list_colors[i]))
        # Add the first color label
        self.mgr5.mgr1.color= get_display(arabic_reshaper.reshape(str(list_colors_fa[len(list_colors_fa) - 1]))) 
        self.mgr7.mgr2.color_fa = self.mgr5.mgr1.color
        # Add material, country of manufacture and product type & details
        self.mgr5.mgr1.material= dataframe_products[(dataframe_products['DKP'] == DKP) ]['material'].values[0]
        self.mgr5.mgr1.made_in= dataframe_products[(dataframe_products['DKP'] == DKP)  ]['made_in'].values[0]
        self.mgr5.mgr1.type= dataframe_products[(dataframe_products['DKP'] == DKP)  ]['type'].values[0]
        self.mgr5.mgr1.detail_1= dataframe_products[(dataframe_products['DKP'] == DKP)  ]['detail_1'].values[0]
        self.mgr5.mgr1.detail_2= dataframe_products[(dataframe_products['DKP'] == DKP)  ]['detail_2'].values[0]
        # Add first price & price_off & off
        self.mgr5.icon_color = list_colors[len(list_colors) - 1]
        a = self.mgr5.icon_color
        self.mgr7.mgr2.icon_color = a
        price = int(dataframe_products[(dataframe_products['DKP'] == DKP) & (dataframe_products['color'] == a) ]['price'].values[0])
        self.mgr5.price = f'{price:,}'
        price_off = int(dataframe_products[(dataframe_products['DKP'] == DKP) & (dataframe_products['color'] == a) ]['price_off'].values[0])
        self.mgr5.price_off = f'{price_off:,}'
        self.mgr7.mgr2.price_off = self.mgr5.price_off
        self.mgr5.off = int(dataframe_products[(dataframe_products['DKP'] == DKP) & (dataframe_products['color'] == a) ]['off'].values[0])
        # Add similar product
        ## Drop all children
        try:
            self.mgr5.mgr1.mgr2.ids._GridLayout.clear_widgets()
        except:
            pass
        ## Get categories
        cat = dataframe_products[(dataframe_products['DKP'] == DKP) ]['cat'].values[0]   
        ## Create list of DKPs in our category without repeat
        list_cat = dataframe_products[(dataframe_products['cat'] == cat) & (dataframe_products['stock'] != 0) ]['DKP'].drop_duplicates().tolist()
        ## Drop current category
        list_cat = [ele for ele in list_cat if ele != DKP]
        ## Select 5 category randomly
        List_similar_product = random.sample(list_cat, 5 if len(list_cat) >= 5 else len(list_cat))
        for i in range(len(List_similar_product)):
            self.mgr5.mgr1.mgr2.ids._GridLayout.add_widget(Factory.Button_scroll5(image_source= 'img/Products/%s/%s-0.jpg'%(List_similar_product[i], List_similar_product[i]) ))
        # Set current screen
        self.current= "product"

    def Price_change_with_variety_change(self, icon_color, color_fa):
        price = int(dataframe_products[(dataframe_products['DKP'] == self.mgr5.dkp) & (dataframe_products['color'] == icon_color) ]['price'].values[0])
        self.mgr5.price = f'{price:,}'
        price_off = int(dataframe_products[(dataframe_products['DKP'] == self.mgr5.dkp) & (dataframe_products['color'] == icon_color) ]['price_off'].values[0])
        self.mgr5.price_off = f'{price_off:,}'
        self.mgr7.mgr2.price_off = self.mgr5.price_off
        self.mgr5.off = int(dataframe_products[(dataframe_products['DKP'] == self.mgr5.dkp) & (dataframe_products['color'] == icon_color) ]['off'].values[0])
        self.mgr7.mgr2.icon_color = icon_color
        self.mgr7.mgr2.color_fa = color_fa

    def main_scroll_gridLayout1_items(self,name):
        if name == 'instagram':
            webbrowser.open('https://www.instagram.com/radin__sprt/')
        elif name == 'digikala':
            webbrowser.open('https://www.digikala.com/seller/aygzu/')
        elif name == 'digistal':
            webbrowser.open('https://www.digistyle.com/')
        elif name == 'weblog':
            webbrowser.open('https://radinsport.blog.ir/')
        elif name == 'contact_us':
            webbrowser.open('https://www.digikala.com/seller/aygzu/')
        elif name == 'kalands':
            webbrowser.open('https://www.kalands.ir/seller/aygzu/')
        elif name == 'bazar':
            webbrowser.open('https://cafebazaar.ir/app/com.radinafzar.radinsport')

    def changeـheartـicon(self):
        self.mgr5.icon = 'cards-heart'

    def zoom_product_image(self, source):
        #self.mgr5.mgr2.add_widget(Factory.MySwiper(source= 'img/Products/%s/%s-%s.jpg'%(DKP, DKP, i)))
        pop = Popup(title='', content=Factory.scatter(source= source),
                    size_hint=(None, None), size=(self.width, self.width),separator_height= 0)
        pop.open()

    def open_category(self, cat):
        category_dict = {'H': 'کلاه و نقاب', 'SH': 'قمقمه و شیکر', 'SW': 'لوازم شنا', 'GL': 'دستکش'}
        self.mgr6.title= get_display(arabic_reshaper.reshape(category_dict[cat]))
        for i in range(10):
            self.mgr6.mgr2.add_widget(Factory.StackLayoutOff(title_= 'salam'))


        self.current= "off"




    def print(self):
        print('OK')
    def printt(self):
        print('OK')
    def print1(self):
        print('OK1')
    def print2(self):
        print('OK2')
    def print3(self):
        print('OK3')
    def print4(self):
        print('OK4')

class DigiApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "900"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.accent_hue  = "900"
       #self.theme_cls.theme_style = "Dark"
        return MainScreen()

    def on_start(self):
        # Access the carousel.
        carousel = self.root.mgr1.mgr3.mgr1.ids._carousel_
        # Schedule after every 3 seconds.
        Clock.schedule_interval(carousel.load_next, 3.0)
        # Add widget to scrollview1 in main screen
        list_DKP = dataframe_products[dataframe_products['off'] != 0]['DKP'].drop_duplicates().to_list()  
        j = 8 #len(list_DKP)
        for i in range(j):
            dkp = list_DKP[i]
            self.root.mgr1.mgr3.mgr2.dkp= dkp
            text_title = dataframe_products[(dataframe_products['DKP'] == dkp)]['title'].tolist()[0]
            if len(text_title) > 20:
                text_title = text_title[:17] + '...'
            self.root.mgr1.mgr3.mgr2.text_title= text_title
            self.root.mgr1.mgr3.mgr2.source_image= 'img/Products/%s/%s-0.jpg'%(dkp, dkp)
            self.root.mgr1.mgr3.mgr2.detail_1= dataframe_products[(dataframe_products['DKP'] == dkp)]['detail_3'].tolist()[0]
            self.root.mgr1.mgr3.mgr2.detail_2= dataframe_products[(dataframe_products['DKP'] == dkp)]['detail_4'].tolist()[0]
            self.root.mgr1.mgr3.mgr2.off= str(dataframe_products[(dataframe_products['DKP'] == dkp)]['off'].tolist()[0])
            price = int(dataframe_products[(dataframe_products['DKP'] == dkp)]['price'].tolist()[0])
            self.root.mgr1.mgr3.mgr2.price= f'{price:,}'
            price_off = dataframe_products[(dataframe_products['DKP'] == dkp)]['price_off'].tolist()[0]
            self.root.mgr1.mgr3.mgr2.price_off= f'{price_off:,}'
            self.root.mgr1.mgr3.mgr2.mgr1.add_widget(Factory.BoxLayout_mainscroll_scroll1())
if __name__=="__main__":
    DigiApp().run()