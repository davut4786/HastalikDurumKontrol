from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def tahmin_et_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        
        # Kullanıcıdan verileri al
        tur = 1 if self.radio_button_12.selected else 0 if self.radio_button_11.selected else None
        GRAN = float(self.GRAN_textbox.text)  
        GRAN_A = float(self.GRAN_A_textbox.text)  
        LYM = float(self.LYM_textbox.text)  
        LYM_A = float(self.LYM_A_textbox.text)  
        MON = float(self.MON_textbox.text)  
        HCT = float(self.HCT_textbox.text)  
        MCH = float(self.MCH_textbox.text)  
        MCHC = float(self.MCHC_textbox.text)  
        MCV = float(self.MCV_textbox.text)  
        RDW = float(self.RDW_textbox.text)  
        WBC = float(self.WBC_textbox.text)

        # Radio button tanımlamaları
        inkordinasyon = 1 if self.inkordinasyon1.selected else 0  # Evet butonu seçiliyse 1, Hayır butonu seçiliyse 0
        ishal = 1 if self.ishal1.selected else 0
        istahsizlik = 1 if self.istahsizlik1.selected else 0
        kusma = 1 if self.kusma1.selected else 0
        solunum_guclugu = 1 if self.solunum1.selected else 0

        # Model tahmini yapma
        sonuc = anvil.server.call(
            'model_tahmin', 
            [tur, GRAN, GRAN_A, LYM, LYM_A, MON, HCT, MCH, MCHC, MCV, RDW, WBC, inkordinasyon, ishal, istahsizlik, kusma, solunum_guclugu]
        )

        # Sonucu göster
        self.sonuc_label.text = f"Tahmin Sonucu: {sonuc}"

    def temizle_button_click(self, **event_args):
        """This method is called when the clear button is clicked"""
        # Tüm giriş alanlarını temizle
        self.GRAN_textbox.text = ""
        self.GRAN_A_textbox.text = ""
        self.LYM_textbox.text = ""
        self.LYM_A_textbox.text = ""
        self.MON_textbox.text = ""
        self.HCT_textbox.text = ""
        self.MCH_textbox.text = ""
        self.MCHC_textbox.text = ""
        self.MCV_textbox.text = ""
        self.RDW_textbox.text = ""
        self.WBC_textbox.text = ""

        # Radio buttonları sıfırla
        self.radio_button_11.selected = False
        self.radio_button_12.selected = False
        self.inkordinasyon1.selected = False
        self.ishal1.selected = False
        self.istahsizlik1.selected = False
        self.kusma1.selected = False
        self.solunum1.selected = False

        # Sonucu sıfırla
        self.sonuc_label.text = "Tahmin Sonucu: "
